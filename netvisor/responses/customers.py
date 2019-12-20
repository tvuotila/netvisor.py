# -*- coding: utf-8 -*-
"""
    netvisor.responses.customers
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from ..schemas import CustomerListSchema, GetCustomerSchema, RepliesSchema
from .base import Response


class CustomerListResponse(Response):
    list = True
    schema_cls = CustomerListSchema
    tag_name = 'customerlist'


class GetCustomerResponse(Response):
    schema_cls = GetCustomerSchema
    tag_name = 'customer'


class CreateCustomerResponse(Response):
    schema_cls = RepliesSchema
    tag_name = 'replies'


class UpdateCustomerResponse(Response):
    schema_cls = None
    tag_name = None
