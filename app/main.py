from fastapi import FastAPI

from app.api.samples import router as samples_router
from app.api.reports import router as reports_router


app = FastAPI(
    title="Precious Metal Samples API",
    description="API для системы учета проб драгоценных металлов",
    version="1.0.0"
)



app.include_router(samples_router)
app.include_router(reports_router)


@app.get("/")
def root():
    return {
        "message": "Precious Metal Samples API"
    }