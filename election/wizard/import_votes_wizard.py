from odoo import fields,api, models, exceptions
import logging
import csv

class ImportVotesWizard(models.TransientModel):
    _name="import.votes.wizard"
    _description="Importing votes from csv"

    voter_name=fields.Char(string="voter_name", required=True)
    candidate_name=fields.Char(string="candidate_name", required=True)

    def import_votes(self):
        voters=(self.env['election.voter'].search([('name','=',self.voter_name)]))
        candidates=(self.env['election.candidate'].search([('name','=',self.candidate_name)]))

        if len(candidates)<1:
            raise exceptions.UserError("Invalid Candidate")

        if len(voters)<1:
            self.env['election.voter'].create({
                "name":self.voter_name,
                "vote":candidates[0].id
            })
            return

        for voter in voters:
            voter.vote = candidates[0].id