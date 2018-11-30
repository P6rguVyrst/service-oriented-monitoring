TODO:
 - Remove static constants and use environment variables instead.


terraform output -module=security_group
terraform output -module=hopper
terraform output -module=kubernetes

ssh root@<public-ip> -A 'ssh root@<internal-ip> ip a'
