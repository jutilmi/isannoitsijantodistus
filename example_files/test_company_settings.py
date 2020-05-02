PARAMETERS = {
    'housing_company_db_settings' : {
        'Database_type' : 'ACCESS',
        'Database_path': '.\\example_files\\housing_company_db1.accdb',
        },

    'accounting_db_settings' : {
        'AccountingSource' : 'MeritAktiva',
        'ApiID': 'your-ApiID',
        'ApiKey': 'your-ApiKey',
        'ACCOUNTING_CODES' : {
            '734004' : 'RL 4 pääomavastikkeet',
            '734005' : 'RL 5 pääomavastikkeet',
            '734006' : 'RL 6 pääomavastikkeet',
            '736004' : 'RL 4 lainaosuussuoritukset',
            '736005' : 'RL 5 lainaosuussuoritukset',
            '736006' : 'RL 6 lainaosuussuoritukset'
            },
        'LOAN_NUMBER_MAP' : {
            '111111-1111111' : ['RL 4 pääomavastikkeet', 'RL 4 lainaosuussuoritukset'],
            '222222-1111111' : ['RL 6 pääomavastikkeet', 'RL 6 lainaosuussuoritukset'],
            '333333-1111111' : ['RL 5 pääomavastikkeet', 'RL 5 lainaosuussuoritukset']
            }
        }
    }
