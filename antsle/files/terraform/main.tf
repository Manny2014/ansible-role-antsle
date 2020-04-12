

provider "antsle" {
  api_key = "Token ${var.token}"
}


# This is just pseudo code. It won't actually work in Terraform.
resource "antsle_antlets" "antlet" {
  count = 3
  dname = "${var.name}-${count.index}"
  template = var.template
  ram = var.ram
  cpu = var.cpu
  antlet_num = "${var.start_ip_octet + count.index}"
  zpool_name = var.zpool_name
  compression = var.compression
  autostart = var.autostart
}