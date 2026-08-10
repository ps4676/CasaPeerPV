import pandas as pd
from pathlib import Path
import streamlit as st


def load_data():

    # Projektordner bestimmen
    projektordner = Path(__file__).resolve().parent.parent

    # CSV-Datei
    file = (
        projektordner
        / "data"
        / "Casa Peer_Energiedetails_13_Jul_2026_to_8_Aug_2026.csv"
    )

    # Prüfen, ob Datei existiert
    if not file.exists():

        st.error(
            f"CSV-Datei wurde nicht gefunden:\n\n{file}"
        )

        st.stop()

    # CSV einlesen
    data = pd.read_csv(
        file,
        sep=",",
        skiprows=1
    )

    # Datum konvertieren
    data["Datum"] = pd.to_datetime(
        data["Datum"],
        dayfirst=True
    )

    return data