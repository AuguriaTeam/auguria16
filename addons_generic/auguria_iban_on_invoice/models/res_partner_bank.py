# -*- coding: utf-8 -*-
# Copyright (C) 2021 - Auguria (<https://www.auguria.fr>).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import models, api, _, fields


class ResPartnerBank(models.Model):
    _inherit = "res.partner.bank"
    _rec_name = 'complete_name'

    complete_name = fields.Char(
        'Complete Name', compute='_compute_complete_name', recursive=True,
        store=True)
    bank_text = fields.Text(string='Notes ou subrogation')

    @api.depends('acc_number', 'bank_id.name')
    def _compute_complete_name(self):
        for bank in self:
            bank.complete_name = '%s - %s' % (bank.acc_number, bank.bank_id.name)
