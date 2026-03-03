import pytest
from sentiment_package.predict import predict

def test_positive_sentiment():
    result = predict("I love this amazing product!")
    assert result['label'] == 'pos'
    assert result['confidence'] > 0.5

def test_negative_sentiment():
    result = predict("This is terrible, I hate it.")
    assert result['label'] == 'neg'
    assert result['confidence'] > 0.5

def test_neutral():
    result = predict("The weather is ok.")
    assert result['label'] == 'neutral'
    assert result['confidence'] == 0.5