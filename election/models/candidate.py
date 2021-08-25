from odoo import fields, models

class ElectionCandidate(models.Model):
    _name= "election.candidate"
    _description="Candidate in election"

    name=fields.Char(string="Name", required=True)
    total_votes=fields.Integer(string="Total Votes",compute="total_votes_function")

    def total_votes_function(self):
        total_votes_temp = self.env['election.voter'].search_count([('vote','=',self.name)])
        self.total_votes=total_votes_temp