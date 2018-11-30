
variable "nomad_ports" {
  # Denies all but these ports. TODO: Whitelist ports I want. 
  default = [80, 443]
}

resource "scaleway_security_group" "cluster" {
  name        = "cluster"
  description = "cluster-sg"
}

resource "scaleway_security_group_rule" "accept-internal" {
  security_group = "${scaleway_security_group.cluster.id}"

  action    = "accept"
  direction = "inbound"

  ip_range = "10.1.0.0/16"
  protocol = "TCP"
}

resource "scaleway_security_group_rule" "drop-external" {
  security_group = "${scaleway_security_group.cluster.id}"

  action    = "drop"
  direction = "inbound"
  ip_range  = "0.0.0.0/0"
  protocol  = "TCP"

  port  = "${element(var.nomad_ports, count.index)}"
  count = "${length(var.nomad_ports)}"
  
  depends_on = ["scaleway_security_group_rule.accept-internal"]
}

output "id" {
  value = "${scaleway_security_group.cluster.id}"
}
