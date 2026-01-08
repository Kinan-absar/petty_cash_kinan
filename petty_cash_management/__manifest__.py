{
    'name': 'Petty Cash Management',
    'version': '1.0',
    'author': 'Kinan',
    'website': 'absar-alomran.com',
    'category': 'Accounting',
    'summary': 'Manage petty cash expenses with approval workflow and draft journal entry creation.',
    'description': """
        Petty Cash Management Module
        ============================

        A complete petty cash management solution designed for internal accounting teams.
        This module provides a structured workflow for recording petty cash expenses, 
        submitting them for approval, validating them by accountants, and generating 
        draft journal entries directly into the accounting system.

        Key Features
        ------------
        - Petty Cash Reports with automatic sequence numbers
        - Multi-line petty cash entries with category, VAT, PO/MR/Invoice references, and descriptions
        - Automatic VAT calculation (optional per line)
        - Category-based account mapping for expense accounts
        - Configurable Petty Cash Account, Input VAT Account, and Accounting Journal
        - Excel Import Wizard for bulk petty cash entry creation (with template download)
        - Attachment support for each petty cash line and full movement of attachments to journal entries
        - Approval workflow:
            • Draft → Submitted (Users)
            • Submitted → Approved / Rejected (Accountants)
            • Approved → Reset to Draft
        - Draft Journal Entry generation with correct debit/credit logic
        - PDF Printout formatted like existing company request forms
        - Chatter integration for comments and tracking
        - Security groups for Users and Accountants
        - Footer totals for untaxed amount, VAT, and total amount
        """,
    'depends': ['base', 'account', 'mail', 'web'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/petty_cash_sequence.xml',
        # REPORTS MUST COME BEFORE VIEWS THAT USE THEM
        'reports/petty_cash_report_action.xml',
        'reports/petty_cash_report_templates.xml',
        'views/petty_cash_category_views.xml',
        'views/petty_cash_line_views.xml',
        'views/petty_cash_views.xml',     # <-- action defined here (must load first)
        'views/res_config_settings_views.xml',
        'views/menus.xml',                # <-- menu referencing action (must load last)
        'wizard/petty_cash_import_wizard_views.xml',
    ],
    'images': ['images/main_screenshot.png'],
    'license': 'OPL-1',
    'price': 24.99,
    'currency': 'USD',
    'installable': True,
    'application': True,
}
