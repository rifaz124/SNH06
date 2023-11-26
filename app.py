from flask import Flask, render_template, request, flash, redirect, url_for
from transformers import pipeline

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Add a secret key for flash messages

# Load sentiment analysis pipeline
sentiment_analysis = pipeline("sentiment-analysis")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    try:
        text_to_analyze = request.form['feedback']
        result = sentiment_analysis(text_to_analyze)[0]

        return render_template('index.html', feedback=text_to_analyze, sentiment=result['label'], confidence=result['score'])

    except Exception as e:
        flash(f"An error occurred: {str(e)}", 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
