from odoo import fields, models


class G2PRegistryAction(models.Model):
    _name = "g2p.registry.action"
    _description = "G2P Registry Action"

    registry_type_id = fields.Many2one(
        "g2p.registry.type",
        string="Registry Type",
        help="The specific registry model linked to this action.",
    )

    action_name = fields.Char(required=True)
    form_builder_id = fields.Many2one(
        "formio.builder",
        string="FormIO",
    )
    formio_uuid = fields.Char(related="form_builder_id.uuid", store=True)
    formio_schema = fields.Text(related="form_builder_id.schema", store=True)
    action_submission_url = fields.Char(help="API endpoint for submitting data")
