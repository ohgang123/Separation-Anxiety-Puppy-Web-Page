from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# CORS 허용 (라즈베리파이 등 외부에서 접근 가능)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 예시: 라즈베리파이에서 불안 감지 결과 전송
@app.post("/anxiety")
async def receive_anxiety(request: Request):
    data = await request.json()
    # 예: {"status": "anxious", "time": "2025-07-17 10:00:00"}
    # 여기서 파일 저장, DB 기록, 실시간 알림 등 처리 가능
    print("[라즈베리파이] 불안 감지 데이터 수신:", data)
    return JSONResponse(content={"result": "ok"})

# 예시: 라즈베리파이에서 영상 프레임 전송 (base64 등)
# @app.post("/frame")
# async def receive_frame(request: Request):
#     data = await request.json()
#     # 예: {"frame": "base64string", "time": "..."}
#     return JSONResponse(content={"result": "ok"})

# 예시: 실시간 상태 조회
@app.get("/status")
async def get_status():
    # 실제로는 최근 데이터, 알람 상태 등 반환
    return JSONResponse(content={"status": "ok", "msg": "서버 정상 작동 중"})

if __name__ == "__main__":
    uvicorn.run("route:app", host="0.0.0.0", port=8000, reload=True)
