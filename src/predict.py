def predict_news(text):

    suspicious_words = [
        "shocking",
        "secret",
        "miracle",
        "exposed",
        "breaking",
        "unbelievable",
        "conspiracy"
    ]

    score = 0

    for word in suspicious_words:
        if word in text.lower():
            score += 1

    credibility = max(
        100 - score * 15,
        20
    )

    if score >= 3:

        prediction = "Likely Fake"

        reason = (
            "The article contains several "
            "sensational or clickbait terms."
        )

    else:

        prediction = "Likely Real"

        reason = (
            "No major fake-news indicators "
            "were detected."
        )

    return {
        "prediction": prediction,
        "credibility_score": credibility,
        "reason": reason
    }
