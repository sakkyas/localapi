from fastapi import FastAPI
from stablediffusion_api.generate.main import sd_generate

from fastapi.middleware.cors import CORSMiddleware #CORS用

app = FastAPI()

#CORS用
# 許可したいオリジンをリストで指定
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    # 必要に応じて他のオリジンも追加可能
]

#CORS用
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # ここに許可したいオリジンを入れる
    allow_credentials=True,
    allow_methods=["*"],  # 全てのHTTPメソッドを許可
    allow_headers=["*"],  # 全てのヘッダーを許可
)

app.include_router(sd_generate)