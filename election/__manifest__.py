# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Election System",
    "version": "1.0",
    "summary": "Election System",
    "sequence": -100,
    "description": """Election Software""",
    "category": "Productivity",
    "website": "https://www.google.com",
    'images':[],
    "depends": [],
    "data": ["security/ir.model.access.csv","views/voter.xml","views/candidate.xml"],
    "demo": [],
    "qweb": [],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
