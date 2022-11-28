# -*- coding: utf-8 -*-
# Copyright (C) 2021 - Auguria (<https://www.auguria.fr>).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    'name': 'Auguria mail config',
    'version': '1.0',
    'author': 'Auguria',
    'website': 'https://www.auguria.fr',
    'summary': "Auguria",
    'description': """change the color a on the buttons that are inside the emails""",
    'sequence': 0,
    'certificate': '',
    'license': 'LGPL-3',
    'depends': ['base','mail','website'],
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
