provider "scaleway" {}

module "security_group" {
  source = "./modules/security_group"
}

module "hopper" {
  source = "./modules/hopper"
  security_group = "${module.security_group.id}"
}
