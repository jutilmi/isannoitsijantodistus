"""This module includes class for superintendents certificate
representing certificate for a specific apartment
"""

#import xml.etree.ElementTree as ET
from hoc import HousingCompany
from cei import Certificate
from spa import ServiceProvidersAndAdministration

class SuperintendentsCertificate:
    """Form a housing company certificate."""

    def __init__(self,
                 apartment_id,
                 diary_number,
                 housing_company_database_settings=None,
                 base_housing_company_certificate=None,
                 context_ref="cxt1",
                 ):
        """Initializes housing company certificate.

        Keyword arguments:
        apartment_id                      -- int, apartment id number
        diary_number                      -- str, diary number of the superintendets certificate
        housing_company_database_settings -- dict, database settings
            {'Database' : str, path to satabase }
        base_housing_company_certificate  -- dict, static data of an housing company
            {
                'HousingCompany' : {},
                'Certificate' : {},
                'TheCompanySServiceProvidersAndAdministration' : {}
                }
        """
        self.context_ref = context_ref
        self.apartment_id = apartment_id
        self.diary_number = diary_number
        self.housing_company = HousingCompany(self.context_ref)
        self.certificate = Certificate(self.context_ref, self.diary_number)
        self.service_providers_and_administration =\
            ServiceProvidersAndAdministration(self.context_ref)

    def print_certificate(self):
        """This function prints the certificate in Word format"""
        pass
