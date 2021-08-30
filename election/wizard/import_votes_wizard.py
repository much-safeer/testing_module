from odoo import fields, models, exceptions
import csv
import base64


class ImportVotesWizard(models.TransientModel):
    _name = "import.votes.wizard"
    _description = "Importing votes from csv"

    data = fields.Binary(string="Upload CSV", required=True)

    def import_votes(self):
        # FIXME use a dictreader, it's neater ;)
        reader = csv.DictReader(base64.b64decode(self.data).decode("utf-8").split("\n"))

        for row in reader:
            voters = self.env["election.voter"].search([("name", "=", row["voter_id"])])
            candidates = self.env["election.candidate"].search(
                [("name", "=", row["candidate_id"])]
            )

            if len(candidates) < 1:
                raise exceptions.UserError("Invalid Candidate")

            if len(voters) < 1:
                self.env["election.voter"].create(
                    {"name": row["voter_id"], "vote": candidates[0].id}
                )
                continue

            for voter in voters:
                voter.vote = candidates[0].id
