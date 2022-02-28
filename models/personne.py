from pyexpat import model
from odoo import models, fields, api, exceptions

class Personne(models.AbstractModel):
    _name = 'prototype.personne'

    nom = fields.Char(string='Nom de la personne', required="1", tracking=True)
    prenom = fields.Char(string='Prénom de la personne', required="1", tracking=True)

