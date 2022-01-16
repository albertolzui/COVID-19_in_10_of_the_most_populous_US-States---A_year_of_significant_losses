def get_population(state):
    switcher={
'California':'- Population: 39,613,493',
'Texas':'- Population: 29,730,311',
'Florida':'- Population: 21,944,577',
'New York':'- Population: 19,299,981',
'Pennsylvania':'- Population: 12,804,123',
'Illinois':'- Population: 12,569,321',
'Ohio':'- Population: 11,714,618',
'Georgia':'- Population: 10,830,007',
'North Carolina':'- Population: 10,701,022',
'Michigan':'- 9,992,427'
}

    return switcher.get(state)




