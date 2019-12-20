# -*- coding: utf-8 -*-
"""
    netvisor.responses.sales_invoices
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from ..schemas import (
    GetSalesInvoiceSchema,
    RepliesSchema,
    SalesInvoiceListSchema
)
from .base import Response


class SalesInvoiceListResponse(Response):
    list = True
    schema_cls = SalesInvoiceListSchema
    tag_name = 'sales_invoice_list'


class GetSalesInvoiceResponse(Response):
    schema_cls = GetSalesInvoiceSchema
    tag_name = 'sales_invoice'


class CreateSalesInvoiceResponse(Response):
    schema_cls = RepliesSchema
    tag_name = 'replies'


class UpdateSalesInvoiceResponse(Response):
    schema_cls = None
    tag_name = None
