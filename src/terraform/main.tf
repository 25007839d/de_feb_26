resource "google_storage_bucket" "terraform_demo" {
  name     = "${var.project_id}-terraform-demo"
  location = var.region

  uniform_bucket_level_access = true
}