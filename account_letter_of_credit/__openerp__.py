# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
    'name':'Sales Order Letter Of Credit',
    'version':'0.1',
    'category':'Accounting',
    'summary': """Modified Sales Order with Letter of Credit""",
    'website': "http://www.alltekusa.com.cn",
    'description':"""
    This Module Adds Letter of Credit to the Sales Order
    """,
    'author':'kasinox',
    'depends':['base','sale'],
    'data':['sales_order_lc_view',
            ],
    'demo':[],
    'installable':True,
    'auto_install':False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
