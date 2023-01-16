# -*- coding: utf-8 -*-

import odoo
from odoo.exceptions import AccessDenied


class DHT11Endpoint(odoo.http.Controller):
    @odoo.http.route("/dht11", type="json", auth="public", methods=["POST"])
    def dht11_response(self,**record):
        if not self.check_auth(record["login"]["username"], record["login"]["password"]):
            return odoo.http.Response("ERROR: Authorization error!", status=401)
        
        self.insertData(record["data"])
        
    def insertData(self, data):
        data["temperature_fahrenheit"] = data["temperature"] * 1.8 + 32
        warm_top, warm_bottom = odoo.http.request.env['ir.config_parameter'].sudo().get_param("cu_nodemcu_dht11.warm_top"), odoo.http.request.env['ir.config_parameter'].sudo().get_param("cu_nodemcu_dht11.warm_bottom")
        state = 0
        data["state"] = '1' if data["temperature"] < int(warm_bottom) else '3' if data["temperature"] > int(warm_top) else '2'
        try:
            odoo.http.request.env["cu_nodemcu_dht11.record"].sudo().create(data)
        except:
            return odoo.http.Response("ERROR: Something is wrong with data!", status=400)
        # return odoo.http.Response("SUCCESS", status=200)
        return "SUCCESS"

    def check_auth(self, username, password):
        user = odoo.http.request.env["res.users"].sudo().search([("login", "=", username)])
        if user:
            try:
                _ = user.authenticate(odoo.http.request.env.cr.dbname, username, password, {"interactive": True})
                return True
            except:
                return False
        else:
            return False
