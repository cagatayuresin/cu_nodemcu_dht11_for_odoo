# -*- coding: utf-8 -*-
# 12/12/2022 - Çağatay Üresin

{
    "name": "CU NodeMCU DHT11",
    "version": "16.0",
    "category": "IoT",
    "sequence": -1,
    "summary": "NodeMCU ESP8266 with DHT11 to Odoo",
    "description": "A simlpe monitoring DHT11 data on Odoo with NodeMCU ESP8266",
    "website": "https://cagatayuresin.com/cu-nodemcu-dht11",
    "maintainer": "Çağatay ÜRESİN - cagatayuresin@gmail.com",
    "depends": [
        "base",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/cu_nodemcu_dht11_record_views.xml",
        "views/cu_nodemcu_dht11_menu_views.xml",
        "views/res_config_settings_views.xml",
        "data/dht11_user.xml",
        "data/default_settings.xml",
    ],
    "auto_install": False,
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
