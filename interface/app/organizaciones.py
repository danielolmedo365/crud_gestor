class Organizaciones:

    def __init__(self, id_org, nom_org, tipo_org, otro_tipo_org, fig_legal,
                 otro_fig_legal, objetivos, anyo_fund, direc_ofi, nom_tec_imple,
                 cel_tec_imple, email_tec_imple, pers_contact, email_contact, telef_contact,
                 org_ases_acomp, num_soci, hombres, mujeres, num_famils, num_ha_org,
                 num_ha_infl_org, prod_sist_aten, otro_sist_aten, sit_web,
                 redes_sociales, nombre_contesta):
        
        self._id_org = id_org
        self._nom_org = nom_org
        self._tipo_org = tipo_org
        self._otro_tipo_org = otro_tipo_org
        self._fig_legal = fig_legal
        self._otro_fig_legal = otro_fig_legal
        self._objetivos = objetivos
        self._anyo_fund = anyo_fund
        self._direc_ofi = direc_ofi
        self._nom_tec_imple = nom_tec_imple
        self._cel_tec_imple = cel_tec_imple
        self._email_tec_imple = email_tec_imple
        self._pers_contact = pers_contact
        self._email_contact = email_contact
        self._telef_contact = telef_contact
        self._org_ases_acomp = org_ases_acomp
        self._num_soci = num_soci
        self._hombres = hombres
        self._mujeres = mujeres
        self._num_famils = num_famils
        self._num_ha_org = num_ha_org
        self._num_ha_infl_org = num_ha_infl_org
        self._prod_sist_aten = prod_sist_aten
        self._otro_sist_aten = otro_sist_aten
        self._sit_web = sit_web
        self._redes_sociales = redes_sociales
        self._nombre_contesta = nombre_contesta

    
    @property
    def id_org(self):
        return self._id_org

    @id_org.setter
    def id_org(self, id_org):
        self._id_org = id_org

    @property
    def nom_org(self):
        return self._nom_org

    @nom_org.setter
    def nom_org(self, nom_org):
        self._nom_org = nom_org

    @property
    def tipo_org(self):
        return self._tipo_org

    @tipo_org.setter
    def tipo_org(self, tipo_org):
        self._tipo_org = tipo_org

    @property
    def otro_tipo_org(self):
        return self._otro_tipo_org

    @otro_tipo_org.setter
    def otro_tipo_org(self, otro_tipo_org):
        self._otro_tipo_org = otro_tipo_org

    @property
    def fig_legal(self):
        return self._fig_legal

    @fig_legal.setter
    def fig_legal(self, fig_legal):
        self._fig_legal = fig_legal

    @property
    def otro_fig_legal(self):
        return self._otro_fig_legal

    @otro_fig_legal.setter
    def otro_fig_legal(self, otro_fig_legal):
        self._otro_fig_legal = otro_fig_legal

    @property
    def objetivos(self):
        return self._objetivos

    @objetivos.setter
    def objetivos(self, objetivos):
        self._objetivos = objetivos

    @property
    def anyo_fund(self):
        return self._anyo_fund

    @anyo_fund.setter
    def anyo_fund(self, anyo_fund):
        self._anyo_fund = anyo_fund

    @property
    def direc_ofi(self):
        return self._direc_ofi

    @direc_ofi.setter
    def direc_ofi(self, direc_ofi):
        self._direc_ofi = direc_ofi

    @property
    def nom_tec_imple(self):
        return self._nom_tec_imple

    @nom_tec_imple.setter
    def nom_tec_imple(self, nom_tec_imple):
        self._nom_tec_imple = nom_tec_imple

    @property
    def cel_tec_imple(self):
        return self._cel_tec_imple

    @cel_tec_imple.setter
    def cel_tec_imple(self, cel_tec_imple):
        self._cel_tec_imple = cel_tec_imple

    @property
    def email_tec_imple(self):
        return self._email_tec_imple

    @email_tec_imple.setter
    def email_tec_imple(self, email_tec_imple):
        self._email_tec_imple = email_tec_imple

    @property
    def pers_contact(self):
        return self._pers_contact

    @pers_contact.setter
    def pers_contact(self, pers_contact):
        self._pers_contact = pers_contact

    @property
    def email_contact(self):
        return self._email_contact

    @email_contact.setter
    def email_contact(self, email_contact):
        self._email_contact = email_contact

    @property
    def telef_contact(self):
        return self._telef_contact

    @telef_contact.setter
    def telef_contact(self, telef_contact):
        self._telef_contact = telef_contact

    @property
    def org_ases_acomp(self):
        return self._org_ases_acomp

    @org_ases_acomp.setter
    def org_ases_acomp(self, org_ases_acomp):
        self._org_ases_acomp = org_ases_acomp

    @property
    def num_soci(self):
        return self._num_soci

    @num_soci.setter
    def num_soci(self, num_soci):
        self._num_soci = num_soci

    @property
    def hombres(self):
        return self._hombres

    @hombres.setter
    def hombres(self, hombres):
        self._hombres = hombres

    @property
    def mujeres(self):
        return self._mujeres

    @mujeres.setter
    def mujeres(self, mujeres):
        self._mujeres = mujeres

    @property
    def num_famils(self):
        return self._num_famils

    @num_famils.setter
    def num_famils(self, num_famils):
        self._num_famils = num_famils

    @property
    def num_ha_org(self):
        return self._num_ha_org

    @num_ha_org.setter
    def num_ha_org(self, num_ha_org):
        self._num_ha_org = num_ha_org

    @property
    def num_ha_infl_org(self):
        return self._num_ha_infl_org

    @num_ha_infl_org.setter
    def num_ha_infl_org(self, num_ha_infl_org):
        self._num_ha_infl_org = num_ha_infl_org

    @property
    def prod_sist_aten(self):
        return self._prod_sist_aten

    @prod_sist_aten.setter
    def prod_sist_aten(self, prod_sist_aten):
        self._prod_sist_aten = prod_sist_aten

    @property
    def otro_sist_aten(self):
        return self._otro_sist_aten

    @otro_sist_aten.setter
    def otro_sist_aten(self, otro_sist_aten):
        self._otro_sist_aten = otro_sist_aten

    @property
    def sit_web(self):
        return self._sit_web

    @sit_web.setter
    def sit_web(self, sit_web):
        self._sit_web = sit_web

    @property
    def redes_sociales(self):
        return self._redes_sociales

    @redes_sociales.setter
    def redes_sociales(self, redes_sociales):
        self._redes_sociales = redes_sociales

    @property
    def nombre_contesta(self):
        return self._nombre_contesta

    @nombre_contesta.setter
    def nombre_contesta(self, nombre_contesta):
        self._nombre_contesta = nombre_contesta