# -*- coding: utf-8 -*-
# Copyright (C) 2021 - Auguria (<https://www.auguria.fr>).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    'name': "auguria_add_key_user_project",

    'summary': """
        Allow the portal user to be assigned to tasks in same project
    """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Auguria",
    'website': "http://www.auguria.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Project',
    'version': '15.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project', 'hr_timesheet', 'sale_project'],

    # always loaded
    'data': [
        'views/edit_project.xml',
        'views/project_portal_task_template.xml',
        'views/project_task_view.xml',
        'views/project_sharing_project_task_view_form.xml',
        'views/project_sharing_project_task_view_tree.xml',
        'views/project_sharing_project_task_action.xml',
        'views/project_sharing_project_task_action_2.xml',
        'views/project_portal_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'sequence': 1,
}
