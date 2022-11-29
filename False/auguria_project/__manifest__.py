# -*- coding: utf-8 -*-
# Copyright (C) 2021 - Auguria (<https://www.auguria.fr>).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    'name': 'Auguria Project',
    'version': '1.0',
    'author': 'Auguria SAS',
    'license': 'LGPL-3',
    'summary': 'Auguria Project Custom',
    'sequence': 15,
    'description': """
custom dev module
    """,
    'category': '',
    'website': 'https://www.auguria.fr/',
    'images': [],
    'depends': [
                'project', 'hr_timesheet',
        ],
    'data': [
        "security/ir.model.access.csv",
        'views/account_analytic_line_view.xml',
        'views/project_task_view.xml',
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
