from fastapi import FastAPI, File, UploadFile
from concurrent.futures import ThreadPoolExecutor
import zipfile
from fastapi.responses import FileResponse
from PIL import Image
import io
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',  
    filemode='w',        
)

logger = logging.getLogger(__name__)
app = FastAPI()
executor = ThreadPoolExecutor(max_workers=5)

def process_image(file: bytes):
    logger.debug("process_image function started")
    with Image.open(io.BytesIO(file)) as img:
        sizes = [(100, 100), (500, 500)]
        resized_images = {}
        for size in sizes:
            img_resized = img.resize(size)
            buf = io.BytesIO()
            img_resized.save(buf, format="JPEG")
            resized_images[size] = buf
        logger.debug("process_image function ended")    
        return resized_images


@app.post("/upload/")
async def upload_images(files: list[UploadFile] = File(...)):
    logger.debug("upload/ api called")
    all_resized_images = {}

    for file in files:
        content = await file.read()
        future = executor.submit(process_image, content)
        resized_images = future.result()
        all_resized_images[file.filename] = resized_images

    zip_filename = "resized_images.zip"
    with zipfile.ZipFile(zip_filename, "w") as zipf:
        for filename, images in all_resized_images.items():
            for size, image_buf in images.items():
                zipf.writestr(f"{filename}_image_{size[0]}x{size[1]}.jpg", image_buf.getvalue())
    logger.debug("api response return")
    return FileResponse(zip_filename, media_type="application/zip", filename=zip_filename)
