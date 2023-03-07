from timeit import default_timer

from fastapi import FastAPI, Response, Request

from configs.routes import DOCS_ROUTE, HEALTHCHECK_ROUTE, BASE_ROUTE, ROUTE_NOT_LOGGED
from src.routers import healthcheck_router, predict_router
from src.utils.logging_utils import logger

app = FastAPI(
    title='Base Model Serving',
    docs_url=DOCS_ROUTE,
    openapi_url=DOCS_ROUTE + '/openapi.json'
)


# Log time taken by the API
@app.middleware("http")
async def log_call_time(req: Request, call_next):

    start_time = default_timer()
    resp: Response = await call_next(req)
    end_time = default_timer()
    time_taken = end_time - start_time

    if req.url.path not in ROUTE_NOT_LOGGED:
        logger().warning(
            f"{req.method} {req.url.path}"
            f" | {resp.status_code}"
            f" | {time_taken:.4f}s")

    return resp


# Sub routes
app.include_router(healthcheck_router.router, prefix=HEALTHCHECK_ROUTE, tags=["healthcheck"])
app.include_router(predict_router.router, prefix=BASE_ROUTE, tags=["predict"])
