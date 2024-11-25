import spacy

nlp = spacy.load("en_core_web_md")

class EmbeddingGenerator:
    def __init__(self):
        self.processed_cache = {}
    
    def get_embeddings(self, word_list):
        embeddings = []
        for word in word_list:
            if word in self.processed_cache:
                embeddings.append(self.processed_cache[word])
            else:
                vector = nlp(word).vector
                self.processed_cache[word] = vector
                embeddings.append(vector)
        return embeddings