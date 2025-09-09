==================================
Register Your Data Migration Notes
==================================

The IATI registry will be replaced by a new system in late 2025 and **all write operations**
to the registry will happen via the Register Your Data API.  General read operations that are not associated with updating/creating records are to be performed using the Dashboard API.

View the full `API specification`_.

.. _API specification: /api-docs/register-your-data-api.html

Language
--------
CKAN used the language of Publisher, Package (and Resource) and User.  In the new IATI
registry we use language of Reporting Organisation, Dataset and User to bring this closer
to the IATI standard.  Furthermore, in CKAN each Package also had a separate Resource because CKAN supported a model where a single package could have more than one file.  In the new IATI
registry a dataset is a combination of Package and Resource.

Remarks on the design of the new registry
-----------------------------------------
In CKAN there is a strong relationship between a dataset and the user that created it.  As
a result when an organisation is deleted in CKAN its datasets can still exist in IATI and be visible in the pipeline.  The new Registry removes this strong connection.  Datasets are
owned by reporting organisations.  When a reporting organisation is deleted, its datasets will
also be deleted.

For these reasons we do not provide an endpoint to return all the datasets that a user has access to. This could encourage an opportunity for a user to inadvertently modify a dataset. For example, if a user had the permission to update dataset metadata for multiple organisations and was carrying out a task to change the licence for all the datasets published by one organisation, they could easily inadvertently modify the licence for datasets owned by another organisation.

For the new Registry we have moved away from using organisation and dataset short names as
primary keys and towards using UUIDs.  For example, rather than calling
``GET /reporting-orgs/bopinc`` you must use the UUID
``GET /reporting-orgs/08beaaaf-d007-402f-aca6-993a18082071``.  The short names still exist
in the registry, it is just that they will no longer be supported as primary keys.

Replacing CKAN API calls: Reporting Orgs (Publishers)
-----------------------------------------------------

List of reporting organisations: /organization_list
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To obtain a list of publishers in CKAN you call the `GET /organization_list <ckan_listpub_>`_
endpoint which allows you to fetch a list of all organisations.  In the new registry you
should call ``GET /reporting-orgs`` that will fetch a list of all reporting organisations
**to which the user has access**.  The endpoint will not return other reporting
organisations.  To achieve this you should make separate calls to the Dashboard API.

Showing reporting organisations details: /organization_show
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The details of a reporting organisation are available from the ``/reporting-orgs`` endpoint
but if you wish to fetch organisation details, similar to the CKAN `GET /organization_show <ckan_showpub_>`_ endpoint again then you can call ``GET /reporting-orgs/{oid}`` where ``oid`` is the UUID for the organisation you want to fetch.

Creating a new reporting organisation: /organization_create
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To create a new reporting organisation in CKAN you call the
`POST /organization_create <ckan_createpub_>`_ endpoint.  In the new registry you must call
``POST /reporting-orgs``.  Note that access to this endpoint is more restricted than
in the CKAN-based registry.  The access token must have the ``ryd:reporting_org:create``
OAuth scope which will only be available to a small number of client applications.

Updating a reporting organisation: /organization_patch and /organization_update
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To update a new reporting organisation in CKAN you either call the
`POST /organization_update <ckan_updatepub_>`_ or `POST /organization_patch <ckan_patchpub_>`_
endpoints.  The difference being that `update <ckan_updatepub_>`_ will remove all fields
not in the provided payload, and `patch <ckan_patchpub_>`_ will replace fields that are
provided.  In the new registry we only support updating organisation metadata using ``PATCH``
via the ``/reporting-orgs/{oid}`` endpoint where ``oid`` is the UUID for the organisation you want to update.

Deleting a reporting organisation: /organization_delete
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To delete an organisation in CKAN you call `POST /organization_delete <ckan_deletepub_>`_.  In
the new registry you must call ``DELETE /reporting-orgs/{oid}`` where ``oid`` is the UUID for the organisation you want to delete.

.. _ckan_listpub: https://iatistandard.org/en/iati-tools-and-resources/iati-registry/iati-registry-api/publisher-endpoints/#ListPub
.. _ckan_showpub: https://iatistandard.org/en/iati-tools-and-resources/iati-registry/iati-registry-api/publisher-endpoints/#APub
.. _ckan_createpub: https://iatistandard.org/en/iati-tools-and-resources/iati-registry/iati-registry-api/publisher-endpoints/#CreatePub
.. _ckan_updatepub: https://iatistandard.org/en/iati-tools-and-resources/iati-registry/iati-registry-api/publisher-endpoints/#UpdatePub
.. _ckan_patchpub: https://iatistandard.org/en/iati-tools-and-resources/iati-registry/iati-registry-api/publisher-endpoints/#PatchPub
.. _ckan_deletepub: https://iatistandard.org/en/iati-tools-and-resources/iati-registry/iati-registry-api/publisher-endpoints/#DeletePub

Replacing CKAN API calls: Datasets (Packages)
---------------------------------------------
In CKAN, getting lists of datasets could be achieved with ``/package_list`, ``/package_search` and ``/organization_show`` with the ``include_datasets=true`` query string.  This is now achieved with ``GET`` to ``/reporting-orgs/{oid}/datasets``.

Creating datasets
^^^^^^^^^^^^^^^^^
In CKAN calls to `POST /package_create <ckan_createpackage_>`_ will create a package and
associated resource.  In the new registry this is achieved with ``POST /datasets/``.

Viewing dataset metadata
^^^^^^^^^^^^^^^^^^^^^^^^
To view dataset (and resource) metadata in CKAN we call the `GET /package_show <ckan_getpackage_>`_
endpoint.  This is achieved with ``GET /datasets/{did}`` where ``did`` is the UUID of the
dataset you want to get.

Updating dataset metadata
^^^^^^^^^^^^^^^^^^^^^^^^^
To update a dataset in CKAN you either call the
`POST /package_update <ckan_updatepackage_>`_ or `POST /package_patch <ckan_patchpackage_>`_
endpoints.  The difference being that `update <ckan_updatepackage_>`_ will remove all fields
not in the provided payload, and `patch <ckan_patchpackage_>`_ will replace fields that are
provided.  In the new registry we only support updating organisation metadata using ``PATCH``
via the ``/datasets/{did}`` endpoint where ``did`` is the UUID for the dataset you want
to update.

Deleting a dataset
^^^^^^^^^^^^^^^^^^
To delete a dataset in CKAN you call `POST /package_delete <ckan_deletepackage_>`_ endpoint.
In the new registry this is achieved with ``DELETE /datasets/{did}``.

.. _ckan_createpackage: https://iatistandard.org/en/iati-tools-and-resources/iati-registry/iati-registry-api/packagedataset-endpoints/#CreateDS
.. _ckan_getpackage: https://iatistandard.org/en/iati-tools-and-resources/iati-registry/iati-registry-api/packagedataset-endpoints/#ADS
.. _ckan_updatepackage: https://iatistandard.org/en/iati-tools-and-resources/iati-registry/iati-registry-api/packagedataset-endpoints/#UpdateDS
.. _ckan_patchpackage: https://iatistandard.org/en/iati-tools-and-resources/iati-registry/iati-registry-api/packagedataset-endpoints/#PatchDS
.. _ckan_deletepackage: https://iatistandard.org/en/iati-tools-and-resources/iati-registry/iati-registry-api/packagedataset-endpoints/#DeleteDS


Example application flow
^^^^^^^^^^^^^^^^^^^^^^^^

Your application wants to show a list of the reporting organisations your user has access to, perhaps with a little bit of metadata associated with them, such as name, number of published datasets, IATI organisation identifier. A call to ``GET /reporting-orgs/?include_meta=yes`` will fetch a list of reporting organisations with metadata on those organisations.

Then your application wants to allow a user to open a page for an organisation that shows a list of datasets. Calling the ``GET /reporting-orgs/{oid}/datasets`` endpoint will return a list of datasets for that organisation and all the metadata associated with each dataset.

Perhaps the user wants to update one of those datasets. A call to ``PATCH /datasets/{did}`` will update the dataset metadata and return the updated dataset metadata.

Perhaps then the user wants to change some user permissions in their organisation (assuming they are an organisation admin). ``GET /reporting-orgs/{oid}/users`` will get a list of users associated with an organisation and their roles. With a list of users your user might then change the role via an interface and you can make that change with a call to ``PUT /users/{uid}/reporting-org/{oid}``.


Registry permissions: Authentication and Authorisation
------------------------------------------------------
Many calls to the CKAN API require an API token for authentication and authorisation.  This
was achieved by obtaining the API token from the `Registry UI <registry_api_>`_ and then
passing this to the CKAN API via the HTTP `Authorization` header.

.. _registry_api: https://iatistandard.org/en/iati-tools-and-resources/iati-registry/iati-registry-api/

Authentication
^^^^^^^^^^^^^^
Apart from machine-to-machine applications, authentication in the new registry is via single
sign-on to a user's IATI Account.  This will provide a short-lived access token that is scoped
for access to the Register Your Data API and should be passed (in a similar way to a CKAN API
token) in calls to the API.

Login via the identity service will also provide a list of *roles* in the id token.  The
two relevant roles for this API are:

+-----------------------------------+-------------------------------------------------------+
| Role                              | Description                                           |
+===================================+=======================================================+
| ``iati_register_your_data``       | User can use the Register Your Data API               |
+-----------------------------------+-------------------------------------------------------+
| ``iati_superadmin``               | User is a superadmin in IATI                          |
+-----------------------------------+-------------------------------------------------------+


Authorisation: Access Control
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Access control to the Register Your Data API is managed via OAuth scopes.  Applications should
request required scopes from the identity server when a user is logged in.  **It is important
to recognise that not all these scopes may be granted** and so you should check these
after login.

+-----------------------------------+-------------------------------------------------------+
| Scope                             | Description                                           |
+===================================+=======================================================+
| ``ryd``                           | Access controlled endpoints                           |
+-----------------------------------+-------------------------------------------------------+
| ``ryd:reporting_org``             | Access read-only reporting org endpoints              |
+-----------------------------------+-------------------------------------------------------+
| ``ryd:reporting_org:create``      | Create reporting orgs                                 |
+-----------------------------------+-------------------------------------------------------+
| ``ryd:reporting_org:update``      | Update reporting orgs                                 |
+-----------------------------------+-------------------------------------------------------+
| ``ryd:reporting_org:delete``      | Delete reporting orgs                                 |
+-----------------------------------+-------------------------------------------------------+
| ``ryd:reporting_org:users``       | List and request to be associated with a reporting org|
+-----------------------------------+-------------------------------------------------------+
| ``ryd:reporting_org:users:update``| Modify users associated with reporting orgs           |
+-----------------------------------+-------------------------------------------------------+
| ``ryd:dataset``                   | Create and read datasets                              |
+-----------------------------------+-------------------------------------------------------+
| ``ryd:dataset:update``            | Update datasets                                       |
+-----------------------------------+-------------------------------------------------------+
| ``ryd:dataset:delete``            | Delete datasets                                       |
+-----------------------------------+-------------------------------------------------------+


Authorisation: Fine Grained
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Permissions to modify specific reporting organisations and their datasets are controlled
through a fine-grained authorisation mechanism.  These are further grouped into
organisational roles: 

* **admin**: For organisation administrators.
* **editor**: For organisation and dataset editors.
* **contributors**: For data editors.

These are roughly analogous to CKAN's admin, editor and member. These can only be assigned
to a user for a particular organisation via calls to the Register Your Data API by an
organisation admin.

The table below shows the fine-grained authorisations that these organisational roles have:

+-------------------------------+---------------------------+---------------------------+---------------------------+
| Authorisation                 | .. centered:: Admin       | .. centered:: Editor      | .. centered:: Contributor |
+===============================+===========================+===========================+===========================+
| ``read-org``                  | .. centered::  x          | .. centered::  x          | .. centered::  x          |
+-------------------------------+---------------------------+---------------------------+---------------------------+
| ``update-org``                | .. centered::  x          | .. centered::  x          |                           |
+-------------------------------+---------------------------+---------------------------+---------------------------+
| ``delete-org``                | .. centered::  x          |                           |                           |
+-------------------------------+---------------------------+---------------------------+---------------------------+
| ``set-org-user-authz``        | .. centered::  x          |                           |                           |
+-------------------------------+---------------------------+---------------------------+---------------------------+
| ``read-dataset``              | .. centered::  x          | .. centered::  x          | .. centered::  x          |
+-------------------------------+---------------------------+---------------------------+---------------------------+
| ``create-dataset``            | .. centered::  x          | .. centered::  x          | .. centered::  x          |
+-------------------------------+---------------------------+---------------------------+---------------------------+
| ``update-dataset``            | .. centered::  x          | .. centered::  x          | .. centered::  x          |
+-------------------------------+---------------------------+---------------------------+---------------------------+
| ``update-dataset-visibility`` | .. centered::  x          |                           |                           |
+-------------------------------+---------------------------+---------------------------+---------------------------+
| ``delete-dataset``            | .. centered::  x          | .. centered::  x          |                           |
+-------------------------------+---------------------------+---------------------------+---------------------------+

Relative to an admin, an editor cannot:

* Delete an organisation.
* Change the public/private visiblity of a dataset.
* Modify the permissions of users associated with an organisation.

Relative to an editor, a contributor cannot:

* Update an organisation's metadata.
* Delete a dataset.
