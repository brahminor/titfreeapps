from odoo import fields, models

class ResPartnerGroup(models.Model):
    _name = "res.partner.group"
    
    name = fields.Char(string="Name", copy=False)
    code = fields.Char(string="Code", copy=False)
    partner_ids = fields.One2many("res.partner", 'partner_group_id', string="Partner")
