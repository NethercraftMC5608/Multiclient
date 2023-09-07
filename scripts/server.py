from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Create the upload directory if it doesn't exist
os.makedirs(upload_dir, exist_ok=True)

@app.get("/listinstances")
def list_files():
    folderz = []
    # Specify the directory you want to list folders from
    directory_path = './'
    # List all folders in the specified directory
    folders = [folder for folder in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, folder))]
    # Print the list of folders
    for folder in folders:
        folderz.append(folder)
    return folderz

@app.post("/upload")
async def upload_file(file: UploadFile):
    with open(os.path.join(upload_dir, file.filename), "wb") as f:
        f.write(file.file.read())
    return {"message": "File uploaded"}

@app.get("/download/{filename}")
def download_file(filename: str):
    file_path = os.path.join(upload_dir, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        return {"error": "File not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

