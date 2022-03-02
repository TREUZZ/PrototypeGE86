from pyexpat import model
from odoo import models, fields, api, exceptions

class Personne(models.AbstractModel):
    _name = 'prototype.personne'
    _description = 'Ceci est une classe abstraite représentant une personne'

    active = fields.Boolean(default=True)

    nom = fields.Char(string='Nom de la personne', required=True)
    prenom = fields.Char(string='Prénom de la personne', required=True)
    
