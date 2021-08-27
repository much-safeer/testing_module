from odoo import fields, models


class ElectionVoter(models.Model):
    _name = "election.voter"
    _description = "Voter data"

    name = fields.Char(string="Name", required=True)
    vote = fields.Many2one("election.candidate", string="Candidate", required=True)
