from collections import Counter
import requests


def listar_nombre_paises(url):
    paises = requests.get(url)
    paises = paises.json()

    for pais in paises:
        print(f"Nombre Oficial en Español: {pais['translations']['spa']['official']}")
        print(f"La capital es: {pais['capital'][0]}")
        monedas = pais['currencies']
        for value in monedas.values():
            print(f"La moneda es: {value['name']} y el simbolo es:{value['symbol']}")
        print(f"El codigo telefonico es: {pais['idd']['root'] + pais['idd']['suffixes'][0]}")
        print(f"El area del pais es: {pais['area']}")
        print(f"La población del pais es: {pais['population']}")
    mayor_poblacion = max(paises, key=lambda x: x['population'])
    print(
        f"El pais con mayor población es {mayor_poblacion['translations']['spa']['official']} con: {mayor_poblacion['population']}")
    mayor_area = max(paises, key=lambda x: x['area'])
    print(f"El pais con mayor area es {mayor_area['translations']['spa']['official']} con: {mayor_area['area']}")
    poblaciones = [pais['population'] for pais in paises]
    poblacion_total = sum(poblaciones)
    print(f"La poblacion total es: {poblacion_total}")
    media_poblacion = sum(poblaciones) / len(poblaciones)
    print(f"La media de la poblacion total es: ", media_poblacion)
    sorted(poblaciones)
    mitad = poblaciones[97]
    mitad1 = poblaciones[98]
    mediana_poblacion = (mitad + mitad1) / 2
    print(f"La mediana de la población total es: ", mediana_poblacion)
    frecuencias = Counter(poblaciones)
    moda_poblacion = frecuencias.most_common(1)[0][0]
    print(f"La moda de la poblacion total es: ", moda_poblacion)


url = 'https://restcountries.com/v3.1/independent?status=true&fields=translations,capital,currencies,idd,area,population'
listar_nombre_paises(url)
