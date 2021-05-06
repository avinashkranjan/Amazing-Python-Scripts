import requests
import matplotlib.pyplot as plt
city = input("Enter you city :  ")
url = 'http://api.waqi.info/feed/' + city + '/?token='
api_key = input("Enter your API key: ")

main_url = url + api_key
r = requests.get(main_url)
data = r.json()['data']
aqi = data['aqi']
iaqi = data['iaqi']


for i in iaqi.items():
    print(i[0], ':', i[1]['v'])
dew = iaqi.get('dew', 'Nil')
no2 = iaqi.get('no2', 'Nil')
o3 = iaqi.get('o3', 'Nil')
so2 = iaqi.get('so2', 'Nil')
pm10 = iaqi.get('pm10', 'Nil')
pm25 = iaqi.get('pm25', 'Nil')

print(f'{city} AQI :', aqi, '\n')
print('Individual Air quality')
print('Dew :', dew)
print('no2 :', no2)
print('Ozone :', o3)
print('sulphur :', so2)
print('pm10 :', so2)
print('pm25 :', pm25)
pollutants = [i for i in iaqi]
values = [i['v'] for i in iaqi.values()]


# Exploding the first slice
explode = [0 for i in pollutants]
mx = values.index(max(values))  # explode 1st slice
explode[mx] = 0.1

# Plot a pie chart
plt.figure(figsize=(8, 6))
plt.pie(values, labels=pollutants, explode=explode,
        autopct='%1.1f%%', shadow=True)

plt.title('Air pollutants and their probable amount in atmosphere [kanpur]')

plt.axis('equal')
plt.show()
