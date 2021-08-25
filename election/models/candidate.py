from odoo import fields, models

class ElectionCandidate(models.Model):
    _name= "election.candidate"
    _description="Candidate in election"

    name=fields.Char(string="Name", required=True)
    total_votes=fields.Integer(string="Total Votes", readonly="1", default=0)