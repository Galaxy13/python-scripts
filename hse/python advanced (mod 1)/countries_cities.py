import sys

country_dict = {}
country_num = int(sys.stdin.readline())
for _ in range(country_num):
    input_line = sys.stdin.readline().split()
    for country in input_line[1:]:
        country_dict[country] = input_line[0]
cities_num = int(sys.stdin.readline())
for _ in range(cities_num):
    country = sys.stdin.readline()
    print(country_dict[country.rstrip('\n')])

# 63ef54498c743f8c5b49bfd4600e824e

