resource "google_storage_bucket" "iot_data_lake" {

  name          = "raw_department_data"

  location      = "ASIA"

  force_destroy = true

  uniform_bucket_level_access = true

}

# ========== bucket object
# Existing Bucket
resource "google_storage_bucket_object" "spark_scripts_folder" {
  name    = "spark_script/"
  bucket  = "raw_department_data"
  content = " "
  depends_on = [
    google_storage_bucket.iot_data_lake
  ]
}

resource "google_storage_bucket_object" "raw_data_folder" {
  name    = "row_data/"
  bucket  = "raw_department_data"
  content = " "
  depends_on = [
       google_storage_bucket.iot_data_lake
  ]
}
