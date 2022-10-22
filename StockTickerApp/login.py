import yaml

"""
Creates URI for DB setup
Add login data to StockTickerApp/config/db_login.yaml
"""


# Load login details
with open('config/db_login.yaml', 'r') as login_f:
    try:
        login_dict = yaml.safe_load(login_f)
        username = login_dict.pop('username')
        password = login_dict.pop('password')
        host = login_dict.pop('host')
        port = login_dict.pop('port')
        db_name = login_dict.pop('db_name')
    except yaml.YAMLError as exc:
        print(exc)

# Using pure python PyMySQL bindings - URI = 'mysql+pymysql://.....'
uri = f'mysql+pymysql://{username}:{password}@{host}:{port}/{db_name}'