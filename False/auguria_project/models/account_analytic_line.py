# -*- coding: utf-8 -*-
# Copyright (C) 2021 - Auguria (<https://www.auguria.fr>).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    first_category = fields.Many2one('project.task.category1', string='Category 1 ', readonly=False,
                                     compute='_compute_category1', store=True)
    second_category = fields.Many2one('project.task.category2', string='Category 2 ', store=True, readonly=False,
                                      compute='_compute_category2')
    third_category = fields.Many2one('project.task.category3', string='Category 3 ', store=True, readonly=False)
    work_type = fields.Many2one('account.analytic.line.type', string='Work type', store=True)
    previous_hours = fields.Float(string='Previous hours')
    previous = fields.Selection([('previous', 'Previous'), ('real', 'Real')],
                                string='P/R')
    milestone_id = fields.Many2one('project.milestone', string='milestone', store=True, compute='_compute_milestone')

    @api.depends('project_id', 'task_id', 'task_id.first_category')
    def _compute_category1(self):
        for line in self:
            if line.project_id and line.task_id:
                line.first_category = line.task_id.first_category

    @api.depends('project_id', 'task_id', 'task_id.second_category')
    def _compute_category2(self):
        for line in self:
            if line.project_id and line.task_id:
                line.second_category = line.task_id.second_category

    @api.depends('project_id', 'task_id', 'task_id.milestone_id')
    def _compute_milestone(self):
        for line in self:
            if line.project_id and line.task_id and line.task_id.milestone_id:
                line.milestone_id = line.task_id.milestone_id

    # @api.depends('project_id', 'task_id', 'task_id.third_category')
    # def _compute_category3(self):
    #     for line in self:
    #         if line.project_id and line.task_id:
    #             line.third_category = line.task_id.third_category


class ProjectTaskCategory1(models.Model):
    _name = 'account.analytic.line.type'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True, help="Name of the work type")
    description = fields.Char(string='Description', help="definition of the work type")


class ProjectTaskCategory3(models.Model):
    _name = 'project.task.category3'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True, help="Name of the category")
    description = fields.Char(string='Description', help="definition of the category")
    category_3 = fields.Many2one('project.task.category2', string='Category parent')
