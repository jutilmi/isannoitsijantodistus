'''Module includes functions to produce loan share calculations and reports
   as an example.'''
import sys
import os
from decimal import Decimal
from datetime import datetime
import calendar

sys.path.insert(1, '.\\git\\isannoitsijantodistus\\example_files')
from test_company_settings import PARAMETERS

# Imports from external databases, for housing company database and accounting database
from housing_company_db_classes import SQL
from accounting_db_classes import MeritAktiva

# Import html report method from reports module
from reports import export_apartment_loan_share_calculation_as_html

TIME_OF_REPORT = datetime.now()

# Check if database exists
if not os.path.isfile(('.\\git\\isannoitsijantodistus\\'\
    + PARAMETERS['housing_company_db_settings']['Database_path'])):
    raise FileExistsError

# Housing companyt database initialize based on company data
HOC_DB = SQL(database=('.\\git\\isannoitsijantodistus\\'\
             + PARAMETERS['housing_company_db_settings']['Database_path']),
             database_type=PARAMETERS['housing_company_db_settings']['Database_type']
             )

# Accounting database initialize
if PARAMETERS['accounting_db_settings']['AccountingSource'] == 'MeritAktiva':
    ACCOUNTING_DB = MeritAktiva(api_id=PARAMETERS['accounting_db_settings']['ApiID'],
                                api_key=PARAMETERS['accounting_db_settings']['ApiKey'])

def loan_details_to_dict(loan_details)->dict:
    '''Functions creates a dictionary having loan identification number as key

       Arguments:
       loan_details            -- list, SQL query of loan details
          (loan identification number, loan interest calculation days)
       '''

    output = {}
    for loan_detail in loan_details:
        output[loan_detail[0]] = loan_detail[1]

    return output

def cumulative_interest(transactions)->Decimal:
    '''Function returns sum of interest from transactions

       Arguments:
       transaction          -- list, list of transactions
       '''

    cumul_interest = Decimal('0.0')
    for transaction in transactions:
        cumul_interest += transaction[12]

    return cumul_interest

def accounting_details(
        period_start: datetime,
        period_end: datetime,
        accounting_codes: dict
        )-> dict:
    '''Retrieves accounting data for share of loans.

       period_start: starting date of period
       period_end: ending date of period
       accounting_codes: accounting code map to income lines
          example:
             {
                 '734004' : 'RL 4 pääomavastikkeet',
                 '734005' : 'RL 5 pääomavastikkeet',
                 '736004' : 'RL 5 lainaosuussuoritukset'
                 }

       return: dict {
           key = accounting_code value
           value = tuple(
               units,
               sum of value of specific accounting code
               )
        }
       '''
    period = {
        'PeriodStart': period_start.strftime('%Y%m%d'),
        'PeriodEnd': period_end.strftime('%Y%m%d')
        }

    print('Haetaan laskut ajanjaksolta '\
          + period_start.strftime('%d.%m.%Y')\
          + '-' + period_end.strftime('%d.%m.%Y')\
          + '...')

    response = ACCOUNTING_DB.get('getinvoices', period)
    print('   Löydetty', len(response), 'laskua ajanjaksolla.')
    print('   Käydään laskut läpi. Odota...')

    # Modifies invoiced details dictionary to add tuple for vastikkeet and lainaosuussuoritukset
    invoiced_details = {}
    for key, value in accounting_codes.items():
        invoiced_details[value] = [0.0] * 2

    # Loops over found invoices
    for invoice in enumerate(response):
        invoice_response = ACCOUNTING_DB.get('getinvoice', {'Id' : invoice[1]['SIHId']})

        if invoice_response['Header']['BatchInfo'].split('-')[0] == 'MY':

            for line in invoice_response['Lines']:
                try:
                    order_desc = accounting_codes[line['AccountCode']]
                    invoiced_details[order_desc][0] += line['Quantity']
                    invoiced_details[order_desc][1] += line['AmountInclVat']
                except KeyError:
                    pass

    #print(json.dumps(json_object, indent=4))
    for key in invoiced_details:
        invoiced_details[key] = tuple(invoiced_details[key])

    return invoiced_details

# SQL strings used in housing company database search
SQL_STRINGS = {
    'SumOfApartmentsLoanShares' :
        '''SELECT
                Sum(LoanShares.RL4_Lainayksikot) AS LoanShares_RL4,\
                Sum(LoanShares.RL5_Lainayksikot) AS LoanShares_RL5,\
                Sum(LoanShares.RL6_Lainayksikot) AS LoanShares_RL6,\
                Sum(LoanShares.RL6b_Lainayksikot) AS LoanShares_RL6b
            FROM LoanShares;
            ''',
    'ApartmentLoanShares' :
        '''SELECT
                ApartmentID,
                RL4_lainayksikot,
                RL5_lainayksikot,
                RL6_lainayksikot
            FROM LoanShares
            WHERE ApartmentID=?;''',
    'DebtCapitalSummary' :
        '''SELECT
                Loans.LoanIdentificationNumber,
                Loans.NameOfLoan,
                Sum(LoansCashFlow.WithdrawalAmount) AS SumOfWithdrawals,
                Sum(LoansCashFlow.ReductionAccordingToPlanAmount)\
                    AS SumOfReductionsAccordingToPlan,
                Sum(LoansCashFlow.ExtraordinaryReductionAmount)\
                    AS SumOfExtraordinaryReductions,
                SumOfWithdrawals+SumOfReductionsAccordingToPlan+SumOfExtraordinaryReductions\
                    AS DebtCapitalRemaining
           FROM Loans INNER JOIN LoansCashFlow
           ON Loans.LoanIdentificationNumber = LoansCashFlow.LoanIdentificationNumber
           GROUP BY
                Loans.LoanIdentificationNumber,
                Loans.NameOfLoan,
                LoansCashFlow.LoanIdentificationNumber,
                Loans.Active
           HAVING (((Loans.Active)=True));
           ''',
    'LoanCashFlowAll' :
    '''SELECT
            LoansCashFlow.LoanIdentificationNumber,
            LoansCashFlow.TransactionDate,
            LoansCashFlow.WithdrawalAmount,
            LoansCashFlow.ReductionAccordingToPlanAmount,
            LoansCashFlow.ExtraordinaryReductionAmount,
            LoansCashFlow.OtherExpenseAmount,
            LoansCashFlow.PaidInterest,
            LoansCashFlow.InterestRate,
            LoansCashFlow.Rounding,
            LoansCashFlow.SurplusOrDecifitFromPreviousPeriod
       FROM LoansCashFlow
       WHERE ((LoansCashFlow.LoanIdentificationNumber)=?)
       ORDER BY LoansCashFlow.TransactionDate;
       ''',
    'LoanCashFlowOfAccountingPeriod' :
    '''SELECT
            LoansCashFlow.LoanIdentificationNumber,
            LoansCashFlow.TransactionDate,
            LoansCashFlow.WithdrawalAmount,
            LoansCashFlow.ReductionAccordingToPlanAmount,
            LoansCashFlow.ExtraordinaryReductionAmount,
            LoansCashFlow.OtherExpenseAmount,
            LoansCashFlow.PaidInterest,
            LoansCashFlow.InterestRate,
            LoansCashFlow.Rounding,
            LoansCashFlow.SurplusOrDecifitFromPreviousPeriod
       FROM LoansCashFlow
       WHERE (
        (
            (LoansCashFlow.LoanIdentificationNumber)=?) AND
            (LoansCashFlow.TransactionDate>=DateSerial(?,1,1)) AND
            (LoansCashFlow.TransactionDate<=DateSerial(?,12,31))
            )
       ORDER BY LoansCashFlow.TransactionDate;
       ''',
    'LoanDetails' :
    '''SELECT
            Loans.LoanIdentificationNumber,
            Loans.AmountOfInterestDatesPerYear,
            Loans.NameOfLoan
       FROM Loans
       WHERE (Loans.Active = True);
       '''
    }

### -- Housing company database queries start
HOC_DB.connect()

TOTAL_LOAN_SHARES = HOC_DB.query(SQL_STRINGS['SumOfApartmentsLoanShares'])
APARTMENT_LOAN_SHARES = HOC_DB.query(SQL_STRINGS['ApartmentLoanShares'], (4,))
DEBT_CAPITAL_SUMMARY = HOC_DB.query(SQL_STRINGS['DebtCapitalSummary'])
LOAN_DETAILS = HOC_DB.query(SQL_STRINGS['LoanDetails'])

LOAN_CASH_FLOWS = []
for LOAN_DETAIL in LOAN_DETAILS:
    LOAN_CASH_FLOWS.append(HOC_DB.query(SQL_STRINGS['LoanCashFlowAll'], (LOAN_DETAIL[0],)))

HOC_DB.close()
### -- Housing company data queries end

LOAN_DETAILS = loan_details_to_dict(LOAN_DETAILS)

ALL_INTEREST_EXPENSES_FROM_PERIOD = []
ALL_OTHER_CAPITAL_EXPENSES_FROM_PERIOD = []
ALL_REDUCTIONS_FROM_PERIOD = []

CASH_FLOWS_WITH_INTEREST_DETAILS = []
CASH_FLOW_CUMULATIVE_DATA = {}

# Obtaining the year from which to calculate
ACCOUNTING_PERIOD = TIME_OF_REPORT.year

# Looping over loan cash flow data to obtain expenses for loan share calculation
for transactions_for_specific_loan in LOAN_CASH_FLOWS:
    # Resetting cumulative values
    cumulat_redutions_acc_to_plan = Decimal('0.0')
    cumulat_extra_reductions = Decimal('0.0')
    cumulat_withdrawals = Decimal('0.0')
    cumulat_other_expenses = Decimal('0.0')
    cumulat_interest = Decimal('0.0')
    cumulat_capital_remaining = Decimal('0.0')
    cumulat_reductions = Decimal('0.0')

    transactions_for_specific_loan_with_interest_details = []
    transaction_num = 0

    for TRANSACTION in transactions_for_specific_loan:

        transaction_with_interest_details = []

        cumulat_capital_remaining += TRANSACTION[4]\
            + TRANSACTION[3] + TRANSACTION[2]

        for item in TRANSACTION:
            transaction_with_interest_details.append(item)

        # Interest calculation period
        if transactions_for_specific_loan[transaction_num] != transactions_for_specific_loan[-1]:
            date_to_add = transactions_for_specific_loan[transaction_num+1][1]
        else:
            date_to_add = TIME_OF_REPORT

        transaction_with_interest_details.append(date_to_add)

        interest_days = (transaction_with_interest_details[-1]\
            - transaction_with_interest_details[1]).days

        # If we are in the first row of calculation, add one day to interest calculation days
        if transaction_num == 0:
            interest_days += 1

        # Calculating interest
        interest_per_transaction = float(-cumulat_capital_remaining)\
            * interest_days / LOAN_DETAILS[TRANSACTION[0]]\
            * transaction_with_interest_details[7]

        if\
            TRANSACTION[1] >= datetime(ACCOUNTING_PERIOD, 1, 1) and\
            TRANSACTION[1] <= datetime(ACCOUNTING_PERIOD, 12, 31):
            cumulat_interest += Decimal(interest_per_transaction)
            cumulat_withdrawals += TRANSACTION[2]
            cumulat_other_expenses += TRANSACTION[5]
            cumulat_extra_reductions += TRANSACTION[3]
            cumulat_redutions_acc_to_plan += TRANSACTION[4]

            cumulat_reductions = cumulat_extra_reductions + cumulat_redutions_acc_to_plan

        if TRANSACTION[1] == datetime(ACCOUNTING_PERIOD, 1, 1):
            capital_in_the_beginning_of_period = cumulat_capital_remaining

            # Check if surplus of deficit from previous accounting period is set
            if TRANSACTION[-1] is None:
                surplus_or_decifit_from_previous_period = Decimal('0.0')
            else:
                surplus_or_decifit_from_previous_period = TRANSACTION[-1].__round__(2)

        transaction_with_interest_details.append(interest_days)
        transaction_with_interest_details.append(cumulat_capital_remaining.__round__(2))
        transaction_with_interest_details.append(interest_per_transaction.__round__(2))

        transaction_with_interest_details.append(cumulat_interest.__round__(2))
        transaction_with_interest_details.append(cumulat_other_expenses.__round__(2))
        transaction_with_interest_details.append(cumulat_reductions.__round__(2))
        #transaction_with_interest_details.append(cumulat_capital_remaining.__round__(2))

        transactions_for_specific_loan_with_interest_details.append(
            tuple(transaction_with_interest_details))

        transaction_num += 1

    CASH_FLOW_CUMULATIVE_DATA[transactions_for_specific_loan_with_interest_details[-1][0]]\
        = [cumulat_interest, cumulat_other_expenses, cumulat_reductions,
           capital_in_the_beginning_of_period, surplus_or_decifit_from_previous_period]

    CASH_FLOWS_WITH_INTEREST_DETAILS.append(transactions_for_specific_loan_with_interest_details)

### Retrieving incomes from database

MONTH_DATA = []
RETRIEVE_YEAR = TIME_OF_REPORT.year

INVOICED_DETAILS = {}
# Add list of lenght two [sum of invoiced units, sum of invoiced amount] to each invoiced row
for accounting_code in PARAMETERS['accounting_db_settings']['ACCOUNTING_CODES'].values():
    INVOICED_DETAILS[accounting_code] = [0.0] * 2

# Looping over months until previous month
for i in range(1, TIME_OF_REPORT.month):
    MONTH_DATA.append(
        accounting_details(
            period_start=datetime(RETRIEVE_YEAR, i, 1),
            period_end=datetime(RETRIEVE_YEAR, i, calendar.monthrange(RETRIEVE_YEAR, i)[1]),
            accounting_codes=PARAMETERS['accounting_db_settings']['ACCOUNTING_CODES']
            )
        )

    # Returning tuple for INVOICED_DETAILS
    for (key, value) in MONTH_DATA[-1].items():
        INVOICED_DETAILS[key] = tuple(
            [INVOICED_DETAILS[key][i]\
            + MONTH_DATA[-1][key][i] for i in range(len(INVOICED_DETAILS[key]))])

###

# Maps loan numbers to invoiced charges as {
# 'loan number : ['Regular capital charge name', 'share loan payment name']}
LOAN_NUMBER_MAP = PARAMETERS['accounting_db_settings']['LOAN_NUMBER_MAP']
LOAN_NUM = 0

print('Laaditaan lainaosuuslaskelmat...')

for loan in CASH_FLOWS_WITH_INTEREST_DETAILS:
    INCOMES = (
        Decimal(INVOICED_DETAILS[LOAN_NUMBER_MAP[loan[-1][0]][0]][1]),
        Decimal(INVOICED_DETAILS[LOAN_NUMBER_MAP[loan[-1][0]][1]][1]),
        Decimal('0.0')) # Data is not available in accounting data

    EXPENSES = (
        CASH_FLOW_CUMULATIVE_DATA[loan[-1][0]][0],
        CASH_FLOW_CUMULATIVE_DATA[loan[-1][0]][1],
        CASH_FLOW_CUMULATIVE_DATA[loan[-1][0]][2]
        )

    SURPLUS_OR_DECIFIT = CASH_FLOW_CUMULATIVE_DATA[loan[-1][0]][4]
    CAPITAL_REMAINING = CASH_FLOW_CUMULATIVE_DATA[loan[-1][0]][3]
    LOAN_DESCRIPTION = ' ' + loan[-1][0]

    LOAN_NUM += 1

    export_apartment_loan_share_calculation_as_html(
        INCOMES, EXPENSES, SURPLUS_OR_DECIFIT, CAPITAL_REMAINING, TOTAL_LOAN_SHARES[0][0],
        APARTMENT_LOAN_SHARES[0][0], APARTMENT_LOAN_SHARES[0][1], 'laskelma_'\
            + loan[-1][0] + '.html', LOAN_DESCRIPTION)
