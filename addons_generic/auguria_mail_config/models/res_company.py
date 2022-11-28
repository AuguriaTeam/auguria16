# -*- coding: utf-8 -*-
# Copyright (C) 2021 - Auguria (<https://www.auguria.fr>).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).


from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    mail_theme_color_text = fields.Char(string='Couleur texte des courriers', default="#7c7bad")
    mail_theme_color_button = fields.Char(string='Couleur button des courriers', default="#7c7bad")
