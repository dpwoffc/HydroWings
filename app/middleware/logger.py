from starlette.middleware.base import BaseHTTPMiddleware

class RequestLogger(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        body = await request.body()

        print("=" * 60)
        print(f"{request.method} {request.url.path}")

        for k, v in request.headers.items():
            print(f"{k}: {v}")

        if body:
            print()
            print(body.decode(errors="ignore"))

        response = await call_next(request)

        print(f"--> {response.status_code}")
        print("=" * 60)

        return response
