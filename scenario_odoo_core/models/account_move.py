from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def create_scenario_invoices(self):
        """
        Creates an invoice for this scenario.
        The invoice makes no sense, but you should understand the error that appears and
        fix this method so it runs through.
        """

        # assume this is imported data for one invoice with column names:
        # name, debit, credit, account
        data = [
            ("Invoice Line A", 30, 0),
            ("Invoice Line C", 30, -30),
            ("Invoice Line D", 0, 880),
            ("Invoice Line E", 4770, 0),
            ("Invoice Line F", -30, 2000),
            ("Invoice Line G", 200, 2020),
        ]

        # Any account for a and b (doesn't matter for this example)
        account_id = self.env["account.account"].search([], limit=1)[0]

        # Create line data
        lines = [
            (
                0,
                0,
                dict(
                    name=line_data[0],
                    debit=line_data[1],
                    credit=line_data[2],
                    account_id=account_id.id,
                ),
            )
            for line_data in data
        ]

        # Miscellaneous journal (you can put anything you want in here)
        journal_id = self.env["account.journal"].search(
            [["name", "=", "Miscellaneous Operations"]], limit=1
        )

        self.env["account.move"].create(
            dict(
                name="Big Invoice",
                invoice_line_ids=lines,
                # move_type="entry",
                journal_id=journal_id.id,
            )
        )
