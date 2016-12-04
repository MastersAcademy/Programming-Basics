# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"

  config.vm.network  :forwarded_port, guest: 3080, host: 3080

  config.vm.hostname = "vagrant-1"
  config.vm.provision :shell, path: "install.sh"

end
