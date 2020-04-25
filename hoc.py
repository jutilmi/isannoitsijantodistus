"""This module considers hoc-content according xbrl data struture in
   superintendents certificate"""

import xml.etree.ElementTree as ET
import functions

class HousingCompany(object):
    """Tämä luokka vastaa isännöitsijäntodistuksen taksonometriassa
    Taloyhtiön tiedot -osioita ja sen luontia."""

    def __init__(self, contextRef="cxt1"):
        """Initializing certificate

            Keyword arguments:
            context_ref             -- str, reference context identifier on elements
            """
        #Luodaan juurielementit
        self.hoc = ET.ElementTree(ET.Element('HousingCompany'))

        self.hoc_dict = {'HousingCompany' : {}}

        self.__build_hoc_information()
        #hoc = self.getCertificateInformation(cei)

        functions.set_context_ref(self.hoc, contextRef)

#    def HousingCompany(self, vHousingCompany)

    def __build_hoc_information(self):
        """Builds HousingCompanyInformation section in hoc entrypoint"""

        sub_elements = {
            'HousingCompanyInfromation' : 'HousingCompanyInfromationItemType',
            'PrintingOfShares' : 'PrintingOfSharesItemType',
            'SpacesStatedInTheArticlesOfAssociation' :
            'SpacesStatedInTheArticlesOfAssociationItemType',
            'OtherObligations' : 'OtherObligationsItemType',
            'PosessionDistributionAgreements' : 'PosessionDistributionAgreementsItemType',
            'Insurances' : 'InsurancesItemType',
            'FinancialInformation' : 'FinancialInformationItemType',
            'RealEstate' : 'RealEstateItemType',
            'Buildings' : 'BuildingsItemType',
            'OtherSpacesInControlOfTheHousingCompany' :
            'OtherSpacesInControlOfTheHousingCompanyItemType'
        }

        for key in sub_elements:
            sub_element = ET.SubElement(self.hoc, 'fi-suc-hoc:'+key)
            if sub_element[key] == 'HousingCompanyInfromationItemType':
                self.__hoc_information_item_type()
            elif sub_element[key] == 'PrintingOfSharesItemType':
                self.__printing_of_shares_item_type()

    def __hoc_information_item_type(self):
        """Builds HousingCompanyInformation section in hoc entrypoint"""

        sub_elements = {
            'HousingCompanyName' : 'stringItemType',
            'HousingCompanyIdentifier' : 'stringItemType',
            'ValidArticlesOfAssociationDate' : 'dateItemType',
            'RegistrationDate' : 'dateItemType',
            'HousingCompanyArticlesOfAssociationIncludesAStatementForRedemption' :
            'booleanItemType',
            'PartiesEntitledForRedemption' : 'stringItemType',
            'HousingCompanyIsAHitas-Entity' : 'booleanItemType',
            'HousingCompanyIsAFinancedByTheGovernmentPerBuilding' : 'booleanItemType',
            'HousingCompanyHasPosessionOfPersonalMortgageSecuredByTheGovernment' :
            'booleanItemType',
            'HousingCompanyIsLiableToVat' : 'stringItemType',
            'VatBenefitsForTheCompanyOrForTheShareholderModelInUse' : 'stringItemType',
            'TheDegreeOfTheEntireHousingCompanySVatLiability' : 'decimalItemType',
            'TheDegreeOfTheVatLiabilityOfAllSpapesInThePosessionOfTheHousingCompany' :
            'decimalItemType',
            'InformationRegardingTheAuthorizationOnIssuingShareOptionsOrOtherRightsToShares' :
            'stringItemType',
            'InformationRegardingOtherKnownFactsThatMayHaveASignificantImpactOnTheCompanyS\
                FinancialPositionOrOperations' :
            'stringItemType',
            'InformationRegardingUndrawnLoansThatTheOwnerApartmentWillBeLiableForAndForWhich\
                TheLoanSharePerOwnerApartmentIsNotKnown' :
            'stringItemType',
            'ArticlesOfAssociationAndDecisionsOfTheAnnualGeneralMeetingOnTheMaintenanceLiability\
                AndTheShareholderSRightToMakeAlterations' :
            'stringItemType',
            'ReportOnMaintenanceNeedsInformation' : 'ReportOnMaintenanceNeedsInformationItemType',
            'ReportOnMaintenanceNeeds' : 'ReportOnMaintenanceNeedsItemType',
            'CompletedModernisationAndRemarkableRepairWork' :
            'CompletedModernisationAndRemarkableRepairWorkItemType',
            'AssessmentOfCondition' : 'AssessmentOfConditionItemType'
        }

        functions.elements_to_element_tree(sub_elements, self.hoc, 'fi-suc-hoc:')

    def __report_on_maintenance_needs_information_item_type(self):
        """Builds HousingCompanyInformation section in hoc entrypoint"""

        sub_elements = {
            'ReportOnMaintenanceNeedsPresentedInTheAnnualGeneralMeeting' : 'booleanItemType',
            'ReportOnMaintenanceNeedsDate' : 'dateItemType'
        }

        functions.elements_to_element_tree(sub_elements, self.hoc, 'fi-suc-hoc:')

    def __report_on_maintenance_needs_item_type(self, root_element_tree):
        sub_elements = {
            'ReportOnMaintenanceNeedsDrafted' : 'booleanItemType',
            'ReportOnMaintenanceNeedsExplanation' : 'stringItemType',
            'ReportOnMaintenanceNeedsDraftedInTheYear' : 'integerItemType',
            'ReportOnMaintenanceNeedsDraftedForPeriodInYears' : 'decimalItemType'
        }

        functions.elements_to_element_tree(sub_elements, self.hoc, 'fi-suc-hoc:')

        return root_element_tree

    def __complete_modernisation_and_remarkable_repairwork_item_type(self):
        sub_elements = {
            'CompletedModernisationAndRemarkableRepairWorkExplanation' : 'stringItemType',
            'CompletedModernisationAndRemarkableRepairWorkStatus' : 'stringItemType',
            'CompletedModernisationAndRemarkableRepairWorkYear' : 'integerItemType'
        }

        functions.elements_to_element_tree(sub_elements, self.hoc, 'fi-suc-hoc:')

    def __assessment_of_condition_item_type(self):
        sub_elements = {
            'LatestAssessmentOfConditionYear' : 'integerItemType',
            'AssessmentOfConditionDescription' : 'stringItemType',
        }

        functions.elements_to_element_tree(sub_elements, self.hoc, 'fi-suc-hoc:')

    def __printing_of_shares_item_type(self):

        sub_elements = {
            'PrintingOfSharesDoneInSecurityPrinting' : 'booleanItemType',
            'SecurityPrintingAdditionalDetail' : 'stringItemType',
            'ApartmentLayoutDescriptionHasBeenChangedAfterTheFirstOfJuly1972' : 'booleanItemType'
        }

        functions.elements_to_element_tree(sub_elements, self.hoc, 'fi-suc-hoc:')

    def __spaces_stated_in_the_articles_of_association_item_type(self, root_element_tree):

        sub_elements = {
            'SpacesStatedInTheArticlesOfAssociationInPosessionOfTheShareHolders' :
            'SpacesStatedInTheArticlesOfAssociationInPosessionOfTheShareHoldersItemType',
            'SpacesStatedInTheArticlesOfAssociationInPosessionOfTheHousingCompany' :
            'SpacesStatedInTheArticlesOfAssociationInPosessionOfTheHousingCompanyItemType'
        }

        for key in sub_elements:
            sub_element = ET.SubElement(root_element_tree, 'fi-suc-hoc:'+key)
            if sub_element[key] == 'SpacesStatedInTheArticlesOfAssociation\
                InPosessionOfTheShareHoldersItemType':
                self.__spaces_stated_in_art_of_ass_in_pos_of_shareholder_it(sub_element)
            elif sub_element[key] == 'SpacesStatedInTheArticlesOfAssociationIn\
                PosessionOfTheHousingCompanyItemType':
                self.__spaces_stated_in_art_of_ass_in_pos_of_hoc_it(sub_element)

        # self.elements_to_element_tree(sub_elements,root_element_tree)

        return root_element_tree

    def __spaces_stated_in_art_of_ass_in_pos_of_shareholder_it(
            self, root_element_tree):

        sub_elements = {
            'ResidentialApartmentsInShareHoldersPosessionAmount' : 'integerItemType',
            'ResidentialApartmentsInShareHoldersPosessionTotalArea' : 'decimalItemType',
            'ResidentialApartmentsInShareHoldersPosessionTotalShares' : 'integerItemType',
            'ResidentialApartmentInShareHoldersPosessionChargeFactor' : 'decimalItemType',
            'CommercialPropertyInShareHoldersPosessionAmount' : 'integerItemType',
            'CommercialPropertyInShareHoldersPosessionTotalSurfaceArea' : 'decimalItemType',
            'CommercialPropertyInShareHoldersPosessionTotalShares' : 'integerItemType',
            'CommercialPropertyInShareHoldersPosessionChargeFactor' : 'decimalItemType',
            'OtherSpacesInShareHoldersPosessionAmount' : 'integerItemType',
            'OtherSpacesInShareHoldersPosessionTotalSurfaceArea' : 'decimalItemType',
            'OtherSpacesInShareHoldersPosessionTotalShares' : 'integerItemType',
            'OtherSpacesInShareHoldersPosessionChargeFactor' : 'decimalItemType',
            'ParkingSpacesInShareHoldersPosessionAmount' : 'integerItemType',
            'ParkingSpacesInShareHoldersPosessionTotalShares' : 'integerItemType',
            'ParkingSpacesInShareHoldersPosessionChargeFactor' : 'decimalItemType',
            'AllSpacesInShareHoldersPosessionTotalAmount' : 'integerItemType',
            'AllSpacesInShareHoldersPosessionTotalSurfaceArea' : 'decimalItemType',
            'AllSpacesInShareHoldersPosessionTotalShares' : 'integerItemType'
        }

        functions.elements_to_element_tree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def __spaces_stated_in_art_of_ass_in_pos_of_hoc_it(self, element):

        sub_elements = {
            'ResidentialApartmentsInHousingCompanySPosessionAmount' : 'integerItemType',
            'ResidentialApartmentsInHousingCompanySPosessionTotalArea' : 'decimalItemType',
            'ResidentialApartmentsInHousingCompanySPosessionTotalShares' : 'integerItemType',

            'CommercialPropertyInHousingCompanySPosessionAmount' : 'integerItemType',
            'CommercialPropertyInHousingCompanySPosessionTotalSurfaceArea' : 'decimalItemType',
            'CommercialPropertyInHousingCompanySPosessionTotalShares' : 'integerItemType',

            'OtherSpacesInHousingCompanySPosessionAmount' : 'integerItemType',
            'OtherSpacesInHousingCompanySPosessionTotalSurfaceArea' : 'decimalItemType',
            'OtherSpacesInHousingCompanySPosessionTotalShares' : 'integerItemType',

            'ParkingSpacesInHousingCompanySPosessionAmount' : 'integerItemType',

            'BuildingsInHousingCompanySPosessionAmount' : 'integerItemType',

            'CourtyardSurfaceArea' : 'integerItemType'
        }

        functions.elements_to_element_tree(sub_elements, element, 'fi-suc-hoc:')

    def __other_obligations_it(self, root_element_tree):

        sub_elements = {
            'ObligationOnParkingSpacesByTheBuildingPermit' : 'integerItemType',
            'RulesOnParkingSpaceDistribution' : 'stringItemType'
        }

        functions.elements_to_element_tree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def __posession_distr_agreements_it(self, root_element_tree):

        sub_elements = {
            'PosessionDistributionAgreement' : 'PosessionDistributionAgreementItemType'
        }

        for key in sub_elements:
            sub_element = ET.SubElement(root_element_tree, 'fi-suc-hoc:'+key)
            if sub_element[key] == 'PosessionDistributionAgreementItemType':
                self.__posession_distr_agreement_it(sub_element)

        return root_element_tree

    def __posession_distr_agreement_it(self, root_element_tree):

        sub_elements = {
            'Owner' : 'OwnerItemType',
            'AgreementDocumentNumber' : 'stringItemType',
            'TermsOfAgreement' : 'stringItemType'
        }

        sub_element = ET.SubElement(root_element_tree, 'fi-suc-hoc:'+'Owner')
        self.__owner_it(sub_element)
        sub_elements.pop('Owner')

        functions.elements_to_element_tree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def __owner_it(self, root_element_tree):

        sub_elements = {
            'OwnerName' : 'stringItemType',
            'Share' : 'decimalItemType'
        }

        functions.elements_to_element_tree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def __insurances_it(self, root_element_tree):

        sub_element = ET.SubElement(root_element_tree, 'fi-suc-hoc:'+'Insurance')
        self.__insurance_it(sub_element)

        return root_element_tree

    def __insurance_it(self, root_element_tree):

        sub_elements = {
            'InsuranceCompany' : 'stringItemType',
            'InsuranceType' : 'stringItemType',
            'OtherInsurance' : 'stringItemType'
            }

        functions.elements_to_element_tree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def __financial_information_it(self, root_element_tree):

        sub_elements = {
            'ChargesAndCompensations' : 'ChargesAndCompensationsItemType',
            'TakenLoansGrantedLoanDecisionsAndCreditentialAccounts' :
            'TakenLoansGrantedLoanDecisionsAndCreditentialAccountsItemType',
            'ComplaintActionRegardingTheReasonablingOfTheArticlesOfAssociation' :
            'ComplaintActionRegardingTheReasonablingOfTheArticlesOfAssociationItemType'
        }

        for key in sub_elements:
            sub_element = ET.SubElement(root_element_tree, 'fi-suc-hoc:'+key)
            if sub_elements[key] == 'ChargesAndCompensationsItemType':
                self.__charges_and_compensations_it(sub_element)
            elif sub_elements[key] == 'TakenLoansGrantedLoanDecisionsAnd\
                CreditentialAccountsItemType':
                self.__taken_and_granted_loans_and_credit_accs_it(sub_element)
            elif sub_elements[key] == 'ComplaintActionRegardingTheReasonabling\
                OfTheArticlesOfAssociationItemType':
                self.__complaint_act_reg_reasonabling_of_artass_it(
                    sub_element)

        return root_element_tree

    def __charges_and_compensations_it(self, root_element_tree):

        sub_element = ET.SubElement(root_element_tree, 'fi-suc-hoc:'+'ChargesOrCompensation')
        self.__charge_and_compensation_it(sub_element)

        return root_element_tree

    def __charge_and_compensation_it(self, root_element_tree):

        sub_elements = {
            'ChargeType' : 'stringItemType',
            'ChargeTypeName' : 'stringItemType',
            'ChargeUnitPrice' : 'monetaryItemType',
            'ChargeBasis' : 'stringItemType',
            'ChargeTimeUnit' : 'stringItemType',
            'ChargeAdditionalDetail' : 'stringItemType'
        }

        functions.elements_to_element_tree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def __taken_and_granted_loans_and_credit_accs_it(self, root_element_tree):

        sub_elements = {
            'Loan' : 'LoanItemType',
            'CredentialAccount' : 'CredentialAccountItemType'
        }

        for key in sub_elements:
            sub_element = ET.SubElement(root_element_tree, 'fi-suc-hoc:'+key)
            if sub_elements[key] == 'LoanItemType':
                self.__loan_it(sub_element)
            elif sub_elements[key] == 'CredentialAccountItemType':
                self.__credential_acc_it(sub_element)

        return root_element_tree

    def __loan_it(self, root_element_tree):

        sub_elements = {
            'LoanWithdrawalDate' : 'dateItemType',
            'LoanEndDate' : 'dateItemType',
            'LoanAmountDecidedByTheAnnualGeneralMeeting' : 'monetaryItemType',
            'LoanUndrawnCapital' : 'monetaryItemType',
            'LoanType' : 'stringItemType',
            'LoanName' : 'stringItemType',
            'LoanAnnualInterestRate' : 'decimalItemType',
            'LoanAnnualInterestRateExplanation' : 'stringItemType',
            'ChargeForFinancialCostsPerChargeUnit' : 'monetaryItemType',
            'ChargeForFinancialCostsExplanation' : 'stringItemType',
            'LoanBalance' : 'monetaryItemType',
            'LoanBalanceDate' : 'dateItemType',
            'LoanSubjectToTransferTax' : 'stringItemType',
            'LoanRestrictionsOnPaymentsAndRepayments' : 'stringItemType',
            'DisclosureOfLiabilitiesIfTheCompanySLoansAre\
                SubjectToVariousShareholders' : 'stringItemType'
        }

        functions.elements_to_element_tree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def __credential_acc_it(self, root_element_tree):

        sub_elements = {
            'Lender' : 'stringItemType',
            'CreditDescription' : 'stringItemType',
            'CreditAmount' : 'monetaryItemType',
            'CreditDate' : 'dateItemType',
            'CreditLimitMount' : 'monetaryItemType'
        }

        functions.elements_to_element_tree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def __complaint_act_reg_reasonabling_of_artass_it(
            self, root_element_tree):

        sub_elements = {
            'ComplaintRegardingParagraphInTheArticlesOfAssociation' : 'stringItemType',
            'ComplaintExplanation' : 'stringItemType'
        }
        functions.elements_to_element_tree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def __real_estate_it(self, root_element_tree):

        sub_element = ET.SubElement(root_element_tree, 'fi-suc-hoc:'+'RealEstateInformation')
        self.__real_estate_information_it(sub_element)

        return root_element_tree

    def __real_estate_information_it(self, root_element_tree):

        sub_elements = {
            'RealEstateIdentifier' : 'stringItemType',
            'RealEstateType' : 'stringItemType',
            'RealEstateMunicipality' : 'stringItemType',
            'RealEstateSurfaceArea' : 'decimalItemType',
            'RealEstatePlotOwnedLeased' : 'stringItemType',
            'RealEstateShareOwned' : 'decimalItemType',
            'BuildingRightsSurfaceArea' : 'decimalItemType',
            'RemainingShareOfBuildingRights' : 'decimalItemType'
        }

        functions.elements_to_element_tree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        sub_element = ET.SubElement(root_element_tree, 'fi-suc-hoc:'+'LeasedPlotInformation')
        self.__leased_plot_info_it(sub_element)

        return root_element_tree

    def __leased_plot_info_it(self, root_element_tree):

        sub_elements = {
            'LeaseholdRightIdentifier' : 'stringItemType',
            'LeaseGiver' : 'stringItemType',
            'LeasePeriodEnd' : 'dateItemType',
            'LeaseAnnualAmount' : 'monetaryItemType',
            'LeaseRevisionBasis' : 'stringItemType',
            'PossibleLeaseRedemptionRightInLeaseAgreement' : 'booleanItemType',
            'InformationRegardingTheUsageOfTheRedemptionRight' : 'booleanItemType',
            'LeaseRevisionBaseIndex' : 'stringItemType',
            'LeasedPlotOtherInformation' : 'stringItemType'
        }

        functions.elements_to_element_tree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def __buildings_it(self, root_element_tree):

        sub_element = ET.SubElement(root_element_tree, 'fi-suc-hoc:'+'BuildingInformation')
        self.__building_info_it(sub_element)

        return root_element_tree

    def __building_info_it(self, root_element_tree):

        sub_elements = {
            'BuildingRealEstateIdentifierReference' : 'stringItemType',
            'BuildingIdentifier' : 'stringItemType',
            'BuildingYearTakenIntoUse' : 'integerItemType',
            'BuildingType' : 'stringItemType',
            'Address' : 'AddressItemType',
            'Structures' : 'StructuresItemType',
            'Systems' : 'SystemsItemType',
            'BuildingElevatorsAmount' : 'integerItemType',
            'BuildingFloorArea' : 'decimalItemType',
            'BuildingVolume' : 'decimalItemType',
            'BuildingNumberOfFloors' : 'integerItemType',
            'BuildingNumberOfStairwells' : 'integerItemType',
            'BuildingYearOfCompletion' : 'integerItemType',
            'BuildingLivingArea' : 'decimalItemType',
            'BuildingGrossArea' : 'decimalItemType',
            'BuildingClarificationRelatedToTheAreas' : 'stringItemType',
            'EnergyConsumptionPerEnergySource' : 'EnergyConsumptionPerEnergySourceItemType',
            'ConsumptionOfWater' : 'decimalItemType',
            'Apartments' : 'ApartmentsItemType'
        }

        functions.elements_to_element_tree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def __address_it(self, root_element_tree):

        sub_elements = {
            'BuildingStreetAddress' : 'stringItemType',
            'BuildingPostalCode' : 'stringItemType',
            'BuildingCity' : 'stringItemType',
            'BuildingCountry' : 'stringItemType'
        }

        functions.elements_to_element_tree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def __structures_it(self, root_element_tree):

        sub_elements = {
            'MainBuildingMaterial' : 'stringItemType',
            'RoofType' : 'stringItemType',
            'Cover' : 'stringItemType'
        }

        functions.elements_to_element_tree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def __systems_it(self, root_element_tree):

        sub_elements = {
            'HeatingSystem' : 'stringItemType',
            'VentilationSystem' : 'stringItemType',
            'CoolingSystem' : 'stringItemType',
            'InformationSystems' : 'stringItemType',
            'AntennaSystems' : 'stringItemType'
        }

        functions.elements_to_element_tree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def __energy_consumption_per_e_source_it(self, root_element_tree):

        sub_elements = {
            'ConsumptionOfHeat' : 'decimalItemType',
            'EnergySource' : 'stringItemType',
            'ConsumptionOfElectricityCommonSpace' : 'decimalItemType'
        }

        functions.elements_to_element_tree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def __apartments_it(self, root_element_tree):

        sub_element = ET.SubElement(root_element_tree, 'fi-suc-hoc:'+'ApartmentInformation')
        self.__apartment_information_it(sub_element)

        return root_element_tree

    def __apartment_information_it(self, root_element_tree):

        sub_elements = {
            'ApartmentIdentifier' : 'stringItemType',
            'RoomNumber' : 'integerItemType',
            'SurfaceAreaDetails' : 'SurfaceAreaDetailsItemType',
            'ApartmentTypeByTheArticlesOfAssociation' : 'stringItemType',
            'Floor' : 'stringItemType',
            'Stairwell' : 'stringItemType',
            'ApartmentNumber' : 'integerItemType',
            'DivisionLetter' : 'stringItemType',
            'PurposeOfUsageByTheArticlesOfAssociation' : 'stringItemType',
            'PurposeOfUsageByBuildingPermit' : 'stringItemType',
            'RedemptionInformation' : 'stringItemType',
            'ApartmentAdditionalInformation' : 'stringItemType'
        }

        functions.elements_to_element_tree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def __surface_area_dets_it(self, root_element_tree):

        sub_elements = {
            'SurfaceArea' : 'decimalItemType',
            'SurfaceAreaMeasurementMethod' : 'stringItemType',
            'SurfaceAreaCheckMeasured' : 'booleanItemType'
        }

        functions.elements_to_element_tree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def __other_spaces_in_control_of_hoc(self, root_element_tree):

        sub_elements = {
            'ParkingSpaces' : 'ParkingSpacesItemType',
            'OtherSpaces' : 'OtherSpacesItemType'
        }

        for key in sub_elements:
            sub_element = ET.SubElement(root_element_tree, 'fi-suc-hoc:'+key)
            if sub_elements[key] == 'ParkingSpacesItemType':
                self.__parking_spaces_it(sub_element)
            elif sub_elements[key] == 'OtherSpacesItemType':
                self.__other_spaces_it(sub_element)

        return root_element_tree

    def __parking_spaces_it(self, root_element_tree):

        sub_elements = {
            'ParkingSpacesNumber' : 'integerItemType',
            'ParkingSpaceType' : 'stringItemType'
        }

        functions.elements_to_element_tree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def __other_spaces_it(self, root_element_tree):

        sub_elements = {
            'OtherSpaceType' : 'stringItemType',
            'OtherSpaceNumber' : 'integerItemType',
            'OtherSpaceAdditionalDetail' : 'stringItemType'
        }

        functions.elements_to_element_tree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    # SQL strings needed to gather required information
    SQL_STRINGS = {
        'ApartmentsCount' :
        '''SELECT Count(Apartments.ApartmentID) AS ApartmentsCount
           FROM Apartments;''',
        'ApartmentsCountInShareholdersPossession' :
        '''SELECT Count(Apartments.Huoneisto) AS CountOfHuoneisto
           FROM Apartments
           HAVING (Apartments.ShareholdersPossession)=True;
           ''',
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
