# -*- coding: utf-8 -*-

{
    "name": "Partners group",
    "version": '14.0.0.0.1',
    "depends": ["base", "account"],
    "author": "TIT-Solutions",
    "website": "https://www.sogesi-dz.com",
    "support": "sogesi@sogesi-dz.com",
    "category": "Sales",
    "summary": """This module allows to assign partners to a group """,
    "description": """This module allows to assign partners to a group """,
    'images': ['static/description/banner.png'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/res_partner_group.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,

}
