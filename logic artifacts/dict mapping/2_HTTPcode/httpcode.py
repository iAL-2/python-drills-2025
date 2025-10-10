def http_status(code):
    codes = {
        200: "OK",
        201: "Created",
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Not Found",
        500: "Internal Server Error",
        502: "Bad Gateway",
        503: "Service Unavailable"
    }
    return codes.get(code, "Unknown")

assert http_status(404) == "Not Found"
assert http_status(500) == "Internal Server Error"
assert http_status(999) == "Unknown"