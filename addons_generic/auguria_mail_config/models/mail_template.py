# -*- coding: utf-8 -*-
# Copyright (C) 2021 - Auguria (<https://www.auguria.fr>).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

import re
from lxml import html as htmltree
from odoo import _, api, models


class MailTemplate(models.Model):
    _inherit = "mail.template"


    @api.model
    def _mail_debrand_body(self, html):
        user_id = self.env.user
        company_id = False
        if user_id:
            company_id = self.env.user.company_id

        if not company_id:
            company_id = self.env['res.company'].sudo().search([], limit=1)


        if 'background-color: #875A7B' in html and company_id.mail_theme_color_button:
            html = re.sub('background-color: #875A7B', 'background-color: '+company_id.mail_theme_color_button, html)

        if 'background-color: #875a7b' in html and company_id.mail_theme_color_button:
            html = re.sub('background-color: #875a7b', 'background-color: '+company_id.mail_theme_color_button, html)

        if 'color: #875A7B' in html and company_id.mail_theme_color_text:
            html = re.sub('color: #875A7B', 'color: '+company_id.mail_theme_color_text, html)

        if 'color: #875a7b' in html and company_id.mail_theme_color_text:
            html = re.sub('color: #875a7b', 'color: '+company_id.mail_theme_color_text, html)

        root = htmltree.fromstring(html)
        return htmltree.tostring(root).decode("utf-8")

    @api.model
    def render_post_process(self, html):
        html = super().render_post_process(html)
        return self._mail_debrand_body(html)
