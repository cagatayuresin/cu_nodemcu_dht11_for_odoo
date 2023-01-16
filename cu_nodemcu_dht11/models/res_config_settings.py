# -*- coding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    cu_nodemcu_dht11_warm_bottom = fields.Integer(
        string="Warm Bottom", config_parameter="cu_nodemcu_dht11.warm_bottom"
    )
    cu_nodemcu_dht11_warm_top = fields.Integer(
        string="Warm Bottom", config_parameter="cu_nodemcu_dht11.warm_top"
    )
