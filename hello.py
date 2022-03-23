

def application(env, start_response):
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text-plain'),
    ]
    body = [bytes(i + '\n', 'ascii') for i in env['QUERY_STRING'].split('&')]
    start_response(status, response_headers)
    return body
