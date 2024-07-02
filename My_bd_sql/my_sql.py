import pymysql
from config_mysql import host, user, password, db_name
# конект к БД
try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print('Successfully connection...')

except Exception as ex:
    print('Connection refused...')
    print(ex)
# Сзодание таблиц
# with connection:
#     with connection.cursor() as cur:
#         sql = """CREATE TABLE book(
#         book_id	 INT PRIMARY KEY AUTO_INCREMENT,
#         title	VARCHAR(50),
#         author	VARCHAR(30),
#         price	DECIMAL(8, 2),
#         amount	INT);"""
#         cur.execute(sql)
# Изменение таблицы
# with connection:
#     with connection.cursor() as curs:
#         change_row = "ALTER TABLE readers CHANGE reader_address reader_adress VARCHAR(1000);"
#         curs.execute(change_row)

# Добавление столбца
# with connection:
#     with connection.cursor() as curs:
#         add_coll = "ALTER TABLE talons ADD visit_amount DECIMAL(10,2);"
#         curs.execute(add_coll)

# Первичный ключ
# with connection:
#     with connection.cursor() as curs:
#         primary = "ALTER TABLE patients ADD PRIMARY KEY (oms_num);"
#         curs.execute(primary)

# Создание внешнего ключа
# with connection:
#     with connection.cursor() as curs:
#         rep_coll = "ALTER TABLE patients ADD FOREIGN KEY (area_num) REFERENCES med_area(area_num);"
#         curs.execute(rep_coll)

# Заполняем таблицу
# with connection:
#     with connection.cursor() as curs:
#         insert_data = """INSERT INTO book(title, author, price, amount)
#             VALUES
#             ('Стихотворения и поэмы', 'Есенин С.А.', 650.00, 15);"""
#         curs.execute(insert_data)
#         connection.commit()


# Обновить данные таблицы
# with connection:
#     with connection.cursor() as curs:
#         update_dat = """UPDATE books_in_use
#         SET fine_amount = (8.45 * (DATEDIFF(return_date, issue_date) - return_period))
#         WHERE DATEDIFF(return_date, issue_date) > return_period;"""
#         curs.execute(update_dat)
#         connection.commit()
# # Удалить данные из таблицы
# with connection:
#     with connection.cursor() as curs:
#         delete_row = "DELETE FROM talons WHERE doctor_num = 2;"
#         curs.execute(delete_row)
#         connection.commit()
# Удаление таблицы
# with connection:
#     with connection.cursor() as curs:
#         delete_table = "DROP TABLE doctors"
#         curs.execute(delete_table)

# Вывести все данные таблицы
# with connection:
#     with connection.cursor() as curs:
#         all_rows = "SELECT CURDATE() AS ex_curdate;"
#         curs.execute(all_rows)
#         rows = curs.fetchall()
#         for row in rows:
#             print(row)
