from fastapi import APIRouter,status

router=APIRouter(prefix="/users",tags=["/users"])

@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    summary="Regiser for user",
    response_model=""
)
async def register():
    pass