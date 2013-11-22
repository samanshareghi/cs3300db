from queryLib.QueryInterface import dbQuery, dbInsert
import time


def stress_sql_query(sql,data,num_tests):
    start_time = time.time()
    for e in range(0, num_tests):
        result = dbQuery(sql, data)
    print 'Executed stress_sql_query (',sql,') : ', num_tests ,' times in % .3f' % (time.time() - start_time), 'seconds: % .3f' % (num_tests/( (time.time() - start_time) + 0.001)) , ' ops per second'
  

def stress_sql_insert(sql,data,num_tests):
    start_time = time.time()
    for e in range(0, num_tests):
        result = dbInsert(sql, data)
    print 'Executed stress_sql_insert (',sql,') : ', num_tests ,' times in % .3f' % (time.time() - start_time), 'seconds: % .3f' % (num_tests/( (time.time() - start_time) + 0.001)) , ' ops per second'
 

def stress_add_users(num_users):
    start_time = time.time() 
    for e in range(0, num_users):
        None
        dbInsert('add_user', ('Bryan', 'Cranston', '1970-01-01', 'heisenberg', 'heisenberg@mail.com', 'password', 'male', 1))
        #dbQuery('is_user_banned', ('heisenberg',))
        #dbQuery('get_all_users', (''))
    print 'Executed ', num_users ,' ops in % .3f' % (time.time() - start_time), 'seconds: % .3f' % (num_users/ (time.time() - start_time))


def stress_check_banned(num_users):
    total = 0
    start_time = time.time() 
    for a in range(0, num_users):
        None
        #dbInsert('createUser', ('Bryan', 'Cranston', '1970-01-01', 'heisenberg', 'heisenberg@mail.com', 'password', 'male', 1))
        result = dbQuery('is_user_banned', ('heisenberg',))
        #total = total + result
        #dbQuery('get_all_users', (''))
    print 'Executed stress_check_banned :', num_users ,' ops in % .3f' % (time.time() - start_time), 'seconds: % .3f' % (num_users/( (time.time() - start_time) + 0.001)) , ' ops per second'
    #print 'Total banned ', total
    
def stress_check_banned_idx(num_users):
    total = 0
    start_time = time.time() 
    for a in range(0, num_users):
        None
        #dbInsert('createUser', ('Bryan', 'Cranston', '1970-01-01', 'heisenberg', 'heisenberg@mail.com', 'password', 'male', 1))
        result = dbQuery('is_user_banned_idx', ('heisenberg',))
        #total = total + result
        #dbQuery('get_all_users', (''))
    print 'Executed stress_check_banned_idx : ', num_users ,' ops in % .3f' % (time.time() - start_time), 'seconds: % .3f' % (num_users/( (time.time() - start_time) + 0.001)) , ' ops per second'
    #print 'Total banned ', total
    
def stress_check_get_all_banned_all_data(num_users):
    total = 0
    start_time = time.time() 
    for a in range(0, num_users):
        None
        #dbInsert('createUser', ('Bryan', 'Cranston', '1970-01-01', 'heisenberg', 'heisenberg@mail.com', 'password', 'male', 1))
        result = dbQuery('get_all_banned_all_data', (''))
        #total = total + result
        #dbQuery('get_all_users', (''))
    print 'Executed stress_check_banned :', num_users ,' ops in % .3f' % (time.time() - start_time), 'seconds: % .3f' % (num_users/( (time.time() - start_time) + 0.001)) , ' ops per second'
    #print 'Total banned ', total
    return len(result)

def stress_check_get_all_banned_username(num_users):
    total = 0
    start_time = time.time() 
    for a in range(0, num_users):
        None
        #dbInsert('createUser', ('Bryan', 'Cranston', '1970-01-01', 'heisenberg', 'heisenberg@mail.com', 'password', 'male', 1))
        result = dbQuery('get_all_banned_username', (''))
        #total = total + result
        #dbQuery('get_all_users', (''))
    print 'Executed stress_check_banned :', num_users ,' ops in % .3f' % (time.time() - start_time), 'seconds: % .3f' % (num_users/( (time.time() - start_time) + 0.001)) , ' ops per second'
    #print 'Total banned ', total
    return len(result)

def stress_check_is_user_banned_by_id(num_users):
    total = 0
    start_time = time.time() 
    for a in range(0, num_users):
        #print 'Checking entity: ' , (a+2001)
        #dbInsert('createUser', ('Bryan', 'Cranston', '1970-01-01', 'heisenberg', 'heisenberg@mail.com', 'password', 'male', 1))
        result = dbQuery('is_user_banned_by_id', (a+2001,))
        #total = total + result
        #dbQuery('get_all_users', (''))
    print 'Executed stress_check_banned :', num_users ,' ops in % .3f' % (time.time() - start_time), 'seconds: % .3f' % (num_users/( (time.time() - start_time) + 0.001)) , ' ops per second'
    #print 'Total banned ', total
    return len(result)

def stress_check_is_user_banned_by_id_all_data(num_users):
    total = 0
    start_time = time.time() 
    for a in range(0, num_users):
        #print 'Checking entity: ' , (a+2001)
        #dbInsert('createUser', ('Bryan', 'Cranston', '1970-01-01', 'heisenberg', 'heisenberg@mail.com', 'password', 'male', 1))
        result = dbQuery('is_user_banned_by_id_all_data', (a+2001,))
        #total = total + result
        #dbQuery('get_all_users', (''))
    print 'Executed stress_check_banned :', num_users ,' ops in % .3f' % (time.time() - start_time), 'seconds: % .3f' % (num_users/( (time.time() - start_time) + 0.001)) , ' ops per second'
    #print 'Total banned ', total
    return len(result)
    
    
def stress_update_wealth(dollar_amount):
    num_users  = dbQuery('num_rows', 'tb_entity')
    start_time = time.time()
    entity = 2000
    for e in range(0, num_users):
        entity = entity + 1
        #print entity
        dbInsert('add_wealth', (dollar_amount, entity))
        #dbQuery('is_user_banned', ('heisenberg',))
        #dbQuery('get_all_users', (''))
        
    print 'Executed ', num_users ,' ops in % .3f' % (time.time() - start_time), 'seconds: % .3f' % (num_users/( (time.time() - start_time) + 0.001)) , ' ops per second'
    
def stress_add_wealth_grthan_idx(dollar_amount, entity, grthan):
    num_users  = dbQuery('num_rows', 'tb_entity')
    print 'updating ', num_users, ' rows'
    start_time = time.time()
    entity = 2000
    for e in range(0, num_users):
        entity = entity + 1
        #print entity
        dbInsert('add_wealth_grthan_idx', (dollar_amount, entity, grthan))
        #dbQuery('is_user_banned', ('heisenberg',))
        #dbQuery('get_all_users', (''))
        
    print 'Executed stress_update_wealth_grthan_idx : ', num_users ,' ops in % .3f' % (time.time() - start_time), 'seconds: % .3f' % (num_users/( (time.time() - start_time) + 0.001)) , ' ops per second'

def stress_add_wealth_grthan(dollar_amount, entity, grthan):
    num_users  = dbQuery('num_rows', 'tb_entity')
    start_time = time.time()
    entity = 2000
    for e in range(0, num_users):
        entity = entity + 1
        #print entity
        dbInsert('add_wealth_grthan', (dollar_amount, entity, grthan))
        #dbQuery('is_user_banned', ('heisenberg',))
        #dbQuery('get_all_users', (''))
        
    print 'Executed stress_update_wealth_grthan : ', num_users ,' ops in % .3f' % (time.time() - start_time), 'seconds: % .3f' % (num_users/( (time.time() - start_time) + 0.001)) , ' ops per second'
    
    
    
def stress_set_wealth_grthan_idx(dollar_amount, entity, grthan):
    num_users  = dbQuery('num_rows', 'tb_entity')
    start_time = time.time()
    entity = 2000
    for e in range(0, num_users):
        entity = entity + 1
        #print entity
        dbInsert('add_wealth_grthan_idx', (dollar_amount, entity, grthan))
        #dbQuery('is_user_banned', ('heisenberg',))
        #dbQuery('get_all_users', (''))
        
    print 'Executed stress_update_wealth_grthan_idx : ', num_users ,' ops in % .3f' % (time.time() - start_time), 'seconds: % .3f' % (num_users/( (time.time() - start_time) + 0.001)) , ' ops per second'

def stress_set_wealth_grthan(dollar_amount, entity, grthan):
    num_users  = dbQuery('num_rows', 'tb_entity')
    start_time = time.time()
    entity = 2000
    for e in range(0, num_users):
        entity = entity + 1
        #print entity
        dbInsert('add_wealth_grthan', (dollar_amount, entity, grthan))
        #dbQuery('is_user_banned', ('heisenberg',))
        #dbQuery('get_all_users', (''))
        
    print 'Executed stress_update_wealth_grthan : ', num_users ,' ops in % .3f' % (time.time() - start_time), 'seconds: % .3f' % (num_users/( (time.time() - start_time) + 0.001)) , ' ops per second'
   
     
