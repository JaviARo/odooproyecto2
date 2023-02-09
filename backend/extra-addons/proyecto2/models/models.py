# -*- coding: utf-8 -*-

from odoo import models, fields, api

class proyecto2(models.Model):
    _name = 'project.project'
    _inherit = 'project.project'

    def _get_default_type_common(self):
        ids = self.env["project.task.type"].search([("active", "=", True)])
        return ids

    type_ids = fields.Many2many(default=lambda self: self._get_default_type_common())
    