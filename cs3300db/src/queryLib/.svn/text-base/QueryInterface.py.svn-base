from QueryEngine            import query_dbQuery, insert_dbInsert
from QueryLib               import sql
from QueryPostProcessing    import postProcess
from QueryPreProcessing     import preProcess

debug = 1
debug_postProcess = 0
debug_preProcess = 0

# Queries only - Returns Error string if failed
# Dictionary with data is success
def dbQuery(query, data):
    # check if its a valid query in our query dictionary
    if query not in sql:
        return 'Error: (1001) That query is not in the query dictionary'
    
    # preProcessing bypasses eevrything else, implies
    # more than 1 query necessary for the job
    if query in preProcess:
        result = preProcess[query](data)
        if debug_preProcess:
            print 'preProcess result: '
        return result
    
    # send the query to the query engine
    result = query_dbQuery(query, data)
        
    # If error, return error string UNLESS it is to be post processed
    # Usually tuples are returned, so a string would be an Err
    if isinstance(result, str) and (not (query in postProcess)):
        return result
    
    # if post processing is necessary (casts,math,etc) send to post processing
    # query here becomes an index into the postProcess dictionary
    # and is a function call
    if query in postProcess:
        result = postProcess[query](result)
        if debug_postProcess:
            print 'postProcess result: ' , result
    return result

# Can be used for INSERT and UPDATE - Returns Error string if failed
# or 1 if success
def dbInsert(query, data):
    # check if its a valid query in our query dictionary
    if query not in sql:
        return 'Error: (1002) That query is not in the query dictionary'
    
    # preProcessing bypasses eevrything else, implies
    # more than 1 query necessary for the job
    if query in preProcess:
        result = preProcess[query](data)
        return result
    
    # send the query to the query engine
    result = insert_dbInsert(query, data)
    
    # If error, return error string
    # Usually tuples are returned, so a string would be an Err
    if isinstance(result, str):
        return result
    
    # if post processing is necessary (casts,math,etc) send to post processing
    # query here becomes an index into the postProcess dictionary
    # and is a function call
    if postProcess.has_key(query):
        result = postProcess[query](result)
    return result

#-----------------------------------------------------

