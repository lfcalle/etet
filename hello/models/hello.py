# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class hello(models.Model): 
    _name = 'ej.hello' 
    dato1 = fields.char(string='dato1', required=True) 
 
    dato2 = fields.text(string='dato2', required=True) 
 
