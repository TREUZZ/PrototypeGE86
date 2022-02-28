from odoo import model, fields

class Etudiant(models.Model):
    _inherit = "personne.model"

    num_etu = fields.integer(string="Nom de l'étudiant", required=True, tracking=True)
    ecole = fields.Char(string="Nom de l'école", required=True, tracking=True)
    note = fields.float(string="Note de l'étudiant", required=True, tracking=True)

    def ajoutNote(self, new_note):
        self.note = new_note