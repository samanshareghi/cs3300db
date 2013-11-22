import QueryInterface, QueryEngine,QueryLib

debug = 1

# Looks at an entity's transaction record and calc his account balance
def pre_accountBalance(data):
    bought = QueryInterface.dbQuery('getCostTotalsByLeagueEntity', (data[0], data[1], 'Buy'))
    sold = QueryInterface.dbQuery('getCostTotalsByLeagueEntity', (data[0], data[1], 'Sell'))

    account_balance = 5000 - (sold - bought)
    if debug:
        print 'Balance: {:.2f}'.format(account_balance)
        print type(account_balance)
    return account_balance

def pre_purchase_stock(parms):
    if len(parms) != 8:
        print "Error(1003): purchase_stock wrong number arguments provided: " , len(parms)
        return "Error(1003): purchase_stock wrong number arguments provided: " , len(parms)
    result1 = QueryInterface.dbQuery('purchase_stock_part1', (parms))
    result2 = QueryInterface.dbQuery('purchase_stock_part1', (parms))
    return 1

#returns num rows found in table
def pre_num_rows(table):
    query_str = 'SELECT COUNT(*) FROM ' + table
    #print query_str
    QueryLib.sql['tmp'] = query_str
    #print QueryLib.sql['tmp']
    result = QueryEngine.query_dbQuery('tmp', (''))
    #print result[0]['COUNT(*)']
    #QueryLib.sql['tmp'] = ''
    return  result[0]['COUNT(*)']
    


preProcess = {
               'accountBalance':    pre_accountBalance,
               'purchase_stock':    pre_purchase_stock,
               'num_rows':          pre_num_rows
               
               }
