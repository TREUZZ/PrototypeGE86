from odoo import models,fields

class Etudiant(models.Model):
    _name = 'prototype.etudiant'
    _inherit = "personne.model"


    num_etu = fields.Integer(string='Numéro d\'étudiant',required=True)
    ecole = fields.Char(string='Nom de l\'école',required=True)
    note = fields.Float(string='Note de l\'étudiant',required=True)

    def ajoutNote(self, new_note):
        self.note = new_note