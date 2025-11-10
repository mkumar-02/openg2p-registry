from odoo import fields, models


class FormioBuilder(models.Model):
    _inherit = "formio.builder"

    category = fields.Selection(
        [
            ("program_application_form", "Program Application Form"),
            ("actions", "Actions"),
        ],
        string="Category",
    )
    program_mnemonic = fields.Char(string="Program Mnemonic")
    summary = fields.Char(string="Summary")
