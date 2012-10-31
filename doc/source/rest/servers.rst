Servers
=======

Contents:

.. toctree::
   :maxdepth: 2


.. http:get:: /servers/(uuid:server_id)

   Lists all configured DNS servers

   **Example request**:

   .. sourcecode:: http

      GET /servers HTTP/1.1
      Host: example.com
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      [
        {
          "id": '',
          "name": '',
          "ipv4": '',
          "ipv6": '',
          "created_at": null,
          "updated_at": null
        },
        {
          "id": '',
          "name": '',
          "ipv4": '',
          "ipv6": '',
          "created_at": null,
          "updated_at": null
        }
      ]

   :statuscode 200: Success
   :statuscode 401: Access Denied


.. http:post:: /servers/(uuid:server_id)

   Adds a DNS server

   **Example request**:

   .. sourcecode:: http

      POST /servers HTTP/1.1
      Host: example.com
      Accept: application/json

   The body of the request will be a JSON-encoded set of data about
   the image to add to the registry. It will be in the following format::

   {'id': <UUID>,
    'name': <FQDN>,
    'ipv4': <IP ADDRESS>}

   * ``id`` must be a uuid in hexadecimal string notation
   (i.e. '71c675ab-d94f-49cd-a114-e12490b328d9')

   * ``name`` must be non-empty, FQDN value 
   (i.e. dnsaas.example.net)

   * ``ipv4`` must be non-empty, IP V4 value  
   (i.e. '192.168.1.120')

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json
      Content-Length: 250
      Location: http://localhost:9001/v1/servers/12345678-abcd-ef12-3456-7890abcdef12
      Date: Wed, 31 Oct 2012 19:59:32 GMT

      { 
        "name": "dnsaas.example.net",
        "id": "12345678-abcd-ef12-3456-7890abcdef12",
        "created_at": "2012-10-31T19:59:32.540961",
        "schema": "/v1/schemas/server",
        "self": "/v1/servers/12345678-abcd-ef12-3456-7890abcdef12",
        "ipv4": "1.2.3.4"
      }

   :statuscode 200: Success
   :statuscode 401: Access Denied

