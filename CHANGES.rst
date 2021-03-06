Changelog
---------

Here you can see the full list of changes between each Netvisor.py release.

0.7.0 (September 19th, 2016)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Added support for getting accounting data.

0.6.0 (August 16th, 2016)
^^^^^^^^^^^^^^^^^^^^^^^^^

- Fixed compatibility with the latest version of xmltodict. Netvisor.py now
  requires xmltodict >= 0.10.1.
- Added support for customer's email invoicing address.
- Fixed case problem with product's unit price type.
- Added official Python 3.5 support.

0.5.0 (November 5th, 2015)
^^^^^^^^^^^^^^^^^^^^^^^^^^

- Added support for invoice line free text field when creating a sales invoice.

0.4.0 (September 28th, 2015)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Updated Marshmallow requirement to >= 2.0.0.
- Added support for additional address line when creating/updating a customer.

0.3.4 (September 10th, 2015)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Fixed UnicodeEncodeError when making a request containing non-ASCII
  characters.

0.3.3 (May 29th, 2015)
^^^^^^^^^^^^^^^^^^^^^^

- Fixed too strict validation for payment term fields returned by Netvisor API
  in ``netvisor.sales_invoices.get()``.

0.3.2 (April 30th, 2015)
^^^^^^^^^^^^^^^^^^^^^^^^

- Fixed ``netvisor.sales_invoices.get()`` crashing when the
  ``<SalesInvoiceAmount>`` element had attributes in the XML response.
- Fixed ``netvisor.sales_invoices.get()`` crashing when any of the following
  elements were empty in the XML response:

  - seller identifier
  - invoicing customer address line
  - invoicing customer post number
  - invoicing customer town
  - delivery address name
  - delivery address line
  - delivery address post number
  - delivery address town
  - delivery address country code
  - accounting account suggestion

- Fixed ``netvisor.sales_invoices.list()`` crashing when customer code was empty
  in the XML response.
- Fixed ``netvisor.sales_invoices.list()`` crashing when invoice status had no
  substatus in the XML response.

0.3.1 (April 29th, 2015)
^^^^^^^^^^^^^^^^^^^^^^^^

- Fixed ``netvisor.schemas`` package missing from the source distribution.

0.3.0 (April 29th, 2015)
^^^^^^^^^^^^^^^^^^^^^^^^

- Added official Python 3.4 support.
- Added creating and updating of customers and sales invoices.
- Changed response parsing not to rename and restructure the responses to keep
  the Python API implementation simpler and more consistent with the Netvisor
  API's XML responses.
- Changed response parsing to use Marshmallow.
- Changed ``Request`` to take ``params`` as a single keyword argument instead of
  as named variable-length arguments.
- Fixed tests to work with responses 0.3.0.

0.2.0 (April 8th, 2014)
^^^^^^^^^^^^^^^^^^^^^^^

- Added support for InvoiceNumber and InvoicesAboveNetvisorKey parameters to
  sales invoice listing.
- Changed xmltodict's dict constructor from ``OrderedDict`` to to ``dict``.
- Fixed parsing of sales invoice with multiple lines.

0.1.0 (March 26th, 2014)
^^^^^^^^^^^^^^^^^^^^^^^^

- Initial public release.
