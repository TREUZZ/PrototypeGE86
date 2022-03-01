from odoo import models,fields

class Alternant(models.Model):
    _name = "prototype.alternant"
    _inherit = ["prototype.salarie" , "prototype.etudiant"]
    type_contrat = fields.Selection([('apprentissage','Apprentissage'), ('contrat pro','Contrat Pro')],string='Type de contrat de l\'apprenti',required=True, tracking=True, default='apprentissage')