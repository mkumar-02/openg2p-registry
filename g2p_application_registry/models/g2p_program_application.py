from odoo import fields, models


class G2PProgramApplication(models.Model):
    _name = "g2p.program.application"
    _description = "G2P Program Application"

    program_mnemonic = fields.Char(required=True)
    registrant_id = fields.Many2one("res.partner", string="Registrant")
    application_id = fields.Char(string="Application ID")
    status = fields.Selection(
        [
            ("draft", "Draft"),
            ("submitted", "Submitted"),
            ("approved", "Approved"),
            ("rejected", "Rejected"),
        ],
        default="draft",
    )
