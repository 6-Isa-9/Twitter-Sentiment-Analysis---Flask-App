from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoConfig, BlipProcessor, BlipForConditionalGeneration
from scipy.special import softmax
import numpy as np
from PIL import Image

# Model Names
sentiment_model_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"
emotion_model_name = "SamLowe/roberta-base-go_emotions"

# Initializing Models

# Sentiment Model
sentiment_tokenizer = AutoTokenizer.from_pretrained(sentiment_model_name)
sentiment_model = AutoModelForSequenceClassification.from_pretrained(sentiment_model_name)
sentiment_config = AutoConfig.from_pretrained(sentiment_model_name)

# Emotion Model
emotion_tokenizer = AutoTokenizer.from_pretrained(emotion_model_name)
emotion_model = AutoModelForSequenceClassification.from_pretrained(emotion_model_name)
emotion_config = AutoConfig.from_pretrained(emotion_model_name)

# Image Caption Model
caption_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
caption_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")


# Function to structure output
def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)


# Sentiment Analyzer
def analyze_sentiment(text):
    text = preprocess(text)
    encoded_input = sentiment_tokenizer(text, return_tensors='pt')
    output = sentiment_model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    ranking = np.argsort(scores)
    ranking = ranking[::-1]
    results = []
    for i in range(scores.shape[0]):
        label = sentiment_config.id2label[ranking[i]]
        score = scores[ranking[i]]
        results.append((label, round(float(score), 4)))
    return results


# Emotion Analyzer
def analyze_emotion(text):
    text = preprocess(text)
    encoded_input = emotion_tokenizer(text, return_tensors='pt')
    output = emotion_model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    ranking = np.argsort(scores)
    ranking = ranking[::-1]
    results = []
    for i in range(scores.shape[0]):
        label = emotion_config.id2label[ranking[i]]
        score = scores[ranking[i]]
        results.append((label, round(float(score), 4)))
    return results


# Image Captioner
def caption_image(image):
    raw_image = Image.open(image).convert('RGB')

    inputs = caption_processor(raw_image, return_tensors='pt')
    out = caption_model.generate(**inputs)

    return caption_processor.decode(out[0], skip_special_tokens=True)