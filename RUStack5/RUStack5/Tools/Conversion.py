__pdoc__={}
__pdoc__['Response_to_float'] = False
__pdoc__['Response_to_float_list'] = False
__pdoc__['Response_to_four_floats'] = False
__pdoc__['Response_to_int'] = False
__pdoc__['Response_to_string'] = False


def Response_to_float(rsp):
    try:
        rsp_string=rsp.decode('UTF-8')
        rsp_string=rsp_string.replace('(', '')
        rsp_string=rsp_string.replace(')', '')
        return float(rsp_string)
    except:
        return(-99999)

def Response_to_int(rsp):
    try:
        rsp_string=rsp.decode('UTF-8')
        rsp_string=rsp_string.replace('(', '')
        rsp_string=rsp_string.replace(')', '')
        return int(rsp_string)
    except:
        return(-99999)

def Response_to_float_list(rsp):
        rsp_string=rsp.decode('UTF-8')
        rsp_string=rsp_string.replace('(', '')
        rsp_string=rsp_string.replace(')', '')
        rsp_splitted = rsp_string.split(",")
        returnlist=[]
        for s in rsp_splitted:
            val=-99999
            try:
                val=float(s)
            except:
                pass
            returnlist.append(val)
        return returnlist

def Response_to_string(rsp):
    rsp_string=rsp.decode('UTF-8')
    rsp_string=rsp_string.replace('(', '')
    rsp_string=rsp_string.replace(')', '')
    return rsp_string

def Response_to_four_floats(rsp):
    rsp_string=rsp.decode('UTF-8') # naar gewone string
    rsp_string=rsp_string.replace('(', '') # haakjes eraf
    rsp_string=rsp_string.replace(')', '')
    split=rsp_string.split(",")
    l=[]
    for i in split:
        val=-99999
        try:
            val=float(i)
        except:
            pass
        l.append(val)
    return l

