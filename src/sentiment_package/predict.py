"""Simple rule-based sentiment analyzer for practice."""

def predict(text: str) -> dict:
    """
    Predict sentiment of input text.
    
    Args:
        text: Input string
        
    Returns:
        dict with 'label' (pos/neg) and 'confidence' (0-1)
    """
    positive_words = ['good', 'great', 'excellent', 'amazing', 'love', 'best', 'awesome']
    negative_words = ['bad', 'terrible', 'awful', 'hate', 'worst', 'poor']
    
    text_lower = text.lower() # 转换为小写
    pos_count = sum(1 for word in positive_words if word in text_lower)
    neg_count = sum(1 for word in negative_words if word in text_lower)
    
    total = pos_count + neg_count
    if total == 0:
        return {'label': 'neutral', 'confidence': 0.5}
    
    pos_score = pos_count / total
    label = 'pos' if pos_score > 0.5 else 'neg'
    confidence = max(pos_score, 1 - pos_score)
    
    return {'label': label, 'confidence': confidence}

if __name__ == '__main__':
    # 测试
    test_texts = [
        "I love this product, it's amazing!",
        "This is terrible, I hate it.",
        "The weather is ok."
    ]
    for text in test_texts:
        result = predict(text)
        print(f"Text: {text}\nSentiment: {result}\n")