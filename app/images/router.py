from fastapi import APIRouter, UploadFile
import shutil


router = APIRouter(
    prefix="/images",
    tags=["Upload Pictures"]
)

@router.post("/hotels")
async def add_hotel_images(name: int, file: UploadFile):
    with open(f"static/images/{name}.webp", "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)