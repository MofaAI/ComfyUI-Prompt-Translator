from .node.translator import *

__version__ = "1.0.0"

NODE_CLASS_MAPPINGS = {
    "PromptTextTranslation": PromptTextTranslation,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptTextTranslation": "文本翻译",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
