# -*- coding: utf-8 -*-
# Copyright (C) 2021 - Auguria (<https://www.auguria.fr>).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models


class ProjectMilestone(models.Model):
    _inherit = 'project.milestone'

    task_ids = fields.One2many('project.task', 'milestone_id', string='Task')
