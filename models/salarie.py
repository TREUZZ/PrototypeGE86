from odoo import models, fields

class Salarie(models.Model):
    _name = 'prototype.salarie'
    _inherit = 'prototype.personne'

    salaire = fields.Float(string="Salaire de la personne",required=True)
    entreprise = fields.Char(string="Nom de l'entreprise",required=True, tracking=True)
 