# -*- coding: utf-8 -*-
import decimal
from datetime import date

import pytest

from netvisor.exc import InvalidData

from ..utils import get_response_content


class TestSalesInvoiceService(object):
    def test_get(self, netvisor, responses):
        responses.add(
            method='GET',
            url='http://koulutus.netvisor.fi/GetSalesInvoice.nv?NetvisorKey=5',
            body=get_response_content('GetSalesInvoice.xml'),
            content_type='text/html; charset=utf-8',
            match_querystring=True
        )
        sales_invoice = netvisor.sales_invoices.get(5)
        assert sales_invoice == {
            'number': 3,
            'date': date(2012, 1, 27),
            'delivery_date': date(2012, 1, 27),
            'due_date': date(2012, 2, 11),
            'reference_number': u'1070',
            'amount': decimal.Decimal(244.00),
            'seller': u'Jarmo',
            'status': u'Unsent',
            'free_text_before_lines': None,
            'free_text_after_lines': None,
            'our_reference': None,
            'your_reference': None,
            'private_comment': None,
            'billing_address': {
                'name': u'Matti Mallikas',
                'street': u'Pajukuja 1',
                'postal_code': u'53100',
                'post_office': u'Lappeenranta',
                'country': u'FINLAND',
            },
            'match_partial_payments_by_default': False,
            'delivery_address': {
                'name': u'Netvisor Oy',
                'street': u'Snelmanninkatu 12',
                'postal_code': u'53100',
                'post_office': u'LPR',
                'country': u'FINLAND',
            },
            'delivery_method': None,
            'delivery_term': None,
            'payment_term_net_days': 14,
            'payment_term_cash_discount_days': 5,
            'payment_term_cash_discount': decimal.Decimal('9'),
            'lines': [
                {
                    'product_code': u'OMENA',
                    'name': u'Omena',
                    'free_text': None,
                    'quantity': decimal.Decimal('2'),
                    'unit_price': decimal.Decimal('6.9000'),
                    'discount_percentage': decimal.Decimal('0'),
                    'vat': {
                        'percentage': decimal.Decimal('22'),
                        'code': u'KOMY',
                        'amount': decimal.Decimal('3.04'),
                    },
                    'amount': decimal.Decimal('16.84'),
                    'accounting_suggestion': u'551',
                },
                {
                    'product_code': u'BANAANI',
                    'name': u'Banaani',
                    'free_text': None,
                    'quantity': decimal.Decimal('1'),
                    'unit_price': decimal.Decimal('2.4900'),
                    'discount_percentage': decimal.Decimal('0'),
                    'vat': {
                        'percentage': decimal.Decimal('22'),
                        'code': u'KOMY',
                        'amount': decimal.Decimal('0.5478'),
                    },
                    'amount': decimal.Decimal('3.0378'),
                    'accounting_suggestion': u'551'
                }
            ]
        }

    def test_get_raises_error_if_sales_invoice_not_found(
        self, netvisor, responses
    ):
        responses.add(
            method='GET',
            url=(
                'http://koulutus.netvisor.fi/GetSalesInvoice.nv?'
                'NetvisorKey=123'
            ),
            body=get_response_content('GetSalesInvoiceNotFound.xml'),
            content_type='text/html; charset=utf-8',
            match_querystring=True
        )
        with pytest.raises(InvalidData) as excinfo:
            netvisor.sales_invoices.get(123)

        assert str(excinfo.value) == (
            'Data form incorrect:. '
            'Sales invoice not found with Netvisor identifier: 123'
        )

    def test_list(self, netvisor, responses):
        responses.add(
            method='GET',
            url='http://koulutus.netvisor.fi/SalesInvoiceList.nv',
            body=get_response_content('SalesInvoiceList.xml'),
            content_type='text/html; charset=utf-8',
            match_querystring=True
        )
        sales_invoices = netvisor.sales_invoices.list()
        assert sales_invoices == [
            {
                'id': 165,
                'number': 5,
                'date': date(2013, 11, 9),
                'status': u'open',
                'substatus': u'overdue',
                'reference_number': u'1070',
                'amount': decimal.Decimal('123.45'),
                'open_amount': decimal.Decimal('45.67'),
                'customer': {
                    'code': u'MM',
                    'name': u'Matti Meikäläinen',
                }
            }
        ]

    def test_empty_list(self, netvisor, responses):
        responses.add(
            method='GET',
            url='http://koulutus.netvisor.fi/SalesInvoiceList.nv',
            body=get_response_content('SalesInvoiceListEmpty.xml'),
            content_type='text/html; charset=utf-8',
            match_querystring=True
        )
        sales_invoices = netvisor.sales_invoices.list()
        assert sales_invoices == []

    def test_list_with_above_id(self, netvisor, responses):
        responses.add(
            method='GET',
            url=(
                'http://koulutus.netvisor.fi/SalesInvoiceList.nv?'
                'InvoicesAboveNetvisorKey=1000'
            ),
            body=get_response_content('SalesInvoiceListEmpty.xml'),
            content_type='text/html; charset=utf-8',
            match_querystring=True
        )
        sales_invoices = netvisor.sales_invoices.list(above_id=1000)
        assert sales_invoices == []

    def test_list_with_invoice_number(self, netvisor, responses):
        responses.add(
            method='GET',
            url=(
                'http://koulutus.netvisor.fi/SalesInvoiceList.nv?'
                'InvoiceNumber=5'
            ),
            body=get_response_content('SalesInvoiceList.xml'),
            content_type='text/html; charset=utf-8',
            match_querystring=True
        )
        sales_invoices = netvisor.sales_invoices.list(invoice_number=5)
        assert len(sales_invoices) == 1
