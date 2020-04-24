"""This module considers hoc-content according xbrl data struture"""

import xml.etree.ElementTree as ET
import CommonFunctions

class HousingCompany(object):
    """Tämä luokka vastaa isännöitsijäntodistuksen taksonometriassa
    Taloyhtiön tiedot -osioita ja sen luontia.

    """

    def __init__(self, contextRef="cxt1"):
        """Tämän funktion argumentti xbrl on tyyppiä etree.ElementTree
            palauttaa täytetyn saman polun"""
        #Luodaan juurielementit
        root_element = ET.Element('HousingCompany')
        self.hoc = ET.ElementTree(root_element)

        self.hoc_dict = {'HousingCompany' : {}}

        self.hoc = self.buildHOCInformation(self.hoc)
        #hoc = self.getCertificateInformation(cei)

        self.hoc = CommonFunctions.SetContextRef(self.hoc, contextRef)

#    def HousingCompany(self, vHousingCompany)

    def buildHOCInformation(self, root_element_tree):
        """Builds HousingCompanyInformation section in hoc entrupoint

        Keyword arguments:
        root_element_tree -- etree.ElementTree
        """

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

        for key in sub_elements.keys():
            sub_element = ET.SubElement(root_element_tree, 'fi-suc-hoc:'+key)
            if sub_elements[key] == 'HousingCompanyInfromationItemType':
                self.HousingCompanyInfromationItemType(sub_element)
            elif sub_elements[key] == 'PrintingOfSharesItemType':
                self.PrintingOfSharesItemType(sub_element)
        return root_element_tree

    def HousingCompanyInfromationItemType(self, root_element_tree):

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
            'InformationRegardingOtherKnownFactsThatMayHaveASignificantImpactOnTheCompanySFinancialPositionOrOperations' :
            'stringItemType',
            'InformationRegardingUndrawnLoansThatTheOwnerApartmentWillBeLiableForAndForWhichTheLoanSharePerOwnerApartmentIsNotKnown' :
            'stringItemType',
            'ArticlesOfAssociationAndDecisionsOfTheAnnualGeneralMeetingOnTheMaintenanceLiabilityAndTheShareholderSRightToMakeAlterations' :
            'stringItemType',
            'ReportOnMaintenanceNeedsInformation' : 'ReportOnMaintenanceNeedsInformationItemType',
            'ReportOnMaintenanceNeeds' : 'ReportOnMaintenanceNeedsItemType',
            'CompletedModernisationAndRemarkableRepairWork' :
            'CompletedModernisationAndRemarkableRepairWorkItemType',
            'AssessmentOfCondition' : 'AssessmentOfConditionItemType'
        }

        CommonFunctions.ElementsToElementTree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def buildReportOnMaintenanceNeedsInformationItemType(self, root_element_tree):
        sub_elements = {
            'ReportOnMaintenanceNeedsPresentedInTheAnnualGeneralMeeting' : 'booleanItemType',
            'ReportOnMaintenanceNeedsDate' : 'dateItemType'
        }

        CommonFunctions.ElementsToElementTree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def ReportOnMaintenanceNeedsItemType(self, root_element_tree):
        sub_elements = {
            'ReportOnMaintenanceNeedsDrafted' : 'booleanItemType',
            'ReportOnMaintenanceNeedsExplanation' : 'stringItemType',
            'ReportOnMaintenanceNeedsDraftedInTheYear' : 'integerItemType',
            'ReportOnMaintenanceNeedsDraftedForPeriodInYears' : 'decimalItemType'
        }

        CommonFunctions.ElementsToElementTree(sub_elements, root_element_tree,'fi-suc-hoc:')

        return root_element_tree

    def CompletedModernisationAndRemarkableRepairWorkItemType(self, root_element_tree):
        sub_elements = {
            'CompletedModernisationAndRemarkableRepairWorkExplanation' : 'stringItemType',
            'CompletedModernisationAndRemarkableRepairWorkStatus' : 'stringItemType',
            'CompletedModernisationAndRemarkableRepairWorkYear' : 'integerItemType'
        }

        CommonFunctions.ElementsToElementTree(sub_elements,root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def AssessmentOfConditionItemType(self, root_element_tree):
        sub_elements = {
            'LatestAssessmentOfConditionYear' : 'integerItemType',
            'AssessmentOfConditionDescription' : 'stringItemType',
        }

        CommonFunctions.ElementsToElementTree(sub_elements,root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def PrintingOfSharesItemType(self, root_element_tree):

        sub_elements = {
            'PrintingOfSharesDoneInSecurityPrinting' : 'booleanItemType',
            'SecurityPrintingAdditionalDetail' : 'stringItemType',
            'ApartmentLayoutDescriptionHasBeenChangedAfterTheFirstOfJuly1972' : 'booleanItemType'
        }

        CommonFunctions.ElementsToElementTree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def SpacesStatedInTheArticlesOfAssociationItemType(self, root_element_tree):

        sub_elements = {
            'SpacesStatedInTheArticlesOfAssociationInPosessionOfTheShareHolders' :
            'SpacesStatedInTheArticlesOfAssociationInPosessionOfTheShareHoldersItemType',
            'SpacesStatedInTheArticlesOfAssociationInPosessionOfTheHousingCompany' :
            'SpacesStatedInTheArticlesOfAssociationInPosessionOfTheHousingCompanyItemType'
        }

        for key in sub_elements.keys():
            SubElement = ET.SubElement(root_element_tree, 'fi-suc-hoc:'+key)
            if sub_elements[key] == 'SpacesStatedInTheArticlesOfAssociationInPosessionOfTheShareHoldersItemType':
                self.SpacesStatedInTheArticlesOfAssociationInPosessionOfTheShareHoldersItemType(SubElement)
            elif sub_elements[key] == 'SpacesStatedInTheArticlesOfAssociationInPosessionOfTheHousingCompanyItemType':
                self.SpacesStatedInTheArticlesOfAssociationInPosessionOfTheHousingCompanyItemType(SubElement)

        # self.ElementsToElementTree(sub_elements,root_element_tree)

        return root_element_tree

    def SpacesStatedInTheArticlesOfAssociationInPosessionOfTheShareHoldersItemType(
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

        CommonFunctions.ElementsToElementTree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def SpacesStatedInTheArticlesOfAssociationInPosessionOfTheHousingCompanyItemType(
        self, root_element_tree):
        
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

        CommonFunctions.ElementsToElementTree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def OtherObligationsItemType(self, root_element_tree):

        sub_elements = {
            'ObligationOnParkingSpacesByTheBuildingPermit' : 'integerItemType',
            'RulesOnParkingSpaceDistribution' : 'stringItemType'
        }

        CommonFunctions.ElementsToElementTree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def PosessionDistributionAgreementsItemType(self, root_element_tree):

        sub_elements = {
            'PosessionDistributionAgreement' : 'PosessionDistributionAgreementItemType'
        }

        for key in sub_elements.keys():
            SubElement = ET.SubElement(root_element_tree, 'fi-suc-hoc:'+key)
            if sub_elements[key] == 'PosessionDistributionAgreementItemType':
                self.PosessionDistributionAgreementItemType(SubElement)

        return root_element_tree

    def PosessionDistributionAgreementItemType(self, root_element_tree):

        sub_elements = {
            'Owner' : 'OwnerItemType',
            'AgreementDocumentNumber' : 'stringItemType',
            'TermsOfAgreement' : 'stringItemType'
        }

        SubElement = ET.SubElement(root_element_tree, 'fi-suc-hoc:'+'Owner')
        self.OwnerItemType(SubElement)         
        sub_elements.pop('Owner')

        CommonFunctions.ElementsToElementTree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def OwnerItemType(self, root_element_tree):

        sub_elements = {
            'OwnerName' : 'stringItemType',
            'Share' : 'decimalItemType'
        }

        CommonFunctions.ElementsToElementTree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def InsurancesItemType(self, root_element_tree):

        SubElement = ET.SubElement(root_element_tree, 'fi-suc-hoc:'+'Insurance')
        self.InsuranceItemType(SubElement)

        return root_element_tree

    def InsuranceItemType(self, root_element_tree):

        sub_elements = {
            'InsuranceCompany' : 'stringItemType',
            'InsuranceType' : 'stringItemType',
            'OtherInsurance' : 'stringItemType'
            }     

        CommonFunctions.ElementsToElementTree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def FinancialInformationItemType(self, root_element_tree):

        sub_elements = {
            'ChargesAndCompensations' : 'ChargesAndCompensationsItemType',
            'TakenLoansGrantedLoanDecisionsAndCreditentialAccounts' :
            'TakenLoansGrantedLoanDecisionsAndCreditentialAccountsItemType',
            'ComplaintActionRegardingTheReasonablingOfTheArticlesOfAssociation' :
            'ComplaintActionRegardingTheReasonablingOfTheArticlesOfAssociationItemType'
        }

        for key in sub_elements.keys():
            SubElement = ET.SubElement(root_element_tree, 'fi-suc-hoc:'+key)
            if sub_elements[key] == 'ChargesAndCompensationsItemType':
                self.ChargesAndCompensationsItemType(SubElement)
            elif sub_elements[key] == 'TakenLoansGrantedLoanDecisionsAndCreditentialAccountsItemType':
                self.TakenLoansGrantedLoanDecisionsAndCreditentialAccountsItemType(SubElement)
            elif sub_elements[key] == 'ComplaintActionRegardingTheReasonablingOfTheArticlesOfAssociationItemType':
                self.ComplaintActionRegardingTheReasonablingOfTheArticlesOfAssociationItemType(
                    SubElement)

        return root_element_tree

    def ChargesAndCompensationsItemType(self, root_element_tree):

        SubElement = ET.SubElement(root_element_tree, 'fi-suc-hoc:'+'ChargesOrCompensation')
        self.ChargesOrCompensationItemType(SubElement)

        return root_element_tree

    def ChargesOrCompensationItemType(self, root_element_tree):

        sub_elements = {
            'ChargeType' : 'stringItemType',
            'ChargeTypeName' : 'stringItemType',
            'ChargeUnitPrice' : 'monetaryItemType',
            'ChargeBasis' : 'stringItemType',
            'ChargeTimeUnit' : 'stringItemType',
            'ChargeAdditionalDetail' : 'stringItemType'
        }

        CommonFunctions.ElementsToElementTree(sub_elements, root_element_tree, 'fi-suc-hoc:')
        
        return root_element_tree
    
    def TakenLoansGrantedLoanDecisionsAndCreditentialAccountsItemType(self, root_element_tree):

        sub_elements = {
            'Loan' : 'LoanItemType',
            'CredentialAccount' : 'CredentialAccountItemType'
        }

        for key in sub_elements.keys():
            SubElement = ET.SubElement(root_element_tree, 'fi-suc-hoc:'+key)
            if sub_elements[key] == 'LoanItemType':
                self.LoanItemType(SubElement)
            elif sub_elements[key] == 'CredentialAccountItemType':
                self.CredentialAccountItemType(SubElement)
        
        return root_element_tree
        
    def LoanItemType(self, root_element_tree):

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
            'DisclosureOfLiabilitiesIfTheCompanySLoansAreSubjectToVariousShareholders' : 'stringItemType'
        }

        CommonFunctions.ElementsToElementTree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def CredentialAccountItemType(self, root_element_tree):

        sub_elements = {
            'Lender' : 'stringItemType',
            'CreditDescription' : 'stringItemType',
            'CreditAmount' : 'monetaryItemType',
            'CreditDate' : 'dateItemType',
            'CreditLimitMount' : 'monetaryItemType'
        }

        CommonFunctions.ElementsToElementTree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def ComplaintActionRegardingTheReasonablingOfTheArticlesOfAssociationItemType(
            self, root_element_tree):

        sub_elements = {
            'ComplaintRegardingParagraphInTheArticlesOfAssociation' : 'stringItemType',
            'ComplaintExplanation' : 'stringItemType'
        }
        CommonFunctions.ElementsToElementTree(sub_elements, root_element_tree, 'fi-suc-hoc:') 

        return root_element_tree

    def RealEstateItemType(self, root_element_tree):
        
        SubElement = ET.SubElement(root_element_tree, 'fi-suc-hoc:'+'RealEstateInformation')
        self.RealEstateInformationItemType(SubElement)

        return root_element_tree
    
    def RealEstateInformationItemType(self, root_element_tree):

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
        
        CommonFunctions.ElementsToElementTree(sub_elements, root_element_tree, 'fi-suc-hoc:')
        
        SubElement = ET.SubElement(root_element_tree, 'fi-suc-hoc:'+'LeasedPlotInformation')
        self.LeasedPlotInformationItemType(SubElement)

        return root_element_tree

    def LeasedPlotInformationItemType(self, root_element_tree):
        
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

        CommonFunctions.ElementsToElementTree(sub_elements, root_element_tree, 'fi-suc-hoc:') 

        return root_element_tree

    def BuildingsItemType(self, root_element_tree):

        SubElement = ET.SubElement(root_element_tree, 'fi-suc-hoc:'+'BuildingInformation')
        self.BuildingInformationItemType(SubElement)

        return root_element_tree
    
    def BuildingInformationItemType(self, root_element_tree):

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

        CommonFunctions.ElementsToElementTree(sub_elements, root_element_tree, 'fi-suc-hoc:') 

        return root_element_tree
        
    def AddressItemType(self, root_element_tree):

        sub_elements = {
            'BuildingStreetAddress' : 'stringItemType',
            'BuildingPostalCode' : 'stringItemType',
            'BuildingCity' : 'stringItemType',
            'BuildingCountry' : 'stringItemType'                                
        }

        CommonFunctions.ElementsToElementTree(sub_elements, root_element_tree, 'fi-suc-hoc:') 

        return root_element_tree

    def StructuresItemType(self, root_element_tree):

        sub_elements = {
            'MainBuildingMaterial' : 'stringItemType',
            'RoofType' : 'stringItemType',
            'Cover' : 'stringItemType'                                
        }

        CommonFunctions.ElementsToElementTree(sub_elements, root_element_tree, 'fi-suc-hoc:')      

        return root_element_tree

    def SystemsItemType(self, root_element_tree):        

        sub_elements = {
            'HeatingSystem' : 'stringItemType',
            'VentilationSystem' : 'stringItemType',
            'CoolingSystem' : 'stringItemType',
            'InformationSystems' : 'stringItemType',
            'AntennaSystems' : 'stringItemType'                                
        }

        CommonFunctions.ElementsToElementTree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def EnergyConsumptionPerEnergySourceItemType(self, root_element_tree):

        sub_elements = {
            'ConsumptionOfHeat' : 'decimalItemType',
            'EnergySource' : 'stringItemType',
            'ConsumptionOfElectricityCommonSpace' : 'decimalItemType'           
        }

        CommonFunctions.ElementsToElementTree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def ApartmentsItemType(self, root_element_tree):

        SubElement = ET.SubElement(root_element_tree, 'fi-suc-hoc:'+'ApartmentInformation')
        self.ApartmentInformationItemType(SubElement)

        return root_element_tree

    def ApartmentInformationItemType(self, root_element_tree):

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

        CommonFunctions.ElementsToElementTree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def SurfaceAreaDetailsItemType(self, root_element_tree):

        sub_elements = {
            'SurfaceArea' : 'decimalItemType',
            'SurfaceAreaMeasurementMethod' : 'stringItemType',
            'SurfaceAreaCheckMeasured' : 'booleanItemType'
        }

        CommonFunctions.ElementsToElementTree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def OtherSpacesInControlOfTheHousingCompanyItemType(self, root_element_tree):

        sub_elements = {
            'ParkingSpaces' : 'ParkingSpacesItemType',
            'OtherSpaces' : 'OtherSpacesItemType'
        }

        for key in sub_elements.keys():
            SubElement = ET.SubElement(root_element_tree, 'fi-suc-hoc:'+key)
            if sub_elements[key] == 'ParkingSpacesItemType':
                self.ParkingSpacesItemType(SubElement)
            elif sub_elements[key] == 'OtherSpacesItemType':
                self.OtherSpacesItemType(SubElement)        

        return root_element_tree

    def ParkingSpacesItemType(self, root_element_tree):

        sub_elements = {
            'ParkingSpacesNumber' : 'integerItemType',
            'ParkingSpaceType' : 'stringItemType'
        }

        CommonFunctions.ElementsToElementTree(sub_elements, root_element_tree, 'fi-suc-hoc:')

        return root_element_tree

    def OtherSpacesItemType(self, root_element_tree):

        sub_elements = {
            'OtherSpaceType' : 'stringItemType',
            'OtherSpaceNumber' : 'integerItemType',
            'OtherSpaceAdditionalDetail' : 'stringItemType'
        }

        CommonFunctions.ElementsToElementTree(sub_elements, root_element_tree, 'fi-suc-hoc:')

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
