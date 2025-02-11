# import os


def get_base_url():
    return 'http://demostore.supersqa.com'

#   env = os.environ.get('ENV', 'test')
#   if env.lower() == 'test'
#       return 'http://demostore.supersqa.com'
#   elif env.lover() == 'prod':
#       return 'http://demostore-prod.supersqa.com'
#   else:
#       raise Exception(f'unknown environment: {env}')

#   =========================================================================
#   def get_database_credentials():
#   env = os.environ.get.('ENV', 'test')
#   db_user = os.environ.get('DB_USER')
#   db_password = os.environ.get('DB_PASSWORD')
#   if not db_user ord db_password:
#       raise Exception('zmienne srodowiskowe user i password sa obowiazkowe.')
#
#   if env == 'test:
#       db_host = '127.0.0.1'
#       db_port = 8889
#   elif env == 'prod':
#       db_host = 'demostore..supersqa.com'
#       db_port = 3306
#   else:
#       raise Exception(f'unknown enviroment: {env}')
#
#   db_info = {'db_host': db_host, 'db_port: db_port,
#             'db_user: db_user, 'db_password: db_password}
#
#   return db_info
