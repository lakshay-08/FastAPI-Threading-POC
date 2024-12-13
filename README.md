# FastAPI Image Resizer API

## Author

**Abhilakshay Singh Pathania**

GitHub: lakshay-08 (https://github.com/lakshay-08)

This project provides a FastAPI-based image resizer API that allows users to upload multiple images, resize them to different sizes, and return the resized images as a ZIP file. The application uses multithreading to process the images concurrently for improved performance.

## Features

- Upload multiple images via a POST request.
- Resize images to multiple sizes (100x100, 500x500).
- Return the resized images in a ZIP file.
- **Threading support** to handle multiple files concurrently.
- **Logging** of important events and errors.
- **Unit tests** for the core functionality (coming soon).

## Requirements

- Python 3.7+
- FastAPI
- Pillow
- uvicorn (for serving the app)
- Logging (for capturing application logs)
- pytest (for unit tests)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/FastAPI-Threading-POC.git
   cd fastapi-image-resizer
   ```
2. Set up a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
### Running the App

To run the application locally using Uvicorn:
```
uvicorn app:app --reload
```
## API Endpoints

### POST /upload/

**Description**: Upload multiple image files to be resized and returned as a ZIP file.

**Request Format**: multipart/form-data

**Request Body**:
    ```
    files: (Multiple image files)
    ```

## Response:
    **Status Code**: 200 OK

    **Body**: A ZIP file containing the resized images.
    
    **Content-Type**: application/zip    

## Versioning

    Version: 0.0.1
    Release Date: 2024-12-13
    Next Major Release: 0.0.2