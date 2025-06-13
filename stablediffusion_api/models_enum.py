from enum import Enum


class model_genre(Enum):

    GENERATE = "generate"

    UPSCALE = "upscale"

class generate_model(Enum):

    ULTRA = "ultra"

    LARGE = "3.5large"

    LARGE_TURBO = "3.5large_turbo"

    MEDIUM = "3.5medium"

    CORE = "core"

class upscale_model(Enum):

    CREATIVE = "creative"

    CONSERVATIVE = "conservative"

    FAST = "fast"