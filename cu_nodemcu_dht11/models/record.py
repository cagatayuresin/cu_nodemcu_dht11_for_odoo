# -*- coding: utf-8 -*-

from odoo import fields, models

class DHT11Record(models.Model):
    _name = "cu_nodemcu_dht11.record"
    _description = "DHT11 Record"

    humidity = fields.Integer(string="Humidity", index=True, readonly=True, store=True)
    temperature = fields.Integer(string="Temperature Celsius", index=True, readonly=True, store=True)
    temperature_fahrenheit = fields.Integer(string="Temperature Fahrenheit", index=True, readonly=True, store=True)
    sensor_id = fields.Char(string="Sensor ID", index=True, readonly=True, store=True)
    state = fields.Selection([('1', 'Cold'), ('2', 'Warm'), ('3', 'Hot')], string="State", index=True, readonly=True, store=True)
    