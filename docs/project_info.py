# Project-specific configuration for Sphinx documentation.
# This file contains settings that vary per repository.
# The main conf.py imports these values and can be synced across all repos.

# Project name (used for titles, headers, and Sphinx internals)
project = "IATI Unified Platform"

# Eyebrow text (small label above the page title)
eyebrow_text = "IATI Tools: Documentation"

# GitHub repository URL (for "Edit on GitHub" links)
github_repository = "https://github.com/IATI/iati-unified-platform-docs"

# Supported languages for the documentation
languages = ["en"]

redoc = [
    {
        "name": "IATI Bulk Data Service API",
        "page": "api-docs/bulk-data-service-api",
        "spec": "specifications/iati-bulk-data-service-api.yaml",
        "embed": False,
        "template": "_templates/redoc-custom.j2",
    },
    {
        "name": "IATI Register Your Data API",
        "page": "api-docs/register-your-data-api",
        "spec": "specifications/iati-register-your-data-api.yaml",
        "embed": False,
        "template": "_templates/redoc-custom.j2",
    },
    {
        "name": "IATI Dashboard API",
        "page": "api-docs/dashboard-api",
        "spec": "specifications/iati-dashboard-api.yaml",
        "embed": False,
        "template": "_templates/redoc-custom.j2",
    },
    {
        "name": "IATI Dashboard CKAN Backwards Compatible API",
        "page": "api-docs/dashboard-ckan-backwards-compatible-api",
        "spec": "specifications/iati-dashboard-limited-ckan-backwards-compatible-api.yml",
        "embed": False,
        "template": "_templates/redoc-custom.j2",
    },
]
