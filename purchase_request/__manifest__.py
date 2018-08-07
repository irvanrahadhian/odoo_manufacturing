# -*- encoding: utf-8 -*-

{
    'name': 'Purchase Request',
    'version': '0.1',
    'category': 'Purchases',
    'author':'GRIT (Rahadhian)',
    'description': """
    Purchase Request Manufactur.
    """,
    'summary': 'Create purchase request',
    'website': 'https://www.gr-it.id',
    'images': ['static/description/icon.jpg'],
    'depends': ['mail',
                'purchase'],
    'data': [
        'data/purchase_request_data.xml',
        'security/purchase_request_security.xml',
        'security/ir.model.access.csv',
        'views/purchase_request_view.xml',
    ],
    'depends': ['hr'],
    'installable': True,
    'auto_install': False,
    'sequence': 105,
    'application': True
}
