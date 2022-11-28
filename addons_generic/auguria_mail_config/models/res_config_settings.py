# -*- coding: utf-8 -*-
# Copyright (C) 2021 - Auguria (<https://www.auguria.fr>).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).


from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'


    mail_theme_color_text = fields.Char(related="company_id.mail_theme_color_text", readonly=False, string='Couleur texte des courriers')
    mail_theme_color_button = fields.Char(related="company_id.mail_theme_color_button", readonly=False, string='Couleur button des courriers')
