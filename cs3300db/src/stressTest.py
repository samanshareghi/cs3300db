from queryLib.TestDriver import *
from queryLib.QueryInterface import dbQuery, dbInsert
from queryLib.QueryLib import sql

#dbQuery('getUsers',(''))

#result = dbQuery('num_rows', 'tb_entity')
#print 'Num rows: ', result

#stress_add_users(2000)

#stress_sql_query('is_user_banned', ('katniss',), 1000)


#     'add_user': 'INSERT INTO tb_entity     (first_name,     last_name,     date_of_birth,    username,    email_address,        password,    gender, banned) VALUES (%s,%s,%s,%s,%s, %s,%s,%s)',
#stress_sql_insert('add_user', ('joe','blow','1971-01-01','jblow','nomail@mail.com','jbpass','alien',0), 1000)

#stress_add_wealth_grthan(1000.00,2001,-100000)

#stress_add_wealth_grthan_idx(1000.00, 2001, -100000)

#dbQuery('getUsers',(''))

#stress_add_users(1000)

#stress_check_banned(1000)

#stress_check_banned_idx(1000)

#result = dbQuery('num_rows', 'tb_entity')
#print result

#result = stress_check_get_all_banned_all_data(100)
#print result

#result = stress_check_get_all_banned_username(100)
#print result

#result = stress_check_is_user_banned_by_id(2000)
#print result

#result = stress_check_is_user_banned_by_id_all_data(2000)
