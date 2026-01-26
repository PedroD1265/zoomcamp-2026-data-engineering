terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "7.16.0"
    }
  }
}

provider "google" {
  project = "zoomcamp-2026-485518"
  region  = "us-central1"
}

resource "google_storage_bucket" "data_lake_bucket" {
  name          = "zoomcamp-2026-485518-data-lake-pedrod1265"
  location      = "US"
  force_destroy = true

  uniform_bucket_level_access = true
}

resource "google_bigquery_dataset" "dataset" {
  dataset_id                 = "zoomcamp_dataset"
  location                   = "US"
  delete_contents_on_destroy = true
}

