# -*- coding: utf-8 -*-
from odoo import http

# class WebsiteSaleDelete(http.Controller):
#     @http.route('/website_sale_delete/website_sale_delete/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_sale_delete/website_sale_delete/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_sale_delete.listing', {
#             'root': '/website_sale_delete/website_sale_delete',
#             'objects': http.request.env['website_sale_delete.website_sale_delete'].search([]),
#         })

#     @http.route('/website_sale_delete/website_sale_delete/objects/<model("website_sale_delete.website_sale_delete"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_sale_delete.object', {
#             'object': obj
#         })