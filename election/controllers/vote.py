from odoo import http
from odoo.http import request, content_disposition
import json
from werkzeug import Response
from werkzeug.exceptions import Unauthorized, BadRequest
import logging

class Vote(http.Controller):
    
    @http.route('/say_hello', type="http")
    def say_hello(self, name):
        return f"Hello {name}"

    @http.route('/say_hello_json', type="http", auth="none")
    def say_hello_json(self, name):
        some_dictionary={
            "name":name
        }
        json_response=some_dictionary
        json_response = json.dumps(some_dictionary, sort_keys=True)
        return Response(json_response, content_type="application/json")

    @http.route('/get_leading_candidate', type="http", csrf=False)
    def get_leading_candidate(self):
        candidates = request.env['election.candidate'].search_read([],order="total_votes desc", limit=1)
        
        # _logger = logging.getLogger(__name__)
        # _logger.info('------------------------')
        # _logger.info(candidates)
        # _logger.info('------------------------')

        leading_candidate = {
            "name":candidates[-1]['name'],
            "total_votes":candidates[-1]['total_votes']
        }
        json_response = json.dumps(leading_candidate, sort_keys=True)
        return Response(json_response, content_type="application/json")

    
    @http.route('/vote',methods=['POST'], type="json", csrf=False)
    def vote(self, voter_name, candidate_name):
        candidate = (request.env['election.candidate'].search([('name','=',candidate_name)]))
        if len(candidate):
            return f"Invalid Candidate Name"
        request.env['election.voter'].sudo().create({
                'name':voter_name,
                'vote': candidate['id']
            })
        return f"User Created"
