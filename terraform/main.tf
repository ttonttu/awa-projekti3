terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "3.73.0"
    }
  }
  required_version = ">= 0.15.0"
}

provider "google" {
  credentials = var.credentials
  project     = var.project
  region      = var.region
  zone        = var.zone
}

# creates a VPC
resource "google_compute_network" "vpc_network" {
  project = var.project
  name = "doggo-vpc"
  auto_create_subnetworks = false
}

# creates one subnetwork
resource "google_compute_subnetwork" "subnetwork" {
  name = "pupperino-subnet"
  ip_cidr_range = "10.0.0.0/27"
  region = var.region
  network = google_compute_network.vpc_network.name
}

# firewall resources, open http and ssh
resource "google_compute_firewall" "allow_http_ssh" {
  name = "allow-http-ssh"
  network = google_compute_network.vpc_network.name
  direction = "INGRESS"
  allow {
    protocol = "tcp"
    ports = ["22","80"]
  }
  target_tags = ["ssh-http-allowed"]
}

# creates a vm instance to work as the server
resource "google_compute_instance" "vm_instance" {
  name         = "doge-serveri"
  machine_type = "n1-standard-1"
  tags = ["ssh-http-allowed"]
  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2004-lts"
    }
  }
  network_interface {
    network = google_compute_network.vpc_network.name
    subnetwork = google_compute_subnetwork.subnetwork.name
    access_config {
    }
  }
  metadata_startup_script   = "startup-script.sh"
  allow_stopping_for_update = true
}