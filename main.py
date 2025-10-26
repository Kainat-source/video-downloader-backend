# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import FileResponse
# from fastapi.staticfiles import StaticFiles
# from pydantic import BaseModel
# import yt_dlp
# import os
# import uuid

# app = FastAPI(title="Adeel Video Downloader")

# # ✅ CORS setup
# origins = [
#     "http://localhost:5173",
#     "https://video-downloader-production.up.railway.app",
#     "https://prodownloadfrontend.vercel.app",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # ✅ Serve frontend if built
# # frontend_dir = os.path.join(os.path.dirname(__file__), "../frontend/dist")
# # if os.path.exists(frontend_dir):
# #     app.mount("/static", StaticFiles(directory=frontend_dir), name="static")


# @app.get("/")
# def home():
#     return {"message": "Adeel Video Downloader API is running 🚀"}


# # ✅ Request body
# class VideoRequest(BaseModel):
#     url: str


# @app.post("/download")
# def download_video(request: VideoRequest):
#     url = request.url.strip()
#     if not url:
#         raise HTTPException(status_code=400, detail="No URL provided")

#     # Create downloads folder
#     os.makedirs("downloads", exist_ok=True)

#     # Unique filename
#     output_filename = f"{uuid.uuid4()}.mp4"
#     output_path = os.path.join("downloads", output_filename)

#     # ✅ yt_dlp options
#     ydl_opts = {
#         "outtmpl": output_path,
#         "format": "best[ext=mp4]/best",  # Safe for YouTube without ffmpeg
#         "quiet": True,
#         "noplaylist": True,  # Avoid downloading playlists accidentally
#     }

#     try:
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([url])
#     except Exception as e:
#         print("YT_DLP ERROR:", str(e))  # Log for debugging
#         raise HTTPException(status_code=400, detail=f"Download failed: {str(e)}")

#     if not os.path.exists(output_path):
#         raise HTTPException(status_code=400, detail="Video download failed")

#     return FileResponse(
#         path=output_path,
#         filename="video.mp4",
#         media_type="video/mp4",
#     )


# # # Serve frontend for other routes
# # @app.get("/{full_path:path}")
# # def serve_react_app(full_path: str):
# #     index_path = os.path.join(frontend_dir, "index.html")
# #     if os.path.exists(index_path):
# #         return FileResponse(index_path)
# #     else:
# #         return {"message": "Frontend not built yet"}




#  mine real code
# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import FileResponse
# from fastapi.staticfiles import StaticFiles
# from pydantic import BaseModel
# import yt_dlp
# import os
# import uuid

# app = FastAPI(title="Adeel Video Downloader")

# # ✅ CORS setup (for local + production)
# origins = [
#     "http://localhost:5173",
#     "https://video-downloader-production.up.railway.app",
#     "https://prodownloadfrontend.vercel.app",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # ✅ Serve the built React frontend
# frontend_dir = os.path.join(os.path.dirname(__file__), "../frontend/dist")
# if os.path.exists(frontend_dir):
#     app.mount("/static", StaticFiles(directory=frontend_dir), name="static")

# @app.get("/")
# def home():
#     """Health check route"""
#     return {"message": "Adeel Video Downloader API is running 🚀"}

# # ✅ Define request body for POST
# class VideoRequest(BaseModel):
#     url: str

# @app.post("/download")
# def download_video(request: VideoRequest):
#     """
#     Download a video from YouTube, TikTok, Instagram, or Facebook
#     """
#     try:
#         url = request.url.strip()
#         if not url:
#             raise HTTPException(status_code=400, detail="No URL provided")

#         # ✅ Create downloads directory
#         os.makedirs("downloads", exist_ok=True)

#         # ✅ Generate unique filename
#         output_filename = f"{uuid.uuid4()}.mp4"
#         output_path = os.path.join("downloads", output_filename)

#         # ✅ Detect platform for custom handling
#         ydl_opts = {
#             'outtmpl': output_path,
#             'format': 'best[ext=mp4]/best',
#             'quiet': True,
#         }

#         # ✅ Add YouTube-specific options
#         if "youtube.com" in url or "youtu.be" in url:
#             ydl_opts.update({
#                 'format': 'bestvideo+bestaudio/best',
#                 'merge_output_format': 'mp4',
#             })

#         # ✅ Download video using yt_dlp
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([url])

#         # ✅ Return video file
#         return FileResponse(
#             path=output_path,
#             filename="video.mp4",
#             media_type="video/mp4",
#         )

#     except Exception as e:
#         raise HTTPException(status_code=400, detail=f"Download failed: {str(e)}")


# # ✅ Serve frontend for all other routes (after build)
# @app.get("/{full_path:path}")
# def serve_react_app(full_path: str):
#     index_path = os.path.join(frontend_dir, "index.html")
#     if os.path.exists(index_path):
#         return FileResponse(index_path)
#     else:
#         return {"message": "Frontend not built yet"}






# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import FileResponse
# from fastapi.staticfiles import StaticFiles
# from pydantic import BaseModel
# import yt_dlp
# import os
# import uuid

# app = FastAPI(title="Adeel Video Downloader")

# # ✅ CORS setup (for local + production)
# origins = [
#     "http://localhost:5173",
#     "https://video-downloader-production.up.railway.app",
#     "https://prodownloadfrontend.vercel.app",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # ✅ Serve the built React frontend
# frontend_dir = os.path.join(os.path.dirname(__file__), "../frontend/dist")
# if os.path.exists(frontend_dir):
#     app.mount("/static", StaticFiles(directory=frontend_dir), name="static")

# @app.get("/")
# def home():
#     """Health check route"""
#     return {"message": "Adeel Video Downloader API is running 🚀"}

# # ✅ Define request body for POST
# class VideoRequest(BaseModel):
#     url: str

# @app.post("/download")
# def download_video(request: VideoRequest):
#     """
#     Download a video from YouTube, TikTok, Instagram, or Facebook
#     """
#     try:
#         url = request.url.strip()
#         if not url:
#             raise HTTPException(status_code=400, detail="No URL provided please provide a url")

#         # ✅ Create downloads directory
#         os.makedirs("downloads", exist_ok=True)

#         # ✅ Generate unique filename
#         output_filename = f"{uuid.uuid4()}.mp4"
#         output_path = os.path.join("downloads", output_filename)

#         # ✅ Detect platform for custom handling
#         ydl_opts = {
#             'outtmpl': output_path,
#             'format': 'best[ext=mp4]/best',
#             'quiet': True,
#         }

#         # ✅ Add YouTube-specific options
#         if "youtube.com" in url or "youtu.be" in url:
#             ydl_opts.update({
#                 'format': 'bestvideo+bestaudio/best',
#                 'merge_output_format': 'mp4',
#             })

#         # ✅ Download video using yt_dlp
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([url])

#         # ✅ Return video file
#         return FileResponse(
#             path=output_path,
#             filename="video.mp4",
#             media_type="video/mp4",
#         )

#     except Exception as e:
#         raise HTTPException(status_code=400, detail=f"Download failed: {str(e)}")


# # ✅ Serve frontend for all other routes (after build)
# @app.get("/{full_path:path}")
# def serve_react_app(full_path: str):
#     index_path = os.path.join(frontend_dir, "index.html")
#     if os.path.exists(index_path):
#         return FileResponse(index_path)
#     else:
#         return {"message": "Frontend not built yet"}










# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import FileResponse, RedirectResponse
# from fastapi.staticfiles import StaticFiles
# from pydantic import BaseModel
# import yt_dlp
# import os
# import uuid
# import requests

# app = FastAPI(title="Adeel Video Downloader")

# # ✅ CORS setup
# origins = [
#     "http://localhost:5173",
#     "https://video-downloader-production.up.railway.app",
#     "https://prodownloadfrontend.vercel.app",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# @app.get("/")
# def home():
#     return {"message": "Adeel Video Downloader API is running 🚀"}


# # ✅ Request body
# class VideoRequest(BaseModel):
#     url: str


# @app.post("/download")
# def download_video(request: VideoRequest):
#     url = request.url.strip()
#     if not url:
#         raise HTTPException(status_code=400, detail="No URL provided")

#     # ✅ If link is from YouTube → use RapidAPI instead of yt_dlp
#     if "youtube.com" in url or "youtu.be" in url:
#         api_url = "https://ytstream-download-youtube-videos.p.rapidapi.com/dl"
#         headers = {
#             "x-rapidapi-key": os.getenv("b034da9d39mshd5bd338c4c32e7ap1198c1jsn98d4076fbf1d"),
#             "x-rapidapi-host": "ytstream-download-youtube-videos.p.rapidapi.com"
#         }

#         # Extract YouTube video ID
#         if "v=" in url:
#             video_id = url.split("v=")[-1].split("&")[0]
#         else:
#             video_id = url.split("/")[-1]

#         params = {"id": video_id}

#         try:
#             res = requests.get(api_url, headers=headers, params=params, timeout=15)
#             if res.status_code != 200:
#                 raise HTTPException(status_code=400, detail="RapidAPI YouTube request failed")

#             data = res.json()

#             # Check if formats are available
#             if not data or "formats" not in data or len(data["formats"]) == 0:
#                 raise HTTPException(status_code=400, detail="No downloadable formats found")

#             # Pick the highest quality mp4 format
#             mp4_formats = [f for f in data["formats"] if f.get("type") == "mp4"]
#             if not mp4_formats:
#                 mp4_formats = data["formats"]

#             best_format = mp4_formats[0]
#             download_link = best_format.get("url")

#             if not download_link:
#                 raise HTTPException(status_code=400, detail="No valid download URL found")

#             # ✅ Return redirect so frontend downloads it directly
#             return RedirectResponse(download_link)

#         except Exception as e:
#             print("YouTube RapidAPI Error:", str(e))
#             raise HTTPException(status_code=400, detail=f"YouTube download failed: {str(e)}")

#     # ✅ For other platforms → use yt_dlp
#     os.makedirs("downloads", exist_ok=True)

#     output_filename = f"{uuid.uuid4()}.mp4"
#     output_path = os.path.join("downloads", output_filename)

#     ydl_opts = {
#         "outtmpl": output_path,
#         "format": "best[ext=mp4]/best",
#         "quiet": True,
#         "noplaylist": True,
#     }

#     try:
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([url])
#     except Exception as e:
#         print("YT_DLP ERROR:", str(e))
#         raise HTTPException(status_code=400, detail=f"Download failed: {str(e)}")

#     if not os.path.exists(output_path):
#         raise HTTPException(status_code=400, detail="Video download failed")

#     return FileResponse(
#         path=output_path,
#         filename="video.mp4",
#         media_type="video/mp4",
#     )




from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, FileResponse
import yt_dlp
import os
import uuid
import json
import asyncio
import threading

app = FastAPI(title="Social Video Downloader")

# Allowed origins
origins = [
    "http://localhost:5173",
    "https://prodownloadfrontend.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "✅ API running"}

@app.get("/download")
async def download_video(url: str = Query(...)):
    if not url:
        raise HTTPException(status_code=400, detail="URL required")

    os.makedirs("downloads", exist_ok=True)
    output_filename = f"{uuid.uuid4()}.mp4"
    output_path = os.path.join("downloads", output_filename)

    progress_state = {"progress": 0.0, "done": False, "error": None}

    # 🟢 yt_dlp progress hook
    def progress_hook(d):
        if d["status"] == "downloading":
            percent_str = d.get("_percent_str", "0.0%").replace("%", "")
            try:
                progress_state["progress"] = float(percent_str)
            except:
                progress_state["progress"] = 0.0
        elif d["status"] == "finished":
            progress_state["progress"] = 100.0
            progress_state["done"] = True

    ydl_opts = {
        "outtmpl": output_path,
        "format": "best[ext=mp4]/best",
        "progress_hooks": [progress_hook],
        "quiet": True,
        "noplaylist": True,
        "merge_output_format": "mp4",
        "cookies": "cookies.txt" if os.path.exists("cookies.txt") else None,
    }

    # 🔄 Download in a separate thread
    def run_download():
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except Exception as e:
            progress_state["error"] = str(e)

    threading.Thread(target=run_download, daemon=True).start()

    # 🧩 SSE event stream
    async def event_stream():
        last_progress = -1
        while True:
            if progress_state["error"]:
                yield f"data: {json.dumps({'error': progress_state['error']})}\n\n"
                break

            progress = progress_state["progress"]
            if progress != last_progress:
                yield f"data: {json.dumps({'progress': progress})}\n\n"
                last_progress = progress

            if progress_state["done"]:
                yield f"data: {json.dumps({'progress': 100, 'done': True, 'file': output_filename})}\n\n"
                break

            await asyncio.sleep(0.3)  # small delay for smoother progress

    headers = {
        "Cache-Control": "no-cache",
        "X-Accel-Buffering": "no",  # important for Nginx/proxy
        "Content-Type": "text/event-stream",
        "Connection": "keep-alive",
        "Access-Control-Allow-Origin": "*",  # optional for dev
    }

    return StreamingResponse(event_stream(), headers=headers, media_type="text/event-stream")


@app.get("/file/{filename}")
def get_file(filename: str):
    file_path = os.path.join("downloads", filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path, filename="video.mp4", media_type="video/mp4")
