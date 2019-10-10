# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
config.vm.box = "centos/7"
  
config.vm.synced_folder "./shared", "/opt/pydev/shared"

config.vm.provider "virtualbox" do |vb|

config.vm.provision "shell", path:"install.sh"

config.vm.provision "shell", inline: <<-SHELL

  yum -y update
  yum -y builddep 
  yum -y yum-utils
  yum -y make
  yum -y wget
  yum -y gcc
  yum -y openssl-devel
  yum -y bzip2-devel
  yum -y libffi-devel
  yum -y install https://centos7.iuscommunity.org/ius-release.rpm

  mkdir /opt/pydev/
  mkdir /opt/pydev/shared
  cd /opt/pydev/
  SHELL
end
