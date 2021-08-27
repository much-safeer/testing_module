from odoo import fields,api, models
import logging
import csv

class ImportVotesWizard(models.TransientModel):
    _name="import.votes.wizard"
    _description="Importing votes from csv"

    voter_name=fields.Char(string="voter_name", required=True)
    candidate_name=fields.Char(string="candidate_name", required=True)

    def import_votes(self):
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                _logger = logging.getLogger(__name__)
                _logger.info('------------------------')
                _logger.info(row)
                _logger.info('------------------------')