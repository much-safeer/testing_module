from odoo import http
from odoo.http import request
import json
from werkzeug import Response


class Vote(http.Controller):
    @http.route("/say_hello", type="http")
    def say_hello(self, name):
        return f"Hello {name}"

    @http.route("/say_hello_json", type="http", auth="none")
    def say_hello_json(self, name):
        some_dictionary = {"name": name}
        json_response = some_dictionary
        json_response = json.dumps(some_dictionary, sort_keys=True)
        return Response(json_response, content_type="application/json")

    @http.route("/get_leading_candidate", type="http", csrf=False)
    def get_leading_candidate(self):
        candidates = request.env["election.candidate"].search_read(
            [], order="total_votes desc", limit=1
        )

        leading_candidate = {
            "name": candidates[-1]["name"],
            "total_votes": candidates[-1]["total_votes"],
        }
        json_response = json.dumps(leading_candidate, sort_keys=True)
        return Response(json_response, content_type="application/json")

    @http.route("/vote", methods=["POST"], type="http", csrf=False)
    def vote(self, voter_id, candidate_id):
        # FIXME please make sure this route works if we use the
        # below curl, a post request should work with the paramters
        # in the body
        # curl - -header
        # "Content-Type: application/json" \
        # --request
        # POST \
        # --data '{"voter_id":1,"candidate_id":2}' \
        # http://localhost:8069/vote
        candidate = (
            request.env["election.candidate"].sudo().search([("id", "=", candidate_id)])
        )
        if len(candidate) < 1:
            return "Invalid Candidate Id"

        voter = request.env["election.voter"].sudo().search([("id", "=", voter_id)])

        if len(voter) < 1:
            return "Invalid Voter Id"

        for v in voter:
            v.vote = int(candidate_id)
        return "Vote Updated"
