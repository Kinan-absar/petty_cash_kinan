from odoo import models, fields, api

class PettyCashConfigWizard(models.TransientModel):
    _name = 'petty.cash.config.wizard'
    _description = 'Petty Cash Configuration Wizard'

    petty_cash_account_id = fields.Many2one(
        'account.account',
        string="Petty Cash Account",
        required=True
    )

    input_vat_account_id = fields.Many2one(
        'account.account',
        string="Input VAT Account",
        required=True
    )

    petty_cash_journal_id = fields.Many2one(
        'account.journal',
        string="Petty Cash Journal",
        domain="[('type','=','general')]",
        required=True
    )

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        params = self.env['ir.config_parameter'].sudo()

        res.update({
            'petty_cash_account_id': int(params.get_param(
                'petty_cash_management.petty_cash_account_id', 0)) or False,
            'input_vat_account_id': int(params.get_param(
                'petty_cash_management.input_vat_account_id', 0)) or False,
            'petty_cash_journal_id': int(params.get_param(
                'petty_cash_management.petty_cash_journal_id', 0)) or False,
        })
        return res

    def action_save(self):
        params = self.env['ir.config_parameter'].sudo()

        params.set_param(
            'petty_cash_management.petty_cash_account_id',
            self.petty_cash_account_id.id
        )
        params.set_param(
            'petty_cash_management.input_vat_account_id',
            self.input_vat_account_id.id
        )
        params.set_param(
            'petty_cash_management.petty_cash_journal_id',
            self.petty_cash_journal_id.id
        )

        return {'type': 'ir.actions.act_window_close'}
