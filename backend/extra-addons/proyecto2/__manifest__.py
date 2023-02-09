# -*- coding: utf-8 -*-
{
    'name': "proyecto2",

    'summary': """
        Módulo de proyecto heredado""",

    'description': """
        Genera los proyectos con etapas, estados y tareas
    """,

    'author': "Javi",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/project2_stages.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        
    ],

    'application': 'True',
}
