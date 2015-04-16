# -*- coding: utf-8 -*-

from openerp.osv import osv,fields

class Sale_order(osv.Model):
    _inherit = 'sale.order'

    _columns = {

         'x_lc_received':fields.boolean('LC Received'),
         'x_lc_number':fields.text('L/C #'),
         'x_bank_advising':fields.text('Bank Advising'),
         'x_lc_open_date':fields.date('L/C Open/Pmt Date'),
         'x_lc_lsd':fields.date('L/C LSD'),
         'x_lc_expired':fields.date('L/C Expired Date'),
         'x_lc_first_tracking':fields.text('LC 1st Draft Out Tracking'),
         'x_lc_final_draft':fields.date('Final LC Draft Out'),
         }
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
