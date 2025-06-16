import os
import re
import json 
import requests
from datetime import datetime
from ...models_enum import model_genre,generate_model,upscale_model
from pathlib import Path
from typing import Any

SAVE_BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

def make_filename(extension: str = "jpeg") -> str:

    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    return f"{date_str}.{extension}"


def add_image_info_list(request_info: Any, file_path: str):
    writing_info = {
        "file_name": request_info["filename"],
        "request_info": {
            "files": request_info["files"],
            "data": request_info["data"],
        }
    }

    # ファイルがなければ空リストを作成
    if not os.path.isfile(file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False, indent=2)

    # 既存データを読み込み
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            if not isinstance(data, list):
                data = []
        except json.JSONDecodeError:
            data = []

    # 新しい情報を追加
    data.append(writing_info)

    # ファイルに書き戻す
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def save_image(content: bytes, model: generate_model, genre: model_genre) -> str:

    save_dir = os.path.join(SAVE_BASE_DIR, "output", genre.name, model.name)

    os.makedirs(save_dir, exist_ok=True)

    filename = make_filename()

    file_path = os.path.join(save_dir, filename)

    with open(file_path, 'wb') as f:

        f.write(content)

    print(f"画像を保存しました: {file_path}")
    
    return filename



def save_config_json(request_info: any, model: generate_model, genre: model_genre) -> None:

    save_dir = os.path.join(SAVE_BASE_DIR, "output", genre.name, model.name)

    file_path = os.path.join(save_dir, 'image_info_list.json')

    add_image_info_list(request_info, file_path)

    print(f"設定情報を保存しました: {file_path}")
