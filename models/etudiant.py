from odoo import models,fields

class Etudiant(models.Model):
    _name = 'prototype.etudiant'
    _inherit = "personne.model"


    num_etu = fields.Integer(string='Numéro d\'étudiant',required=True)
    ecole = fields.Char(string='Nom de l\'école',required=True)
    note = fields.Float(string='Note de l\'étudiant (moyenne)',required=True)

    def ajoutNote(self, new_note,coef):
        '''
        Fonction de modification de la moyenne de l'étudiant.
        
        :params new_note : Float : Note sur 20 de l'étudiant.
        :params coef : Integer : Coefficient de la note.
        '''
        if self.note != 0:
            self.note += coef * new_note
        else:
            self.note = coef * new_note