variable "security_group" {
  description = "Security Group to place servers in"
}

data "scaleway_image" "debian_stretch" {
  architecture = "x86_64"
  name         = "Debian Stretch"
}

resource "scaleway_ip" "hopper" {
  server = "${scaleway_server.hopper.id}"
}

resource "scaleway_server" "hopper" {
  name = "hopper"
  image = "${data.scaleway_image.debian_stretch.id}"
  type  = "VC1S" 
  dynamic_ip_required = true

  tags = ["hopper"]

  security_group = "${var.security_group}"
}

output "public_ip" {
  value = "${scaleway_ip.hopper.ip}"
}
