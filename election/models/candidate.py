from odoo import api, fields, models

class ElectionCandidate(models.Model):
    _name= "election.candidate"
    _description="Candidate in election"
    _order="total_votes asc"

    name=fields.Char(string="Name", required=True)
    voter_ids = fields.One2many("election.voter","vote", readonly="1")
    total_votes=fields.Integer(string="Total Votes",compute="_compute_total_votes_function" , store=True)

    @api.depends('voter_ids')
    def _compute_total_votes_function(self):
        for candidate in self:
            candidate.total_votes=len(candidate.voter_ids)
