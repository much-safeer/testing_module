from odoo import fields,api, models

class ElectionVoter(models.Model):
    _name="election.voter"
    _description="Voter data"

    voter_name=fields.Char(string="voter_name", required=True)
    candidate_name=fields.Char(string="candidate_name", required=True)