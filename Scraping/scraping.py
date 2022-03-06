from bs4 import BeautifulSoup 
import pip._vendor.requests as request
import pandas as pd


url = 'https://resultados.as.com/resultados/futbol/champions/clasificacion/'
page = request.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#Equipos

eq = soup.find_all('span', {'class': 'nombre-equipo'})

equipos = list()

count = 0

for i in eq:
    if count < 20:
        equipos.append(i.text)
    else:
        break
    count += 1


#Puntos

pt = soup.find_all('td', {'class': 'destacado'})

puntos = list()

count = 0

for i in pt:
    if count < 20:
        puntos.append(i.text)
    else:
        break
    count += 1


df = pd.DataFrame({'Nombre':equipos, 'Puntos': puntos}, index=list(range(1,21)))
print(df)

df.to_csv('Clasificacion.csv', index=False)
