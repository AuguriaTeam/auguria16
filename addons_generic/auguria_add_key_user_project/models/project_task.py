# -*- coding: utf-8 -*-
# Copyright (C) 2021 - Auguria (<https://www.auguria.fr>).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models, _, api

CUSTOM_PROJECT_TASK_READABLE_FIELDS = {
    'id',
    'active',
    'description',
    'priority',
    'kanban_state_label',
    'project_id',
    'display_project_id',
    'color',
    'partner_is_company',
    'commercial_partner_id',
    'allow_subtasks',
    'subtask_count',
    'child_text',
    'is_closed',
    'email_from',
    'create_date',
    'write_date',
    'company_id',
    'displayed_image_id',
    'display_name',
    'portal_user_names',
    'legend_normal',
    'legend_blocked',
    'legend_done',
    'user_ids',
    'ag_user_ids',
    'ag_portal_user_names',
    'project_id.ag_user_ids',
    'name',
    'partner_id',
    'partner_email',
    'date_deadline',
    'tag_ids',
    'sequence',
    'stage_id',
    'child_ids',
    'parent_id',
    'planned_hours',
    'remaining_hours',
    'encode_uom_in_days',
    'progress',
    'allow_timesheets',
    'subtask_effective_hours',
    'effective_hours',
    'subtask_planned_hours',
    'timesheet_ids',
    'total_hours_spent',
    'analytic_account_active',
    'sale_line_id',
    'sale_order_id',
    'planned_date_begin',
    'stage_id.fold',
    'planned_date_end',
    'planned_date_end',
    'planned_hours'
}

CUSTOM_PROJECT_TASK_WRITABLE_FIELDS = {
    'stage_id',
    'kanban_state',
    'sequence',
}


class Task(models.Model):
    _inherit = "project.task"

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
        tracking=True,
    )

    ag_portal_user_names = fields.Char(compute='_ag_compute_portal_user_names', compute_sudo=True)

    @api.depends('ag_user_ids')
    def _ag_compute_portal_user_names(self):
        if self.ids:
            self.browse(self.ids)._read(['ag_user_ids'])
        for task in self.with_context(prefetch_fields=False):
            task.ag_portal_user_names = ', '.join(task.ag_user_ids.mapped('name'))

    @property
    def SELF_READABLE_FIELDS(self):
        return CUSTOM_PROJECT_TASK_READABLE_FIELDS | self.SELF_WRITABLE_FIELDS

    @property
    def SELF_WRITABLE_FIELDS(self):
        return CUSTOM_PROJECT_TASK_WRITABLE_FIELDS

    def check_portal_user_task(self, user_id):
        if user_id in [u.id for u in self.project_id.ag_user_ids] or user_id in [u.id for u in self.ag_user_ids]:
            return True
        return False
