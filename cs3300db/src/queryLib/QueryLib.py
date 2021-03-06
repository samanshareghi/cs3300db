sql = {
       
     #*****************************DONE************************************#
     # SELECT
     # old initial queries for testing
     'getUsers':                        'SELECT * FROM tb_entity',
     'get_all_banned_all_data':         'SELECT * FROM tb_entity WHERE ( banned=1 )',
     'get_all_banned_username':         'SELECT username FROM tb_entity WHERE ( banned=1 )',
     'is_user_banned':                  'SELECT banned FROM tb_entity WHERE (tb_entity.username=%s AND banned=1)',
     'is_user_banned_idx':              'SELECT banned FROM tb_entity USE INDEX (banned_idx) WHERE (tb_entity.username=%s AND banned=1)',
     'is_user_banned_by_id':            'SELECT username FROM tb_entity WHERE (tb_entity.entity=%s)', # I wanna get rid of this, it's useless
     'is_user_banned_by_id_all_data':   'SELECT * FROM tb_entity WHERE (tb_entity.entity=%s)', # I wanna get rid of this, it's useless
     'login':                           'SELECT * FROM tb_entity WHERE username=%s AND password=%s',
     'userExists':                      'SELECT * FROM tb_entity WHERE username=%s',
     
     # new 11-13-13
     # warning: GUI should be tracking stock pk, not symbol, but may work anyway
     # stock pk is tb_stock.stock (INT AUTO INC)
     'get_stock':           'SELECT * FROM tb_stock WHERE symbol=%s',
     'get_all_stocks':      'SELECT * FROM tb_stock',
     'authentication':      'SELECT * FROM tb_entity WHERE (username=%s AND password=%s)', # this is useless, login does the same thing
     'get_all_users':       'SELECT tb_entity.username,tb_entity.first_name,tb_entity.last_name FROM tb_entity', #useless, getUsers does this already 
     'get_user':            'SELECT * FROM tb_entity WHERE username=%s',
     
     
     # INSERTS/UPDATES
     'transaction':     'INSERT INTO tb_transaction (stock, quantity, price_at_date, dated, portfolio, transaction_type) VALUES (%s,%s,%s,%s,%s,%s)'  ,
     'add_user':        'INSERT INTO tb_entity     (first_name,     last_name,     date_of_birth,    username,    email_address,        password,    gender, banned) VALUES (%s,%s,%s,%s,%s, %s,%s,%s)',
     #*************************************************************************#     
     
     
     #*****************************NEEDS TESTING************************************#
     'getUserTransactions':  'SELECT a.first_name, a.last_name,a.entity,b.portfolio,b.league,c.transaction,e.label,d.label,g.label,c.price_at_date,c.quantity, '
                             '(c.price_at_date * c.quantity) as Cost, c.dated  FROM tb_entity a '
                             'INNER JOIN tb_portfolio b ON a.entity=b.entity '
                             'INNER JOIN tb_transaction c ON c.portfolio=b.portfolio '
                             'INNER JOIN tb_stock d  ON d.stock = c.stock '
                             'INNER JOIN tb_transaction_type e ON c.transaction_type=e.transaction_type '
                             'INNER JOIN tb_stock_index f ON d.stock_index=f.stock_index '
                             'INNER JOIN tb_stock_exchange g ON d.stock_exchange=g.stock_exchange '
                             'WHERE (b.entity=%s AND b.league =%s AND e.label=%s) '
                             'ORDER BY c.transaction',
     #*************************************************************************#                  
               
     
     #*****************************NOT DONE************************************#
     'getWinners':      'SELECT tb_portfolio.entity, MAX(tb_portfolio.balance) FROM tb_portfolio',
     
     # New 11-13-13
     # warning: when stocks are added, no price info is entered
     'add_stock':          "INSERT INTO tb_stock (symbol) VALUES (%s)",
     'delete_stock':       "DELETE FROM tb_stock WHERE symbol=%s",
     # failing ATM due to foreign key
     'delete_user':        'DELETE FROM tb_entity WHERE username=%s', 
     'update_entity_first_name':         'UPDATE tb_entity SET first_name = %s WHERE username=%s',
     'update_entity_last_name':          'UPDATE tb_entity SET last_name = %s WHERE username=%s',
     'update_entity_date_of_birth':      'UPDATE tb_entity SET date_of_birth = %s WHERE username=%s',
     'update_entity_email_address':      'UPDATE tb_entity SET email_address = %s WHERE username=%s',
     'update_entity_password':           'UPDATE tb_entity SET password = %s WHERE username=%s',
     'update_entity_gender':             'UPDATE tb_entity SET gender = %s WHERE username=%s',
     'update_entity_banned':             'UPDATE tb_entity SET banned = %s WHERE username=%s',
     'ban_user':                         'UPDATE tb_entity SET banned = 1 WHERE username=%s',
     'unban_user':                       'UPDATE tb_entity SET banned = 0 WHERE username=%s',

     'purchase_stock':                   'sends to preprocessor -  nothing here',
     'purchase_stock_part1':             'INSERT INTO tb_transaction           (stock, portfolio, cost, quantity, price_at_date, dated, transaction_type) VALUES (%s, %s, %s, %s, %s, NOW(), 7001)',
     'purchase_stock_part2':             'INSERT INTO tb_portfolio_content     (stock, portfolio, cost, quantity, recorded) VALUES (%s, %s, %s, %s, %s)',
     'add_wealth':                       'UPDATE tb_entity SET wealth = wealth + %s WHERE entity=%s',
     #'add_wealth_grthan_idx':            'UPDATE tb_entity SET wealth = wealth + %s WHERE (entity=%s AND wealth_idx >= %s)',
     'add_wealth_grthan_idx':            'UPDATE tb_entity USE INDEX (wealth_idx) SET wealth = wealth + %s WHERE (entity=%s AND wealth >= %s)',
     'add_wealth_grthan':                'UPDATE tb_entity SET wealth = wealth + %s WHERE (entity=%s AND wealth >= %s)',
     #*************************************************************************#
     
     
     #*****************************SPECIAL************************************#
     'num_rows':            'preprocess num_rows',
     'num_rows_sql':        'SELECT COUNT(*) FROM %s',
     #*************************************************************************#

     
     #*****************************EXPERIMENTAL************************************#
     'getCostTotalsByLeagueEntity': 'SELECT SUM(c.price_at_date * c.quantity) as \'Total\'  FROM tb_entity a '
                                    'INNER JOIN tb_portfolio b ON a.entity=b.entity '
                                    'INNER JOIN tb_transaction c ON c.portfolio=b.portfolio '
                                    'INNER JOIN tb_stock d  ON d.stock = c.stock '
                                    'INNER JOIN tb_transaction_type e ON c.transaction_type=e.transaction_type '
                                    'INNER JOIN tb_stock_index f ON d.stock_index=f.stock_index '
                                    'INNER JOIN tb_stock_exchange g ON d.stock_exchange=g.stock_exchange '
                                    'WHERE (b.league =%s AND b.entity=%s AND e.label=%s)',
     
     #*************************************************************************#
         
    }