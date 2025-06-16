from fastapi import APIRouter
from ..common.convert_json import get_credit_info, get_request_body_info
from ..models_enum import model_genre,generate_model,upscale_model
from ..types.generate_type import GenerateRequest
from .generate_api import start_generate_
from ..common.save.save_local import save_image, save_config_json

router = APIRouter()

@router.post("/sd/generate/start_generate")
def start_generate(request:GenerateRequest ):
    result = start_generate_(request)
    filename = save_image(result["response"].content, request.model, request.genre)
    result["request_info"]["filename"] = filename
    save_config_json(result["request_info"], request.model,request.genre)

@router.get("/sd/generate/get_credit")
def get_credit(genre:model_genre, model:generate_model ):
    return get_credit_info(genre, model)

@router.get("/sd/generate/get_request_param_format")
def get_request_param_format(genre:model_genre, model:generate_model):
    return get_request_body_info(genre, model)

sd_generate = router