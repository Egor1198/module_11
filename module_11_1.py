import requests
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt


s_city = "Moscow,RU"
city_id = 0
appid = "73bf58f56b406a82ff6e1a582a2f998c"

# Получить ID города
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/find",
                       params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
    data = res.json()
    cities = ["{} ({})".format(d['name'], d['sys']['country'])
              for d in data['list']]
    print("city:", cities)
    city_id = data['list'][0]['id']
    print('city_id=', city_id)
except Exception as e:
    print("Exception (find):", e)
    pass

#Прогноз погоды на 5 дней
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                       params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()

# Сохраненеие данных
    forecast_data = []
    for i in data['list']:
        print(i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['description'])
        forecast_data.append({
            'Дата и время': i['dt_txt'],
            'Температура (°C)': i['main']['temp'],
            'Минимальная температура (°C)': i['main']['temp_min'],
            'Максимальная температура (°C)': i['main']['temp_max'],
            'Описание погоды': i['weather'][0]['description']
        })

    df = pd.DataFrame(forecast_data)

    df.to_excel('py_classssss.xlsx', index=False, engine='openpyxl')
    print("Данные сохранены в файл 'py_classssss.xlsx'.")

# Построение столбчатой диаграммы
    plt.figure(figsize=(12, 6))
    plt.bar(df['Дата и время'], df['Температура (°C)'], color='skyblue')
    plt.title('Температура в Москве на 5 дней', fontsize=16)
    plt.xlabel('Дата и время', fontsize=12)
    plt.ylabel('Температура (°C)', fontsize=12)
    plt.xticks(rotation=45, fontsize=8)
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

except Exception as e:
    print("Exception (forecast):", e)
    pass
