import requests


class Superhero:
    base_host = 'https://akabab.github.io/superhero-api/api'

    def get_max_int_hero(self, hero_name):
        dict_hero = {}
        uri = '/all.json'
        requests_url = self.base_host + uri
        response = requests.get(requests_url)
        all_list = response.json()
        for j in hero_name:
            for i in all_list:
                if j == i['name']:
                    dict_hero.update({i['name']: i['powerstats']['intelligence']})
        return max(dict_hero)

if __name__ == '__main__':
    hero = Superhero()
    print(hero.get_max_int_hero(['Hulk', 'Captain America', 'Thanos']))