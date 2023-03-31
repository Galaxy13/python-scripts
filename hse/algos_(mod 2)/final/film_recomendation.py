import json
import argparse


class FilmRecommendation:
    """
    Class FilmRecommendation can be used as module
    @@@
    from film_recommendation.py import FilmRecommendation as F
    film_r = F(movies, similarities, friends)
    or you can read data manually from file
    ...
    film_r.get_best_film()
    @@@
    """
    def __init__(self, films=[], similarities=[], friends=[]):
        self.films = films
        self.similarities = similarities
        self.similarities_d = self._similarities_to_hashmap(similarities) if similarities else {}
        self.friends = self._friends_list_to_hashmap(friends)
        self.friends_d = self._friends_list_to_hashmap(friends) if friends else {}

    def _similarities_to_hashmap(self, similarities_arrays):
        """
        This functions receives list of similar movies, and returns hashmap, where for every movie from similarity array
        method created a pointer to hashset, where stores all similar to each other movie
        :param similarities_arrays: list of pairs of similar movies
        similarities_arrays: list[list[str, str]]
        :return:
        sim_dict: dict()
        """
        sim_dict = {}
        for film1, film2 in similarities_arrays:
            if sim_dict.get(film1):
                sim_dict[film1].update(set([film1, film2]))
                sim_dict[film2] = sim_dict[film1]
            elif sim_dict.get(film2):
                sim_dict[film2].update(set([film1, film2]))
                sim_dict[film1] = sim_dict[film2]
            else:
                sim_dict[film1] = set([film1, film2])
                sim_dict[film2] = sim_dict[film1]
        return sim_dict

    def _friends_list_to_hashmap(self, friends_list):
        """
        This function receives list of friends views, where for each nested list is corresponding views of each friend
        and return hashmap of counted views of every films
        :param friends_list: nested list of views of film for each friend
        friends_list = [['Joker'], ['Joker', 'Matrix']...]: list[list[str]]
        :return:
        friends_dict: dict()
        """
        friends_dict = {}
        for friend in friends_list:
            for film in friend:
                friends_dict[film] = friends_dict.get(film, 0) + 1
        return friends_dict

    def read_from_input(self):
        """
        Very optional and not very useful function
        to input data via "stdin" module
        Preferred type of input - from input.txt or input.json
        :return:
        """
        self.films = input("Input films with pattern\nfilm1 film2 ...")
        self.films = self.films.rstrip('\n').split()
        self.films = self._friends_list_to_hashmap(self.films)

        self.similarities = input("Input similarities with pattern\n[film1,film2] [film3,film4] ...")
        self.similarities = self._similarities_to_hashmap(
            [list(map(lambda x: x.strip('""'), sim_s.split(","))) for sim_s in self.similarities.rstrip("\n").split()])

        print("Input friend's films, each on next row like: \nfilm1\n film2 film3\nfilm4 film5...")
        friends_list = []
        while friend_f := input("Enter films or press 'Enter' to finish input\n"):
            self.friends_list.append(list(map(lambda x: x.strip('""'), friend_f.rstrip("\n").split())))
        self.films = self._friends_list_to_hashmap(friends_list)

    def read_from_text(self, filename):
        """
        This function reads data from file, parsed from CLI via:
        film_recommendation.py text input.txt

        For reading file, function uses standard json.loads() method
        :param filename: filepath to input file (.txt format)
        :return:
        """
        if filename.split('.')[-1] != 'txt':
            exit(f'File {filename} is not .txt type!')
        try:
            with open(filename) as f:
                self.films = [film[1:-1] for film in f.readline().split('=')[1].strip()[1:-1].split(",")]
                self.similarities = json.loads(f.readline().split('=')[1].strip())
                self.similarities_d = self._similarities_to_hashmap(self.similarities)
                self.friends = json.loads(f.readline().split('=')[1].strip())
                self.friends_d = self._friends_list_to_hashmap(self.friends)
        except FileNotFoundError:
            exit(f'File {filename} not found')

    def read_from_json(self, filename):
        """
        This function reads data from file, parsed from CLI via:
        film_recommendation.py json input.json

        For reading JSON file, function uses standard json.load() method
        :param filename: filepath to input file (.json format)
        :return:
        """
        if filename.split('.')[-1] != 'json':
            exit(f'File{filename} is not .json type!')
        try:
            with open(filename) as f:
                j = json.load(f)
                self.films = j.get('movies', [])
                self.similarities = j.get('similarities', [])
                self.friends = j.get('friends', [])
                self.similarities_d = self._similarities_to_hashmap(self.similarities)
                self.friends_d = self._friends_list_to_hashmap(self.friends)
        except FileNotFoundError:
            exit(f'File{filename} not found')

    def _count_film_views(self, film):
        """
        Method returns number of views for film. This method obtain views from self.friends_d, which has to be
        precalculated
        If film is not viewed - method returns 0
        :param film: str
        :return:
        film_views: int
        """
        return self.friends_d.get(film, 0)

    def _count_similar(self, friend_view_list, init_film):
        """
        Method obtains, if films, which are views from user, are similar to movie, we are interested for
        Initial film is not counted
        :param friend_view_list: list[str]
        :param init_film: str
        :return:
        counter: int
        """
        counter = 0
        for film in friend_view_list:
            if film != init_film and film in self.similarities_d.get(init_film, set()):
                counter += 1
        return counter

    def _count_film_mean_similarities(self, film):
        """
        Obtaining number of similar views by friends and calculates mean similarity (dividing by number of friends)
        :param film: str
        :return:
        mean_similarity: float
        """
        if not self.friends:
            return 0
        overall_counter = 0
        for friend_views in self.friends:
            overall_counter += self._count_similar(friend_views, film)
        return overall_counter / len(self.friends)

    def get_best_film(self):
        """
        Main function, that for each film in 'self.films' count the score value, using self._count_film_views and
        self._count_film_mean_similarities methods (score = film_views / mean_similarity)
        mean_similarity can be zero, if this happen, programs set new best_movie, if there is no init before and
        continues if there is any value
        :return:
        best_movie: str
        """
        if not self.films:
            return 'No data initialized'
        max_value, best_movie = 0, ''
        for film in self.films:
            film_views = self._count_film_views(film)
            mean_similarity = self._count_film_mean_similarities(film)
            if not mean_similarity:
                if not best_movie:
                    best_movie = film
            else:
                if max_value < film_views / mean_similarity:
                    best_movie = film
        return best_movie if best_movie else 'No data initialized'


if __name__ == '__main__':
    f = FilmRecommendation()
    parser = argparse.ArgumentParser(description='Recommendation of best film')
    parser.add_argument('filetype', type=str, help="Define file type of input file. Types: {text, json}")
    parser.add_argument('filepath', type=str, help="Path to file, with film data (input.txt, input.json)")
    args = parser.parse_args()
    match args.filetype:
        case 'text':
            f.read_from_text(args.filepath)
        case 'json':
            f.read_from_json(args.filepath)
        case other:
            exit('Wrong filetype argument. Use "text, json".')
    print(f.get_best_film())
