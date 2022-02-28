from odoo import models, fields

class Salarie(models.Model):
    _name = 'prototype.salarie'
    _inherit = 'prototype.personne'

    salaire = fields.Float(string="Salaire de la personne",required=True)
    entreprise = fields.Char(string="Nom de l'entreprise",required=True, tracking=True)

    def modificationSalaire(self,pourcentage_augmentation):
        '''
        Méthode de modification du salaire.

        :params pourcentage_augmentation : float : Pourcentage de modification du salaire initial. 
        '''
        self.salaire = self.salaire * ( pourcentage_augmentation / 100 )
