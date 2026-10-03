from collections import deque

historique = {
    "back": deque(['url_D3', 'url_C1', 'url_A8', 'url_A5']),
    "current": 'url_F',
    "forward": deque(['url_Z', 'url_alpha1'])
}

def reculer(hist) :
    if hist["back"] :
        hist["forward"].appendleft(hist["current"])
        hist["current"] = hist["back"].popleft()
    return hist

def avancer(hist) :
    if hist["forward"] :
        hist["back"].appendleft(hist["current"])
        hist["current"] = hist["forward"].popleft()
    return hist

def nouvelle_url(hist, url) :
    hist["back"].appendleft(hist["current"])
    hist["current"] = url
    hist["forward"].clear()
    return hist
