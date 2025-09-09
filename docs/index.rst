*********************
IATI Unified Platform
*********************

The IATI Unified Platform is an integrated suite of tools for managing and analysing data reported to IATI. 

Accessing Data 
--------------

IATI provides a number of tools to access IATI data. For more information and to choose the most appropriate one for you, see the `Tools & Resources page on the IATI website <https://iatistandard.org/en/iati-tools-and-resources/>`_ 


Platform Overview
-----------------

The IATI Registry is the list of URLs provided by reporting organisations for publication of their IATI data. It is provided at `iatiregistry.org <https://iatiregistry.org>`_.


.. caution::

   The IATI Registry will be replaced in late 2025 with a completely new system. The Registry will then be accessed via the IATI Dashboard



The Bulk Data Service runs on a continuous basis to maintain a copy of every file listed in the IATI Registry. Changes to published data can be reflected in as little as an hour, but may take up to 24 hours depending on the reporting organisation's technical configuration. Bulk downloads, debug information and download session listings are available from the Bulk Data Service. 

All downloaded files are passed to the :ref:`Validator`, which assesses them against the IATI Standard. Validation reports are available on the web and via API. 

Data access tools import data that has been downloaded by the Bulk Data Service and use information from the Validator to decide which data to use. 


.. caution::

    D-portal does not use the Unified Platform. Please refer to the `D-portal documentation <https://docs.d-portal.org/en/latest/>`_ to understand how it works.


The :ref:`Datastore` saves all IATI activities, budgets and transactions from files that do not contain critical errors into a document store database and provides extensive querying and filtering capabilities. The Datastore can be accessed via a website and an API.

The :ref:`Dashboard` provides a range of summaries, statistics and computed metrics of IATI data. In addition to summarising current IATI data, it provides historical data for most of the metrics of which it keeps track.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 3
    :caption: Unified Platform

    Overview <self>

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 3
    :caption: Pipeline

    Bulk Data Service <bulk-data-service>

    Validator <validator>

    Datastore <datastore>

    Dashboard <dashboard>

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 3
    :caption: Register Your Data

    Register Your Data API <register-your-data-api>

    Register Your Data API Migration Notes <register-your-data-api-migration>

