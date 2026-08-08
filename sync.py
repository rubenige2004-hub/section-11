import argparse
import json
import os
import requests

def fetch_intervals_data(api_key, athlete_id):
    url = f"https://intervals.icu{athlete_id}/wellness"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Error al conectar con Intervals.icu: {response.status_code}")
    return response.json()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="dossier.json")
    args = parser.parse_args()

    api_key = os.environ.get("INTERVALS_ICU_API_KEY")
    athlete_id = os.environ.get("INTERVALS_ICU_ATHLETE_ID")

    if not api_key or not athlete_id:
        raise Exception("Faltan las credenciales en los secretos de GitHub")

    data = fetch_intervals_data(api_key, athlete_id)
    with open(args.output, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Datos guardados con éxito en {args.output}")
