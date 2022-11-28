# -*- coding: utf-8 -*-
# Copyright (C) 2021 - Auguria (<https://www.auguria.fr>).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import models, api, _, fields


class Saleorder(models.Model):
    _inherit = "sale.order"

    def _prepare_invoice(self):
        invoice_vals = super(Saleorder, self)._prepare_invoice()

        invoice_vals[
            'partner_bank_id'] = self.partner_id.payment_partner_bank_id.bank_account_id or self.company_id.default_bank_id
        return invoice_vals


class Sale_Advance_Payment_Inv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    # def _prepare_invoice_values(self, order, name, amount, so_line):
    #     invoice_vals = super(Sale_Advance_Payment_Inv, self)._prepare_invoice_values(order, name, amount, so_line)
    #     invoice_vals['partner_bank_id'] = order.partner_id.payment_partner_bank_id.bank_account_id or self.company_id.default_bank_id
    #     return invoice_vals
