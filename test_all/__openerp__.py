# -*- encoding: utf-8 -*-
##############################################################################
#
#    GRAP - TEST ALL module for Odoo
#    Copyright (C) 2014-Today GRAP (http://www.grap.coop)
#    @author Sylvain LE GAL (https://twitter.com/legalsylvain)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'GRAP - Test All',
    'version': '1.0',
    'summary': 'Install and test all modules used by GRAP',
    'category': 'Custom',
    'description': """
Install and test all modules used by GRAP
=========================================

Copyright, Authors and Licence:
-------------------------------
    * Copyright: 2014, GRAP: Groupement Régional Alimentaire de Proximité;
    * Author: Sylvain LE GAL (https://twitter.com/legalsylvain);
    * Licence: AGPL-3 (http://www.gnu.org/licenses/);""",
    'author': 'GRAP',
    'website': 'http://www.grap.coop',
    'license': 'AGPL-3',
    'depends': [
        'account',
        'account_accountant',
        'account_cancel',
        'account_chart',
        'account_delete_move_null_amount',
        'account_export_ebp',
        'account_financial_report_webkit',
        'account_financial_report_webkit_xls',
        'account_fiscal_company',
        'account_invoice_pricelist',
        'account_invoice_reorder_lines',
        'account_mass_drop_moves',
        'account_merge_moves_by_patterns',
        'account_move_change_number',
        'account_move_period_date_conform',
        'account_recurring_invoice_duplication',
        'account_statement_reconciliation',
        'account_tax_update',
        'account_voucher',
        'account_voucher_fiscal_company',
        'analytic',
        'auth_admin_passkey',
        'auth_generate_password',
        'base',
        'base_fiscal_company',
        'base_headers_webkit',
        'base_iban',
        'base_setup',
        'base_status',
        'base_vat',
        'board',
        'cron_run_manually',
        'decimal_precision',
        'delivery',
        'disable_openerp_online',
        'document',
        'document_page',
        'edi',
        'email_template',
        'email_template_dateutil',
        'grap_change_access',
        'grap_change_account_move_line',
        'grap_change_data',
        'grap_change_email',
        'grap_change_ir_values',
        'grap_change_l10n_fr',
        'grap_change_precision',
        'grap_change_print',
        'grap_change_translation',
        'grap_change_views',
        'grap_cooperative',
        'grap_reporting',
        'intercompany_trade_account',
        'intercompany_trade_base',
        'intercompany_trade_fiscal_company',
        'intercompany_trade_product',
        'intercompany_trade_purchase_discount',
        'intercompany_trade_purchase_order_reorder_lines',
        'intercompany_trade_purchase_package_qty',
        'intercompany_trade_purchase_sale',
        'intercompany_trade_sale_margin',
        'intercompany_trade_sale_order_dates',
        'intercompany_trade_stock',
        'invoice_verified_state',
        'knowledge',
        'l10n_fr',
        'l10n_fr_department',
        'l10n_fr_fiscal_company',
        'l10n_fr_rib',
        'l10n_fr_state',
        'mail',
        'mail_send_bcc',
        'manage_accounts_integrity',
        'mass_editing',
        'module_parent_dependencies',
        'point_of_sale',
        'pos_backup_draft_orders',
        'pos_both_mode',
        'pos_change_payment',
        'pos_check_session_state',
        'pos_fiscal_company',
        'pos_improve_header',
        'pos_improve_images',
        'pos_improve_posbox',
        'pos_invoicing',
        'pos_keep_draft_orders',
        'pos_multicompany',
        'pos_multiple_cash_control',
        'pos_order_pricelist_change',
        'pos_remove_default_partner',
        'pos_reporting',
        'pos_restaurant',
        'pos_sale_reporting',
        'pos_second_header',
        'pos_select_customer',
        'pos_street_market',
        'pos_tare',
        'pos_tax',
        'process',
        'procurement',
        'product',
        'product_average_consumption',
        'product_category_improve',
        'product_category_recursive_property',
        'product_categ_search_complete_name',
        'product_ean_duplicates',
        'product_fiscal_company',
        'product_get_cost_field',
        'product_improved_search',
        'product_margin',
        'product_margin_improve',
        'product_simple_pricelist',
        'product_standard_margin',
        'product_standard_price_vat_incl',
        'product_stock_cost_field_report',
        'product_supplierinfo_quick_edit',
        'product_taxes_group',
        'purchase',
        'purchase_compute_order',
        'purchase_compute_order_pos',
        'purchase_compute_order_sale',
        'purchase_discount',
        'purchase_fiscal_company',
        'purchase_order_reorder_lines',
        'purchase_package_qty',
        'report_webkit',
        'report_xls',
        'sale',
        'sale_eshop',
        'sale_fiscal_company',
        'sale_food',
        'sale_margin',
        'sale_order_dates',
        'sale_order_mass_action',
        'sale_recovery_moment',
        'sale_recurring_order_duplication',
        'sale_reporting',
        'sale_stock',
        'sale_visible_tax',
        'simple_tax_account',
        'simple_tax_purchase',
        'simple_tax_sale',
        'stock',
        'stock_easy_valuation',
        'stock_fiscal_company',
        'stock_internal_use_of_products',
        'stock_inventory_improve',
        'stock_inventory_sum_duplicates',
        'stock_inventory_valuation',
        'stock_invoice_directly',
        'stock_picking_mass_assign',
        'stock_picking_quick_edit',
        'stock_picking_reorder_lines',
        'users_partners_access',
        'web',
        'web_calendar',
        'web_ckeditor4',
        'web_confirm_window_close',
        'web_dashboard_tile',
        'web_diagram',
        'web_easy_switch_company',
        'web_export_view',
        'web_gantt',
        'web_graph',
        'web_kanban',
        'web_m2x_options',
        'web_popup_large',
        'web_shortcuts',
        'web_tests',
        'web_widget_color',
        'web_widget_float_formula',
    ],
}
