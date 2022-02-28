from odoo import models,fields

class Alternant(models.Model):
    _name = "prototype.alternant"
    _inherit = ["prototype.salarie" , "prototype.etudiant"]

class ExtensionParent(models.Model):
    _name = 'extension.extension'
    _description = 'Extension'
    name = fields.Char(default="I AM EXTENSION")
class ExtensionChild(models.Model):
    _inherit = 'extension.extension'
    description = fields.Char(default="Extended")
    type_contrat = fields.Selection([('apprentissage','Apprentissage'), ('contrat pro','Contrat Pro')],string='Type de contrat de l\'apprenti',required=True, tracking=True, default='apprentissage')