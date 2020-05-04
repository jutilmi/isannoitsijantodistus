"""This module considers hoc-content according xbrl data struture in
   superintendents certificate"""

import xml.etree.ElementTree as ET
import functions

class HousingCompany:
    """Tämä luokka vastaa isännöitsijäntodistuksen taksonometriassa
    Taloyhtiön tiedot -osioita ja sen luontia."""

    def __init__(self, contextRef="ctx1"):
        """Initializing certificate

            Keyword arguments:
            context_ref             -- str, reference context identifier on elements
            """
        # Creating root element for xml document
        self.hoc = ET.Element('fi-suc-hoc:HousingCompany')
        self.__hoc_elements()

        # Creating element for dictionary
        # self.hoc_dict = {'fi-suc-hoc:HousingCompany' : {}}

        #hoc = self.getCertificateInformation(cei)

        functions.set_context_ref(self.hoc, contextRef)

#    def HousingCompany(self, vHousingCompany)

    def __hoc_elements(self):
        """Subelements in housing company parent module"""

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

        for key, value in sub_elements.items():
            sub_element = ET.SubElement(self.hoc, 'fi-suc-hoc:'+key)
            if value == 'HousingCompanyInfromationItemType':
                self.__hoc_information_item_type(sub_element)
            elif value == 'PrintingOfSharesItemType':
                self.__printing_of_shares_item_type(sub_element)
            elif value == 'SpacesStatedInTheArticlesOfAssociationItemType':
                self.__spaces_stated_in_the_articles_of_association_item_type(sub_element)
            elif value == 'OtherObligationsItemType':
                self.__other_obligations_it(sub_element)
            elif value == 'PosessionDistributionAgreementsItemType':
                self.__posession_distr_agreements_it(sub_element)
            elif value == 'InsurancesItemType':
                self.__insurances_it(sub_element)
            elif value == 'FinancialInformationItemType':
                self.__financial_information_it(sub_element)
            elif value == 'RealEstateItemType':
                self.__real_estate_it(sub_element)
            elif value == 'BuildingsItemType':
                self.__buildings_it(sub_element)
            elif value == 'OtherSpacesInControlOfTheHousingCompanyItemType':
                self.__other_spaces_in_control_of_hoc(sub_element)

    def __hoc_information_item_type(self, parent_element):
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

        parent_element = functions.elements_to_element_tree(
            sub_elements,
            parent_element,
            'fi-suc-hoc:')

        for child in parent_element:
            if child.tag == 'fi-suc-hoc:ReportOnMaintenanceNeedsInformation':
                self.__report_on_maintenance_needs_information_item_type(child)
            elif child.tag == 'fi-suc-hoc:ReportOnMaintenanceNeeds':
                self.__report_on_maintenance_needs_item_type(child)
            elif child.tag == 'fi-suc-hoc:CompletedModernisationAndRemarkableRepairWork':
                self.__complete_modernisation_and_remarkable_repairwork_item_type(child)
            elif child.tag == 'fi-suc-hoc:AssessmentOfCondition':
                self.__assessment_of_condition_item_type(child)

    def __report_on_maintenance_needs_information_item_type(self, parent_element):
        """Builds HousingCompanyInformation section in hoc entrypoint"""

        sub_elements = {
            'ReportOnMaintenanceNeedsPresentedInTheAnnualGeneralMeeting' : 'booleanItemType',
            'ReportOnMaintenanceNeedsDate' : 'dateItemType'
            }

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-hoc:')

    def __report_on_maintenance_needs_item_type(self, parent_element):
        sub_elements = {
            'ReportOnMaintenanceNeedsDrafted' : 'booleanItemType',
            'ReportOnMaintenanceNeedsExplanation' : 'stringItemType',
            'ReportOnMaintenanceNeedsDraftedInTheYear' : 'integerItemType',
            'ReportOnMaintenanceNeedsDraftedForPeriodInYears' : 'decimalItemType'
        }

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-hoc:')

    def __complete_modernisation_and_remarkable_repairwork_item_type(self, parent_element):
        sub_elements = {
            'CompletedModernisationAndRemarkableRepairWorkExplanation' : 'stringItemType',
            'CompletedModernisationAndRemarkableRepairWorkStatus' : 'stringItemType',
            'CompletedModernisationAndRemarkableRepairWorkYear' : 'integerItemType'
        }

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-hoc:')

    def __assessment_of_condition_item_type(self, parent_element):
        sub_elements = {
            'LatestAssessmentOfConditionYear' : 'integerItemType',
            'AssessmentOfConditionDescription' : 'stringItemType',
        }

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-hoc:')

    def __printing_of_shares_item_type(self, parent_element):

        sub_elements = {
            'PrintingOfSharesDoneInSecurityPrinting' : 'booleanItemType',
            'SecurityPrintingAdditionalDetail' : 'stringItemType',
            'ApartmentLayoutDescriptionHasBeenChangedAfterTheFirstOfJuly1972' : 'booleanItemType'
        }

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-hoc:')

    def __spaces_stated_in_the_articles_of_association_item_type(self, parent_element):

        sub_elements = {
            'SpacesStatedInTheArticlesOfAssociationInPosessionOfTheShareHolders' :
            'SpacesStatedInTheArticlesOfAssociationInPosessionOfTheShareHoldersItemType',
            'SpacesStatedInTheArticlesOfAssociationInPosessionOfTheHousingCompany' :
            'SpacesStatedInTheArticlesOfAssociationInPosessionOfTheHousingCompanyItemType'
        }

        for key, value in sub_elements.items():
            sub_element = ET.SubElement(parent_element, 'fi-suc-hoc:'+key)
            if value == 'SpacesStatedInTheArticlesOfAssociation\
                InPosessionOfTheShareHoldersItemType':
                self.__spaces_stated_in_art_of_ass_in_pos_of_shareholder_it(sub_element)
            elif value == 'SpacesStatedInTheArticlesOfAssociationIn\
                PosessionOfTheHousingCompanyItemType':
                self.__spaces_stated_in_art_of_ass_in_pos_of_hoc_it(sub_element)

    def __spaces_stated_in_art_of_ass_in_pos_of_shareholder_it(
            self, parent_element):

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

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-hoc:')

    def __spaces_stated_in_art_of_ass_in_pos_of_hoc_it(self, parent_element):

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

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-hoc:')

    def __other_obligations_it(self, parent_element):

        sub_elements = {
            'ObligationOnParkingSpacesByTheBuildingPermit' : 'integerItemType',
            'RulesOnParkingSpaceDistribution' : 'stringItemType'
        }

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-hoc:')

    def __posession_distr_agreements_it(self, parent_element):

        sub_elements = {
            'PosessionDistributionAgreement' : 'PosessionDistributionAgreementItemType'
        }

        for key in sub_elements:
            sub_element = ET.SubElement(parent_element, 'fi-suc-hoc:'+key)
            if sub_element.tag == 'fi-suc-hoc:PosessionDistributionAgreementItemType':
                self.__posession_distr_agreement_it(sub_element)

    def __posession_distr_agreement_it(self, parent_element):

        sub_elements = {
            'Owner' : 'OwnerItemType',
            'AgreementDocumentNumber' : 'stringItemType',
            'TermsOfAgreement' : 'stringItemType'
        }

        sub_element = ET.SubElement(parent_element, 'fi-suc-hoc:'+'Owner')
        self.__owner_it(sub_element)
        sub_elements.pop('Owner')

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-hoc:')

    def __owner_it(self, parent_element):

        sub_elements = {
            'OwnerName' : 'stringItemType',
            'Share' : 'decimalItemType'
        }

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-hoc:')

    def __insurances_it(self, parent_element):

        sub_element = ET.SubElement(parent_element, 'fi-suc-hoc:'+'Insurance')
        self.__insurance_it(sub_element)

    def __insurance_it(self, parent_element):

        sub_elements = {
            'InsuranceCompany' : 'stringItemType',
            'InsuranceType' : 'stringItemType',
            'OtherInsurance' : 'stringItemType'
            }

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-hoc:')

    def __financial_information_it(self, parent_element):

        sub_elements = {
            'ChargesAndCompensations' : 'ChargesAndCompensationsItemType',
            'TakenLoansGrantedLoanDecisionsAndCreditentialAccounts' :
                'TakenLoansGrantedLoanDecisionsAndCreditentialAccountsItemType',
            'ComplaintActionRegardingTheReasonablingOfTheArticlesOfAssociation' :
                'ComplaintActionRegardingTheReasonablingOfTheArticlesOfAssociationItemType'
            }

        for key, value in sub_elements.items():
            sub_element = ET.SubElement(parent_element, 'fi-suc-hoc:'+key)
            if value == 'ChargesAndCompensationsItemType':
                self.__charges_and_compensations_it(sub_element)
            elif value == 'TakenLoansGrantedLoanDecisionsAnd\
                CreditentialAccountsItemType':
                self.__taken_and_granted_loans_and_credit_accs_it(sub_element)
            elif value == 'ComplaintActionRegardingTheReasonabling\
                OfTheArticlesOfAssociationItemType':
                self.__complaint_act_reg_reasonabling_of_artass_it(
                    sub_element)

    def __charges_and_compensations_it(self, parent_element):

        sub_element = ET.SubElement(parent_element, 'fi-suc-hoc:'+'ChargesOrCompensation')
        self.__charge_and_compensation_it(sub_element)

    def __charge_and_compensation_it(self, parent_element):

        sub_elements = {
            'ChargeType' : 'stringItemType',
            'ChargeTypeName' : 'stringItemType',
            'ChargeUnitPrice' : 'monetaryItemType',
            'ChargeBasis' : 'stringItemType',
            'ChargeTimeUnit' : 'stringItemType',
            'ChargeAdditionalDetail' : 'stringItemType'
        }

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-hoc:')

    def __taken_and_granted_loans_and_credit_accs_it(self, parent_element):

        sub_elements = {
            'Loan' : 'LoanItemType',
            'CredentialAccount' : 'CredentialAccountItemType'
        }

        for key in sub_elements:
            sub_element = ET.SubElement(parent_element, 'fi-suc-hoc:'+key)
            if sub_element.tag == 'fi-suc-hoc:LoanItemType':
                self.__loan_it(sub_element)
            elif sub_element.tag == 'fi-suc-hoc:CredentialAccountItemType':
                self.__credential_acc_it(sub_element)

    def __loan_it(self, parent_element):

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

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-hoc:')

    def __credential_acc_it(self, parent_element):

        sub_elements = {
            'Lender' : 'stringItemType',
            'CreditDescription' : 'stringItemType',
            'CreditAmount' : 'monetaryItemType',
            'CreditDate' : 'dateItemType',
            'CreditLimitMount' : 'monetaryItemType'
        }

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-hoc:')

    def __complaint_act_reg_reasonabling_of_artass_it(self, parent_element):

        sub_elements = {
            'ComplaintRegardingParagraphInTheArticlesOfAssociation' : 'stringItemType',
            'ComplaintExplanation' : 'stringItemType'
        }
        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-hoc:')

    def __real_estate_it(self, parent_element):

        sub_element = ET.SubElement(parent_element, 'fi-suc-hoc:'+'RealEstateInformation')
        self.__real_estate_information_it(sub_element)

    def __real_estate_information_it(self, parent_element):

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

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-hoc:')

        sub_element = ET.SubElement(parent_element, 'fi-suc-hoc:'+'LeasedPlotInformation')
        self.__leased_plot_info_it(sub_element)

    def __leased_plot_info_it(self, parent_element):

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

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-hoc:')

    def __buildings_it(self, parent_element):

        sub_element = ET.SubElement(parent_element, 'fi-suc-hoc:'+'BuildingInformation')
        self.__building_info_it(sub_element)

    def __building_info_it(self, parent_element):

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

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-hoc:')

    def __address_it(self, parent_element):

        sub_elements = {
            'BuildingStreetAddress' : 'stringItemType',
            'BuildingPostalCode' : 'stringItemType',
            'BuildingCity' : 'stringItemType',
            'BuildingCountry' : 'stringItemType'
        }

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-hoc:')

    def __structures_it(self, parent_element):

        sub_elements = {
            'MainBuildingMaterial' : 'stringItemType',
            'RoofType' : 'stringItemType',
            'Cover' : 'stringItemType'
        }

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-hoc:')

    def __systems_it(self, parent_element):

        sub_elements = {
            'HeatingSystem' : 'stringItemType',
            'VentilationSystem' : 'stringItemType',
            'CoolingSystem' : 'stringItemType',
            'InformationSystems' : 'stringItemType',
            'AntennaSystems' : 'stringItemType'
        }

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-hoc:')

    def __energy_consumption_per_e_source_it(self, parent_element):

        sub_elements = {
            'ConsumptionOfHeat' : 'decimalItemType',
            'EnergySource' : 'stringItemType',
            'ConsumptionOfElectricityCommonSpace' : 'decimalItemType'
        }

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-hoc:')

    def __apartments_it(self, parent_element):

        sub_element = ET.SubElement(parent_element, 'fi-suc-hoc:'+'ApartmentInformation')
        self.__apartment_information_it(sub_element)

    def __apartment_information_it(self, parent_element):

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

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-hoc:')

    def __surface_area_dets_it(self, parent_element):

        sub_elements = {
            'SurfaceArea' : 'decimalItemType',
            'SurfaceAreaMeasurementMethod' : 'stringItemType',
            'SurfaceAreaCheckMeasured' : 'booleanItemType'
        }

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-hoc:')

    def __other_spaces_in_control_of_hoc(self, parent_element):

        sub_elements = {
            'ParkingSpaces' : 'ParkingSpacesItemType',
            'OtherSpaces' : 'OtherSpacesItemType'
            }

        for key, value in sub_elements.items():
            sub_element = ET.SubElement(parent_element, 'fi-suc-hoc:'+key)
            if value == 'ParkingSpacesItemType':
                self.__parking_spaces_it(sub_element)
            elif value == 'OtherSpacesItemType':
                self.__other_spaces_it(sub_element)

    def __parking_spaces_it(self, parent_element):

        sub_elements = {
            'ParkingSpacesNumber' : 'integerItemType',
            'ParkingSpaceType' : 'stringItemType'
            }

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-hoc:')

    def __other_spaces_it(self, parent_element):

        sub_elements = {
            'OtherSpaceType' : 'stringItemType',
            'OtherSpaceNumber' : 'integerItemType',
            'OtherSpaceAdditionalDetail' : 'stringItemType'
            }

        functions.elements_to_element_tree(sub_elements, parent_element, 'fi-suc-hoc:')

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
