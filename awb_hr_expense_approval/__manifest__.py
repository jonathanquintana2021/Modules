# -*- coding: utf-8 -*-
##############################################################################
#
#   ACHIEVE WITHOUT BORDERS
#
##############################################################################
{
    'name': "AWB HR Expense Approval",
    'summary': """
        AWB Hr Expense Approval
        """,
    'description': """
        AWB HR Expense Approval
    """,
    'author': "Achieve Without Borders, Inc",
    'website': "http://www.achievewithoutborders.com",
    'category': "Operations/Expense",
    'version': '13.0.1.0.0',
    'depends': ['hr_expense'],
    'data': [
        'security/ir.model.access.csv',
        'security/ir.rule.csv',
        'views/expense_approval_views.xml',
        'views/hr_expense_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False
}