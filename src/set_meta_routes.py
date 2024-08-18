import pandas as pd

route_titles = [
                'route_id',
                'agency_id',
                'route_short_name',
                'route_long_name',
                'route_desc',
                'route_type',
                'route_url',
                'route_color',
                'route_text_color'
            ]


df = pd.read_csv('routes.csv', index_col=0)

dfj = df.to_dict('records')

data = []

for i in dfj:
    # print(i)
    route = {
                    'route_id':i.get('id'),
                    'agency_id':i.get('agency_id'),
                    'route_short_name':i.get('id'),
                    'route_long_name':i.get('name'),
                    'route_desc':i.get('route_desc'),
                    'route_type':3,
                    'route_url':i.get('route_url'),
                    'route_color':i.get('route_color'),
                    'route_text_color':i.get('route_text_color')
            }
    data.append(route)



dataframe = pd.DataFrame(data)

dataframe.to_csv('../gtfs/routes.txt', index=False)
