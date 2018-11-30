variable "server_count" {
  default     = "3"
  description = "The number of nomad servers to launch."
}

variable "security_group" {
  description = "Security Group to place servers in"
}

variable "bastion_host" {
  description = "IP of bastion host used for provisioning"
}

data "scaleway_image" "debian_stretch" {
  architecture = "x86_64"
  name         = "Debian Stretch"
}

resource "scaleway_server" "server" {
  count               = "${var.server_count}"
  name                = "k8s-${count.index + 1}"
  image               = "${data.scaleway_image.debian_stretch.id}"
  type                = "VC1S"
  dynamic_ip_required = true
  
  tags = ["cluster", "k8s"]

  security_group = "${var.security_group}"

  connection {
    type         = "ssh"
    user         = "toomas"
    host         = "${self.private_ip}"
    bastion_host = "${var.bastion_host}"
    bastion_user = "toomas"
    agent        = true
  }
}


output "public_ips" {
  value = "${list(scaleway_server.server.*.public_ip)}"
}

output "private_ips" {
  value = "${list(scaleway_server.server.*.private_ip)}"
}
