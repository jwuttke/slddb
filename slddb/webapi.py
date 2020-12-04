import json

from urllib import request, parse
from . import SLDDB, DB_FILE
from .dbconfig import WEBAPI_URL
from .material import Material, Formula


class SLD_API():
    """
      Python API for users of the SLDDB data.

      Allows to query the online database for materials, calculate SLDs and add new materials.
      If connection to the server fails, a local copy of the database is used, instead.

      Usage:
        from slddb import api
        res=api.search(fomula="Fe2O3")
        res[0]['density'] => ....

        m=api.material(res[0]['ID']) # retreive all data for the given material, see Material class.
        sldn=m.rho_n # get nuclear neutron SLD (complex number)
        sldm=m.rho_m # get magnetic neutron SLD (real number)
        sldx=m.f_of_E(E=8.047823) # get x-ray SLD (complex number) for given energy, default is Cu-Kalpha

        # custom material just for SLD calculation, requires either dens, fu_volume, rho_n or xsld+xE
        m=api.custom(formula='Au', dens=19.3)

      Units of results/queries:
        density: g/cm³
        roh_n: Å^{-2}
        roh_m: Å^{-2}
        sldx: Å^{-2}
        fu_volume: Å³
    """

    def __init__(self):
        self.first_access=True

    def check(self):
        # make sure the local database file is up to date, if not try to download newest version
        if self.first_access:
            # TODO: Supply local databse file to download and check date here.
            self.db=SLDDB(DB_FILE) # after potential update, make connection with local database
            self.first_access=False
        else:
            return

    def webquery(self, dict):
        data=parse.urlencode(dict)
        #req=request.Request(WEBAPI_URL, data=data, method='GET')  # this will make the method "POST"
        webdata=request.urlopen(WEBAPI_URL+'?'+data)
        return json.loads(webdata.read()) # return decoded data

    def search(self, **opts):
        '''
        Search for a particular material using a combination of provided search keys.

        Examples:
             api.search(formula="Fe2O3")
             api.search(density=5.242)
             api.search(name='iron')
        '''
        self.check()
        # TODO: add some validation to the search query.
        res=self.webquery(opts)
        return res

    def material(self, ID):
        """
        Returns the material object for a certain databse entry specified by its unique ID.

        Example:
            res=api.search(formula='Fe')
            material=api.material(res[0]['ID'])
            print(material.dens, material.rho_n, material.f_of_E(8.0))
        """
        self.check()
        res=self.webquery({'ID': int(ID)})

        f=Formula(res['formula'], sort=False)
        out=Material([(self.db.elements.get_element(element), amount) for element, amount in f],
                   dens=float(res['density']))
        return out

    def custom(self, formula, dens=None, fu_volume=None, rho_n=None, mu=0., xsld=None, xE=None):
        """
        Returns the material object for a certain material as specified by caller.

        Example:
            res=api.custom('Fe', dens=7.8)
            print(material.dens, material.rho_n, material.f_of_E(8.0))
        """
        self.check()
        f=Formula(formula, sort=False)
        out=Material([(self.db.elements.get_element(element), amount) for element, amount in f],
                   dens=dens, fu_volume=fu_volume, rho_n=rho_n, mu=0.0, xsld=xsld, xE=xE)
        return out
