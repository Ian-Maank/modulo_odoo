# -*- coding: utf-8 -*-

from odoo import models, fields
 
class tareassos(models.Model):
	_name = "tareassos.tareassos"
	titulo = fields.Char(string='Titulo Tarea', required=True)
	descripcion = fields.Text('Descripción', required=True,)
	photo = fields.Binary(string='Photo')
	terminada = fields.Boolean('Terminada', default=False, help='')
	activa = fields.Boolean('¿Tarea activa?', default=True) 