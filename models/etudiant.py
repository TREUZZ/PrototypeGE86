from odoo import models,fields

class Etudiant(models.Model):
    _name = 'prototype.etudiant'
    _inherit = "personne.model"


    num_etu = fields.Integer(required=True)
    ecole = fields.Char(required=True)
    note = fields.Float(required=True)

    def ajoutNote(self, new_note):
        self.note = new_note