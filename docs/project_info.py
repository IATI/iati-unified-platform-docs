# Project-specific configuration for Sphinx documentation.
# This file contains settings that vary per repository.
# The main conf.py imports these values and can be synced across all repos.

from urllib.parse import urlparse

# Project name (used for titles, headers, and Sphinx internals)
project = "IATI Unified Platform"

# URL of the live tool this repo documents. None when the docs themselves
# are the deliverable (no separate tool to link).
tool_url = None

# Short label used in the nav. Defaults to ``project`` when None.
nav_label = None

# Eyebrow text (small label above the page title)
eyebrow_text = "IATI Tools: Documentation"

# GitHub repository URL (for "Edit on GitHub" links)
github_repository = "https://github.com/IATI/iati-unified-platform-docs"

# Plausible analytics domain, derived from tool_url so docs are tracked
# under the tool's site. Set to None to disable.
plausible_domain = "docs.unified-platform.iatistandard.org"

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
