import xml.etree.ElementTree as ET
import CommonFunctions

class ServiceProvidersAndAdministration(object):
    """Tämä luokka vastaa isännöitsijäntodistuksen taksonometriassa
        Yhtiön palvelunttuottajat ja hallinto -osioita ja sen luontia."""

    def __init__(self, contextRef = "cxt1"):
        """Tämän funktion argumentti xbrl on tyyppiä etree.ElementTree
            palauttaa täytetyn saman polun"""
        self.spa = ET.Element('TheCompanySServiceProvidersAndAdministration') #Luodaan juurielementti
        
        self.spa = self.buildSPAInformation(self.spa)

        self.spa = CommonFunctions.SetContextRef(self.spa, contextRef)
    
    def buildSPAInformation(self, RootElementTree):

        SubElements = {
            'RealEstatePropertyManagement' : 'RealEstatePropertyManagementItemType',
            'SuperintendentPersonalDetails' : 'SuperintendentPersonalDetailsItemType',
            'RealEstateManagementOrganizationDetails' : 'RealEstateManagementOrganizationDetailsItemType',
            'Administration' : 'AdministrationItemType'
        }

        CommonFunctions.ElementsToElementTree(SubElements, RootElementTree, 'fi-suc-spa:')

        return RootElementTree


    def RealEstatePropertyManagementItemType(self, RootElementTree):

        SubElements = {
            'PropertyManagementApproach' : 'stringItemType',
            'PropertyManagementApproachAddiionalDetail' : 'stringItemType',
            'PropertyManagementProvider' : 'PropertyManagementProviderItemType'
        }

        SubElement = ET.SubElement(RootElementTree, 'fi-suc-spa'+'PropertyManagementProvider')
        self.PropertyManagementProviderItemType(SubElement)

        SubElements.pop('PropertyManagementProvider')

        CommonFunctions.ElementsToElementTree(SubElements, RootElementTree, 'fi-suc-spa:')

        return RootElementTree

    def PropertyManagementProviderItemType(self, RootElementTree):

        SubElements = {
            'PropertyManagementProviderContactName' : 'stringItemType',
            'PropertyManagementProviderAddress' : 'PropertyManagementProviderAddressItemType',
            'PropertyManagementProviderPhoneNumber' : 'stringItemType',
            'PropertyManagementProviderEmail' : 'stringItemType'
        }
        
        SubElement = ET.SubElement(RootElementTree, 'fi-suc-spa:'+'PropertyManagementProviderAddress')
        self.PropertyManagementProviderAddressItemType(SubElement)

        SubElements.pop('PropertyManagementProviderAddress')

        CommonFunctions.ElementsToElementTree(SubElements, RootElementTree, 'fi-suc-spa:')

        return RootElementTree
    
    def PropertyManagementProviderAddressItemType(self, RootElementTree):

        SubElements = {
            'PropertyManagementProviderStreetAddress' : 'stringItemType',
            'PropertyManagementProviderPostalCode' : 'stringItemType',
            'PropertyManagementProviderCity' : 'stringItemType',
            'PropertyManagementProviderCountry' : 'stringItemType'                                   
        }

        CommonFunctions.ElementsToElementTree(SubElements, RootElementTree, 'fi-suc-spa:')

        return RootElementTree

    def SuperintendentPersonalDetailsItemType(self, RootElementTree):

        SubElements = {
            'SuperintendentName' : 'stringItemType',
            'SuperintendentQualificationCertificate' : 'stringItemType',
            'SuperintendentPhoneNumber' : 'stringItemType',
            'SuperintendentEmail' : 'stringItemType',
            'SuperintendentAuthorizationIsa' : 'booleanItemType'                                                
        }
   
        CommonFunctions.ElementsToElementTree(SubElements, RootElementTree, 'fi-suc-spa:')

        return RootElementTree

    def RealEstateManagementOrganizationDetailsItemType(self, RootElementTree):

        SubElements = {
            'RealEstateManagementOrganizationName' : 'stringItemType',
            'RealEstateManagementOrganizationAddress' : 'RealEstateManagementOrganizationAddressItemType',
            'RealEstateManagementOrganizationOrganizationIdentifier' : 'stringItemType',
            'RealEstateManagementOrganizationAuthorizationIsa' : 'booleanItemType'
        }

        CommonFunctions.ElementsToElementTree(SubElements, RootElementTree, 'fi-suc-spa:')

        return RootElementTree

    def RealEstateManagementOrganizationAddressItemType(self, RootElementTree):

        SubElements = {
            'RealEstateManagementOrganizationStreetAddress' : 'stringItemType',
            'RealEstateManagementOrganizationPostalCode' : 'stringItemType',
            'RealEstateManagementOrganizationCity' : 'stringItemType',
            'RealEstateManagementOrganizationCountry' : 'stringItemType'                                   
        }

        CommonFunctions.ElementsToElementTree(SubElements, RootElementTree, 'fi-suc-spa:')

        return RootElementTree        

    def AdministrationItemType(self, RootElementTree):

        SubElements = {
            'AdministrationMember' : 'AdministrationMemberItemType'
        }
    
        CommonFunctions.ElementsToElementTree(SubElements, RootElementTree, 'fi-suc-spa:')

        return RootElementTree

    def AdministrationMemberItemType(self, RootElementTree):
        
        SubElements = {
            'AdministrationMemberRole' : 'stringItemType',
            'AdministrationMemberName' : 'stringItemType',
            'AdministrationMemberContactDetail' : 'stringItemType'                        
        }
    
        CommonFunctions.ElementsToElementTree(SubElements, RootElementTree, 'fi-suc-spa:')

        return RootElementTree