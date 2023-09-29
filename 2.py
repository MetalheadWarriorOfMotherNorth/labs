import requests
city='Moscow,RU'
appid='6dcf1910f0c1a8f89c59a14ca7eeb2f8'

res=requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'q':city,'units':'metric','lang':'ru','APPID':appid})
data=res.json()

print('Погода на данный момент')
print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
print("Cкорость ветра:", data['wind']['speed'])
print("Видимость", data['visibility'], 'м')

###########################

res=requests.get("http://api.openweathermap.org/data/2.5/forecast",
                 params={'q':city,'units':'metric','lang':'ru','APPID':appid})
data=res.json()

print('Прогноз погоды на неделю:')
for i in data['list']:
    print('Дата <',i['dt_txt'],'>\r\nТемпреатура: <',
          '{0:+3.0f}'.format(i['main']['temp']),'>\r\nПогодные условия:',
          i['weather'][0]['description'],'>\r\nСкорость ветра: <',
          i['wind']['speed'],'>\r\nВидимость: <',
          i['visibility'],'м >'
          )
    print('---------------------------------')