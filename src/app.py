from fastapi import FastAPI, Request, Response, Depends

from configs.routes import DOCS_ROUTE, HEALTHCHECK_ROUTE, BASE_ROUTE
from src.routers import healthcheck_router, predict_router


app = FastAPI(
    title='Base Model Serving',
    docs_url=DOCS_ROUTE,
    openapi_url=DOCS_ROUTE + '/openapi.json'
)


# Sub routes
app.include_router(healthcheck_router.router, prefix=HEALTHCHECK_ROUTE, tags=["healthcheck"])
app.include_router(predict_router.router, prefix=BASE_ROUTE, tags=["predict"])
