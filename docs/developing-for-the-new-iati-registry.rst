.. _new_registry_dev_guide:
====================================
Developing for the New IATI Registry
====================================

.. caution::

    The New IATI Registry is currently under development. If you believe that you will technically rely on the contents of these documents, please contact us to discuss your work.

.. contents::
   :depth: 3
   :local:

The IATI registry will be replaced by a new system in late 2025.  There are a number of architectural differences between the new registry and the current CKAN-based registry.  This document describes some of those architectural differences, and how applications will work with the new registry to aid in the transition of tools and infrastructure to the new registry.


Applications and Single Sign-On (SSO)
-------------------------------------
One of the key differences between the old CKAN-based registry and the new registry is the use of Single Sign-On (SSO) as the method of authentication.  This has been designed to simply the user experience and enable a range of third party integrations with IATI infrastructure.  However, to enable this enhanced functionality, applications will need to be refactored to facilitate SSO via our Identity Service.  Although we emphasise SSO (via OpenID Connect) we will also support some limited OAuth2-based authentication.  OAuth2/OpenID Connect interactions with the Identity Service will yield a short-lived access token that will be used to access an API for write access to the registry.  Details of how to use the access token are provided in the :ref:`Register Your Data API specification <register-your-data-api>`.

Third party tool providers that would like to connect to IATI infrastructure cannot do this without being registered in advance with the IATI Secretariat.  Through this registration process we will discuss your needs with you, will setup your application in the Identity Service, supply you with credentials to use when making calls to the Identity Service, and provide developer support.  We intend to support three modes of connection:

* Single Sign-On via OpenID Connect: in this mode client's will log users into their application using OpenID Connect and will obtain an access token that will permit access to the organisation(s) associated with that user.  This will be available at launch.

* Machine-to-machine applications: we will support connections using a Client Credentials OAuth2 grant.  These connections are far more limited in terms of the organisations and calls that can be made to the API.  We expect this to be available before the end of 2025.

* Account linking: we eventually expect to support clients that want to retain their own login system but facilitate linking to an existing IATI account.  This will not be available until 2026.

.. note::

    SSO will eventually be deployed out across IATI and will provide access for users to a range of services across the IATI ecosystem via a single user account.  If your application logs in a user then that user will now be logged into IATI and will also be able to access other tools.  The converse is also true, that a user may arrive at your application having already logged into IATI through SSO in another tool.

Restrictions
^^^^^^^^^^^^
Our new `Register Your Data API <../register-your-data-api>`_ implements the same functionality as present in the current CKAN-based registry but we have implemented additional per-application controls.  As a result, the functionality available to third party tools will be less permissive.  In particular:

* Third party applications will not be able to create new reporting organisations in the registry.
* Applications using machine-to-machine OAuth2 connections will not be able to modify any user permissions or delete organisations.


Access tokens and API tokens
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
CKAN moved from API keys to API tokens as a progression from more simplified application-level authentication to more specific user-centric authentication and authorisation.  The development of the new registry continues this progression and introduces **individual authentication with short-lived, auto-expiring access tokens**.  Any functionality that relies on using an API key or token generated in CKAN must be refactored to work with the new registry. An access token contains no information about what organisation(s) a user is attached to.  This information is only available via the :ref:`Register Your Data API <register-your-data-api>`.

To call the :ref:`Register Your Data API <register-your-data-api>` and write any changes to the registry a short-lived access token must be obtained from the IATI Identity Service (e.g., through single sign on, SSO) and passed to the API.  This should be passed to the API via the HTTP ``Authorization`` header as a ``Bearer`` token.  It is entirely possible that the token will automatically expire between SSO and an API call being made, so tools should be prepared to handle error messages from the API and refresh the access token. As explained above, applications that wish to obtain an access token to call the API must be registered in advance with the IATI Secretariat.


User permissions
----------------

In CKAN, per organisation user permissions are controlled with the roles *admin*, *editor*, and *member*.  In the new IATI registry we have two levels to user permissions: we have coarse access control that determines what endpoints an access token can reach, and *fine-grained* authorisation that determines what organisations and datasets can be changed, and what information can be changed.

Access Control: OAuth scopes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Access control to call certain API endpoints are restricted using OAuth2 scopes.  An application should request the scopes it requires as part of it's OIDC/OAuth2 flow with the Identity Service.  **It is important to recognise that not all these scopes may be granted** and so applications should should check these after the Identity Service flow has completed. If an API endpoint is called with an access token that does not have the required scopes, a 403 Forbidden HTTP response will be returned.  The :ref:`Register Your Data API specification <register-your-data-api>` lists the required scopes against each API endpoint.

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

Associated with this, a user with access to the :ref:`Register Your Data API <register-your-data-api>` will have ``iati_register_your_data`` as a ``role`` in the OAuth2 claims obtained from the Identity Service userinfo endpoint.

Fine-grained Authorisation
^^^^^^^^^^^^^^^^^^^^^^^^^^
Per organisation user permissions are controlled with a system of *fine-grained* authorisations similar to the permissions system in CKAN.  These control which organisations and datasets a user is able to access, and what changes they can make.  Similar to CKAN, we group these into three roles:

* **admin**: For organisation administrators.
* **editor**: For organisation and dataset editors.
* **contributors**: For data editors.

These are roughly analogous to CKAN's *admin*, *editor* and *member*. These can only be assigned to a user for a particular organisation via calls to the Register Your Data API by an organisation admin.

The table below shows the fine-grained authorisations that these organisational roles have:

.. list-table::
   :widths: 80 40 40 40
   :header-rows: 1

   * - Authorisation
     - .. centered:: Admin
     - .. centered:: Editor
     - .. centered:: Contributor
   * - ``read-org``
     - .. centered:: x
     - .. centered:: x
     - .. centered:: x
   * - ``update-org``
     - .. centered:: x
     - .. centered:: x
     -
   * - ``delete-org``
     - .. centered:: x
     -
     -
   * - ``set-org-user-authz``
     - .. centered:: x
     -
     -
   * - ``read-dataset``
     - .. centered:: x
     - .. centered:: x
     - .. centered:: x
   * - ``create-dataset``
     - .. centered:: x
     - .. centered:: x
     - .. centered:: x
   * - ``update-dataset``
     - .. centered:: x
     - .. centered:: x
     -
   * - ``update-dataset-visibility``
     - .. centered:: x
     -
     -
   * - ``delete-dataset``
     - .. centered:: x
     - .. centered:: x
     -

Relative to an admin, an editor cannot:

* Delete an organisation.
* Change the public/private visiblity of a dataset.
* Modify the permissions of users associated with an organisation.

Relative to an editor, a contributor cannot:

* Update an organisation's metadata.
* Delete a dataset.

Super-administration and other enhanced permissions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
IATI Secretariat staff will have a superadmin authorisation where their access tokens afford them full access to any organisation and dataset.  Superadmins can be identified by examining the ``role`` claim in the payload from the Identity Service userinfo endpoint and which should include ``iati_superadmin``.  However, API endpoints will return no organisation associations for these users.

To support third parties in developing tools and supporting the community, we have implemented a system of enhanced permissions that we refer to as *Provider Admin*.  This functionality means that a reporting organisation who wants assistance through a third party tool provider will be able to authorise that application provider to have enhanced privileges.  This will give some limited admin access to an organisation's records.

Augmenting SSO user data
------------------------
There is nothing in the SSO model that prevents third party tools from having additional user data or user permissions to suit the functionality of the tool.

Additional user data
^^^^^^^^^^^^^^^^^^^^
An example of this case might be that a tool wants to record the last dataset that a user was working on so that they can optionally return the user to that dataset upon login.

This functionality can be implemented by having a separate user database in the third party tool and where the user record in that database can be looked up using the unique identifier (``sub``) that is received from the Identity Service.  It is important to recognise however, that any personal data about that user (for example, their name or working country) could be changed between logins by the user.

Additional permissions
^^^^^^^^^^^^^^^^^^^^^^
Some example use cases might be:

* A tool that automatically generates XML files may want to add additional permissions such that some users can over-write an existing XML file, and some cannot.
* A tool that allows some users to edit dataset metadata for records that point to activity files, vs. organisation files.

These must be added on top of user permissions provided by the new registry and recorded separately, in a similar fashion to additional user data.  It is important to recognise that there is nothing to stop a user from logging into another tool and modifying data.  For example, if you add permissions to restrict users from modifying the metadata for different categories of XML dataset record, a user can still log into other tools and modify the data.

Key architectural changes
-------------------------
Naming and Identifying Resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
CKAN used the naming system of *Publisher*, *Package* (and associated *Resource(s)*) and *User*.  The new registry changes this language to bring the registry into line with the IATI Standard.

Publisher
~~~~~~~~~
In the new registry we describe a publisher as a **Reporting Organisation** following the IATI standard ``iati-organisation``, ``iati-organisations`` and ``reporting-org`` `elements <iati_standard_reporting_org_>`_.  Any reference to a reporting organisation or a reporting org should be read in the same way as a publisher in CKAN.

.. _iati_standard_reporting_org: https://iatistandard.org/en/iati-standard/203/organisation-standard/iati-organisations/iati-organisation/reporting-org/

Package (and Resource)
~~~~~~~~~~~~~~~~~~~~~~
In CKAN a dataset was comprised of a package with one (or potentially more) resources attached because CKAN supported a model where a single package could have more than one file.  In the new IATI registry a **Dataset** is a combination of Package and Resource.

Primary keys: organisation and dataset shortnames
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
For the new Registry we have moved away from using organisation and dataset short names as primary keys and towards using UUIDs.  For example, rather than calling ``GET /reporting-orgs/bopinc`` you must use the UUID ``GET /reporting-orgs/08beaaaf-d007-402f-aca6-993a18082071``.  The short names still exist in the new registry, it is just that they will no longer be supported as primary keys.


Relationships and Record Ownership
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Multiple organisations
~~~~~~~~~~~~~~~~~~~~~~
As with CKAN, in the new registry users can have permissions to administrate and manage metadata for more than one organisation.  For example, a user could be an admin for "Organisation A", admin for "Organisation B", and editor for "Organisation C".  Accordingly, the ``/reporting-orgs`` endpoints for the :ref:`Register Your Data API <register-your-data-api>` can return more than one organisation for a logged in user.  All tools that call the API should be able to handle a response that includes multiple organisations, even if they only expect a single organisation.

Dataset Ownership
~~~~~~~~~~~~~~~~~
In CKAN there is a strong relationship between a dataset and the user that created it.  As a result when an organisation is deleted in CKAN its datasets can still exist in IATI and be visible in the pipeline.  The new Registry removes this strong connection.  Datasets are owned by reporting organisations.  When a reporting organisation is deleted, its datasets will also be deleted.

Links will still exist between datasets and users, but no ownership is implied:

* We store the user that creates a dataset.
* We record lists of actions that are carried out on datasets (e.g., changing a URL) and which user made that change.

For these reasons we do not provide a :ref:`Register Your Data API <register-your-data-api>` endpoint to return all the datasets that a user has access to. This could encourage an opportunity for a user to inadvertently modify a dataset. For example, if a user had the permission to update dataset metadata for multiple organisations and was carrying out a task to change the licence for all the datasets published by one organisation, they could easily inadvertently modify the licence for datasets owned by another organisation.

Migration from the CKAN API to the Register Your Data API
---------------------------------------------------------
These notes are aimed at providing guidance for migrating from the CKAN API to the new :ref:`Register Your Data API <register-your-data-api>` by describing how equivalent operations are performed in the :ref:`Register Your Data API <register-your-data-api>`.

Reporting Orgs (Publishers)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

List of reporting organisations: /organization_list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To obtain a list of publishers in CKAN you call the `GET /organization_list <ckan_listpub_>`_ endpoint which allows you to fetch a list of all organisations.  In the new registry you should call ``GET /reporting-orgs`` that will fetch a list of all reporting organisations **to which the user has access**.  The endpoint will not return other reporting organisations.  To achieve this you should make separate calls to the Dashboard API.

Showing reporting organisations details: /organization_show
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The details of a reporting organisation are available from the ``/reporting-orgs`` endpoint but if you wish to fetch organisation details, similar to the CKAN `GET /organization_show <ckan_showpub_>`_ endpoint again then you can call ``GET /reporting-orgs/{oid}`` where ``oid`` is the UUID for the organisation you want to fetch.

Creating a new reporting organisation: /organization_create
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To create a new reporting organisation in CKAN you call the `POST /organization_create <ckan_createpub_>`_ endpoint.  In the new registry you must call ``POST /reporting-orgs``.  Note that access to this endpoint is more restricted than in the CKAN-based registry.  The access token must have the ``ryd:reporting_org:create`` OAuth scope which will only be available to a small number of client applications.

Updating a reporting organisation: /organization_patch and /organization_update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To update a new reporting organisation in CKAN you either call the `POST /organization_update <ckan_updatepub_>`_ or `POST /organization_patch <ckan_patchpub_>`_ endpoints.  The difference being that `update <ckan_updatepub_>`_ will remove all fields not in the provided payload, and `patch <ckan_patchpub_>`_ will replace fields that are provided.  In the new registry we only support updating organisation metadata using ``PATCH`` via the ``/reporting-orgs/{oid}`` endpoint where ``oid`` is the UUID for the organisation you want to update.

Deleting a reporting organisation: /organization_delete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To delete an organisation in CKAN you call `POST /organization_delete <ckan_deletepub_>`_.  In the new registry you must call ``DELETE /reporting-orgs/{oid}`` where ``oid`` is the UUID for the organisation you want to delete.

.. _ckan_listpub: https://iatistandard.org/en/iati-tools-and-resources/iati-registry/iati-registry-api/publisher-endpoints/#ListPub
.. _ckan_showpub: https://iatistandard.org/en/iati-tools-and-resources/iati-registry/iati-registry-api/publisher-endpoints/#APub
.. _ckan_createpub: https://iatistandard.org/en/iati-tools-and-resources/iati-registry/iati-registry-api/publisher-endpoints/#CreatePub
.. _ckan_updatepub: https://iatistandard.org/en/iati-tools-and-resources/iati-registry/iati-registry-api/publisher-endpoints/#UpdatePub
.. _ckan_patchpub: https://iatistandard.org/en/iati-tools-and-resources/iati-registry/iati-registry-api/publisher-endpoints/#PatchPub
.. _ckan_deletepub: https://iatistandard.org/en/iati-tools-and-resources/iati-registry/iati-registry-api/publisher-endpoints/#DeletePub


Datasets (Packages)
^^^^^^^^^^^^^^^^^^^
In CKAN, getting lists of datasets could be achieved with ``/package_list`, ``/package_search` and ``/organization_show`` with the ``include_datasets=true`` query string.  This is now achieved with ``GET`` to ``/reporting-orgs/{oid}/datasets``.

Creating datasets
~~~~~~~~~~~~~~~~~
In CKAN calls to `POST /package_create <ckan_createpackage_>`_ will create a package and associated resource.  In the new registry this is achieved with ``POST /datasets/``.

Viewing dataset metadata
~~~~~~~~~~~~~~~~~~~~~~~~
To view dataset (and resource) metadata in CKAN we call the `GET /package_show <ckan_getpackage_>`_ endpoint.  This is achieved with ``GET /datasets/{did}`` where ``did`` is the UUID of the dataset you want to get.

Updating dataset metadata
~~~~~~~~~~~~~~~~~~~~~~~~~
To update a dataset in CKAN you either call the `POST /package_update <ckan_updatepackage_>`_ or `POST /package_patch <ckan_patchpackage_>`_ endpoints.  The difference being that `update <ckan_updatepackage_>`_ will remove all fields not in the provided payload, and `patch <ckan_patchpackage_>`_ will replace fields that are provided.  In the new registry we only support updating organisation metadata using ``PATCH`` via the ``/datasets/{did}`` endpoint where ``did`` is the UUID for the dataset you want
to update.

Deleting a dataset
~~~~~~~~~~~~~~~~~~
To delete a dataset in CKAN you call `POST /package_delete <ckan_deletepackage_>`_ endpoint. In the new registry this is achieved with ``DELETE /datasets/{did}``.

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


