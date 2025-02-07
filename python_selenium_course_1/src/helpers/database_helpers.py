# pip install pymysql
# wymaga postawienie serwera i bazy MySQL
# poniżej to tylko przykład

import pymysql

# connect to database
# ustawienie pobierania danych jako slownik w liscie [{}, {}, {}]
# pobranie wszystkich rekordow
# zamkniecie polaczenia
# zwrocenie wyniku

def read_from_db(sql):

    connection = pymysql.connect(host='127.0.0.1', port=8889,
                                 user='root', password='root')

    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        db_data = cursor.fetchall()
        cursor.close()
    finally:
        connection.close()
    return db_data


def get_order_from_db_by_order_no(order_no):

    sql = f'SELECT * FROM localdemostore.wp_posts WHERE ID = {order_no} AND post_type = "shop_order";'

    db_order = read_from_db(sql)

    return db_order