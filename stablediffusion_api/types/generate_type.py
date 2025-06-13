from ..models_enum import model_genre,generate_model,upscale_model
from pydantic import BaseModel
from typing import Any

class GenerateRequest(BaseModel):
    genre: model_genre
    model: generate_model
    is_img2img: bool
    required_param: dict[str, Any]
    standard_param: dict[str, Any]