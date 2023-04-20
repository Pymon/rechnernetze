HTTP_REQUEST = "GET /edu/2022/rn HTTP/1.0"


def parse_request(request):
    method, uri, protocol = HTTP_REQUEST.split()
    return {"method": method, "uri": uri, "protocol": protocol}


print(parse_request(HTTP_REQUEST))
