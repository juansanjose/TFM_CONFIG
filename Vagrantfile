Vagrant.configure("2") do |config|

  config.vm.define "router" do |cfg|
    cfg.vm.box = "ubuntu/jammy64"
    cfg.vm.hostname = "router"
    
    cfg.vm.network "private_network", ip: "192.168.10.10"
    cfg.vm.network "private_network", ip: "192.168.152.10"
    cfg.vm.network "private_network", ip: "192.168.68.10"

    cfg.vm.provider "virtualbox" do |vb, override|
      vb.gui = true
      vb.name = "router"
      vb.customize ["modifyvm", :id, "--memory", 512]
      vb.customize ["modifyvm", :id, "--cpus", 2]
      vb.customize ["modifyvm", :id, "--vram", "32"]
      vb.customize ["modifyvm", :id, "--nicpromisc2", "allow-all"]
      vb.customize ["modifyvm", :id, "--clipboard", "bidirectional"]
      vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      vb.customize ["setextradata", "global", "GUI/SuppressMessages", "all" ]
    end
    cfg.vm.provision 'shell',run: "always", inline: <<-SHELL
    echo 1 > /proc/sys/net/ipv4/ip_forward

      SHELL

  end
  config.vm.define "gNB" do |cfg|
    cfg.vm.box = "fasmat/ubuntu2204-desktop"
    cfg.vm.hostname = "gNB"
    
   
    cfg.vm.network "private_network", ip: "192.168.152.11",gateway: "192.168.152.10", dns: "8.8.8.8" 
    cfg.vm.network "private_network", ip: "192.168.10.121",gateway: "192.168.10.10", dns: "8.8.8.8" 

    cfg.vm.provider "virtualbox" do |vb, override|
      vb.gui = true
      vb.name = "gNB"
      vb.customize ["modifyvm", :id, "--memory", 2048]
      vb.customize ["modifyvm", :id, "--cpus", 2]
      vb.customize ["modifyvm", :id, "--vram", "32"]
      vb.customize ["modifyvm", :id, "--nicpromisc2", "allow-all"]
      vb.customize ["modifyvm", :id, "--clipboard", "bidirectional"]
      vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      vb.customize ["setextradata", "global", "GUI/SuppressMessages", "all" ]
    end
      cfg.vm.provision 'shell',run: "always", inline: <<-SHELL
      # sudo ip route del default via 10.0.2.2
      # sudo ip route add default via 192.168.152.10
      sudo ip route add 192.168.0.0/16 via 192.168.152.10

    SHELL

   
  end
config.vm.define "gNB-falso" do |cfg|
    cfg.vm.box = "fasmat/ubuntu2204-desktop"
    cfg.vm.hostname = "gNB-falso"
    
   
    cfg.vm.network "private_network", ip: "192.168.152.88",gateway: "192.168.152.10", dns: "8.8.8.8" 

    cfg.vm.provider "virtualbox" do |vb, override|
      vb.gui = true
      vb.name = "gNB-falso"
      vb.customize ["modifyvm", :id, "--memory", 2048]
      vb.customize ["modifyvm", :id, "--cpus", 2]
      vb.customize ["modifyvm", :id, "--vram", "32"]
      vb.customize ["modifyvm", :id, "--nicpromisc2", "allow-all"]
      vb.customize ["modifyvm", :id, "--clipboard", "bidirectional"]
      vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      vb.customize ["setextradata", "global", "GUI/SuppressMessages", "all" ]
    end
      cfg.vm.provision 'shell',run: "always", inline: <<-SHELL
      # sudo ip route del default via 10.0.2.2
      # sudo ip route add default via 192.168.152.10
      sudo ip route add 192.168.0.0/16 via 192.168.152.10

    SHELL

   
  end
  config.vm.define "CORE" do |cfg|
    cfg.vm.box = "fasmat/ubuntu2204-desktop"
    cfg.vm.hostname = "CORE"
    
   
    cfg.vm.network "private_network", ip: "192.168.10.20",gateway: "192.168.10.10", dns: "8.8.8.8" 
    cfg.vm.network "private_network", ip: "192.168.10.111",gateway: "192.168.10.10", dns: "8.8.8.8"
    cfg.vm.network "private_network", ip: "192.168.10.112",gateway: "192.168.10.10", dns: "8.8.8.8"

    cfg.vm.provider "virtualbox" do |vb, override|
      vb.gui = true
      vb.name = "CORE"
      vb.customize ["modifyvm", :id, "--memory", 1512]
      vb.customize ["modifyvm", :id, "--cpus", 2]
      vb.customize ["modifyvm", :id, "--vram", "32"]
      vb.customize ["modifyvm", :id, "--nicpromisc2", "allow-all"]
      vb.customize ["modifyvm", :id, "--clipboard", "bidirectional"]
      vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      vb.customize ["setextradata", "global", "GUI/SuppressMessages", "all" ]
    end
    cfg.vm.provision 'shell',run: "always", inline: <<-SHELL
    # sudo ip route del default via 10.0.2.2
    # sudo ip route add default via 192.168.10.10
    sudo ip route add 192.168.0.0/16 via 192.168.10.10

    SHELL

   
  end

  config.vm.define "srsUE" do |cfg|
    cfg.vm.box = "fasmat/ubuntu2204-desktop"
    cfg.vm.hostname = "srsUE"
    
   
    cfg.vm.network "private_network", ip: "192.168.68.32",gateway: "192.168.68.10", dns: "8.8.8.8" 
    cfg.vm.network "private_network", ip: "192.168.10.122",gateway: "192.168.10.10", dns: "8.8.8.8" 
    

    cfg.vm.provider "virtualbox" do |vb, override|
      vb.gui = true
      vb.name = "srsUE"
      vb.customize ["modifyvm", :id, "--cableconnected1", "on"]
      vb.customize ["modifyvm", :id, "--memory", 2048]
      vb.customize ["modifyvm", :id, "--cpus", 2]
      vb.customize ["modifyvm", :id, "--vram", "32"]
      vb.customize ["modifyvm", :id, "--nicpromisc2", "allow-all"]
      vb.customize ["modifyvm", :id, "--clipboard", "bidirectional"]
      vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      vb.customize ["setextradata", "global", "GUI/SuppressMessages", "all" ]
    end
    cfg.vm.provision 'shell',run: "always", inline: <<-SHELL
    # sudo ip route del default via 10.0.2.2
    # sudo ip route add default via 192.168.10.10
    sudo ip route add 192.168.0.0/16 via 192.168.10.10

    SHELL

   
  end
  config.vm.define "U-PLANE" do |cfg|
    cfg.vm.box = "fasmat/ubuntu2204-desktop"
    cfg.vm.hostname = "Uplane"
    
   
    cfg.vm.network "private_network", ip: "192.168.10.113",gateway: "192.168.10.10", dns: "8.8.8.8" 
    cfg.vm.network "private_network", ip: "192.168.10.114",gateway: "192.168.10.10", dns: "8.8.8.8" 

    cfg.vm.provider "virtualbox" do |vb, override|
      vb.gui = true
      vb.name = "Uplane"
      vb.customize ["modifyvm", :id, "--memory", 1512]
      vb.customize ["modifyvm", :id, "--cpus", 2]
      vb.customize ["modifyvm", :id, "--vram", "32"]
      vb.customize ["modifyvm", :id, "--nicpromisc2", "allow-all"]
      vb.customize ["modifyvm", :id, "--clipboard", "bidirectional"]
      vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      vb.customize ["setextradata", "global", "GUI/SuppressMessages", "all" ]
    end
    cfg.vm.provision 'shell',run: "always", inline: <<-SHELL
    # sudo ip route del default via 10.0.2.2
    # sudo ip route add default via 192.168.10.10
    sudo ip route add 192.168.0.0/16 via 192.168.10.10
    sudo ip tuntap add name ogstun mode tun
    sudo ip addr add 10.45.0.1/16 dev ogstun
    sudo ip link set ogstun up
    echo 1 > /proc/sys/net/ipv4/ip_forward
    sudo iptables -t nat -A POSTROUTING -s 10.45.0.0/16 ! -o ogstun -j MASQUERADE


    SHELL

   
  end
  
end
