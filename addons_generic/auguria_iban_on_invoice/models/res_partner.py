# -*- coding: utf-8 -*-
# Copyright (C) 2021 - Auguria (<https://www.auguria.fr>).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).


from odoo import api, exceptions, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def _default_partner_bank(self):
        # if self.ref_company_ids == False:
        bank = self.env.company.default_bank_id.journal_id.id
        return bank

    def _current_company(self):
        return self.env.company.id

    payment_partner_bank_id = fields.Many2one('account.journal', string='Bank Account', default=_default_partner_bank, domain="[('type', '=', 'bank')]")
