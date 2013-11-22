from queryLib.QueryInterface import dbQuery, dbInsert
import time

# dbQuery(SQL, dataTuple)
# dbInsert(SQL, dataTuple) dbInsert handles INSERT, UPDATE, DELETE
# The second parameter MUST be a tuple ie: (1,2) or (1,2,3)
# There are 3 ways to parameterize the calls as tuples
# 1) No parameters,  use ('')
# 2) One parameter, use ('heisenberg',)
# 3) More than one parm, use ('heisenberg','password','myemail')
# And use primitives without quotes ('heisenberg', 1)
# Python will throw errors if you get the parameter's numbers or types wrong
# If MySQL throws an error (gracefully through a try:catch) you should direct those errors to the db team

#----------------------------------------------------------------------------------------
#new tests 11-13-13
#----------------------------------------------------------------------------------------
#dbInsert('add_stock', ('GOOG',))
#dbQuery('get_stock', ('GOOG',))
#dbQuery('get_all_stocks', (''))
#dbInsert('delete_stock', ('GOOG',))
#dbQuery('authentication', ('heisenberg','BCpassword'))
#dbQuery('get_all_users', (''))
#broekn    dbInsert('delete_user',('heisenberg',))
#dbInsert('update_entity_first_name',('BryanNew','heisenbergee')),
#dbInsert('update_entity_last_name',('LawrenceNew','katniss')),  
#dbInsert('update_entity_date_of_birth',('1970-01-01','heisenberg')),
#dbInsert('update_entity_email_address',('no@mail.com','heisenberg')),
#dbInsert('update_entity_password',('BCpasswordNEW','heisenberg')),
#dbInsert('update_entity_gender',('ALIEN NATION','heisenberg')),
#dbInsert('update_entity_banned',('1','heisenberg')),
#dbInsert('ban_user',('heisenberg',)),
#dbInsert('unban_user',('heisenberg',)),
#result  = dbQuery('is_user_banned',('heisenberg',))
#print 'Banned ? ', result
#dbQuery('is_user_banned',('katniss',)),

dbQuery('getUsers', (''))
#dbInsert('purchase_stock',(''))
#----------------------------------------------------------------------------------------
# old tests
#----------------------------------------------------------------------------------------
#dbQuery('getWinners', (''))
#dbQuery('is_user_banned', ('heisenberg',))
#dbQuery('login', ('heisenberg', 'BCpassword'))
#dbQuery('userExists', ('heisenberg',))

# (first_name,last_name,date_of_birth,username,email_address,password,gender, banned)
# (str,str,date,str,str,str,str,INT)
# hard code what you aren't using
#dbInsert('createUser', ('Bryan', 'Cranston', '1970-01-01', 'heisenberg', 'heisenberg@mail.com', 'password', 'male', 1))

#dbInsert('add_user', ('Bryan', 'Cranston', '1970-01-01', 'heisenberg', 'heisenberg@mail.com', 'password', 'male', 0))


# Capture data from the GUI and insert it
#firstNameFromGUI = 'Joe'
#lastNameFromGUI = 'Smith'
#DOBFromGUI = '1970-01-01'
#userNameFromGUI = 'JoeSmith'
#emailFromGUI = 'Joe@mail.com'
#passwordFromGUI = 'JoeRocks'
#genderFromGUI = 'Male'.lower()
#dbInsert('createUser', (firstNameFromGUI, lastNameFromGUI, DOBFromGUI, userNameFromGUI, emailFromGUI, passwordFromGUI, genderFromGUI, 0))

# (stock,                 quantity,     price_at_date,     dated,     portfolio,                                transaction_type)
# INT ID(30003 AT&T),    INT,        DECIMAL(6,2),        DATETIME,    INT ID(3001 Bryan Cranston league 1),    INT ID(7001 BUY)
# 30003,10,34.20,'2013-10-07',3001,7001
#dbInsert('transaction', (30003, 10, 34.20, '2013-10-07 22:02.15', 3001, 7001))





