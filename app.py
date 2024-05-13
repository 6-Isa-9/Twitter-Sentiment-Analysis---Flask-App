from flask import Flask, render_template
from analyzer import analyze_emotion, analyze_sentiment, caption_image
from app_forms import UserInput
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'h#@hbJHB$@uygAHB!3137__yu_@_bl@(k_n!G@__JKH@#nlNAUBKJ~/AS,.69<>ASDfl..911,aSFOJ'
app.config['UPLOAD_FOLDER'] = 'static/imgs'

@app.route('/', methods=['GET', 'POST'])
def main():
    form = UserInput()

    # Tweet values to pass to HTML
    tweet_emotion = None
    tweet_sentiment = None
    tweet_text = None
    image = None

    if form.validate_on_submit():
        # Text submission
        if form.hidden.data == "text":
            if form.text.data != '':
                # Analyze sentiment of tweet text
                tweet_sentiment = analyze_sentiment(form.text.data)
                # Calculating top 3 emotions with %
                all_emotions = analyze_emotion(form.text.data)
                tweet_emotion = []
                other_total = 0     
                for i in range(0, len(all_emotions) - 1):
                    if i <= 2:
                        tweet_emotion.append((all_emotions[i][0].capitalize(), round(all_emotions[i][1] * 100, 2)))
                    else:
                        other_total += all_emotions[i][1]
                tweet_emotion.append(('Other', round(other_total * 100, 2)))
                # Setting tweet_text to user's text
                tweet_text = form.text.data

        # Image submission
        if form.hidden.data == "image":
            if form.image.data.filename != '':
                # Removing older image if exists
                upload_path = 'static/imgs'
                if os.path.exists(upload_path) and os.path.isdir(upload_path):
                    for filename in os.listdir(upload_path):
                        file_path = os.path.join(upload_path, filename)
                        if os.path.isfile(file_path):
                            os.remove(file_path)

                # Saving the image
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], form.image.data.filename)
                form.image.data.save(image_path)
                
                # Caption the image
                caption = caption_image(image_path)
                
                # Analyze sentiment of image
                tweet_sentiment = analyze_sentiment(caption)
                
                # Analyze emotion portrayed by image
                all_emotions = analyze_emotion(caption)
                tweet_emotion = []
                other_total = 0     
                for i in range(0, len(all_emotions) - 1):
                    if i <= 2:
                        tweet_emotion.append((all_emotions[i][0].capitalize(), round(all_emotions[i][1] * 100, 2)))
                    else:
                        other_total += all_emotions[i][1]
                tweet_emotion.append(('Other', round(other_total * 100, 2)))

                # Setting tweet_text to image caption and passing image path
                tweet_text = "Image caption: " + caption
                image = image_path

    return render_template("main.html", form = form, sentiment = tweet_sentiment, emotion = tweet_emotion, tweet = tweet_text, image = image)

if __name__ == '__main__':
    app.run(debug=True)


