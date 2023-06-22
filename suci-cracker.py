import pyshark
import sys
import re
import subprocess
import time
import paramiko



def find_imsi():
        log_file_path = '/home/vagrant/open5gs/install/var/log/open5gs/mme.log'

    
        with open(log_file_path, 'r') as log_file:
            # Read all lines from the log file
            log_lines = log_file.readlines()
            # Iterate over the log lines in reverse order
            for line in reversed(log_lines):
        
                if "[mme] INFO:     IMSI[" in line:
                    imsi_pattern = r'IMSI\[(\d+)\]'
                    imsi_match = re.search(imsi_pattern, line)
                    imsi_match = re.search(imsi_pattern, line)
                    imsi_value = imsi_match.group(1)
                    
                    return imsi_value



def find_suci():
        log_file_path = '/home/vagrant/open5gs/install/var/log/open5gs/amf.log'

        
        # Open the log file in read mode
        with open(log_file_path, 'r') as log_file:
            # Read all lines from the log file
            log_lines = log_file.readlines()
            # Iterate over the log lines in reverse order
            # for i in range(len(log_lines) - 1):
                
            for line in reversed(log_lines):
                # line = log_lines[i].strip()

                if (("[amf] WARNING:" in line) and ("[gmm] WARNING: Authentication failure" in log_lines[log_lines.index(line)-1].strip())):
                    imsi=find_imsi()
                    suci_pattern = r'\[suci-(\d+-\d+-\d+-\d+-\d+-\d+-\w+)\]'
                    suci_match = re.search(suci_pattern, line)
                    suci_value = suci_match.group(1)
                    print("IMSI: "+ imsi + " doesn't match with SUCI: "+ suci_value )
                    sys.exit(0)
                elif "[gmm] ERROR:" in line:
                    print("IMSI MATCHES WITH SUCI")
                    suci_pattern = r'\[suci-(\d+-\d+-\d+-\d+-\d+-\d+-\w+)\]'
                    suci_match = re.search(suci_pattern, line)
                    suci_value = suci_match.group(1)
                    imsi=find_imsi()
                    print("SUCI: " +suci_value + " matches with IMSI: " +imsi)
                    sys.exit(0)




def segunda_parte(rand,autn):


        filename = "/home/vagrant/open5gs/src/amf/nausf-handler.c"

        # Read the file and modify the specific lines
        with open(filename, "r") as file:
            lines = file.readlines()
     
        lines[106] = f"      const  char* rand_f = \"{rand}\";\n"
        lines[107] = f"      const char* autn_f = \"{autn}\";\n"

        # Write the modified lines back to the file
        with open(filename, "w") as file:
            file.writelines(lines)

       

        # Execute the command in the specified directory
        subprocess.run(["ninja", "-C", "build"], cwd="/home/vagrant/open5gs",stdout=subprocess.DEVNULL)
        #subprocess.run(["pkill", "open5gs"])
        subprocess.run(["ninja", "install"], cwd="/home/vagrant/open5gs/build",stdout=subprocess.DEVNULL)



        # Define the commands
        commands = [
            
            "/home/vagrant/open5gs/install/bin/open5gs-amfd > /dev/null 2>&1 &",
            "sleep 2"
                       
        ]

        # Execute the commands
        for command in commands:
            subprocess.run(command, shell=True,stdout=subprocess.DEVNULL)


        

        # SSH connection parameters for the first host
        hostname1 = '192.168.10.121'
        username1 = 'vagrant'
        password1 = 'vagrant'

        # SSH connection parameters for the second host
        hostname2 = '192.168.10.122'
        username2 = 'vagrant'
        password2 = 'vagrant'

        # Command to be executed on both hosts
        command = 'sudo ./UERANSIM/build/nr-gnb -c /home/vagrant/UERANSIM/config/open5gs-gnb.yaml'
        command2 = 'sudo ./UERANSIM/build/nr-ue -c /home/vagrant/UERANSIM/config/open5gs-ueF.yaml'
        command3 = 'touch prueba2.txt'


        def execute_ssh_command(hostname, username, password, command):
            # Establish SSH connection
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname, username=username, password=password)

            # Execute the command
            stdin, stdout, stderr = ssh_client.exec_command(command)

            # # Print command output
            # print(f"Command output on {hostname}:")
            # #print(stdout.read().decode())

            # Close the SSH connection
           
        
        
            
        # Connect to the first host and execute the command
        execute_ssh_command(hostname2, username2, password2, command2)
        execute_ssh_command(hostname1, username1, password1, command)

        time.sleep(2)                         
        find_suci()
        
                                    
                                    
                                    
                                   
        

def main():

    commands = [
        "/home/vagrant/open5gs/install/bin/open5gs-nrfd > /dev/null 2>&1 &",
        "/home/vagrant/open5gs/install/bin/open5gs-scpd  > /dev/null 2>&1 &",

        #"/home/vagrant/open5gs/install/bin/open5gs-smfd > /dev/null 2>&1 &",
        "/home/vagrant/open5gs/install/bin/open5gs-ausfd > /dev/null 2>&1 &",
        "/home/vagrant/open5gs/install/bin/open5gs-udmd > /dev/null 2>&1 &",
        "/home/vagrant/open5gs/install/bin/open5gs-udrd > /dev/null 2>&1  &",
        "/home/vagrant/open5gs/install/bin/open5gs-pcfd > /dev/null 2>&1 &",
        "/home/vagrant/open5gs/install/bin/open5gs-nssfd > /dev/null 2>&1 &",
        "/home/vagrant/open5gs/install/bin/open5gs-bsfd > /dev/null 2>&1 &"
    ]

    # Execute the commands
    for command in commands:
        subprocess.run(command, shell=True, stdout=subprocess.DEVNULL)

  

    capture = pyshark.LiveCapture(interface="any")

    # Start the packet capture
    capture.sniff_continuously()

    # Process each packet in the pcap file
    for packet in capture:
        # Access packet information and print relevant details
    
        if(hasattr(packet, "s1ap") and hasattr(packet.s1ap, "procedureCode") and packet.s1ap.procedureCode =='11'  ) and hasattr(packet.s1ap, "nas_pdu"):
            for layer in packet.layers:
                        
                        nas_pdu_hex = packet.s1ap.nas_pdu
                        nas_pdu_hex = nas_pdu_hex.replace(":", "")
                        if (nas_pdu_hex.startswith('075200')):
                            
                            
                            rand = nas_pdu_hex[6:38]
                            print("Rand:", rand)
                            autn = nas_pdu_hex[40:]
                            print("Autn:", autn)
                            # capture.stop()
                            segunda_parte(rand,autn)
                            return
                            

                        







if __name__ == "__main__":
    main()
