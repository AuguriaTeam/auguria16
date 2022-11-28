# -*- coding: utf-8 -*-
# Copyright (C) 2021 - Auguria (<https://www.auguria.fr>).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': "auguria_kanban_helpdesk",

    'summary': """
        show the number of tickets with each step""",

    'description': """
        
    """,

    'author': 'Auguria SAS',
    'licence': 'LGPL Version 3',
    'website': 'https://www.auguria.fr',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'helpdesk'],

    # always loaded
    'data': [
        'views/helpdesk_team_view_kanban.xml',
        'views/helpdesk_stage_form_view.xml',
    ],
}
