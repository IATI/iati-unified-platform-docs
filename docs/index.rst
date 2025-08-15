*********************
IATI Unified Platform
*********************

The IATI Unified Platform is an integrated suite of tools for managing and analysing data reported to IATI. 

Accessing Data 
--------------

IATI provides a number of tools to access IATI data. For more information and to choose the most appropriate one for you, see the `Tools & Resources page on the IATI website <https://iatistandard.org/en/iati-tools-and-resources/>`_ 


Platform Overview
-----------------

The IATI Registry is the list of URLs provided by reporting organisations for publication of their IATI data. It is provided at iatiregistry.org 


.. caution::

   The IATI Registry will be replaced in late 2025 with a completely new system. The Registry will then be accessed via the IATI Dashboard



The Data Getter runs on a continuous basis to maintain a copy of every file listed in the IATI Registry. Changes to published data can be reflected in as little as an hour, but may take up to 24 hours depending on the reporting organisation's technical configuration. Bulk downloads, debug information and listings are available from the Bulk Data Service. 

All downloaded files are passed to the :ref:`Validator`, which assesses them against the IATI Standard. Validation reports are available on the web and via API. 

Data access tools import data that has been downloaded by the Data Getter and use information from the Validator to decide which data to use. 


.. caution::

    D-portal does not use the Unified Platform; refer to its documentation to understand how it works


TODO: explain a bit more about how data gets into the tools, using admonitions to explain weirdness and forthcoming changes

TODO: explain the Dashboard 



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

    Data Getter <datagetter>
    Validator <validator>

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 3
    :caption: Datastore

    Datastore <datastore>






