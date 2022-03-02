from odoo import models,fields

class Alternant(models.Model):
    _name = "prototype.alternant"
    _inherit = ["prototype.salarie" , "prototype.etudiant"]
    _description = 'Ceci est une classe représentant un alternant'

    type_contrat = fields.Selection([('apprentissage','Apprentissage'), ('contrat_pro','Contrat Pro')],string='Type de contrat de l\'apprenti',required=True, default='apprentissage')