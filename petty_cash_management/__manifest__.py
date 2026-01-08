{
    'name': 'Petty Cash Management (Advanced)',
    'version': '18.0.1.0.0',
    'author': 'Kinan',
    'website': 'https://absar-alomran.com',
    'category': 'Accounting',
    'summary': 'Manage petty cash expenses with approval workflow and automated accounting entries.',
    'description': """
Petty Cash Management
=====================

A professional petty cash management solution designed for internal accounting teams
that need full control, auditability, and accounting accuracy.

This module provides a structured workflow for recording petty cash expenses,
submitting them for approval, validating them by accountants, and generating
draft journal entries directly in Odoo Accounting.

Key Features
------------
• Petty Cash Reports with automatic sequence numbers  
• Multi-line petty cash entries with category-based expense accounts  
• Optional VAT per line with automatic VAT calculation  
• Support for PO / MR / Invoice references per expense line  
• Configurable Petty Cash Account, Input VAT Account, and Journal  
• Excel import wizard for bulk petty cash entries (with template download)  
• Attachment support on each expense line  
• Automatic movement of attachments to generated journal entries  
• Approval workflow:
  - Draft → Submitted (Users)
  - Submitted → Approved / Refused (Accountants)
  - Approved → Reset to Draft if correction is required  
• Draft journal entry generation with correct debit / credit logic  
• Professionally formatted PDF report  
• Chatter integration for communication and tracking  
• Dedicated security groups for Users and Accountants  
• Automatic totals for untaxed amount, VAT, and total amount  

This module is ideal for companies managing site expenses, small cash purchases,
and operational costs outside the standard vendor bill flow.
    """,
    'depends': [
        'base',
        'account',
        'mail',
        'web',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/petty_cash_sequence.xml',

        # Reports (must load before views that reference them)
        'reports/petty_cash_report_action.xml',
        'reports/petty_cash_report_templates.xml',

        # Views
        'views/petty_cash_category_views.xml',
        'views/petty_cash_line_views.xml',
        'views/petty_cash_views.xml',
        'views/res_config_settings_views.xml',
        'views/menus.xml',

        # Wizards
        'wizard/petty_cash_import_wizard_views.xml',
    ],
    'images': [
        'images/main_screenshot.png',
    ],
    'license': 'OPL-1',
    'price': 24.99,
    'currency': 'USD',
    'installable': True,
    'application': True,
}
