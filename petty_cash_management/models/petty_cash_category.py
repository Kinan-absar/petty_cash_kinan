from odoo import models, fields

class PettyCashCategory(models.Model):
    _name = 'petty.cash.category'
    _description = 'Petty Cash Category'
    _order = 'sequence, name'

    name = fields.Char(
        string="Category Name",
        required=True
    )

    account_id = fields.Many2one(
        'account.account',
        string="Expense Account",
        required=True,
        help="The expense account used when posting petty cash journal entries."
    )

    sequence = fields.Integer(
        string="Sequence",
        default=10,
        help="Used to order categories in dropdown lists."
    )

    tax_id = fields.Many2one(
        'account.tax',
        string="Tax",
        help="Tax to apply when VAT Applicable is True."
    )
    
    analytic_account_id = fields.Many2one(
        'account.analytic.account',
        string="Analytic Account"
    )
