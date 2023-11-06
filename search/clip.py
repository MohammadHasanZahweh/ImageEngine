import open_clip
import torch

from ImageEngine.settings import AI_MODELS_PATH
# from PIL import Image

model,preprocess,tokenizer=None,None,None

def getModel():
    global model,preprocess,tokenizer
    if model is None or preprocess is None:
        model, _, preprocess = open_clip.create_model_and_transforms('ViT-bigG-14', pretrained=AI_MODELS_PATH+"\\CLIP-G\\open_clip_pytorch_model.bin")
    if tokenizer is None:
        tokenizer = open_clip.get_tokenizer('ViT-bigG-14')
    return model,preprocess,tokenizer

def test_similarity(image,text):
    model,preprocess,tokenizer=getModel()
    
    image = preprocess(image).unsqueeze(0)
    text = tokenizer(text)
    
    with torch.no_grad():
        image_features = model.encode_image(image)
        text_features = model.encode_text(text)
        image_features /= image_features.norm(dim=-1, keepdim=True)
        text_features /= text_features.norm(dim=-1, keepdim=True)

        text_probs = (100.0 * image_features @ text_features.T).softmax(dim=-1)
        return text_probs

def encode_image(image):
    model,preprocess,tokenizer=getModel()
    image = preprocess(image).unsqueeze(0)
    with torch.no_grad():
        image_features = model.encode_image(image)
        image_features /= image_features.norm(dim=-1, keepdim=True)
        return image_features[0]

def encode_text(text):
    model,preprocess,tokenizer=getModel()
    text = tokenizer(text)
    with torch.no_grad():
        text_features = model.encode_text(text)
        return text_features[0]

