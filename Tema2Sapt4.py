# Alexandra version
description = ('Country', [
    '2011 ', '2012 ', '2013 ', '2014 ', '2015 ', '2016 ', '2017 ', '2018 ', '2019 '
])
dataset = [
    ('AL', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '84 ', ': ']),
    ('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 ']),
    ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ', '72 ']),
    ('BE', ['77 ', '78 ', '80 ', '83 ', '82 ', '85 ', '86 ', '87 ', '90 ']),
    ('BG', ['45 ', '51 ', '54 ', '57 ', '59 ', '64 ', '67 ', '72 ', '75 ']),
    ('CH', [': ', ': ', ': ', '91 ', ': ', ': ', '93 b', ': ', '96 ']),
    ('CY', ['57 ', '62 ', '65 ', '69 ', '71 ', '74 ', '79 ', '86 ', '90 ']),
    ('CZ', ['67 ', '73 ', '73 ', '78 ', '79 ', '82 ', '83 ', '86 ', '87 ']),
    ('DE', ['83 ', '85 ', '88 ', '89 ', '90 ', '92 ', '93 ', '94 ', '95 ']),
    ('DK', ['90 ', '92 ', '93 ', '93 ', '92 ', '94 ', '97 ', '93 ', '95 ']),
    ('EA', ['74 ', '76 ', '79 ', '81 ', '83 ', '85 ', '87 ', '89 ', '90 ']),
    ('EE', ['69 ', '74 ', '79 ', '83 ', '88 ', '86 ', '88 ', '90 ', '90 ']),
    ('EL', ['50 ', '54 ', '56 ', '66 ', '68 ', '69 ', '71 ', '76 ', '79 ']),
    ('ES', ['63 ', '67 ', '70 ', '74 ', '79 ', '82 ', '83 ', '86 ', '91 ']),
    ('FI', ['84 ', '87 ', '89 ', '90 ', '90 ', '92 ', '94 ', '94 ', '94 ']),
    ('FR', ['76 ', '80 ', '82 ', '83 ', '83 ', '86 ', '86 ', '89 ', '90 ']),
    ('HR', ['61 ', '66 ', '65 ', '68 ', '77 ', '77 ', '76 ', '82 ', '81 ']),
    ('HU', ['63 ', '67 ', '70 ', '73 ', '76 ', '79 ', '82 ', '83 ', '86 ']),
    ('IE', ['78 ', '81 ', '82 ', '82 ', '85 ', '87 ', '88 ', '89 ', '91 ']),
    ('IS', ['93 ', '95 ', '96 ', '96 ', ': ', ': ', '98 ', '99 ', '98 ']),
    ('IT', ['62 ', '63 ', '69 ', '73 ', '75 ', '79 ', '81 ', '84 ', '85 ']),
    ('LT', ['60 ', '60 ', '65 ', '66 ', '68 ', '72 ', '75 ', '78 ', '82 ']),
    ('LU', ['91 ', '93 ', '94 ', '96 ', '97 ', '97 ', '97 ', '93 b', '95 ']),
    ('LV', ['64 ', '69 ', '72 ', '73 ', '76 ', '77 b', '79 ', '82 ', '85 ']),
    ('ME', [': ', '55 ', ': ', ': ', ': ', ': ', '71 ', '72 ', '74 ']),
    ('MK', [': ', '58 ', '65 ', '68 ', '69 ', '75 ', '74 ', '79 ', '82 ']),
    ('MT', ['75 ', '77 ', '78 ', '80 ', '81 ', '81 ', '85 ', '84 ', '86 ']),
    ('NL', ['94 ', '94 ', '95 ', '96 ', '96 ', '97 ', '98 ', '98 ', '98 ']),
    ('NO', ['92 ', '93 ', '94 ', '93 ', '97 ', '97 ', '97 ', '96 ', '98 ']),
    ('PL', ['67 ', '70 ', '72 ', '75 ', '76 ', '80 ', '82 ', '84 ', '87 ']),
    ('PT', ['58 ', '61 ', '62 ', '65 ', '70 ', '74 ', '77 ', '79 ', '81 ']),
    ('RO', ['47 ', '54 ', '58 ', '61 b', '68 ', '72 ', '76 ', '81 ', '84 ']),
    ('RS', [': ', ': ', ': ', ': ', '64 ', ': ', '68 ', '73 ', '80 ']),
    ('SE', ['91 ', '92 ', '93 ', '90 ', '91 ', '94 b', '95 ', '93 ', '96 ']),
    ('SI', ['73 ', '74 ', '76 ', '77 ', '78 ', '78 ', '82 ', '87 ', '89 ']),
    ('SK', ['71 ', '75 ', '78 ', '78 ', '79 ', '81 ', '81 ', '81 ', '82 ']),
    ('TR', [': ', '47 ', '49 ', '60 ', '70 ', '76 ', '81 ', '84 ', '88 ']),
    ('UK', ['83 ', '87 ', '88 ', '90 ', '91 ', '93 ', '94 ', '95 ', '96 ']),
    ('XK', [': ', ': ', ': ', ': ', ': ', ': ', '89 ', '93 ', '93 ']),
]
countries_list = {"AL": "Albania", "AT": "Austria", "BA": "Bosnia and Herzegovina", "BE": "Belgium", "BG": "Bulgaria",
                  "CH": "Switzerland", "CY": "Cyprus", "CZ": "Czech Republic", "DE": "Germany", "DK": "Denmark",
                  "EA": "Europe", "EE": "Estonia", "EL": "Greece", "ES": "Spain", "FI": "Finland",
                  "FR": "France", "HR": "Croatia", "HU": "Hungary", "IE": "Ireland", "IS": "Iceland",
                  "IT": "Italy", "LT": "Lithuania", "LU": "Luxembourg", "LV": "Latvia", "ME": "Montenegro",
                  "MK": "North Macedonia", "MT": "Malta", "NL": "Netherlands", "NO": "Norway", "PL": "Poland",
                  "PT": "Portugal", "RO": "Romania", "RS": "Serbia", "SE": "Sweden", "SI": "Slovenia",
                  "SK": "Slovakia", "TR": "Turkey", "UK": "United Kingdom", "XK": "Kosovo"}


# get_year_data(dataset, "2019") returneaza  {'2019': [('Romania', 84), ('Germany', 95), ..., ('Latvia', 85)]}
def main():
    dict_of_values = {}
    for item in dataset:
        dict_of_values[countries_list[item[0]]] = []
        for i, v in enumerate(description[1]):
            dict_of_values[countries_list[item[0]]].append(
                {'year': "".join(x for x in v if x.isdigit()),
                 'coverage': "".join(x for x in item[1][i] if x.isdigit())})
    return dict_of_values


# 'Romania': [
#          {
#             'year': '2019',
#              'coverage': 84
#          }, {
#              'year': '2018',
#              'coverage': 67
#          }]
# print(main())

def get_year_data(dataset, year='2019'):
    list_formatted = ["".join(x for x in year if x.isdigit()) for year in description[1]]
    index = list_formatted.index(year)
    dict_to_return = {
        year: [(countries_list[line[0]], int("".join(x for x in line[1][index] if x.isdigit())) if "".join(
            x for x in line[1][index] if x.isdigit()) != "" else '') for line in dataset]}
    return dict_to_return




# exemplu = {'2019': [('Romania', 84), ('Germany', 95), ('Latvia', 85)]}
# print(get_year_data(dataset))

# exemplu = {"Romania": [("2019", 84), ("2018", 86), ..., ("2011", 72)]}


def get_country_data(dataset, country="Romania"):
    dict_to_return = {country: []}
    lista = []
    for value in dataset[country]:
        for item, dict_values in value.items():
            if item == 'coverage':
                value['coverage'] = int(dict_values)
                lista.append(tuple(value.values()))
        dict_to_return[country] = lista
    return dict_to_return


# print(get_country_data(main()))


# perform_average(country_data['Romania']) => 79.4
def perform_average(data):
    media = 0
    lista = [valori_lista[1] for item in data.values() for valori_lista in item]
    # for item in data.values():
    #     for valori_lista in item:
    #         lista.append(valori_lista[1])
    return sum(lista) / len(lista)

print(perform_average(get_country_data(main())))