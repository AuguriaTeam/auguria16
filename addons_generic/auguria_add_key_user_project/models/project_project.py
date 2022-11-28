# -*- coding: utf-8 -*-
# Copyright (C) 2021 - Auguria (<https://www.auguria.fr>).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models, _, api


class ProjectProject(models.Model):
    _inherit = "project.project"

    @api.onchange('partner_id')
    def _campus_onchange_partner_id(self):
        return {'domain': {
            'ag_user_ids': [
                ('groups_id', 'in', self.env.ref('base.group_portal').id),
                ('partner_id', 'in', [p.id for p in self.partner_id.child_ids])]
            }
        }

    ag_user_ids = fields.Many2many(
        'res.users',
        string=_('Portal users'),
        context={'active_test': False},
        tracking=True
    )
