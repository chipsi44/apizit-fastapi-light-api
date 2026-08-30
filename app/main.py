import asyncio

from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field

SLOW_RESPONSE_SECONDS = 80


class EchoRequest(BaseModel):
    message: str = Field(min_length=1)
    count: int = Field(strict=True)


def create_app() -> FastAPI:
    application = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

    @application.get("/health")
    async def health():
        return {"status": "ok"}

    @application.get("/info")
    async def info():
        return {"framework": "fastapi", "profile": "light"}

    @application.post("/echo")
    async def echo(payload: EchoRequest):
        return {"received": {"message": payload.message, "count": payload.count}}

    @application.get("/items/{item_id}")
    async def item(
        item_id: int = Path(ge=1),
        include_details: bool = Query(default=False),
    ):
        response = {"item_id": item_id, "include_details": include_details}
        if include_details:
            response["details"] = f"Reference item {item_id}"
        return response

    @application.get("/slow")
    async def slow():
        await asyncio.sleep(SLOW_RESPONSE_SECONDS)
        return {"delay_seconds": SLOW_RESPONSE_SECONDS, "status": "completed"}

    return application


app = create_app()
