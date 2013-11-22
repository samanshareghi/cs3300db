import mysql.connector
import time
from QueryPostProcessing    import postProcess
from QueryPreProcessing     import preProcess
from QueryLib               import sql

debug = 1
   
    
#--------------------------------------------------------------
#connect to and query the db, returns string if error
#dictionary if data
# query = index into the sql lib
# sql[query] gives you the actual sql command
def query_dbQuery(query, data):
    start_time = time.time()
    
    try:
        cnx = mysql.connector.connect(**connectParms)
        print "wtf"

    except mysql.connector.Error as e:
        if debug:
            print "Error:", e  # errno, sqlstate, msg values
        s = str(e)
        return s 

    try:
        #cursor = cnx.cursor()
        cursor = cnx.cursor(cursor_class=MySQLCursorDict)
        cursor.execute(sql[query], data)
        result = cursor.fetchall()
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        if debug:
            print "Error:", e  # errno, sqlstate, msg values
        s = str(e)
        return s

    if debug:
        print 'Executed in % .3f' % (time.time() - start_time), 'seconds'
        #print type(result)
        # if it has post processing, some valid result
        # OTHER THAN a data row (list) will be return, such as BOOLEANS
        # so don't print "nothing returned" when something valid (post processed data) WAS returned
        if (len(result) < 1) and ( not (query in postProcess) ):
            print ('No data returned by the query')
        
        
        if (len(result) > 0) and ( not (query in postProcess) ):
            # a list of the keys from the result
            keylist = getKeys(result)
            # print the list of keys from the result
            printKeyList(result)
            
            #output the data to console
            for dictRow in result:
                for k, v in dictRow.iteritems():
                    print "{} |".format(v),
                print ''
                
        if ( (query in postProcess) ):
            print 'Found rows for postProcessing-Sending: ' , query
        
        
        # old array method
        #for row in result :
        #    for attr in row:
        #        print '|{}'.format(attr) + '\t',
        #    print '|'
        

    cursor.close()
    cnx.close()

    return result

#--------------------------------------------------------------
#connect to and insert/update the db, returns string if error
# or None tpye:Nonetype if success
# query = index into the sql lib
# sql[query] gives you the actual sql command
def insert_dbInsert(query, data):
    start_time = time.time()
    
    try:
        cnx = mysql.connector.connect(**connectParms)
    except mysql.connector.Error as e:
        if debug:
            print "Error:", e  # errno, sqlstate, msg values
        s = str(e)
        return s     

    try:
        #cursor = cnx.cursor()
        cursor = cnx.cursor(cursor_class=MySQLCursorDict)
        result = cursor.execute(sql[query], data)
    except mysql.connector.Error as e:
        cursor.close()
        cnx.close()
        if debug:
            print "Error:", e  # errno, sqlstate, msg values
        s = str(e)
        return s
    
    if debug:
        print 'Executed in % .3f' % (time.time() - start_time), 'seconds'
        
        if (result):
            print 'Insert,Update,or Delete returned: ' , str(result)
            
        

    cnx.commit()
    cursor.close()
    cnx.close()

    return 1

#--------------------------------------------------------------

db_connect_cs3300db_testcases = {
    'user': 'mark',
    'password': 'cs3300db',
    'host': 'cs3300.dyndns.org',
    'port': '33000',
    'database': 'cs3300db_testcases'
    }

db_connect_cs3300db_stressTests = {
    'user': 'mark',
    'password': 'cs3300db',
    'host': 'cs3300.dyndns.org',
    'port': '33000',
    'database': 'cs3300db_stressTests'
    }


db_connect_cs3300db = {
    'user': 'middleware',
    'password': 'middleware3300',
    'host': 'cs3300.dyndns.org',
    'port': '33000',
    'database': 'cs3300db'
    }

db_connect_cs3300db_stressTests_linux = {
    'user': 'mark',
    'password': 'cs3300db',
    'host': '192.168.223.12',
    'port': '33000',
    'database': 'cs3300db_stressTests'
    }

db_connect_saman = {
    'user': 'saman',
    'password': '3300dbdev',
    'host': 'cs3300.dyndns.org',
    'port': '33000',
    'database': 'cs3300db'
}

connectParms = db_connect_saman
#connectParms = db_connect_cs3300db_stressTests


#--------------------------------------------------------------
# Override _row_to_python, zips together the column names 
# along with the row data
# return dict(zip(self.column_names, row))
#
class MySQLCursorDict(mysql.connector.cursor.MySQLCursor):
    def _row_to_python(self, rowdata, desc=None):
        row = super(MySQLCursorDict, self)._row_to_python(rowdata, desc)
        if row:
            return dict(zip(self.column_names, row))
        return None

#return the keys from the db query result as a list
def getKeys(dbresult):
    #errorcheck empty list
    if (len(dbresult) < 1):
        return ('No data',)
    
    #return after first loop iteration - every row has key lists
    #so, just retunr the first row's key list
    for dictRow in dbresult:
        return dictRow.keys()
        

#return the keys from the db query result as a list
def getKeys_old(dbresult):
    #errorcheck empty list
    if (len(dbresult) < 1):
        return ('No data',)
    #generate the list from the first list dictionary
    keylist = []
    for dictRow in dbresult:
        for k, v in dictRow.iteritems():
            keylist.append(k)
            #return after first loop iteration
        return keylist

#prints the keys from the db query result
def printKeyList(dbresult):
    #errorcheck empty list
    if (len(dbresult) < 1):
        print ('No data')
        return
    #getKeys returns a list of keys
    keylist = getKeys(dbresult)
    #- print the list
    for k in keylist:
        print "{} |".format(k),
    print ''
 



