variable "region" {
  default = "ap-south-1"
}

variable "vpc_id" {
  default = "vpc-0c74bf30515d7ba0c"
}

variable "private_subnet_ids" {
  default = [
    "subnet-02845f5899d7b33ae",
    "subnet-08f59c7529f614f9e"
  ]
}

variable "cluster_name" {
  default = "visa-advisor-eks"
}

variable "node_instance_type" {
  default = "t3.medium"
}

variable "desired_nodes" {
  default = 2
}

variable "max_nodes" {
  default = 5
}

variable "min_nodes" {
  default = 2
}