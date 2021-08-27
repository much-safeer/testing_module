from odoo import fields,api, models, exceptions
import csv
import base64
import io

class ImportVotesWizard(models.TransientModel):
    _name="import.votes.wizard"
    _description="Importing votes from csv"

    data=fields.Binary(string="Upload CSV", required=True)

    def import_votes(self):
        print("CLicked")
        print(self.data)
        csv_data = base64.b64decode(self.data)
        data_file = io.StringIO(csv_data.decode("utf-8"))
        data_file.seek(0)
        file_reader = []
        csv_reader = csv.reader(data_file, delimiter=',')
        file_reader.extend(csv_reader)

        for row in file_reader:
            voters=(self.env['election.voter'].search([('name','=',row[0])]))
            candidates=(self.env['election.candidate'].search([('name','=',row[1])]))

            if len(candidates)<1:
                raise exceptions.UserError("Invalid Candidate")

            if len(voters)<1:
                self.env['election.voter'].create({
                    "name":row[0],
                    "vote":candidates[0].id
                })
                continue

            for voter in voters:
                voter.vote = candidates[0].id