# -*- coding: utf-8 -*-
# Copyright (C) 2021 - Auguria (<https://www.auguria.fr>).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import models, api, fields


class res_company(models.Model):
    _inherit = "res.company"

    default_bank_id = fields.Many2one('res.partner.bank', string='Bank Account', domain="[('partner_id', '=', partner_id)]")
