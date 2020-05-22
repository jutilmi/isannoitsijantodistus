"""Module includes ServiceProvidesAndAdministration-class and
   its methods according cei entry point"""

import xml.etree.ElementTree as ET
import functions

class ServiceProvidersAndAdministration:
    """Luokka vastaa isännöitsijäntodistuksen taksonometriassa
        Yhtiön palveluntuottajat ja hallinto -osioita ja sen luontia."""

    def __init__(self, namespace, contextRef="ctx1"):
        """Funktion argumentti xbrl on tyyppiä etree.ElementTree

            Keyword arguments:
            context_ref             -- str, reference context identifier on elements
            """
        # Creating root element for xml document
        self.namespace = namespace

        self.spa = ET.Element('{'+self.namespace+'}'+'TheCompanySServiceProvidersAndAdministration')
        self.__spa_elements()

        self.spa = functions.set_context_ref(self.spa, contextRef)

    def __spa_elements(self):

        sub_elements = {
            'RealEstatePropertyManagement' : 'RealEstatePropertyManagementItemType',
            'SuperintendentPersonalDetails' : 'SuperintendentPersonalDetailsItemType',
            'RealEstateManagementOrganizationDetails' :
                'RealEstateManagementOrganizationDetailsItemType',
            'Administration' : 'AdministrationItemType'
            }

        for key, value in sub_elements.items():
            sub_element = ET.SubElement(self.spa, '{'+self.namespace+'}'+key)
            if value == 'RealEstatePropertyManagementItemType':
                self.__real_estate_property_management_it(sub_element)
            elif value == 'SuperintendentPersonalDetailsItemType':
                self.__superintendets_personal_details_it(sub_element)
            elif value == 'RealEstateManagementOrganizationDetailsItemType':
                self.__real_estate_managment_org_dets_it(sub_element)
            elif value == 'AdministrationItemType':
                self.__administration_it(sub_element)

#        functions.elements_to_element_tree(sub_elements, parent_element, '{'+self.namespace+'}'')

    def __real_estate_property_management_it(self, parent_element):

        sub_elements = {
            'PropertyManagementApproach' : 'stringItemType',
            'PropertyManagementApproachAddiionalDetail' : 'stringItemType',
            'PropertyManagementProvider' : 'PropertyManagementProviderItemType'
        }

        sub_elements.pop('PropertyManagementProvider')
        functions.elements_to_element_tree(sub_elements, parent_element, '{'+self.namespace+'}')

        sub_element = ET.SubElement(parent_element,
                                    '{'+self.namespace+'}'+'PropertyManagementProvider')
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
            '{'+self.namespace+'}'+'PropertyManagementProviderAddress')
        self.__property_management_provider_address_it(sub_element)

        sub_elements.pop('PropertyManagementProviderAddress')

        functions.elements_to_element_tree(sub_elements, parent_element, '{'+self.namespace+'}')

    def __property_management_provider_address_it(self, parent_element):

        sub_elements = {
            'PropertyManagementProviderStreetAddress' : 'stringItemType',
            'PropertyManagementProviderPostalCode' : 'stringItemType',
            'PropertyManagementProviderCity' : 'stringItemType',
            'PropertyManagementProviderCountry' : 'stringItemType'
        }

        functions.elements_to_element_tree(sub_elements, parent_element, '{'+self.namespace+'}')

    def __superintendets_personal_details_it(self, parent_element):

        sub_elements = {
            'SuperintendentName' : 'stringItemType',
            'SuperintendentQualificationCertificate' : 'stringItemType',
            'SuperintendentPhoneNumber' : 'stringItemType',
            'SuperintendentEmail' : 'stringItemType',
            'SuperintendentAuthorizationIsa' : 'booleanItemType'
        }

        functions.elements_to_element_tree(sub_elements, parent_element, '{'+self.namespace+'}')

    def __real_estate_managment_org_dets_it(self, parent_element):

        sub_elements = {
            'RealEstateManagementOrganizationName' : 'stringItemType',
            'RealEstateManagementOrganizationAddress' :
                'RealEstateManagementOrganizationAddressItemType',
            'RealEstateManagementOrganizationOrganizationIdentifier' : 'stringItemType',
            'RealEstateManagementOrganizationAuthorizationIsa' : 'booleanItemType'
        }

        functions.elements_to_element_tree(sub_elements, parent_element, '{'+self.namespace+'}')

        for child in parent_element:
            if child.tag == '{'+self.namespace+'}'+'RealEstateManagementOrganizationAddress':
                self.__real_estate_manag_org_address_it(child)

    def __real_estate_manag_org_address_it(self, parent_element):

        sub_elements = {
            'RealEstateManagementOrganizationStreetAddress' : 'stringItemType',
            'RealEstateManagementOrganizationPostalCode' : 'stringItemType',
            'RealEstateManagementOrganizationCity' : 'stringItemType',
            'RealEstateManagementOrganizationCountry' : 'stringItemType'
        }

        functions.elements_to_element_tree(sub_elements, parent_element, '{'+self.namespace+'}')

    def __administration_it(self, parent_element):

        sub_elements = {
            'AdministrationMember' : 'AdministrationMemberItemType'
        }

        functions.elements_to_element_tree(sub_elements, parent_element, '{'+self.namespace+'}')

        self.__administration_member_it(parent_element[0])

    def __administration_member_it(self, parent_element):

        sub_elements = {
            'AdministrationMemberRole' : 'stringItemType',
            'AdministrationMemberName' : 'stringItemType',
            'AdministrationMemberContactDetail' : 'stringItemType'
        }

        functions.elements_to_element_tree(sub_elements, parent_element, '{'+self.namespace+'}')
