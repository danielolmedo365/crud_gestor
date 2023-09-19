from organizaciones import Organizaciones

from dbpostgresql import DBPostgresql




TABLE = {
    'id_org': {
        'type': 'string',
        'min_length': 1,
        'max_length': 50
    },
    'nom_org': {
        'type': 'string',
        'min_length': 3,
        'max_length': 50
    },
    'tipo_org': {
        'type': 'string',
        'min_length': 3,
        'max_length': 50
    },
    'otro_tipo_org': {
        'type': 'string',
        'min_length': 3,
        'max_length': 50
    },
    'fig_legal': {
        'type': 'string',
        'min_length': 3,
        'max_length': 50
    },
    'otro_fig_legal': {
        'type': 'string',
        'min_length': 3,
        'max_length': 50
    },
    'objetivos': {
        'type': 'string',
        'min_length': 3,
        'max_length': 200
    },
    'anyo_fund': {
        'type': 'integer',
        'min_value': 1900,
        'max_value': 2100
    },
    'direc_ofi': {
        'type': 'string',
        'min_length': 3,
        'max_length': 100
    },
    'nom_tec_imple': {
        'type': 'string',
        'min_length': 3,
        'max_length': 50
    },
    'cel_tec_imple': {
        'type': 'string',
        'min_length': 3,
        'max_length': 15
    },
    'email_tec_imple': {
        'type': 'string',
        'min_length': 5,
        'max_length': 50
    },
    'pers_contact': {
        'type': 'string',
        'min_length': 3,
        'max_length': 50
    },
    'email_contact': {
        'type': 'string',
        'min_length': 5,
        'max_length': 50
    },
    'telef_contact': {
        'type': 'string',
        'min_length': 7,
        'max_length': 15
    },
    'org_ases_acomp': {
        'type': 'string',
        'min_length': 3,
        'max_length': 100
    },
    'num_soci': {
        'type': 'integer',
        'min_value': 0,
        'max_value': 1000000
    },
    'hombres': {
        'type': 'integer',
        'min_value': 0,
        'max_value': 1000000
    },
    'mujeres': {
        'type': 'integer',
        'min_value': 0,
        'max_value': 1000000
    },
    'num_famils': {
        'type': 'integer',
        'min_value': 0,
        'max_value': 1000000
    },
    'num_ha_org': {
        'type': 'float',
        'min_value': 0,
        'max_value': 1000000
    },
    'num_ha_infl_org': {
        'type': 'float',
        'min_value': 0,
        'max_value': 1000000
    },
    'prod_sist_aten': {
        'type': 'string',
        'min_length': 3,
        'max_length': 200
    },
    'otro_sist_aten': {
        'type': 'string',
        'min_length': 3,
        'max_length': 200
    },
    'sit_web': {
        'type': 'string',
        'min_length': 3,
        'max_length': 100
    },
    'redes_sociales': {
        'type': 'string',
        'min_length': 3,
        'max_length': 100
    },
    'nombre_contesta': {
        'type': 'string',
        'min_length': 3,
        'max_length': 50
    }
}


class DBOrganizaciones(DBPostgresql):

    def __init__(self):
        super().__init__(TABLE, 'datos_generales')

    

    
    
    def update_contact(self, id_object, data):
        if not id_object:
            raise ValueError('Debes envíar el id del contacto')
        if not data:
            raise ValueError('Debes envíar al menos un parámetro a actualizar')
        self.update(id_object, data)

    """
    def save_contact(self, registro):
        data = {
            'identificador':registro.id_organizacion, 
            'nombre':registro.nombre, 

        }
        return self.insert(data)



    def delete_contact(self, id_object):
        if not id_object:
            raise ValueError('Debes envíar el id del contacto')
        self.delete(id_object)


    def list_contacts(self):
        list_contacts = self.get_all()
        return self._create_object_contacts(list_contacts)

    
    def get_schema(self):
        return TABLE
    


    def search_contacts(self, filters):
        if not filters:
            raise ValueError('Debes envíar al menos un filtro')

        list_contacts = self.get_by_filters(filters)
        return self._create_object_contacts(list_contacts)

   
    def _create_object_contacts(self, list_contacts):

        if not list_contacts:
            return None

        object_contacts = []
        # Convertimos los datos a objectos de tipo registro
        for registro in list_contacts:
            c = Organizaciones(registro['id'], registro['name'], registro['surname'], registro['email'], registro['phone'], registro['birthday'])
            object_contacts.append(c)

        return object_contacts
        
    """