# -*- coding: utf-8 -*-
# Copyright (C) 2021 - Auguria (<https://www.auguria.fr>).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    first_category = fields.Many2one('project.task.category1', string='Category 1 ')
    second_category = fields.Many2one('project.task.category2', string='Category 2 ')
    budget = fields.Selection([('planned', 'Planned in the budget'), ('additional', 'Additional')],
                              string='Budget')
    kanban_color = fields.Char(string='Couleur kanban', default="#7c7bad")
    milestone_id = fields.Many2one('project.milestone', string='milestone')


class ProjectTaskCategory1(models.Model):
    _name = 'project.task.category1'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True, help="Name of the category")
    description = fields.Char(string='Description', help="definition of the category")
    # relation with category2
    category_2 = fields.One2many('project.task.category2', 'category_2', string='Category 2')


class ProjectTaskCategory2(models.Model):
    _name = 'project.task.category2'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True, help="Name of the category")
    description = fields.Char(string='Description', help="definition of the category")
    kanban_color = fields.Char(string='Couleur kanban', default="#7c7bad")
    category_2 = fields.Many2one('project.task.category1', string='Category parent')
    # relation with category3
    category_3 = fields.One2many('project.task.category3', 'category_3', string='category 3')
