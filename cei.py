"""This module includes Certificate-class and its methods according cei entry point"""

import xml.etree.ElementTree as ET
import functions

class Certificate():
    """Luokka vastaa isännöitsijäntodistuksen taksonometriassa
        Todistukseen liittyvät tiedot -osiota ja sen luontia."""

    def __init__(self, root_element, namespace, context_ref="ctx1"):
        """Initializing certificate

            Keyword arguments:
            context_ref             -- str, reference context identifier on elements
            """

         #Luodaan juurielementti
        self.namespace = namespace
        self.cei = ET.SubElement(root_element, '{'+self.namespace+'}'+'Certificate')
        self.__cei_elements()

        #Lisää contextRef-tieto
        self.cei = functions.set_context_ref(self.cei, context_ref)

    def __cei_elements(self):

        sub_elements = {
            'ObjectOfManagerSCertificate' : 'ObjectOfManagerSCertificateItemType',
            'CertificateInformation' : 'CertificateInformationItemType'
            }

        for key, value in sub_elements.items():
            sub_element = ET.SubElement(self.cei, '{'+self.namespace+'}'+key)
            if value == 'ObjectOfManagerSCertificateItemType':
                self.__object_managers_certificate_struct(sub_element)
            elif value == 'CertificateInformationItemType':
                self.__cert_info_struct(sub_element)

    def __object_managers_certificate_struct(self, parent_element):
        """Function updates defined element tree to include required information

           Keyword arguments:
           parent_element                  -- xml.etree.ElementTree, element tree to be updated

           Output:                         -- xml.etree.ElementTree, updated element tree
           """

        share_group_information = ET.SubElement(
            parent_element,
            '{'+self.namespace+'}'+'ShareGroupInformation')

        ET.SubElement(share_group_information, '{'+self.namespace+'}'+'ShareGroup',
                      attrib={'contextRef' : ''})

        ET.SubElement(share_group_information, '{'+self.namespace+'}'+'AmountOfShares', attrib={
            'decimals' : '0',
            'contextRef' : '',
            'unitRef' : 'pure'})

        ET.SubElement(share_group_information, '{'+self.namespace+'}'+'Classifier', attrib={
            'contextRef' : ''})
        
        ET.SubElement(share_group_information, '{'+self.namespace+'}'+'AmountOfVotes', attrib={
            'decimals' : '0',
            'contextRef' : '',
            'unitRef' : 'pure'})

        owners = ET.SubElement(parent_element, '{'+self.namespace+'}'+'Owners')

        info_of_cond_hoc = ET.SubElement(
            parent_element,
            '{'+self.namespace+'}'+'InformationRegardingTheCondition\
OfTheOwnerApartmentKnownByTheHousingCompany')

        ET.SubElement(
            info_of_cond_hoc,
            '{'+self.namespace+'}'+'RemarkableFlawsSubjectToTheMaintenanceLiabilityOf\
EitherTheShareHolderOrTheHousingCompanyKnownByTheHousingCompany',
            attrib={'contextRef' : ''})

        ET.SubElement(
            info_of_cond_hoc,
            '{'+self.namespace+'}'+'InformationRegardingOtherFactorsThatMaySubstancially\
ImpactTheUsageOrCostOfUsageOfTheOwnerApartmentKnownByTheHousingCompany',
            attrib={'contextRef' : ''})

        ET.SubElement(
            parent_element,
            '{'+self.namespace+'}'+'AgreementsAndPracticesThatDifferFromTheHousingCompanyAct',
            attrib={'contextRef' : ''})

        ET.SubElement(
            parent_element,
            '{'+self.namespace+'}'+'MaintenanceAndAlterationWorkDoneByThe\
ShareHolderKnownByTheHousingCompany')

        pos_rights_authorized_by_sg = ET.SubElement(
            parent_element,
            '{'+self.namespace+'}'+'PosessionRightsAuthorizedByTheShareGroup')

        pos_rights_authorized_by_sg_det = ET.SubElement(
            pos_rights_authorized_by_sg,
            '{'+self.namespace+'}'+'PosessionRightsAuthorizedByTheShareGroupDetails')

        ET.SubElement(
            pos_rights_authorized_by_sg_det,
            '{'+self.namespace+'}'+'SpaceIdentifierReference',
            attrib={'contextRef' : ''})

        ET.SubElement(
            pos_rights_authorized_by_sg_det,
            '{'+self.namespace+'}'+'ApartmentRoomNumberAnnouncedByTheShareHolder',
            attrib={
                'decimals' : '0',
                'contextRef' : '',
                'unitRef' : 'pure'})

        ET.SubElement(
            pos_rights_authorized_by_sg_det,
            '{'+self.namespace+'}'+'SpaceType',
            attrib={'contextRef' : ''})

        pos_limitation_on_the_ownership = ET.SubElement(
            parent_element,
            '{'+self.namespace+'}'+'PosessionLimitationsOnTheShareGroupOwnership')

        ET.SubElement(
            pos_limitation_on_the_ownership,
            '{'+self.namespace+'}'+'PosessionRightOfAWidow',
            attrib={'contextRef' : ''})

        ET.SubElement(
            pos_limitation_on_the_ownership,
            '{'+self.namespace+'}'+'PosessionLimitationOther',
            attrib={'contextRef' : ''})

        pos_limitation_on_the_apartment_pos_right = ET.SubElement(
            parent_element,
            '{'+self.namespace+'}'+'PosessionLimitationsOnTheApartmentPosessionRight')

        ET.SubElement(
            pos_limitation_on_the_apartment_pos_right,
            '{'+self.namespace+'}'+'PosessionLimitationsRelatedToShareGroupOrApartment\
PosessionRightsMarkedInTheSharesListing',
            attrib={'contextRef' : ''})

        hoc_dec_on_pos_taking_and_duration = ET.SubElement(
            parent_element,
            '{'+self.namespace+'}'+'HousingCompanyDecisionOnThePosession\
TakingOfTheApartmentAndPosessionDuration')

        ET.SubElement(
            hoc_dec_on_pos_taking_and_duration,
            '{'+self.namespace+'}'+'AnnualGeneralMeetingHasDecidedUponTheApartmentPosessionTaking',
            attrib={'contextRef' : ''})

        ET.SubElement(
            hoc_dec_on_pos_taking_and_duration,
            '{'+self.namespace+'}'+'PosessionStartingDate',
            attrib={'contextRef' : ''})

        ET.SubElement(
            hoc_dec_on_pos_taking_and_duration,
            '{'+self.namespace+'}'+'PosessionEndingDate',
            attrib={'contextRef' : ''})

        ET.SubElement(
            hoc_dec_on_pos_taking_and_duration,
            '{'+self.namespace+'}'+'HousingCompanyHasLeasedThePosessionTakenApartment',
            attrib={'contextRef' : ''})

        charges_and_compensations = ET.SubElement(
            parent_element,
            '{'+self.namespace+'}'+'ChargesAndCompensationsForTheApartment')

        charges_and_compensations_details = ET.SubElement(
            charges_and_compensations,
            '{'+self.namespace+'}'+'ChargesAndCompensationsForTheApartmentDetails')

        ET.SubElement(
            charges_and_compensations_details,
            '{'+self.namespace+'}'+'ChargeOrCompensationType',
            attrib={'contextRef' : ''})

        ET.SubElement(
            charges_and_compensations_details,
            '{'+self.namespace+'}'+'ChargeOrCompensationTypeName',
            attrib={'contextRef' : ''})

        ET.SubElement(
            charges_and_compensations_details,
            '{'+self.namespace+'}'+'UnitPrice',
            attrib={
                'decimals' : '2',
                'contextRef' : '',
                'unitRef' : 'EUR'})

        ET.SubElement(
            charges_and_compensations_details,
            '{'+self.namespace+'}'+'ChargeOrCompensationBasis',
            attrib={'contextRef' : ''})

        ET.SubElement(
            charges_and_compensations_details,
            '{'+self.namespace+'}'+'TimeUnit',
            attrib={'contextRef' : ''})

        ET.SubElement(
            charges_and_compensations_details,
            '{'+self.namespace+'}'+'TotalAggregatedAmountForTheChargeOrCompensationType',
            attrib={
                'decimals' : '2',
                'contextRef' : '',
                'unitRef' : 'EUR'})

        ET.SubElement(
            parent_element,
            '{'+self.namespace+'}'+'ApartmentIsRegisteredAsVat-Liable',
            attrib={'contextRef' : ''})

        shh_overdue_unpaid_chages = ET.SubElement(
            parent_element,
            '{'+self.namespace+'}'+'ShareholderSOverdueUnpaidChargesForCommonExpenses')

        ET.SubElement(
            shh_overdue_unpaid_chages,
            '{'+self.namespace+'}'+'OverdueChargesForCommonExpensesWithInterestTotal',
            attrib={
                'decimals' : '2',
                'contextRef' : '',
                'unitRef' : 'EUR'})

        ET.SubElement(
            shh_overdue_unpaid_chages,
            '{'+self.namespace+'}'+'OverdueChargesForCommonExpensesWithInterestDate',
            attrib={'contextRef' : ''})

        ET.SubElement(
            shh_overdue_unpaid_chages,
            '{'+self.namespace+'}'+'OverdueChargesForCommonExpensesOnSellerSResponsibilityTotal',
            attrib={
                'decimals' : '2',
                'contextRef' : '',
                'unitRef' : 'EUR'})

        ET.SubElement(
            shh_overdue_unpaid_chages,
            '{'+self.namespace+'}'+'OverdueChargesForCommonExpensesOnSellerSResponsibilityDate',
            attrib={'contextRef' : ''})

        ET.SubElement(
            shh_overdue_unpaid_chages,
            '{'+self.namespace+'}'+'Collectively-ResponsibleOverdueChargesForCommonExpenses\
OverThePrecedingSixMonths',
            attrib={
                'decimals' : '2',
                'contextRef' : '',
                'unitRef' : 'EUR'})

        ET.SubElement(
            shh_overdue_unpaid_chages,
            '{'+self.namespace+'}'+'OverdueChargesForCommonExpensesIncludeVat',
            attrib={'contextRef' : ''})

        apartment_loan_share = ET.SubElement(
            parent_element,
            '{'+self.namespace+'}'+'ApartmentLoanShare')

        apartment_loan_share_details = ET.SubElement(
            apartment_loan_share,
            '{'+self.namespace+'}'+'ApartmentLoanShareDetails')

        ET.SubElement(
            apartment_loan_share_details,
            '{'+self.namespace+'}'+'ApartmentLoanName',
            attrib={'contextRef' : ''})

        ET.SubElement(
            apartment_loan_share_details,
            '{'+self.namespace+'}'+'ApartmentLoanAmount',
            attrib={
                'decimals' : '2',
                'contextRef' : '',
                'unitRef' : 'EUR'})

        ET.SubElement(
            apartment_loan_share_details,
            '{'+self.namespace+'}'+'ApartmentLoanAmountDate',
            attrib={'contextRef' : ''})

        ET.SubElement(
            apartment_loan_share_details,
            '{'+self.namespace+'}'+'ApartmentLoanCharges',
            attrib={
                'decimals' : '2',
                'contextRef' : '',
                'unitRef' : 'EUR'})

        ET.SubElement(
            parent_element,
            '{'+self.namespace+'}'+'CertificateAdditionalInformation',
            attrib={'contextRef' : ''})

    def __cert_info_struct(self, parent_element):
        """This method creates certification information structure"""

        diary_number = ET.SubElement(
            parent_element,
            '{'+self.namespace+'}'+'DiaryNumber',
            attrib={'contextRef' : ''})

        ET.SubElement(
            parent_element,
            '{'+self.namespace+'}'+'CertificateDate',
            attrib={'contextRef' : ''})

        certificate_order = ET.SubElement(
            parent_element,
            '{'+self.namespace+'}'+'CertificateOrder')

        ET.SubElement(
            certificate_order,
            '{'+self.namespace+'}'+'CertificateOrderPlacedByName',
            attrib={'contextRef' : ''})

        ET.SubElement(
            certificate_order,
            '{'+self.namespace+'}'+'CertificateOrderPlacedByRole',
            attrib={'contextRef' : ''})

        ET.SubElement(
            certificate_order,
            '{'+self.namespace+'}'+'CertificateOrderPlacedByContactDetail',
            attrib={'contextRef' : ''})

        certificate_provider = ET.SubElement(
            parent_element,
            '{'+self.namespace+'}'+'CertificateProvider')

        ET.SubElement(
            parent_element,
            '{'+self.namespace+'}'+'CertificateProviderName',
            attrib={'context' : ''})

        ET.SubElement(
            certificate_provider,
            '{'+self.namespace+'}'+'CertificateProviderRole',
            attrib={'contextRef' : ''})

        ET.SubElement(
            certificate_provider,
            '{'+self.namespace+'}'+'CertificateProviderContactDetail',
            attrib={'contextRef' : ''})

        ET.SubElement(
            certificate_provider,
            '{'+self.namespace+'}'+'CertificateProviderOrganization',
            attrib={'contextRef' : ''})

        ET.SubElement(
            certificate_provider,
            '{'+self.namespace+'}'+'CertificateProviderOrganizationIdentifier',
            attrib={'contextRef' : ''})

        rec_attachements_to_the_superintendents_cert = ET.SubElement(
            parent_element,
            '{'+self.namespace+'}'+'RecommendedAttachmentsToTheSuperintendentSCertificate')

        ET.SubElement(
            rec_attachements_to_the_superintendents_cert,
            '{'+self.namespace+'}'+'ConfirmedFinancialStatements',
            attrib={'contextRef' : ''})

        ET.SubElement(
            rec_attachements_to_the_superintendents_cert,
            '{'+self.namespace+'}'+'ReinforcedBudget',
            attrib={'contextRef' : ''})

        ET.SubElement(
            rec_attachements_to_the_superintendents_cert,
            '{'+self.namespace+'}'+'ArticlesOfAssociation',
            attrib={'contextRef' : ''})

        ET.SubElement(
            rec_attachements_to_the_superintendents_cert,
            '{'+self.namespace+'}'+'ActivityReport',
            attrib={'contextRef' : ''})

        ET.SubElement(
            rec_attachements_to_the_superintendents_cert,
            '{'+self.namespace+'}'+'AuditorSReport',
            attrib={'contextRef' : ''})

        ET.SubElement(
            rec_attachements_to_the_superintendents_cert,
            '{'+self.namespace+'}'+'PerformanceAuditReport',
            attrib={'contextRef' : ''})

        other_attachments_to_the_superintendents_certificate = ET.SubElement(
            parent_element,
            '{'+self.namespace+'}'+'OtherAttachmentsToTheSuperintendentSCertificate')

        ET.SubElement(
            other_attachments_to_the_superintendents_certificate,
            '{'+self.namespace+'}'+'FloorPlanForApartments',
            attrib={'contextRef' : ''})

        ET.SubElement(
            other_attachments_to_the_superintendents_certificate,
            '{'+self.namespace+'}'+'BoardOfDirectorsReportOnTheCompanySBuildingsAnd\
PropertyMaintenanceNeeds',
            attrib={'contextRef' : ''})

        ET.SubElement(
            other_attachments_to_the_superintendents_certificate,
            '{'+self.namespace+'}'+'SummaryOfConditionAssessment',
            attrib={'contextRef' : ''})

        ET.SubElement(
            other_attachments_to_the_superintendents_certificate,
            '{'+self.namespace+'}'+'HousingCompanySConditionCertificate',
            attrib={'contextRef' : ''})

        ET.SubElement(
            other_attachments_to_the_superintendents_certificate,
            '{'+self.namespace+'}'+'EnergyCertificate',
            attrib={'contextRef' : ''})

        ET.SubElement(
            other_attachments_to_the_superintendents_certificate,
            '{'+self.namespace+'}'+'ReportOnTheMaintenanceAndAlterationWorkDoneOnTheCompanyS\
RealEstatePropertyAndTheYearOfCompletion',
            attrib={'contextRef' : ''})

        ET.SubElement(
            other_attachments_to_the_superintendents_certificate,
            '{'+self.namespace+'}'+'InformationRegardingTheAuthorizationOnIssuing\
ShareOptionsOrOtherRightsToShares',
            attrib={'contextRef' : ''})

        ET.SubElement(
            other_attachments_to_the_superintendents_certificate,
            '{'+self.namespace+'}'+'OtherAttachments',
            attrib={'contextRef' : ''})

    # SQL strings needed to gather required information
    SQL_STRINGS = {
        'ShareGroup' :
        '''SELECT ShareGroup, AmountOfShares
FROM Apartments
WHERE ApartmentID = (?);''',
        'ShareOwners' :
        '''SELECT Apartments.ApartmentID, Personnel.LastName, Personnel.FirstName,
Shareholders.OwnerShareOfOwnership, ShareHolders.OwnerRegisteredInTheShareListingDate
FROM Personnel INNER JOIN (Shareholders INNER JOIN Apartments ON
Shareholders.ShareGroup = Apartments.ShareGroup) ON Personnel.ID = Shareholders.PersonnelID
WHERE (((Shareholders.OwnerShareOfOwnership)>0) AND Apartments.ApartmentID = ?);''',
        'RemarkableFlaws' :
        '''SELECT Apartments.ExceptionalFlawOrNotifications
FROM Apartments
WHERE ApartmentID = (?);''',
        'ApartmentModifications' :
        '''SELECT ApartmentModifications.ApartmentID, ApartmentModifications.ReadyDate,
ApartmentModifications.Description
FROM ApartmentModifications
WHERE (((ApartmentModifications.ApartmentID)=?));''',
        'ResidentialApartmentsTotalArea' :
        '''SELECT Sum(Apartments.SurfaceAreaByTheArticlesOfAssociation) AS TotalArea
           FROM Apartments;''',
        'ResidentialApartmentsInShareHoldersPosessionTotalArea' :
        '''SELECT Sum(Apartments.SurfaceAreaByTheArticlesOfAssociation) AS TotalArea
           FROM Apartments
           HAVING (Apartments.ShareholdersPossession)=True;''',
        'ResidentialApartmentsTotalShares' :
        '''SELECT Sum(CountOfShares) AS SharesCount
           FROM Apartments;''',
        'ResidentialApartmentsInShareHoldersPosessionTotalShares' :
        '''SELECT Sum(CountOfShares) AS SharesCount FROM Apartments;''',
        'WareHousesInShareHoldersPosessionAmount' :
        '''SELECT COUNT(Apartment) AS ApartmentsCount,
           SUM(WarehouseArea) as SumOfWarehouseArea
           FROM Apartments
           HAVING (WarehouseBelongsToShares)=True;''',
        'SumOfOtherSpacesInShareHoldersPosessionAmount' :
        '''SELECT SUM(Apartments.NumberOfOtherSpacesBelongsToShares) AS SumOfOtherSpaces,
           Sum(Apartments.AreaOfOtherSpacesBelongsToShares) AS SumOfWarehouseArea
           FROM Apartments;''',
        'OtherSpacesInHousingCompanySPosessionAmount' :
        '''SELECT COUNT(OtherSpaces.DescriptiveAbbreviation) AS CountOfOtherSpaces
           FROM OtherSpaces;''',
        'OtherSpacesInHousingCompanySPosessionTotalSurfaceArea' :
        '''SELECT SUM(OtherSpaces.SurfaceArea) AS SumOfOtherSpacesInHousingCompaniesPossession
           FROM OtherSpaces;''',
        'ParkingSpacesInHousingCompanySPosessionAmount' :
        '''SELECT COUNT(ID) as AmountOfAutopaikat
           FROM ParkingSpaces;''',
        'Insurances' :
        '''SELECT InsuranceCompany,
           InsuranceType,
           InsuranceTypeText,
           OtherInsurance
        FROM Vakuutukset
        WHERE (Active)=True;''',
        'MaintenanceCharges' :
        '''SELECT Charges.ChargeType, Charges.ChargeExplanation, ChargeAmounts.ChargeUnitPrice,
           ChargeAmounts.ChargeBasis, ChargeAmounts.ChargeTimeUnit
           FROM Charges LEFT JOIN ChargeAmounts ON Charges.ID = ChargeAmounts.ID
           WHERE (((Charges.Active)=True) AND ((Charges.MaintenanceCharge)=True));''',
        'InvestmentCharges' :
        '''SELECT Charges.ChargeType, Charges.ChargeExplanation, ChargeAmounts.ChargeUnitPrice,
           ChargeAmounts.ChargeBasis, ChargeAmounts.ChargeTimeUnit
           FROM Charges LEFT JOIN ChargeAmounts ON Charges.ID = ChargeAmounts.ID
           WHERE (((Charges.Active)=True) AND ((Charges.CapitalCharge)=True));''',
        'TakenLoansGrantedLoanDecisionsAndCreditentialAccounts' :
        'SELECT * FROM Loans WHERE (Active)=True;',
        'Apartments' :
        'SELECT * FROM Apartments;',
        'ParkingSpaces' :
        '''SELECT ParkingPlaces.ID, ParkingPlaces.HeatingPossibility
           FROM ParkingPlaces;'''
        }
