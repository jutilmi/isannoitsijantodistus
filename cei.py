import xml.etree.ElementTree as ET
import CommonFunctions

class Certificate(object):
    """Tämä luokka vastaa isännöitsijäntodistuksen taksonometriassa
        Todistukseen liittyvät tiedot -osiota ja sen luontia."""

    def __init__(self, contextRef = "cxt1", DiaryNumber = ""):
        self.cei = ET.Element('fi-suc-cei:Certificate') #Luodaan juurielementti
        
        #cei = self.getObjectOfManagerSCertificate(cei)
        self.cei = self.CreateObjectOfManagerSCertificateStructure(self.cei)
        #cei = self.getCertificateInformation(cei)
        self.cei = self.CreateCertificateInformationStructure(self.cei, DiaryNumber)

        #Lisää contextRef-tieto
        self.cei = CommonFunctions.SetContextRef(self.cei, contextRef)

    def CreateObjectOfManagerSCertificateStructure(self, RootElementTree):
        
        ObjectOfManagerSCertificate = ET.SubElement(RootElementTree, 'fi-suc-cei:ObjectOfManagerSCertificate')

        ShareGroupInformation = ET.SubElement(ObjectOfManagerSCertificate, 'fi-suc-cei:ShareGroupInformation')
        ET.SubElement(ShareGroupInformation, 'fi-suc-cei:ShareGroup', attrib={
            'contextRef' : ''
        })

        ET.SubElement(ShareGroupInformation, 'fi-suc-cei:AmountOfShares', attrib={
            'decimals' : '0',
            'contextRef' : '',
            'unitRef' : 'pure'
        })
        
        ET.SubElement(ShareGroupInformation, 'fi-suc-cei:AmountOfVotes', attrib={
            'decimals' : '0',
            'contextRef' : '',
            'unitRef' : 'pure'
        })

        Owners = ET.SubElement(ObjectOfManagerSCertificate, 'fi-suc-cei:Owners')
        Owner = ET.SubElement(Owners, 'fi-suc-cei:Owner')
        
        ET.SubElement(Owner, 'fi-suc-cei:OwnerName', attrib={
            'contextRef' : ''
        })

        ET.SubElement(Owner, 'fi-suc-cei:OwnerShareOfOwnership', attrib={
            'decimals' : '1',
            'contextRef' : '',
            'unitRef' : 'pure'
        })

        ET.SubElement(Owner, 'fi-suc-cei:OwnershipHasChangedDate', attrib={
            'contextRef' : ''
        })

        ET.SubElement(Owner, 'fi-suc-cei:OwnerRegisteredInTheShareListingDate', attrib={
            'contextRef' : ''
        })

        ET.SubElement(Owner, 'fi-suc-cei:ApartmentUsageAsACommonHomeForSpouses', attrib={
            'contextRef' : ''
        })

        InformationRegardingTheConditionOfTheOwnerApartmentKnownByTheHousingCompany = ET.SubElement(ObjectOfManagerSCertificate,
        'fi-suc-cei:InformationRegardingTheConditionOfTheOwnerApartmentKnownByTheHousingCompany')

        ET.SubElement(
        InformationRegardingTheConditionOfTheOwnerApartmentKnownByTheHousingCompany,
        'fi-suc-cei:RemarkableFlawsSubjectToTheMaintenanceLiabilityOfEitherTheShareHolderOrTheHousingCompanyKnownByTheHousingCompany', attrib={
            'contextRef' : ''
        })

        ET.SubElement(
        InformationRegardingTheConditionOfTheOwnerApartmentKnownByTheHousingCompany,
        'fi-suc-cei:InformationRegardingOtherFactorsThatMaySubstanciallyImpactTheUsageOrCostOfUsageOfTheOwnerApartmentKnownByTheHousingCompany', attrib={
            'contextRef' : ''
        })

        ET.SubElement(ObjectOfManagerSCertificate, 'fi-suc-cei:AgreementsAndPracticesThatDifferFromTheHousingCompanyAct', attrib={
            'contextRef' : ''
        })

        MaintenanceAndAlterationWorkDoneByTheShareHolderKnownByTheHousingCompany = ET.SubElement(ObjectOfManagerSCertificate, 
        'fi-suc-cei:MaintenanceAndAlterationWorkDoneByTheShareHolderKnownByTheHousingCompany')

        ET.SubElement(
        MaintenanceAndAlterationWorkDoneByTheShareHolderKnownByTheHousingCompany, 
        'fi-suc-cei:MaintenanceAndAlterationWorkDoneByTheShareHolderKnownByTheHousingCompanyDescription', attrib={
           'contextRef' : ''
        })

        ET.SubElement(
        MaintenanceAndAlterationWorkDoneByTheShareHolderKnownByTheHousingCompany,
        'fi-suc-cei:MaintenanceAndAlterationWorkDoneByTheShareHolderKnownByTheHousingCompanyYearOfCompletion', attrib={
            'decimals' : '0',
            'contextRef' : '',
            'unitRef' : 'pure'
        })

        PosessionRightsAuthorizedByTheShareGroup = ET.SubElement(ObjectOfManagerSCertificate, 'fi-suc-cei:PosessionRightsAuthorizedByTheShareGroup')
        PosessionRightsAuthorizedByTheShareGroupDetails = ET.SubElement(PosessionRightsAuthorizedByTheShareGroup, 'fi-suc-cei:PosessionRightsAuthorizedByTheShareGroupDetails')

        ET.SubElement(PosessionRightsAuthorizedByTheShareGroupDetails, 'fi-suc-cei:SpaceIdentifierReference', attrib={
            'contextRef' : ''
        })
        ET.SubElement(PosessionRightsAuthorizedByTheShareGroupDetails, 'fi-suc-cei:ApartmentRoomNumberAnnouncedByTheShareHolder', attrib={
            'decimals' : '0',
            'contextRef' : '',
            'unitRef' : 'pure'
        })

        ET.SubElement(PosessionRightsAuthorizedByTheShareGroupDetails, 'fi-suc-cei:SpaceType', attrib={
            'contextRef' : ''
        })

        PosessionLimitationsOnTheShareGroupOwnership = ET.SubElement(ObjectOfManagerSCertificate, 'fi-suc-cei:PosessionLimitationsOnTheShareGroupOwnership')
        ET.SubElement(PosessionLimitationsOnTheShareGroupOwnership, 'fi-suc-cei:PosessionRightOfAWidow', attrib={
            'contextRef' : ''
        })

        ET.SubElement(PosessionLimitationsOnTheShareGroupOwnership, 'fi-suc-cei:PosessionLimitationOther', attrib={
            'contextRef' : ''
        })

        PosessionLimitationsOnTheApartmentPosessionRight = ET.SubElement(ObjectOfManagerSCertificate, 'fi-suc-cei:PosessionLimitationsOnTheApartmentPosessionRight')
        ET.SubElement(PosessionLimitationsOnTheApartmentPosessionRight,
        'fi-suc-cei:PosessionLimitationsRelatedToShareGroupOrApartmentPosessionRightsMarkedInTheSharesListing', attrib={
            'contextRef' : ''
        })

        HousingCompanyDecisionOnThePosessionTakingOfTheApartmentAndPosessionDuration = ET.SubElement(ObjectOfManagerSCertificate,
        'fi-suc-cei:HousingCompanyDecisionOnThePosessionTakingOfTheApartmentAndPosessionDuration')
        
        ET.SubElement(HousingCompanyDecisionOnThePosessionTakingOfTheApartmentAndPosessionDuration,
        'fi-suc-cei:AnnualGeneralMeetingHasDecidedUponTheApartmentPosessionTaking', attrib={
            'contextRef' : ''
        })

        ET.SubElement(HousingCompanyDecisionOnThePosessionTakingOfTheApartmentAndPosessionDuration,
        'fi-suc-cei:PosessionStartingDate', attrib={
            'contextRef' : ''
        })

        ET.SubElement(HousingCompanyDecisionOnThePosessionTakingOfTheApartmentAndPosessionDuration,
        'fi-suc-cei:PosessionEndingDate', attrib={
            'contextRef' : ''
        })

        ET.SubElement(HousingCompanyDecisionOnThePosessionTakingOfTheApartmentAndPosessionDuration,
        'fi-suc-cei:HousingCompanyHasLeasedThePosessionTakenApartment', attrib={
            'contextRef' : ''
        })

        ChargesAndCompensationsForTheApartment = ET.SubElement(ObjectOfManagerSCertificate, 'fi-suc-cei:ChargesAndCompensationsForTheApartment')
        ChargesAndCompensationsForTheApartmentDetails = ET.SubElement(ChargesAndCompensationsForTheApartment, 'fi-suc-cei:ChargesAndCompensationsForTheApartmentDetails')

        ET.SubElement(ChargesAndCompensationsForTheApartmentDetails, 'fi-suc-cei:ChargeOrCompensationType', attrib={
            'contextRef' : ''
        })

        ET.SubElement(ChargesAndCompensationsForTheApartmentDetails, 'fi-suc-cei:ChargeOrCompensationTypeName', attrib={
            'contextRef' : ''
        })

        ET.SubElement(ChargesAndCompensationsForTheApartmentDetails, 'fi-suc-cei:UnitPrice', attrib={
            'decimals' : '2',
            'contextRef' : '',
            'unitRef' : 'EUR'
        })

        ET.SubElement(ChargesAndCompensationsForTheApartmentDetails, 'fi-suc-cei:ChargeOrCompensationBasis', attrib={
            'contextRef' : ''
        })

        ET.SubElement(ChargesAndCompensationsForTheApartmentDetails, 'fi-suc-cei:TimeUnit', attrib={
            'contextRef' : ''
        })

        ET.SubElement(ChargesAndCompensationsForTheApartmentDetails,
        'fi-suc-cei:TotalAggregatedAmountForTheChargeOrCompensationType', attrib={
            'decimals' : '2',
            'contextRef' : '',
            'unitRef' : 'EUR'
        })

        ET.SubElement(ObjectOfManagerSCertificate, 'fi-suc-cei:ApartmentIsRegisteredAsVat-Liable', attrib={
            'contextRef' : ''
        })

        ShareholderSOverdueUnpaidChargesForCommonExpenses = ET.SubElement(ObjectOfManagerSCertificate,
        'fi-suc-cei:ShareholderSOverdueUnpaidChargesForCommonExpenses')

        ET.SubElement(ShareholderSOverdueUnpaidChargesForCommonExpenses,
        'fi-suc-cei:OverdueChargesForCommonExpensesWithInterestTotal', attrib={
            'decimals' : '2',
            'contextRef' : '',
            'unitRef' : 'EUR'
        })

        ET.SubElement(ShareholderSOverdueUnpaidChargesForCommonExpenses,
        'fi-suc-cei:OverdueChargesForCommonExpensesWithInterestDate', attrib={
            'contextRef' : ''
        })

        ET.SubElement(ShareholderSOverdueUnpaidChargesForCommonExpenses,
        'fi-suc-cei:OverdueChargesForCommonExpensesOnSellerSResponsibilityTotal', attrib={
            'decimals' : '2',
            'contextRef' : '',
            'unitRef' : 'EUR'
        })

        ET.SubElement(ShareholderSOverdueUnpaidChargesForCommonExpenses,
        'fi-suc-cei:OverdueChargesForCommonExpensesOnSellerSResponsibilityDate', attrib={
            'contextRef' : ''
        })

        ET.SubElement(ShareholderSOverdueUnpaidChargesForCommonExpenses,
        'fi-suc-cei:Collectively-ResponsibleOverdueChargesForCommonExpensesOverThePrecedingSixMonths', attrib={
            'decimals' : '2',
            'contextRef' : '',
            'unitRef' : 'EUR'
        })

        ET.SubElement(ShareholderSOverdueUnpaidChargesForCommonExpenses,
        'fi-suc-cei:OverdueChargesForCommonExpensesIncludeVat', attrib={
            'contextRef' : ''
        })

        ApartmentLoanShare = ET.SubElement(ObjectOfManagerSCertificate, 'fi-suc-cei:ApartmentLoanShare')
        ApartmentLoanShareDetails = ET.SubElement(ApartmentLoanShare, 'fi-suc-cei:ApartmentLoanShareDetails')
        
        ET.SubElement(ApartmentLoanShareDetails, 'fi-suc-cei:ApartmentLoanName', attrib={
            'contextRef' : ''
        })

        ET.SubElement(ApartmentLoanShareDetails, 'fi-suc-cei:ApartmentLoanAmount', attrib={
            'decimals' : '2',
            'contextRef' : '',
            'unitRef' : 'EUR'
        })

        ET.SubElement(ApartmentLoanShareDetails, 'fi-suc-cei:ApartmentLoanAmountDate', attrib={
            'contextRef' : ''
        })

        ET.SubElement(ApartmentLoanShareDetails, 'fi-suc-cei:ApartmentLoanCharges', attrib={
            'decimals' : '2',
            'contextRef' : '',
            'unitRef' : 'EUR'
        })

        ET.SubElement(ObjectOfManagerSCertificate,
        'fi-suc-cei:CertificateAdditionalInformation', attrib={
            'contextRef' : ''
        })

        return RootElementTree
    
    def CreateCertificateInformationStructure(self, RootElementTree, DiaryNumber):
        
        CertificateInformation = ET.SubElement(RootElementTree, 'fi-suc-cei:CertificateInformation')

        DiaryNumber = ET.SubElement(CertificateInformation, 'fi-suc-cei:DiaryNumber', attrib={
            'contextRef' : ''
        })
        
        ET.SubElement(CertificateInformation, 'fi-suc-cei:CertificateDate', attrib={
            'contextRef' : ''
        })

        CertificateOrder = ET.SubElement(CertificateInformation, 'fi-suc-cei:CertificateOrder')
        ET.SubElement(CertificateOrder, 'fi-suc-cei:CertificateOrderPlacedByName', attrib={
            'contextRef' : ''
        })

        ET.SubElement(CertificateOrder, 'fi-suc-cei:CertificateOrderPlacedByRole', attrib={
            'contextRef' : ''        
        })

        ET.SubElement(CertificateOrder, 'fi-suc-cei:CertificateOrderPlacedByContactDetail', attrib={
            'contextRef' : ''
        })

        CertificateProvider = ET.SubElement(CertificateInformation, 'fi-suc-cei:CertificateProvider')
        ET.SubElement(CertificateProvider, 'fi-suc-cei:CertificateProviderName', attrib={
            'context' : ''
        })

        ET.SubElement(CertificateProvider, 'fi-suc-cei:CertificateProviderRole', attrib={
            'contextRef' : ''
        })

        ET.SubElement(CertificateProvider, 'fi-suc-cei:CertificateProviderContactDetail', attrib={
            'contextRef' : ''
        })

        ET.SubElement(CertificateProvider, 'fi-suc-cei:CertificateProviderOrganization', attrib={
            'contextRef' : ''
        })

        ET.SubElement(CertificateProvider,
        'fi-suc-cei:CertificateProviderOrganizationIdentifier', attrib={
            'contextRef' : ''
        })

        RecommendedAttachmentsToTheSuperintendentSCertificate = ET.SubElement(CertificateInformation, 'fi-suc-cei:RecommendedAttachmentsToTheSuperintendentSCertificate')
        
        ET.SubElement(RecommendedAttachmentsToTheSuperintendentSCertificate,
        'fi-suc-cei:ConfirmedFinancialStatements', attrib={
            'contextRef' : ''
        })

        ET.SubElement(RecommendedAttachmentsToTheSuperintendentSCertificate,
        'fi-suc-cei:ReinforcedBudget', attrib={
            'contextRef' : ''
        })

        ET.SubElement(RecommendedAttachmentsToTheSuperintendentSCertificate,
        'fi-suc-cei:ArticlesOfAssociation', attrib={
            'contextRef' : ''
        })

        ET.SubElement(RecommendedAttachmentsToTheSuperintendentSCertificate,
        'fi-suc-cei:ActivityReport', attrib={
            'contextRef' : ''
        })

        ET.SubElement(RecommendedAttachmentsToTheSuperintendentSCertificate,
        'fi-suc-cei:AuditorSReport', attrib={
            'contextRef' : ''
        })

        ET.SubElement(RecommendedAttachmentsToTheSuperintendentSCertificate,
        'fi-suc-cei:PerformanceAuditReport', attrib={
            'contextRef' : ''
        })

        OtherAttachmentsToTheSuperintendentSCertificate = ET.SubElement(CertificateInformation, 'fi-suc-cei:OtherAttachmentsToTheSuperintendentSCertificate')

        ET.SubElement(OtherAttachmentsToTheSuperintendentSCertificate,
        'fi-suc-cei:FloorPlanForApartments', attrib={
            'contextRef' : ''
        })

        ET.SubElement(OtherAttachmentsToTheSuperintendentSCertificate,
        'fi-suc-cei:BoardOfDirectorsReportOnTheCompanySBuildingsAndPropertyMaintenanceNeeds', attrib={
            'contextRef' : ''
        })

        ET.SubElement(OtherAttachmentsToTheSuperintendentSCertificate,
        'fi-suc-cei:SummaryOfConditionAssessment', attrib={
            'contextRef' : ''
        })

        ET.SubElement(OtherAttachmentsToTheSuperintendentSCertificate,
        'fi-suc-cei:HousingCompanySConditionCertificate', attrib={
            'contextRef' : ''
        })

        ET.SubElement(OtherAttachmentsToTheSuperintendentSCertificate,
        'fi-suc-cei:EnergyCertificate', attrib={
            'contextRef' : ''
        })

        ET.SubElement(OtherAttachmentsToTheSuperintendentSCertificate,
        'fi-suc-cei:ReportOnTheMaintenanceAndAlterationWorkDoneOnTheCompanySRealEstatePropertyAndTheYearOfCompletion', attrib={
            'contextRef' : ''
        })

        ET.SubElement(OtherAttachmentsToTheSuperintendentSCertificate,
        'fi-suc-cei:InformationRegardingTheAuthorizationOnIssuingShareOptionsOrOtherRightsToShares', attrib={
            'contextRef' : ''
        })

        ET.SubElement(OtherAttachmentsToTheSuperintendentSCertificate,
        'fi-suc-cei:OtherAttachments', attrib={
            'contextRef' : ''
        })
        
        return RootElementTree














    #def __init__(self):
