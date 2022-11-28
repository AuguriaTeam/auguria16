# -*- coding: utf-8 -*-
# Copyright (C) 2021 - Auguria (<https://www.auguria.fr>).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).


from odoo import models


class MailRanderMixin(models.AbstractModel):
    _inherit = "mail.render.mixin"

    def _replace_local_links(self, html, base_url=None):
        html_debranded = self.env["mail.template"]._mail_debrand_body(html)
        return html_debranded
