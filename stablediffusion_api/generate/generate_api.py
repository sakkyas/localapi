from ..types.generate_type import GenerateRequest
from typing import Any
from ..models_enum import model_genre,generate_model
from ..common.convert_json import get_url_info,get_auth_key
import requests

def set_headers(auth_key:str) -> dict[str, str]:
    return {
        "authorization": auth_key,
        "accept": "image/*"
    }

def set_files(img2img_info:str) -> dict[str, str]:
    if not img2img_info:
        return { "none":'' }
    else:
        return {"image": ('images.jpg', img2img_info, "image/jpeg")}

def set_data(request:GenerateRequest) -> dict[str, str]:
    target_keys = ["required_param","standard_param"]
    data = {}
    data.update(request.required_param)
    data.update(request.standard_param)
    return data 

def start_generate_(request:GenerateRequest) :

    access_url = get_url_info(request.genre,request.model)
    headers = set_headers(get_auth_key())
    if not request.is_img2img:
        files = set_files(img2img_info = None)
    else:
        files = set_files(request.required_param["image"])
    data = set_data(request)
    response = requests.post(
        access_url,
        headers = headers,
        files = files,
        data = data
    )
    if response.status_code == 200:
        return {
            "response": response,
            "request_info":{
                "url": access_url,
                "headers": headers,
                "files": files,
                "data": data
            }
        }
    else:
        raise Exception(str(response.json()))

