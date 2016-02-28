def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    pairs = environ['QUERY_STRING'].split('&')
    #from collections import defaultdict as dd
    #d = dd(list)
    #for pp in pairs:
    #    a, b = pp.splir('=')
    #    d[a].append(b)
    return pairs

