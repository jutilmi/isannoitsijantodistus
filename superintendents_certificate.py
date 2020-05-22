"""Module includes class for superintendents certificate
   representing certificate for a specific apartment
   """

from os import path
from datetime import datetime

import xml.etree.ElementTree as ET
from hoc import HousingCompany
from cei import Certificate
from spa import ServiceProvidersAndAdministration

# Imports from external databases, for housing company database and accounting database
from housing_company_db_classes import SQL
from accounting_db_classes import MeritAktiva

# Import html report method from reports module
from reports import export_apartment_loan_share_calculation_as_html

class SuperintendentsCertificate:
    """Form a housing company certificate."""

    def __init__(self,
                 apartment_id,
                 diary_number,
                 housing_company_database_settings=None,
                 accounting_database_settings=None,
                 base_housing_company_certificate=None,
                 context_ref="ctx1",
                 ):
        """Initializes housing company certificate.

           Keyword arguments:
           apartment_id                      -- int, apartment id number
           diary_number                      -- str, diary number of the superintendets certificate
           housing_company_database_settings -- dict, housing company database settings
               {'Type' : str (ACCESS/SQLite/MySQL),
                'Path' : path to database}
           accounting_database_settings      -- dict, accounting database settings
           base_housing_company_certificate  -- dict, static data of an housing company
            {
                'HousingCompany' : {},
                'Certificate' : {},
                'TheCompanySServiceProvidersAndAdministration' : {}
                }
        """
        self.time_of_report = datetime.now()
        self.context_ref = context_ref
        self.apartment_id = apartment_id
        self.diary_number = diary_number

        self.namespaces = {
            'fi-suc-entrypoint' : "http://www.xbrl.fi/suc/entrypoints/suc/01-01-2017",
            'link' : "http://www.xbrl.org/2003/linkbase",
            'fi-suc-cei' : "http://www.xbrl.fi/suc/common_data/base/cei/01-01-2017",
            'fi-suc-spa' : "http://www.xbrl.fi/suc/common_data/base/spa/01-01-2017",
            'xsi' : "http://www.w3.org/2001/XMLSchema-instance",
            'xbrli' : "http://www.xbrl.org/2003/instance",
            'iso4217' : "http://www.xbrl.org/2003/iso4217",
            'utr' : "http://www.xbrl.org/2009/utr",
            'xlink' : "http://www.w3.org/1999/xlink",
            'fi-suc-hoc' : "http://www.xbrl.fi/suc/common_data/base/hoc/01-01-2017"
            }

        for key, value in self.namespaces.items():
            ET.register_namespace(key, value)

        self.xbrl = ET.ElementTree(ET.Element('{' + self.namespaces['xbrli'] + '}' + 'xbrl'))

        self.housing_company = HousingCompany(self.namespaces['fi-suc-hoc'], self.context_ref)
        self.certificate = Certificate(self.xbrl.getroot(), self.namespaces['fi-suc-cei'],
                                       self.context_ref)
        self.service_providers_and_administration =\
            ServiceProvidersAndAdministration(self.context_ref, self.namespaces['fi-suc-spa'])

        # Check if database exists
        if not path.isfile(housing_company_database_settings['Path']):
            raise FileExistsError

        # Housing companyt database initialize based on company data
        self.hoc_db = SQL(database=(housing_company_database_settings['Path']),
                          database_type=housing_company_database_settings['Type'])

        # Accounting database initialize
        if accounting_database_settings['AccountingSource'] == 'MeritAktiva':
            self.accounting_db = MeritAktiva(api_id=accounting_database_settings['ApiID'],
                                             api_key=accounting_database_settings['ApiKey'])

    def print_certificate(self):
        """This function prints the certificate in Word format"""
        pass
