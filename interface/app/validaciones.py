import re

regex_email = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
regex_phone = '^[0-9]{9}$'

class ValidacionesOrganizaciones:

    def __init__(self):
        pass

    def validateIdOrg(self, id_org):
        if len(id_org) < 1 or len(id_org) > 50:
            raise ValueError(f'El identificador de la organización debe tener como mínimo 1 caractares y un máximo de 50 caracteres, tamaño actual: {len(id_org)}')
        return True

    def validateNom_org(self, nom_org):
        if len(nom_org) < 3 or len(nom_org) > 50:
            raise ValueError(f'El nombre de la organización debe tener como mínimo 3 caracteres y un máximo de 50 caracteres, tamaño actual: {len(nom_org)}')
        return True

    def validateTipoOrg(self, tipo_org):
        if len(tipo_org) < 3 or len(tipo_org) > 50:
            raise ValueError(f'El tipo de organización debe tener como mínimo 3 caracteres y un máximo de 50 caracteres, tamaño actual: {len(tipo_org)}')
        return True

    def validateOtroTipoOrg(self, otro_tipo_org):
        if len(otro_tipo_org) < 3 or len(otro_tipo_org) > 50:
            raise ValueError(f'Otro tipo de organización debe tener como mínimo 3 caracteres y un máximo de 50 caracteres, tamaño actual: {len(otro_tipo_org)}')
        return True

    def validateFigLegal(self, fig_legal):
        if len(fig_legal) < 3 or len(fig_legal) > 50:
            raise ValueError(f'La figura legal debe tener como mínimo 3 caracteres y un máximo de 50 caracteres, tamaño actual: {len(fig_legal)}')
        return True

    def validateOtroFigLegal(self, otro_fig_legal):
        if len(otro_fig_legal) < 3 or len(otro_fig_legal) > 50:
            raise ValueError(f'Otra figura legal debe tener como mínimo 3 caracteres y un máximo de 50 caracteres, tamaño actual: {len(otro_fig_legal)}')
        return True

    def validateObjetivos(self, objetivos):
        if len(objetivos) < 3 or len(objetivos) > 200:
            raise ValueError(f'Los objetivos deben tener como mínimo 3 caracteres y un máximo de 200 caracteres, tamaño actual: {len(objetivos)}')
        return True

    def validateAnyoFund(self, anyo_fund):
        if not (1900 <= anyo_fund <= 2100):
            raise ValueError('El año de fundación debe estar entre 1900 y 2100')
        return True

    def validateDirecOfi(self, direc_ofi):
        if len(direc_ofi) < 3 or len(direc_ofi) > 100:
            raise ValueError(f'La dirección de oficina debe tener como mínimo 3 caracteres y un máximo de 100 caracteres, tamaño actual: {len(direc_ofi)}')
        return True

    def validateNomTecImple(self, nom_tec_imple):
        if len(nom_tec_imple) < 3 or len(nom_tec_imple) > 50:
            raise ValueError(f'El nombre del técnico implementador debe tener como mínimo 3 caracteres y un máximo de 50 caracteres, tamaño actual: {len(nom_tec_imple)}')
        return True

    def validateCelTecImple(self, cel_tec_imple):
        if not re.search(regex_phone, cel_tec_imple):
            raise ValueError('El formato del teléfono del técnico implementador no es válido, debe ser un número de 9 cifras sin guiones ni puntos')
        return True

    def validateEmailTecImple(self, email_tec_imple):
        if not re.search(regex_email, email_tec_imple):
            raise ValueError('El formato del email del técnico implementador no es válido')
        return True

    def validatePersContact(self, pers_contact):
        if len(pers_contact) < 3 or len(pers_contact) > 50:
            raise ValueError(f'La persona de contacto debe tener como mínimo 3 caracteres y un máximo de 50 caracteres, tamaño actual: {len(pers_contact)}')
        return True

    def validateEmailContact(self, email_contact):
        if not re.search(regex_email, email_contact):
            raise ValueError('El formato del email de contacto no es válido')
        return True

    def validateTelefContact(self, telef_contact):
        if not re.search(regex_phone, telef_contact):
            raise ValueError('El formato del teléfono de contacto no es válido, debe ser un número de 9 cifras sin guiones ni puntos')
        return True

    def validateOrgAsesAcomp(self, org_ases_acomp):
        if len(org_ases_acomp) < 3 or len(org_ases_acomp) > 100:
            raise ValueError(f'La organización de asesoramiento y acompañamiento debe tener como mínimo 3 caracteres y un máximo de 100 caracteres, tamaño actual: {len(org_ases_acomp)}')
        return True

    def validateNumSoci(self, num_soci):
        if not (0 <= num_soci <= 1000000):
            raise ValueError('El número de socios debe ser un valor entre 0 y 1,000,000')
        return True

    def validateHombres(self, hombres):
        if not (0 <= hombres <= 1000000):
            raise ValueError('La cantidad de hombres debe ser un valor entre 0 y 1,000,000')
        return True

    def validateMujeres(self, mujeres):
        if not (0 <= mujeres <= 1000000):
            raise ValueError('La cantidad de mujeres debe ser un valor entre 0 y 1,000,000')
        return True

    def validateNumFamils(self, num_famils):
        if not (0 <= num_famils <= 1000000):
            raise ValueError('El número de familias debe ser un valor entre 0 y 1,000,000')
        return True

    def validateNumHaOrg(self, num_ha_org):
        if not (0 <= num_ha_org <= 1000000):
            raise ValueError('El número de hectáreas de la organización debe ser un valor entre 0 y 1,000,000')
        return True

    def validateNumHaInflOrg(self, num_ha_infl_org):
        if not (0 <= num_ha_infl_org <= 1000000):
            raise ValueError('El número de hectáreas influyentes de la organización debe ser un valor entre 0 y 1,000,000')
        return True

    def validateProdSistAten(self, prod_sist_aten):
        if len(prod_sist_aten) < 3 or len(prod_sist_aten) > 200:
            raise ValueError(f'Los productos o sistemas de atención deben tener como mínimo 3 caracteres y un máximo de 200 caracteres, tamaño actual: {len(prod_sist_aten)}')
        return True

    def validateOtroSistAten(self, otro_sist_aten):
        if len(otro_sist_aten) < 3 or len(otro_sist_aten) > 200:
            raise ValueError(f'Otro sistema de atención debe tener como mínimo 3 caracteres y un máximo de 200 caracteres, tamaño actual: {len(otro_sist_aten)}')
        return True

    def validateSitWeb(self, sit_web):
        if len(sit_web) < 3 or len(sit_web) > 100:
            raise ValueError(f'La dirección del sitio web debe tener como mínimo 3 caracteres y un máximo de 100 caracteres, tamaño actual: {len(sit_web)}')
        return True

    def validateRedesSociales(self, redes_sociales):
        if len(redes_sociales) < 3 or len(redes_sociales) > 100:
            raise ValueError(f'Las redes sociales deben tener como mínimo 3 caracteres y un máximo de 100 caracteres, tamaño actual: {len(redes_sociales)}')
        return True

    def validateNombreContesta(self, nombre_contesta):
        if len(nombre_contesta) < 3 or len(nombre_contesta) > 50:
            raise ValueError(f'El nombre del contacto debe tener como mínimo 3 caracteres y un máximo de 50 caracteres, tamaño actual: {len(nombre_contesta)}')
        return True

