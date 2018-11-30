provider "scaleway" {}

module "kubernetes" {
  source = "./modules/kubernetes"

  security_group = "3f923273-e275-4d28-b127-de6e7dc7fc81"
  bastion_host   = "51.15.229.104"

}
