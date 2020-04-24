"""This module includes Certificate-class and its methods according cei entry point"""

import xml.etree.ElementTree as ET
import functions

class Certificate():
    """Tämä luokka vastaa isännöitsijäntodistuksen taksonometriassa
        Todistukseen liittyvät tiedot -osiota ja sen luontia."""

    def __init__(self, context_ref="cxt1", diary_number=""):
        self.cei = ET.Element('fi-suc-cei:Certificate') #Luodaan juurielementti
        self.diary_number = diary_number

        #cei = self.getObjectOfManagerSCertificate(cei)
        self.cei = self.create_object_managers_certificate_structure(self.cei)
        #cei = self.getCertificateInformation(cei)
        self.cei = self.create_certicification_information_structure()

        #Lisää contextRef-tieto
        self.cei = functions.set_context_ref(self.cei, context_ref)

    def create_object_managers_certificate_structure(self, root_element_tree):
        """This functions updated defined element tree to include required information

           Keyword arguments:
           root_element_tree               -- xml.etree.ElementTree, element tree to be updated

           Output:                         -- xml.etree.ElementTree, updated element tree
           """

        object_of_managers_certificate = ET.SubElement(
            root_element_tree,
            'fi-suc-cei:object_of_managers_certificate')

        share_group_information = ET.SubElement(
            object_of_managers_certificate,
            'fi-suc-cei:share_group_information')
        ET.SubElement(share_group_information, 'fi-suc-cei:ShareGroup', attrib={
            'contextRef' : ''
        })

        ET.SubElement(share_group_information, 'fi-suc-cei:AmountOfShares', attrib={
            'decimals' : '0',
            'contextRef' : '',
            'unitRef' : 'pure'
        })

        ET.SubElement(share_group_information, 'fi-suc-cei:AmountOfVotes', attrib={
            'decimals' : '0',
            'contextRef' : '',
            'unitRef' : 'pure'
        })

        owners = ET.SubElement(object_of_managers_certificate, 'fi-suc-cei:owners')
        owner = ET.SubElement(owners, 'fi-suc-cei:owner')

        ET.SubElement(owner, 'fi-suc-cei:OwnerName', attrib={
            'contextRef' : ''
        })

        ET.SubElement(owner, 'fi-suc-cei:OwnerShareOfOwnership', attrib={
            'decimals' : '1',
            'contextRef' : '',
            'unitRef' : 'pure'
        })

        ET.SubElement(owner, 'fi-suc-cei:OwnershipHasChangedDate', attrib={
            'contextRef' : ''
        })

        ET.SubElement(owner, 'fi-suc-cei:OwnerRegisteredInTheShareListingDate', attrib={
            'contextRef' : ''
        })

        ET.SubElement(owner, 'fi-suc-cei:ApartmentUsageAsACommonHomeForSpouses', attrib={
            'contextRef' : ''
        })

        info_of_cond_hoc = ET.SubElement(
            object_of_managers_certificate,
            'fi-suc-cei:InformationRegardingTheCondition\
                OfTheOwnerApartmentKnownByTheHousingCompany')

        ET.SubElement(
            info_of_cond_hoc,
            'fi-suc-cei:RemarkableFlawsSubjectToTheMaintenanceLiabilityOf\
                EitherTheShareHolderOrTheHousingCompanyKnownByTheHousingCompany',
            attrib={'contextRef' : ''})

        ET.SubElement(
            info_of_cond_hoc,
            'fi-suc-cei:InformationRegardingOtherFactorsThatMaySubstancially\
                ImpactTheUsageOrCostOfUsageOfTheOwnerApartmentKnownByTheHousingCompany',
            attrib={'contextRef' : ''})

        ET.SubElement(
            object_of_managers_certificate,
            'fi-suc-cei:AgreementsAndPracticesThatDifferFromTheHousingCompanyAct',
            attrib={'contextRef' : ''})

        maintenance_and_alter_known_by_hoc = ET.SubElement(
            object_of_managers_certificate,
            'fi-suc-cei:MaintenanceAndAlterationWorkDoneByThe\
                ShareHolderKnownByTheHousingCompany')

        ET.SubElement(
            maintenance_and_alter_known_by_hoc,
            'fi-suc-cei:MaintenanceAndAlterationWorkDoneByTheShareHolder\
                KnownByTheHousingCompanyDescription',
            attrib={'contextRef' : ''})

        ET.SubElement(
            maintenance_and_alter_known_by_hoc,
            'fi-suc-cei:MaintenanceAndAlterationWorkDoneByTheShareHolderKnown\
                ByTheHousingCompanyYearOfCompletion',
            attrib={
                'decimals' : '0',
                'contextRef' : '',
                'unitRef' : 'pure'
                }
            )

        pos_rights_authorized_by_sg = ET.SubElement(
            object_of_managers_certificate,
            'fi-suc-cei:PosessionRightsAuthorizedByTheShareGroup'
            )
        pos_rights_authorized_by_sg_det = ET.SubElement(
            pos_rights_authorized_by_sg,
            'fi-suc-cei:PosessionRightsAuthorizedByTheShareGroupDetails'
            )

        ET.SubElement(
            pos_rights_authorized_by_sg_det,
            'fi-suc-cei:SpaceIdentifierReference',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            pos_rights_authorized_by_sg_det,
            'fi-suc-cei:ApartmentRoomNumberAnnouncedByTheShareHolder',
            attrib={
                'decimals' : '0',
                'contextRef' : '',
                'unitRef' : 'pure'
                }
            )

        ET.SubElement(
            pos_rights_authorized_by_sg_det,
            'fi-suc-cei:SpaceType',
            attrib={'contextRef' : ''}
            )

        pos_limitation_on_the_ownership = ET.SubElement(
            object_of_managers_certificate,
            'fi-suc-cei:PosessionLimitationsOnTheShareGroupOwnership'
            )
        ET.SubElement(
            pos_limitation_on_the_ownership,
            'fi-suc-cei:PosessionRightOfAWidow',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            pos_limitation_on_the_ownership,
            'fi-suc-cei:PosessionLimitationOther',
            attrib={'contextRef' : ''}
            )

        pos_limitation_on_the_apartment_pos_right = ET.SubElement(
            object_of_managers_certificate,
            'fi-suc-cei:PosessionLimitationsOnTheApartmentPosessionRight'
            )

        ET.SubElement(
            pos_limitation_on_the_apartment_pos_right,
            'fi-suc-cei:PosessionLimitationsRelatedToShareGroupOrApartment\
                PosessionRightsMarkedInTheSharesListing',
            attrib={'contextRef' : ''})

        hoc_dec_on_pos_taking_and_duration = ET.SubElement(
            object_of_managers_certificate,
            'fi-suc-cei:HousingCompanyDecisionOnThePosession\
                TakingOfTheApartmentAndPosessionDuration'
            )

        ET.SubElement(
            hoc_dec_on_pos_taking_and_duration,
            'fi-suc-cei:AnnualGeneralMeetingHasDecidedUponTheApartmentPosessionTaking',
            attrib={'contextRef' : ''})

        ET.SubElement(
            hoc_dec_on_pos_taking_and_duration,
            'fi-suc-cei:PosessionStartingDate',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            hoc_dec_on_pos_taking_and_duration,
            'fi-suc-cei:PosessionEndingDate',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            hoc_dec_on_pos_taking_and_duration,
            'fi-suc-cei:HousingCompanyHasLeasedThePosessionTakenApartment',
            attrib={'contextRef' : ''}
            )

        charges_and_compensations = ET.SubElement(
            object_of_managers_certificate,
            'fi-suc-cei:ChargesAndCompensationsForTheApartment'
            )
        charges_and_compensations_details = ET.SubElement(
            charges_and_compensations,
            'fi-suc-cei:ChargesAndCompensationsForTheApartmentDetails'
            )

        ET.SubElement(
            charges_and_compensations_details,
            'fi-suc-cei:ChargeOrCompensationType',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            charges_and_compensations_details,
            'fi-suc-cei:ChargeOrCompensationTypeName',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            charges_and_compensations_details,
            'fi-suc-cei:UnitPrice',
            attrib={
                'decimals' : '2',
                'contextRef' : '',
                'unitRef' : 'EUR'
                }
            )

        ET.SubElement(
            charges_and_compensations_details,
            'fi-suc-cei:ChargeOrCompensationBasis',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            charges_and_compensations_details,
            'fi-suc-cei:TimeUnit',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            charges_and_compensations_details,
            'fi-suc-cei:TotalAggregatedAmountForTheChargeOrCompensationType',
            attrib={
                'decimals' : '2',
                'contextRef' : '',
                'unitRef' : 'EUR'
                }
            )

        ET.SubElement(
            object_of_managers_certificate,
            'fi-suc-cei:ApartmentIsRegisteredAsVat-Liable',
            attrib={'contextRef' : ''}
            )

        shh_overdue_unpaid_chages = ET.SubElement(
            object_of_managers_certificate,
            'fi-suc-cei:ShareholderSOverdueUnpaidChargesForCommonExpenses'
            )

        ET.SubElement(
            shh_overdue_unpaid_chages,
            'fi-suc-cei:OverdueChargesForCommonExpensesWithInterestTotal',
            attrib={
                'decimals' : '2',
                'contextRef' : '',
                'unitRef' : 'EUR'
                }
            )

        ET.SubElement(
            shh_overdue_unpaid_chages,
            'fi-suc-cei:OverdueChargesForCommonExpensesWithInterestDate',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            shh_overdue_unpaid_chages,
            'fi-suc-cei:OverdueChargesForCommonExpensesOnSellerSResponsibilityTotal',
            attrib={
                'decimals' : '2',
                'contextRef' : '',
                'unitRef' : 'EUR'
                }
            )

        ET.SubElement(
            shh_overdue_unpaid_chages,
            'fi-suc-cei:OverdueChargesForCommonExpensesOnSellerSResponsibilityDate',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            shh_overdue_unpaid_chages,
            'fi-suc-cei:Collectively-ResponsibleOverdueChargesForCommonExpenses\
                OverThePrecedingSixMonths',
            attrib={
                'decimals' : '2',
                'contextRef' : '',
                'unitRef' : 'EUR'
                }
            )

        ET.SubElement(
            shh_overdue_unpaid_chages,
            'fi-suc-cei:OverdueChargesForCommonExpensesIncludeVat',
            attrib={'contextRef' : ''}
            )

        apartment_loan_share = ET.SubElement(
            object_of_managers_certificate,
            'fi-suc-cei:ApartmentLoanShare'
            )

        apartment_loan_share_details = ET.SubElement(
            apartment_loan_share,
            'fi-suc-cei:ApartmentLoanShareDetails'
            )

        ET.SubElement(
            apartment_loan_share_details,
            'fi-suc-cei:ApartmentLoanName',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            apartment_loan_share_details,
            'fi-suc-cei:ApartmentLoanAmount',
            attrib={
                'decimals' : '2',
                'contextRef' : '',
                'unitRef' : 'EUR'
                }
            )

        ET.SubElement(
            apartment_loan_share_details,
            'fi-suc-cei:ApartmentLoanAmountDate',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            apartment_loan_share_details,
            'fi-suc-cei:ApartmentLoanCharges',
            attrib={
                'decimals' : '2',
                'contextRef' : '',
                'unitRef' : 'EUR'
                }
            )

        ET.SubElement(
            object_of_managers_certificate,
            'fi-suc-cei:CertificateAdditionalInformation',
            attrib={'contextRef' : ''}
            )

        return root_element_tree

    def create_certicification_information_structure(self):
        """This method creates certification information structure"""

        certificate_information = ET.SubElement(
            self.cei,
            'fi-suc-cei:CertificateInformation'
            )

        diary_number = ET.SubElement(
            certificate_information,
            'fi-suc-cei:DiaryNumber',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            certificate_information,
            'fi-suc-cei:CertificateDate',
            attrib={'contextRef' : ''}
            )

        certificate_order = ET.SubElement(
            certificate_information,
            'fi-suc-cei:CertificateOrder'
            )

        ET.SubElement(
            certificate_order,
            'fi-suc-cei:CertificateOrderPlacedByName',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            certificate_order,
            'fi-suc-cei:CertificateOrderPlacedByRole',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            certificate_order,
            'fi-suc-cei:CertificateOrderPlacedByContactDetail',
            attrib={'contextRef' : ''}
            )

        certificate_provider = ET.SubElement(
            certificate_information,
            'fi-suc-cei:CertificateProvider'
            )

        ET.SubElement(
            certificate_provider,
            'fi-suc-cei:CertificateProviderName',
            attrib={'context' : ''}
            )

        ET.SubElement(
            certificate_provider,
            'fi-suc-cei:CertificateProviderRole',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            certificate_provider,
            'fi-suc-cei:CertificateProviderContactDetail',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            certificate_provider,
            'fi-suc-cei:CertificateProviderOrganization',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            certificate_provider,
            'fi-suc-cei:CertificateProviderOrganizationIdentifier',
            attrib={'contextRef' : ''}
            )

        rec_attachements_to_the_superintendents_cert = ET.SubElement(
            certificate_information,
            'fi-suc-cei:RecommendedAttachmentsToTheSuperintendentSCertificate'
            )

        ET.SubElement(
            rec_attachements_to_the_superintendents_cert,
            'fi-suc-cei:ConfirmedFinancialStatements',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            rec_attachements_to_the_superintendents_cert,
            'fi-suc-cei:ReinforcedBudget',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            rec_attachements_to_the_superintendents_cert,
            'fi-suc-cei:ArticlesOfAssociation',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            rec_attachements_to_the_superintendents_cert,
            'fi-suc-cei:ActivityReport',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            rec_attachements_to_the_superintendents_cert,
            'fi-suc-cei:AuditorSReport',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            rec_attachements_to_the_superintendents_cert,
            'fi-suc-cei:PerformanceAuditReport',
            attrib={'contextRef' : ''}
            )

        other_attachments_to_the_superintendents_certificate = ET.SubElement(
            certificate_information,
            'fi-suc-cei:OtherAttachmentsToTheSuperintendentSCertificate'
            )

        ET.SubElement(
            other_attachments_to_the_superintendents_certificate,
            'fi-suc-cei:FloorPlanForApartments',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            other_attachments_to_the_superintendents_certificate,
            'fi-suc-cei:BoardOfDirectorsReportOnTheCompanySBuildingsAndPropertyMaintenanceNeeds',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            other_attachments_to_the_superintendents_certificate,
            'fi-suc-cei:SummaryOfConditionAssessment',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            other_attachments_to_the_superintendents_certificate,
            'fi-suc-cei:HousingCompanySConditionCertificate',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            other_attachments_to_the_superintendents_certificate,
            'fi-suc-cei:EnergyCertificate',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            other_attachments_to_the_superintendents_certificate,
            'fi-suc-cei:ReportOnTheMaintenanceAndAlterationWorkDoneOnTheCompanyS\
                RealEstatePropertyAndTheYearOfCompletion',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            other_attachments_to_the_superintendents_certificate,
            'fi-suc-cei:InformationRegardingTheAuthorizationOnIssuing\
                ShareOptionsOrOtherRightsToShares',
            attrib={'contextRef' : ''}
            )

        ET.SubElement(
            other_attachments_to_the_superintendents_certificate,
            'fi-suc-cei:OtherAttachments',
            attrib={'contextRef' : ''}
            )

        return self.cei















    #def __init__(self):
