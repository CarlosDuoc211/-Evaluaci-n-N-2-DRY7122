import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "99pKnf5HsQTUoSPEEPHlR54ecvgq825S"  # Reemplaza con tu clave de API de MapQuest

def calcular_consumo_combustible(origen, destino):
    url = main_api + urllib.parse.urlencode({"key": key, "from": origen, "to": destino})
    print("URL: ", url)
    json_data = requests.get(url).json()

    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("Estado de la API " + str(json_status) + " = Llamada de ruta exitosa.\n")
        print("=============================================")
        print("Direcciones desde " + origen + " hasta " + destino)
        print("Duración del viaje: " + json_data["route"]["formattedTime"])
        distancia_km = json_data["route"]["distance"] * 1.6
        print("Distancia: {:.2f} km".format(distancia_km))
        consumo_aproximado_litros = distancia_km * 0.12  # Fórmula aproximada de consumo de combustible (puedes ajustar el valor según tus necesidades)
        print("Consumo de combustible estimado: {:.2f} litros".format(consumo_aproximado_litros))
        print("\nIndicaciones de la narrativa:")
        maneuvers = json_data["route"]["legs"][0]["maneuvers"]
        for index, maneuver in enumerate(maneuvers, start=1):
            print(f"{index}. {maneuver['narrative']}")
        print("Narrativa del viaje:")
        for leg in json_data["route"]["legs"]:
            print("- Instrucción: " + leg["maneuvers"][0]["narrative"])
            print("  Distancia: {:.2f} km".format(leg["distance"] * 1.6))
            print("  Duración: " + leg["formattedTime"])
        print("=============================================")

while True:
    ciudad_origen = input("Ubicación de inicio (o 'q' para salir): ")
    if ciudad_origen.lower() == "q" or ciudad_origen.lower() == "s" or ciudad_origen.lower() == "q":
        break

    ciudad_destino = input("Destino: ")
    if ciudad_destino.lower() == "salir" or ciudad_destino.lower() == "s" or ciudad_destino.lower() == "q":
        break

    calcular_consumo_combustible(ciudad_origen, ciudad_destino)
