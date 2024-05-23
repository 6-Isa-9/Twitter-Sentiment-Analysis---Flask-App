Twitter Sentiment Analysis
This is a web application designed in Flask that accepts text or images as user input and analyzes its sentiment (it's affect on the world) and the emotions portrayed by it.

Requirements
Python 3.8+

Installation & Usage

Setting up the server
1. While in the main directory type "pip install -r requirements.txt" to install all the required python libraries.
2. Run the Flask app with the "flask run --debug" command.
3. Launching the server may take a while but once launched it should be good to go.

Using the server
1. Enter a tweet message or any text in the text input OR upload any image that is to be analyzed as input.
2. Click submit or upload to get the results below.

AI Models Used
- cardiffnlp/twitter-roberta-base-sentiment-latest
- SamLowe/roberta-base-go_emotions
- Salesforce/blip-image-captioning-large
