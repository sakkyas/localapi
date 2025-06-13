from ..types.generate_type import GenerateRequest


def set_headers(auth_key:str) -> Dict[str, str]:
    return {
        "authorization": auth_key,
        "accept": "image/*"
    }

def set_files(img2img_info:str) -> Dict[str, str]:
    if not img2img_info:
        return { "none":'' }
    else:
        return {"image": ('images.jpg', img2img_info, "image/jpeg")}

def set_data(request:GenerateRequest) -> Dict[str, str]:
    

    

def start_txt2img(request:GenerateRequest) :

    headers = set_headers()
    if not request.is_img2img:
        files = set_files(img2img_info = None)
    else
        files = set_files(request.required_param["image"])

    data = set_data(request)

    response = requsets.post(
        access_url,
        headers,
        files,
        data
    )
    if response.status_code == 200:
        return response
    else:
        raise Exception(str(response.json()))

