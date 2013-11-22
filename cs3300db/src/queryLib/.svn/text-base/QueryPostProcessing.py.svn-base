# from queryLib.QueryInterface import *

debug = 1

# Extracts the first element from the result tuple
def post_getCostTotalsByLeagueEntity(data):
    return data[0][0]

def post_is_user_banned(result):
    if len(result) > 0:
        return 1
    return 0

def post_authentication(result):
    if len(result) == 0:
        return 0
    if len(result) > 1:
        if debug:
            print 'Too many users authenticated with this credential'
        return 0
    # the only valid result
    if len(result) == 1:
        return result[0]['username']
    return 0

def post_add_user(result):
    return 0
    #below is todo
    if len(result) == 0:
        return 0
    if len(result) > 1:
        if debug:
            print 'Too many users authenticated with this credential'
        return 0
    # the only valid result
    if len(result) == 1:
        return result[0]['username']
    return 0



postProcess = {
               'getCostTotalsByLeagueEntity': post_getCostTotalsByLeagueEntity,
               'is_user_banned':    post_is_user_banned,
               'is_user_banned_idx':    post_is_user_banned,
               'authentication':    post_authentication,
               'add_user':          post_add_user
               
}
