variable "token" {
    type = string
}

variable "name" {
    type = string
}

variable "instance_count" {
    type = number
    default = 1
}

variable "template" {
    type = string
    default = "CentOS-7"
}

variable "ram" {
    type = number
    default = 6144
}

variable "start_ip_octet" {
    type = number
}

variable "zpool_name" {
    type = string
    default = "antlets"
}

variable "compression" {
    type = string
    default = "off"
}

variable "autostart" {
    type = bool
    default = true
}

variable "cpu" {
    type = number 
    default = 1
}