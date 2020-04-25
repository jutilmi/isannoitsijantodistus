"""This module includes ServiceProvidesAndAdministration-class and
   its methods according cei entry point"""

import xml.etree.ElementTree as ET
import functions

class ServiceProvidersAndAdministration:
    """Tämä luokka vastaa isännöitsijäntodistuksen taksonometriassa
        Yhtiön palvelunttuottajat ja hallinto -osioita ja sen luontia."""

    def __init__(self, contextRef="ctx1"):
        """Tämän funktion argumentti xbrl on tyyppiä etree.ElementTree
            palauttaa täytetyn saman polun

            Keyword arguments:
            context_ref             -- str, reference context identifier on elements
            """
        # Creating root element for xml document
        self.spa = ET.Element('fi-suc-spa:TheCompanySServiceProvidersAndAdministration')
        self.__spa_elements(self.spa)

        self.spa = functions.set_context_ref(self.spa, contextRef)

    def __spa_elements(self, parent_element):

        sub_elements = {
            'RealEstatePropertyManagement' : 'RealEstatePropertyManagementItemType',
            'SuperintendentPersonalDetails' : 'SuperintendentPersonalDetailsItemType',
            'RealEstateManagementOrganizationDetails' :
                'RealEstateManagementOrganizationDetailsItemType',
            'Administration' : 'AdministrationItemType'
            }

        for key in sub_elements:
            sub_element = ET.SubElement(parent_element, 'fi-suc-spa:'+key)
            if sub_element.tag == 'fi-suc-spa:RealEstatePropertyManagement':
                self.__real_estate_property_management_it(sub_element)
            elif sub_element.tag == 'fi-suc-spa:SuperintendentPersonalDetails':
                self.__superintendets_personal_details_it(sub_element)
            elif sub_element.tag == 'fi-suc-spa:RealEstateManagementOrganizationDetails':
                self.__real_estate_managment_org_dets_it(sub_element)
            elif sub_element.tag == 'fi-suc-spa:Administration':
                self.__administration_it(sub_element)

#        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-spa:')

    def __real_estate_property_management_it(self, parent_element):

        sub_elements = {
            'PropertyManagementApproach' : 'stringItemType',
            'PropertyManagementApproachAddiionalDetail' : 'stringItemType',
            'PropertyManagementProvider' : 'PropertyManagementProviderItemType'
        }

        sub_elements.pop('PropertyManagementProvider')
        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-spa:')

        sub_element = ET.SubElement(parent_element, 'fi-suc-spa:PropertyManagementProvider')
        self.__property_management_provider_it(sub_element)

    def __property_management_provider_it(self, parent_element):

        sub_elements = {
            'PropertyManagementProviderContactName' : 'stringItemType',
            'PropertyManagementProviderAddress' : 'PropertyManagementProviderAddressItemType',
            'PropertyManagementProviderPhoneNumber' : 'stringItemType',
            'PropertyManagementProviderEmail' : 'stringItemType'
        }

        sub_element = ET.SubElement(
            parent_element,
            'fi-suc-spa:PropertyManagementProviderAddress')
        self.__property_management_provider_address_it(sub_element)

        sub_elements.pop('PropertyManagementProviderAddress')

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-spa:')

    def __property_management_provider_address_it(self, parent_element):

        sub_elements = {
            'PropertyManagementProviderStreetAddress' : 'stringItemType',
            'PropertyManagementProviderPostalCode' : 'stringItemType',
            'PropertyManagementProviderCity' : 'stringItemType',
            'PropertyManagementProviderCountry' : 'stringItemType'
        }

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-spa:')

    def __superintendets_personal_details_it(self, parent_element):

        sub_elements = {
            'SuperintendentName' : 'stringItemType',
            'SuperintendentQualificationCertificate' : 'stringItemType',
            'SuperintendentPhoneNumber' : 'stringItemType',
            'SuperintendentEmail' : 'stringItemType',
            'SuperintendentAuthorizationIsa' : 'booleanItemType'
        }

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-spa:')

    def __real_estate_managment_org_dets_it(self, parent_element):

        sub_elements = {
            'RealEstateManagementOrganizationName' : 'stringItemType',
            'RealEstateManagementOrganizationAddress' :
                'RealEstateManagementOrganizationAddressItemType',
            'RealEstateManagementOrganizationOrganizationIdentifier' : 'stringItemType',
            'RealEstateManagementOrganizationAuthorizationIsa' : 'booleanItemType'
        }

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-spa:')

        for child in parent_element:
            if child.tag == 'fi-suc-spa:RealEstateManagementOrganizationAddress':
                self.__real_estate_manag_org_address_it(child)

    def __real_estate_manag_org_address_it(self, parent_element):

        sub_elements = {
            'RealEstateManagementOrganizationStreetAddress' : 'stringItemType',
            'RealEstateManagementOrganizationPostalCode' : 'stringItemType',
            'RealEstateManagementOrganizationCity' : 'stringItemType',
            'RealEstateManagementOrganizationCountry' : 'stringItemType'
        }

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-spa:')

    def __administration_it(self, parent_element):

        sub_elements = {
            'AdministrationMember' : 'AdministrationMemberItemType'
        }

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-spa:')

        self.__administration_member_it(parent_element[0])

    def __administration_member_it(self, parent_element):

        sub_elements = {
            'AdministrationMemberRole' : 'stringItemType',
            'AdministrationMemberName' : 'stringItemType',
            'AdministrationMemberContactDetail' : 'stringItemType'
        }

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-spa:')
