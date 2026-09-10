from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
import json

dic = {
    
}


# server start up from the official wsgi documentation
def simple_app(environ, start_response):

    path = environ["PATH_INFO"]
    headers = [('content-Type: application/json', 'text/plain; charset=utf-8')]

    # /tasks endpoint
    if path == "/tasks":
        # GET
        if environ["REQUEST_METHOD"] == "GET":

            params = parse_qs(environ["QUERY_STRING"])
            print(path)
            id = params.get("id")
            if(id != None):
                key = int(id[0])
                value = dic.get(key)
                if value == None:
                    status = '404 Not Found'
                    start_response(status, headers)
                    return [b"No task with such id exists"]
                status = '200 OK'
                start_response(status, headers)
                return [json.dumps(value).encode("utf-8")]

            else:
                print("get all")
                value = json.dumps(dic)
                status = '200 OK'
                start_response(status, headers)
                return [value.encode("utf-8")]
        # POST
        elif environ["REQUEST_METHOD"] == "POST":
            params = parse_qs(environ["QUERY_STRING"])
            print(path)
            length = int(environ.get("CONTENT_LENGTH", 0))
            body = environ["wsgi.input"].read(length)
            data = json.loads(body)
            
            i = 0
            while dic.get(i) != None:
                i += 1
            dic[i] = data
            status = '201 Created'
            start_response(status, headers)
            return [json.dumps(dic[i]).encode("utf-8")]
        # PATCH
        elif environ["REQUEST_METHOD"] == "PATCH":
            params = parse_qs(environ["QUERY_STRING"])
            print(path)
            length = int(environ.get("CONTENT_LENGTH", 0))
            body = environ["wsgi.input"].read(length)
            data = json.loads(body)
            
            id = int(params.get("id")[0])
            if dic.get(id) == None:
                status = '404 Not Found'
                start_response(status, headers)
                return [b"No tasks with such id found"]
            dic.get(id).update(data)
            #dic[id] = data
            status = '201 Created'
            start_response(status, headers)
            return [json.dumps(dic[id]).encode("utf-8")]
        # DELETE
        elif environ["REQUEST_METHOD"] == "DELETE":

            params = parse_qs(environ["QUERY_STRING"])
            id = params.get("id")
            if(id != None):
                key = int(id[0])
                value = dic.get(key)
                if not (key in dic.keys()):
                    status = '404 Not Found'
                    start_response(status, headers)
                    return [b"no hay una keydubi"]
                if value == None:
                    status = '204 No Content'
                    start_response(status, headers)
                    return [b"no hay una tareubi"]
                del dic[int(id[0])]
                status = '200 OK'
                start_response(status, headers)
                return [b""]
        else:
            status = '405 Not Allowed'
            start_response(status, headers)
            return [b"Not Allowed"]
    
    # Default Endpoint
    status = '404 Not Found'
    start_response(status, headers)
    return [b"Not Found"]
    
with make_server('', 9292, simple_app) as httpd:
    print("Serving on port 9292...")
    httpd.serve_forever()

