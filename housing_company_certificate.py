"""This module includes HousingCompanyCertificate class
representing certificate for a specific apartment
"""

#import xml.etree.ElementTree as ET
from hoc import HousingCompany
from cei import Certificate
from spa import ServiceProvidersAndAdministration

class HousingCompanyCertificate(object):
    """Form a housing company certificate."""

    def __init__(self, apartment_id,
                 housing_company_database_settings = None,
                 base_housing_company_certificate = None):
        """Initializes housing company certificate.

        Keyword arguments:
        apartment_number                  -- int, apartment id number
        housing_company_database_settings -- dict, database settings
            {'Database' : str, path to satabase }
        base_housing_company_certificate  -- dict, static data of an housing company
            {
                'HousingCompany' : {},
                'Certificate' : {},
                'TheCompanySServiceProvidersAndAdministration' : {}
                }
        """
        self.apartment_id = apartment_id
        self.housing_company = HousingCompany()
        self.certificate = Certificate()
        self.service_providers_and_administration = ServiceProvidersAndAdministration()

        #housing_company_certificate = ET.Element('HousingCompanyCertificate')
        #housing_company_certificate_etree = ET.ElementTree(housing_company_certificate)

    def print_certificate(self):
        """This function prints the certificate in Word format"""
        pass
