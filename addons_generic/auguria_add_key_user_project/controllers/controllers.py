# -*- coding: utf-8 -*-
# Copyright (C) 2021 - Auguria (<https://www.auguria.fr>).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo.addons.portal.controllers.portal import CustomerPortal


class ProjectCustomerPortal(CustomerPortal):

    def _prepare_project_sharing_session_info(self, project):
        session_info = super()._prepare_project_sharing_session_info(project)
        if project.ag_user_ids:
            if session_info.get('uid') not in [u.id for u in project.ag_user_ids]:
                session_info.update(
                    action_name='auguria_add_key_user_project.ag_project_sharing_project_task_action'
                )
                return session_info
            else:
                session_info.update(
                    action_name='auguria_add_key_user_project.ag_project_sharing_project_task_action_2'
                )
                return session_info
        return session_info
