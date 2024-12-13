# FastAPI Image Resizer API

This project provides a FastAPI-based image resizer API that allows users to upload multiple images, resize them to different sizes, and return the resized images as a ZIP file. The application uses multithreading to process the images concurrently for improved performance.

## Features

- Upload multiple images via a POST request.
- Resize images to multiple sizes (100x100, 500x500).
- Return the resized images in a ZIP file.
- **Threading support** to handle multiple files concurrently.
- **Logging** of important events and errors (coming soon).
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
   git clone https://github.com/your-username/fastapi-image-resizer.git
   cd fastapi-image-resizer
   ```
2. Set up a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
