import json
from textblob import TextBlob

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        text = body.get('text', '')

        if not text:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Text input is required'})
            }

        sentiment_score = TextBlob(text).sentiment.polarity

        result = {
            'text': text,
            'sentiment_score': sentiment_score,
            'sentiment_label': (
                "positive" if sentiment_score > 0 else
                "negative" if sentiment_score < 0 else
                "neutral"
            )
        }

        return {
            'statusCode': 200,
            'body': json.dumps(result)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
