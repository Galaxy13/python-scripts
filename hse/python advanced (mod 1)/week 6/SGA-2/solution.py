import argparse
import json
from copy import copy


class InvertedIndex:
    def __init__(self, word_to_docs_mapping):
        self.invert_index = word_to_docs_mapping

    def query(self, words: list) -> set:
        set_for_all_words = copy(self.invert_index.get(words[0], set()))
        for word in words:
            set_for_all_words.intersection_update(self.invert_index.get(word, set()))
            if not set_for_all_words:
                return set()
        return set_for_all_words  # set of common article_id for all words

    def dump(self, filepath):
        # optimizing sets to json format
        def serialize_set(obj):
            if isinstance(obj, set):
                return list(obj)

        with open(filepath, 'w') as outfile:
            json.dump(self.invert_index, outfile, default=serialize_set)

    @classmethod
    def load(cls, filepath):
        with open(filepath, 'r') as readfile:
            data = json.load(readfile)
        return InvertedIndex({word: set(ids) for word, ids in data.items()})  # InvertedIndex object


def load_document(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        doc_list = []
        for line in f:
            doc_list.append(line.split('\t', 1))
    return {int(id_): content.strip() for id_, content in doc_list}  # {article_id: article_content}


def build_inverted_index(articles):
    inv_dict = {}
    for key, content in articles.items():
        for word in content.split():
            inv_dict.setdefault(word, set()).add(key)
    return InvertedIndex(inv_dict)


def query_file_to_lists(filepath):
    query = []
    with open(filepath, 'r') as f:
        for line in f:
            query.append(line.rstrip('\n').split())
    return query


def build(dataset_path, index_path):
    build_inverted_index(load_document(dataset_path)).dump(index_path)


def make_query(index_path, query_path):
    inv_obj = InvertedIndex.load(index_path)
    for set_of_words in query_file_to_lists(query_path):
        print(','.join(map(str, (sorted(list(inv_obj.query(set_of_words)))))))


parser = argparse.ArgumentParser()
parser.add_argument('command', type=str)
parser.add_argument('--dataset', type=str)
parser.add_argument('--index', type=str)
parser.add_argument('--query_file', type=str)
args = parser.parse_args()

build(args.dataset, args.index) if args.command == 'build' else make_query(args.index, args.query_file)
