from fastapi import APIRouter

router = APIRouter()


@router.head("", include_in_schema=False)
def healthcheck_head():
    return


@router.get("", include_in_schema=False)
def healthcheck():
    return {
        "status": "Live"
    }
