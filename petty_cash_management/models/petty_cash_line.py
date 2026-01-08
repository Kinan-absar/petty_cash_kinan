from odoo import models, fields, api

class PettyCashLine(models.Model):
    _name = 'petty.cash.line'
    _description = 'Petty Cash Line'
    _order = 'date desc, id desc'

    petty_cash_id = fields.Many2one(
        'petty.cash',
        string="Petty Cash Report",
        ondelete='cascade'
    )

    date = fields.Date(
        string="Expense Date",
        default=fields.Date.context_today,
        required=True
    )

    supplier = fields.Char(
        string="Supplier",
        required=False
    )

    invoice_number = fields.Char(
        string="Invoice / Receipt No"
    )

    po_number = fields.Char(
        string="PO No"
    )

    mr_number = fields.Char(
        string="MR No"
    )

    zone = fields.Char(
        string="Zone"
    )

    description = fields.Text(
        string="Description"
    )

    category_id = fields.Many2one(
        'petty.cash.category',
        string="Category",
        required=True
    )

    amount_before_vat = fields.Float(
        string="Amount Before VAT",
        required=True
    )

    vat_applicable = fields.Boolean(
        string="VAT 15%",
        default=True
    )

    vat_amount = fields.Float(
        string="VAT Amount",
        compute="_compute_amounts",
        store=True
    )

    amount_total = fields.Float(
        string="Total Amount",
        compute="_compute_amounts",
        store=True
    )

    attachment_ids = fields.Many2many(
        'ir.attachment',
        'petty_cash_line_ir_attachments_rel',
        'line_id',
        'attachment_id',
        string='Attachments'
    )

    currency_id = fields.Many2one(
        related='petty_cash_id.currency_id',
        store=True,
        readonly=True
    )

    label = fields.Char(
        string="Label",
        compute="_compute_label",
        store=True
    )

    # ---------------- COMPUTATION ----------------
    @api.depends('amount_before_vat', 'vat_applicable', 'category_id.tax_id')
    def _compute_amounts(self):
        for line in self:
            # Default VAT = 0
            line.vat_amount = 0.0

            if line.vat_applicable and line.category_id.tax_id:
                # Use Odoo tax engine to compute VAT properly
                taxes_data = line.category_id.tax_id.compute_all(
                    line.amount_before_vat,
                    currency=line.currency_id,
                    quantity=1.0
                )
                line.vat_amount = taxes_data['taxes'][0]['amount']

            # Total = amount_before_vat + real VAT
            line.amount_total = line.amount_before_vat + line.vat_amount

    @api.depends('description', 'po_number', 'mr_number', 'zone')
    def _compute_label(self):
        for line in self:
            parts = []

            if line.description:
                parts.append(line.description)
            if line.po_number:
                parts.append(f"PO {line.po_number}")
            if line.mr_number:
                parts.append(f"MR {line.mr_number}")
            if line.zone:
                parts.append(f"Zone {line.zone}")

            line.label = " / ".join(parts) if parts else "/"
