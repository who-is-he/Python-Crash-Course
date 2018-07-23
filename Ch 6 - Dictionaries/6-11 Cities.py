cities = {
    'tokyo': {
        'country': 'japan',
        'population': '9.273 million',
        'fact': 'tokyo was formerly known as edo in the 20th century. the name was changed to tokyo in 1890 in light of the meiji restoration.'
    },

    'paris': {
        'country': 'france',
        'population': '2.224 million',
        'fact': 'the eiffel tower was supposed to be a temporary installation, intended to stand for 20 years after being built for the 1889 world fair.'

    },

    'london': {
        'country': 'england',
        'population': '8.136 million',
        'fact': 'the london underground is the oldest underground railway network in the world.'
    }
}

for city in cities:
    print(city + ':')
    for info, value in cities[city].items():
        print(info + ': ' + value)
    print()