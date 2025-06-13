import os
import json
from ..models_enum import model_genre,generate_model,upscale_model


def load_config(jsonfile='sd_info.json'):
    
    #このファイルの親のパスを指定
    current_dir = os.path.dirname(os.path.abspath(__file__))
    #current_dirのもう一個親のパスを指定
    parent_dir = os.path.dirname(current_dir)
    #仮引数のjsonfileの名前を足して、jsonファイルまでのパスを作成
    path = os.path.join(parent_dir,jsonfile)

    with open(path, 'r') as f:
        return json.load(f)


def get_all_info(genre: model_genre ,model: generate_model) -> str:
    return load_config()["stablediffusion"][genre.value][model.value]

def get_credit_info(genre: model_genre ,model: generate_model) -> int:
    return get_all_info(genre,model)["credit"]

def get_request_body_info(genre: model_genre, model:generate_model) -> dict:
    result = get_all_info(genre, model)
    request_body = result["request_body"].copy()
    
    request_body["img2img"] = result.get("img2img", False)
    request_body["txt2img"] = result.get("txt2img", False)
    
    return request_body

def get_url_info(genre: model_genre ,model: generate_model) -> str:
    return load_config()["stablediffusion"][genre.value][model.value]["url"]
