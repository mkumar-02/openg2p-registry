from odoo import fields, models


class G2PRegistryAction(models.Model):
    _name = "g2p.registry.actions"
    _description = "G2P Registry Action"

    name = fields.Char(required=True)
    formio_id = fields.Many2one("formio.builder", string="Form Builder")
    active = fields.Boolean(default=True)
    description = fields.Text()
