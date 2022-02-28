from odoo import model

class Etudiant(models.Model):
    _inherit = "prototype.personne"

    num_etu = fields.integer(required=True)
    ecole = fields.Char(required=True)
    note = fields.float

    def ajoutNote(self, new_note):
        self.note = new_note