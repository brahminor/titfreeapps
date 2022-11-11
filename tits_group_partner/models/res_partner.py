from odoo import fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"
    
    partner_group_id = fields.Many2one("res.partner.group", string="Partner group", copy=False)
