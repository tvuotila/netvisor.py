# -*- coding: utf-8 -*-
"""
    netvisor.schemas.sales_invoices.get
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2015 by Fast Monkeys Oy.
    :license: MIT, see LICENSE for more details.
"""
from marshmallow import Schema, fields

from ..common import DateSchema, DecimalSchema, StringSchema
from ..fields import Boolean, Decimal


class VatPercentageSchema(Schema):
    percentage = Decimal(required=True, load_from='#text')
    code = fields.String(required=True, load_from='@vatcode')


class SalesInvoiceProductLineSchema(Schema):
    name = fields.String(load_from='product_name')
    identifier = fields.Nested(
        StringSchema,
        load_from='productidentifier'
    )
    unit_price = Decimal(load_from='product_unit_price')
    quantity = Decimal(load_from='sales_invoice_product_line_quantity')
    discount_percentage = Decimal(
        load_from='sales_invoice_product_line_discount_percentage'
    )
    free_text = fields.String(
        allow_none=True,
        load_from='sales_invoice_product_line_free_text'
    )
    accounting_account_suggestion = fields.String(allow_none=True)
    sum = Decimal(load_from='sales_invoice_product_line_sum')
    vat_percentage = fields.Nested(
        VatPercentageSchema,
        load_from='product_vat_percentage'
    )
    vat_sum = Decimal(load_from='sales_invoice_product_line_vat_sum')


class InvoiceLineSchema(Schema):
    product_lines = fields.List(
        fields.Nested(SalesInvoiceProductLineSchema),
        load_from='sales_invoice_product_line'
    )


@InvoiceLineSchema.preprocessor
def preprocess_invoice_line(schema, input_data):
    if input_data:
        return input_data['product_lines']


class InvoiceLinesSchema(Schema):
    invoice_line = fields.Nested(InvoiceLineSchema)


@InvoiceLinesSchema.preprocessor
def preprocess_invoice_lines(schema, input_data):
    if input_data:
        return input_data['invoice_line']


class GetSalesInvoiceSchema(Schema):
    number = fields.Integer(
        required=True,
        load_from='sales_invoice_number'
    )
    date = fields.Nested(
        DateSchema,
        required=True,
        load_from='sales_invoice_date'
    )
    delivery_date = fields.Nested(
        DateSchema,
        required=True,
        load_from='sales_invoice_delivery_date'
    )
    due_date = fields.Nested(
        DateSchema,
        required=True,
        load_from='sales_invoice_due_date'
    )
    reference_number = fields.String(
        required=True,
        load_from='sales_invoice_referencenumber'
    )
    amount = fields.Nested(
        DecimalSchema(),
        required=True,
        load_from='sales_invoice_amount'
    )
    delivery_method = fields.String(
        required=True,
        allow_none=True
    )
    delivery_term = fields.String(
        required=True,
        allow_none=True
    )
    free_text_after_lines = fields.String(
        required=True,
        allow_none=True,
        load_from='sales_invoice_free_text_after_lines'
    )
    free_text_before_lines = fields.String(
        required=True,
        allow_none=True,
        load_from='sales_invoice_free_text_before_lines'
    )
    payment_term_cash_discount = fields.Nested(DecimalSchema)
    payment_term_cash_discount_days = fields.Integer(allow_none=True)
    payment_term_net_days = fields.Integer(allow_none=True)
    invoicing_customer_name = fields.String(required=True)
    invoicing_customer_address_line = fields.String(
        allow_none=True,
        required=True,
        load_from='invoicing_customer_addressline'
    )
    invoicing_customer_post_number = fields.String(
        allow_none=True,
        required=True,
        load_from='invoicing_customer_postnumber'
    )
    invoicing_customer_town = fields.String(allow_none=True, required=True)
    invoicing_customer_country_code = fields.String(required=True)
    delivery_address_name = fields.String(allow_none=True, required=True)
    delivery_address_line = fields.String(allow_none=True, required=True)
    delivery_address_post_number = fields.String(
        allow_none=True,
        required=True,
        load_from='delivery_address_postnumber'
    )
    delivery_address_town = fields.String(allow_none=True, required=True)
    delivery_address_country_code = fields.String(
        allow_none=True,
        required=True
    )
    our_reference = fields.String(
        allow_none=True,
        load_from='sales_invoice_our_reference'
    )
    your_reference = fields.String(
        allow_none=True,
        load_from='sales_invoice_your_reference'
    )
    private_comment = fields.String(
        allow_none=True,
        load_from='sales_invoice_private_comment'
    )
    seller_identifier = fields.Nested(StringSchema)
    invoice_status = fields.String(required=True)
    invoice_lines = fields.Nested(InvoiceLinesSchema)
    match_partial_payments_by_default = Boolean(true='Yes', false='No')
