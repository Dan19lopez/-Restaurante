from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class Recommender:
    def __init__(self, items):
        self.items = items
        corpus = [
            (it.get("description") or "") + " " + (it.get("ingredients") or "")
            for it in items
        ]

        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.matrix = self.vectorizer.fit_transform(corpus)

    def recommend(self, item_id, top_n=5):
        idx = next(i for i, it in enumerate(self.items) if it["id"] == item_id)

        similarities = linear_kernel(
            self.matrix[idx:idx+1], self.matrix
        ).flatten()

        indexes = similarities.argsort()[::-1]
        indexes = [i for i in indexes if i != idx]

        return [self.items[i] for i in indexes[:top_n]]
