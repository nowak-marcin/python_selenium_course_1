# pip install pymysql
# wymaga postawienia serwera i bazy MySQL
# poniżej to tylko przykład

# import pymysql
# from python_selenium_course_1.src.helpers.config.helpers import get_data_base_credentials
# from python_selenium_course_1.src.configs.generic_configs import GenericConfigs

# connect to database
# ustawienie pobierania danych jako slownik w liscie [{}, {}, {}]
# pobranie wszystkich rekordow
# zamkniecie polaczenia
# zwrocenie wyniku

#   def read_from_db(sql):
#   db_creds = get_data_base_credentials()

#   connection = pymysql.connect(host=db_creds['db_host'], db_cred['db_port],
#                                user=db_creds['db_user'], password=db_creds['db_password'])
#
#   try:
#       cursor = connection.cursor(pymysql.cursors.DictCursor)
#       cursor.execute(sql)
#       db_data = cursor.fetchall()
#       cursor.close()
#   finally:
#       connection.close()
#   return db_data


#   def get_order_from_db_by_order_no(order_no):

#   schema = GenericConfigs.DATABASE.SCHEMA
#   table_prefix = GenericConfigs.DATABASE.TABLE_PREFIX

#   sql = f'SELECT * FROM {schema}.{table_prefix}posts WHERE ID = {order_no} AND post_type = "shop_order";'
#   db_order = read_from_db(sql)
#   return db_order
