# -*- coding: utf-8 -*-

from odoo import models, fields, api
 
class tareassos(models.Model):
	_name = "tareassos.tareassos"
	titulo = fields.Char(string='Titulo Tarea', required=True)
	descripcion = fields.Text('Descripción', required=True,)
	photo = fields.Binary(string='Photo')
	is_done = fields.Boolean('¿Terminada?')
	active = fields.Boolean('¿Tarea activa?', default=True) 
	
	@api.one def do_toggle_done(self):
    self.is_done = not self.is_done
    return True

	@api.multi def do_clear_done(self):
    done_recs = self.search([('is_done', '=', True)])
    done_recs.write({'active': False})
    return True