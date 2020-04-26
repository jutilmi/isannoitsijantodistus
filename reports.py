"""Module includes functions for creating reports"""

from decimal import Decimal
from datetime import datetime as dt

def export_apartment_loan_share_calculation_as_html(
        income_of_accounting_period: tuple,
        expense_of_accounting_period: tuple,
        surplus_or_deficit_of_previous_accounting_period: float,
        debt_capital_remaining: float,
        loan_shares_sum: float,
        apartment_id: int,
        apartment_loan_share: float,
        export_file: str):
    """Function outputs an apartment loan share calculation in html format.

       Keyword arguments
       income_of_accounting_period           -- decimal.Decimal, income of existing\
           accounting period
           (invoiced charge amount, invoiced loan shares amount, other income)
        expense_of_accounting_period         -- decimal.Decimal, expenses of existing\
            accounting period
           (intereset expenses, other capital expenses, loan reductions)
       surplus_or_deficit_of_previous_accounting_period -- currency surplus/decifit
           from previous accounting period
       debt_capital_remaining                -- remaining capital for the loan
       loan_shares_sum                       -- sum of all loan shares for the loan
       apartment_id                          -- apartment id where to calculation will be done
       apartment_loan_share                  -- amount of loan shares for apartment
       export_file                           -- path to file where the report will be created
       """

    income_sum = sum(income_of_accounting_period)
    expense_sum = sum(expense_of_accounting_period)

    debt_in_total = income_sum\
        + expense_sum\
        + surplus_or_deficit_of_previous_accounting_period\
        + debt_capital_remaining

    loan_share_per_unit = debt_in_total.__float__() / loan_shares_sum
    loan_share_for_apartment = loan_share_per_unit * apartment_loan_share

    income_sum_s = Decimal(sum(income_of_accounting_period)).\
        __round__(2).__str__().replace('.', ',')
    expense_sum_s = Decimal(sum(expense_of_accounting_period)).\
        __round__(2).__str__().replace('.', ',')
    surplus_or_deficit_s = Decimal(
        surplus_or_deficit_of_previous_accounting_period).\
            __round__(2).__str__().replace('.', ',')
    debt_capital_remaining_s = Decimal(debt_capital_remaining).\
        __round__(2).__str__().replace('.', ',')
    debt_in_total_s = Decimal(debt_in_total).\
        __round__(2).__str__().replace('.', ',')
    loan_shares_sum_s = Decimal(loan_shares_sum).\
        __round__(2).__str__().replace('.', ',')
    loan_share_per_unit_s = Decimal(loan_share_per_unit).\
        __round__(2).__str__().replace('.', ',')
    loan_share_for_apartment_s = Decimal(loan_share_for_apartment).\
        __round__(2).__str__().replace('.', ',')

    h_str = '<!DOCTYPE html>\n'
    h_str += '<html lang="fi">\n'
    h_str += '<head>\n'
    h_str += '<meta charser="utf-8"/>'
    h_str += '</head>\n'
    h_str += '<body>\n'

    h_str += '<h1>Lainaosuuslaskelma</h1>\n'
    h_str += ('<p>Päiväys: ' + dt.now().strftime('%Y-%m-%d') + '\n')

    h_str += '<h2>TILIKAUDEN TUOTOT</h2>\n'
    h_str += '<table style="width:40%">\n'
    h_str += '<tr>\n'
    h_str += '<td>Pääomavastikkeet</td>\n'
    h_str += '<td style="text-align:right">'\
        + income_of_accounting_period[0].__round__(2).__str__().replace('.', ',') + '</td>\n'
    h_str += '<tr>\n'
    h_str += '<td>Lainaosuussuoritukset</td>\n'
    h_str += '<td style="text-align:right">'\
        + income_of_accounting_period[1].__round__(2).__str__().replace('.', ',') + '</td>\n'
    h_str += '</tr>\n'
    h_str += '<tr>\n'
    h_str += '<td>Muut tuotot</td>\n'
    h_str += '<td style="text-align:right">'\
        + income_of_accounting_period[2].__round__(2).__str__().replace('.', ',') + '</td>\n'
    h_str += '</tr>\n'
    h_str += '<tr>\n'
    h_str += '<td><b>Tuotot yhteensä</b></td>\n'
    h_str += '<td style="text-align:right">' + income_sum_s + '</td>\n'
    h_str += '</tr>\n'
    h_str += '</table>\n'


    h_str += '<h2>TILIKAUDEN MENOT</h2>\n'
    h_str += '<table style="width:40%">\n'
    h_str += '<tr>\n'
    h_str += '<td>Korkokulut</td>\n'
    h_str += '<td style="text-align:right">'\
        + expense_of_accounting_period[0].__round__(2).__str__().replace('.', ',') + '</td>\n'
    h_str += '<tr>\n'
    h_str += '<td>Lainanlyhennykset</td>\n'
    h_str += '<td style="text-align:right">'\
        + expense_of_accounting_period[2].__round__(2).__str__().replace('.', ',') + '</td>\n'
    h_str += '</tr>\n'
    h_str += '<tr>\n'
    h_str += '<td>Muut rahoituskulut</td>\n'
    h_str += '<td style="text-align:right">'\
        + expense_of_accounting_period[1].__round__(2).__str__().replace('.', ',') + '</td>\n'
    h_str += '</tr>\n'
    h_str += '<tr>\n'
    h_str += '<td><b>Kulut yhteensä</b></td>\n'
    h_str += '<td style="text-align:right">'\
        +  expense_sum_s + '</td>\n'
    h_str += '</tr>\n'
    h_str += '</table>\n'

    h_str += '<p>EDELLISELTÄ KAUDELTA SIIRTYVÄ PÄÄOMAVASTIKE YLIJÄÄMÄ\
        ALIJÄÄMÄ: ' + surplus_or_deficit_s + '\n'

    h_str += ('<p>LAINAPÄÄOMA: ' + debt_capital_remaining_s + '\n')
    h_str += ('<p>LAINARASITUS YHTEENSÄ: ' + debt_in_total_s + '\n')

    h_str += ('<p>LAINASTA VASTAAVAT YKSIKÖT: ' + loan_shares_sum_s + '\n')
    h_str += ('<p>LAINARASITUS PER VELALLINEN YKSIKKÖ: ' + loan_share_per_unit_s + '\n')

    h_str += ('<h2>HUONEISTON ' + apartment_id.__str__() + ' LAINAOSUUS</h2>\n')

    h_str += '<table style="width:40%">\n'
    h_str += '<tr>\n'
    h_str += '<th>Huoneiston lainayksikot</th>\n'
    h_str += '<th>Lainaosuus per yksikko</th>\n'
    h_str += '<th>Lainaosuus huoneistolle</th>\n'
    h_str += '</tr>\n'
    h_str += '<tr>\n'
    h_str += '<td style="text-align:right">'\
        + apartment_loan_share.__round__(6).__str__() + '</td>\n'
    h_str += '<td style="text-align:right">'\
        + loan_share_per_unit_s + '</td>\n'
    h_str += '<td style="text-align:right"><b>'\
        + loan_share_for_apartment_s + '</b></td>\n'
    h_str += '</tr>\n'
    h_str += '</table>\n'

    h_str += '</body>\n'
    h_str += '</html>'

    with open(export_file, 'w', encoding='utf-8') as f:
        print(h_str, file=f)
