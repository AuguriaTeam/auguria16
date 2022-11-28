# -*- coding: utf-8 -*-
# Copyright (C) 2021 - Auguria (<https://www.auguria.fr>).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import models, api, _, fields


class account_move(models.Model):
    _inherit = "account.move"

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        res = super(account_move, self)._onchange_partner_id()
        if self.move_type in ['out_invoice', 'out_refund']:
            if self.partner_id:
                self.partner_bank_id = self.partner_id.payment_partner_bank_id.bank_account_id or self.company_id.default_bank_id
        return res
