from fastapi import APIRouter
from ..common.convert_json import get_credit_info, get_request_body_info
from ..models_enum import model_genre,generate_model,upscale_model
from ..types.generate_type import GenerateRequest

router = APIRouter()

@router.post("/sd/generate/start_generate")
def start_generate(request:GenerateRequest ):
    if not request.is_img2img :
        start_txt2img(request)
    else:        
        return request

@router.get("/sd/generate/get_credit")
def get_credit(genre:model_genre, model:generate_model ):
    return get_credit_info(genre, model)

@router.get("/sd/generate/get_request_param_format")
def get_request_param_format(genre:model_genre, model:generate_model):
    return get_request_body_info(genre, model)

sd_generate = router