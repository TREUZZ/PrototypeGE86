from pyexpat import model
from odoo import models, fields, api, exceptions

class Personne(models.AbstractModel):
    _name = 'prototype.personne'

    active = fields.Boolean(default=True)

    nom = fields.Char(string='Nom de la personne', required=True, tracking=True)
    prenom = fields.Char(string='Prénom de la personne', required=True, tracking=True)

