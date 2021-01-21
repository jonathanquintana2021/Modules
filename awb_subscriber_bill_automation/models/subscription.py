# -*- coding: utf-8 -*-
##############################################################################
#
#   ACHIEVE WITHOUT BORDERS
#
##############################################################################

from odoo import api, fields, models

import logging

_logger = logging.getLogger(__name__)


class SaleSubscription(models.Model):
    _inherit = "sale.subscription"

    account_identification = fields.Char(string="Account ID")
    subscription_status = fields.Selection([('new', 'New'),
                                            ('upgrade', 'Upgrade'),
                                            ('convert', 'Convert'),
                                            ('downgrade', 'Downgrade'),
                                            ('re-contract', 'Re-contract'),
                                            ('pre-termination', 'Pre-Termination'),
                                            ('disconnection', 'Disconnection'),
                                            ('reconnection', 'Reconnection')], default='new', string="Subscription Status")

    opportunity_id = fields.Many2one('crm.lead', string="Opportunity")

    def _prepare_renewal_order_values(self):
        res = super(SaleSubscription, self)._prepare_renewal_order_values()
        if self.opportunity_id:
            res[self.id].update({
                'opportunity_id': self.opportunity_id.id,
                'sale_order_template_id': self.opportunity_id.plan.id,
            })
        _logger.debug(f'Result {res}')
        return res

    def prepare_renewal_order(self):
        res = super(SaleSubscription, self).prepare_renewal_order()
        if self.opportunity_id:
            order = self.env['sale.order'].search([('id', '=', res['res_id'])])
            order.action_confirm()
        _logger.debug(f'Result Order order{order}')
        _logger.debug(f"Result Order {res['res_id']}")
        _logger.debug(f'Result Renewal {res}')
        return res