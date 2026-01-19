*********************
IATI Unified Platform
*********************

The IATI Unified Platform is the data platform operated by the IATI Secretariat. It provides tools for registering published IATI data and downloading IATI data in various forms. 

Accessing Data 
--------------

IATI provides a number of tools to access IATI data. For more information and to choose the most appropriate one for you, see the `Tools & Resources page on the IATI website <https://iatistandard.org/en/iati-tools-and-resources/>`_ 


Platform Overview
-----------------

Register Your Data service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The IATI Registry was replaced in December 2025. We have written a :ref:`developers guide <new_registry_dev_guide>` to help adapt tools to work with the new set up.

Information about reporting organisations and their IATI files is now available on the `IATI Dashboard <https://dashboard.iatistandard.org/publishers/>`_.

Reporting organisations can manage their IATI file information in `IATI Account <https://account.iatistandard.org/>`_.


Bulk Data Service
~~~~~~~~~~~~~~~~~

The Bulk Data Service runs on a continuous basis to maintain a copy of every file listed in the IATI Registry. Changes to published data can be reflected in as little as an hour, but may take up to 24 hours depending on the reporting organisation's technical configuration. Bulk downloads, debug information and download session listings are available from the Bulk Data Service. 

Validator
~~~~~~~~~

All downloaded files are passed to the :ref:`Validator`, which assesses them against the IATI Standard. Validation reports are available on the web and via API. 

Data Access Tools
~~~~~~~~~~~~~~~~~

Data access tools import data that has been downloaded by the Bulk Data Service and use information from the Validator to decide which data to use. 

.. caution::

    D-portal does not use the Unified Platform. Please refer to the `D-portal documentation <https://docs.d-portal.org/en/latest/>`_ to understand how it works.


The :ref:`Datastore` saves all IATI activities, budgets and transactions from files that do not contain critical errors into a document store database and provides extensive querying and filtering capabilities. The Datastore can be accessed via a website and an API.

IATI Dashboard
~~~~~~~~~~~~~~

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
    :caption: IATI Registry Replacement

    Developer Guide <developer-guide-registry-replacement>


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
    :caption: Register Data

    Register Your Data API <register-your-data-api>

