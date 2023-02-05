class CountVectorizer:
    def __init__(self, ngram_size):
        self.unique_set = None
        self.ngram_size = ngram_size

    def fit(self, corpus):
        self.unique_set = set()
        for word in corpus:
            for point1, point2 in zip(range(0, len(word) - self.ngram_size + 1), range(self.ngram_size, len(word) + 1)):
                self.unique_set.add(word[point1:point2])
        self.unique_set = sorted(list(self.unique_set))


    def pre_transform(self, corpus):
        count_dictionary_word = dict.fromkeys(corpus)
        for word in corpus:
            count_dictionary_word[word] = {}
            for point1, point2 in zip(range(0, len(word) - self.ngram_size + 1), range(self.ngram_size, len(word) + 1)):
                count_dictionary_word[word][word[point1:point2]] = count_dictionary_word[word].get(word[point1:point2],
                                                                                                   0) + 1
        return count_dictionary_word

    def transform(self, corpus):
        word_dict = self.pre_transform(corpus)
        return [[word_dict[word_key].get(key, 0) for key in self.unique_set] for word_key in
                corpus]

    def fit_transform(self, corpus):
        self.fit(corpus)
        return self.transform(corpus)