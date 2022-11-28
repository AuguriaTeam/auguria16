# -*- coding: utf-8 -*-
# Copyright (C) 2021 - Auguria (<https://www.auguria.fr>).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    'name': 'Auguria iban on invoice',
    'version': '2.0',
    'author': 'Auguria SAS',
    'licence': 'LGPL Version 3',
    'summary': 'Auguria iban on invoice',
    'sequence': 15,
    'description': """
custom company partner iban on invoice
    """,
    'category': '',
    'website': 'https://www.auguria.fr',
    'images': [],
    'depends': [
                'account', 'sale', 'base', 'base_iban',
        ],
    'data': [
             'views/partner_view.xml',
             'views/account_journal_view.xml',
             'views/report_invoice.xml',
             'views/report_saleorder.xml',
             'views/res_company_views.xml',
             'views/account_move_view.xml',
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'post_init_hook': '',
}
