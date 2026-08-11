import pandas as pd
from pathlib import Path


def load_data(uploaded_file=None):

    # ------------------------------------------------------------
    # CSV-Datei auswählen
    # ------------------------------------------------------------

    if uploaded_file is not None:

        data = pd.read_csv(
            uploaded_file,
            sep=",",
            skiprows=1
        )

    else:

        base_dir = Path(__file__).resolve().parent.parent

        file = (
            base_dir
            / "data"
            / "Casa Peer_Energiedetails_13_Jul_2026_to_8_Aug_2026.csv"
        )

        data = pd.read_csv(
            file,
            sep=",",
            skiprows=1
        )

    # ------------------------------------------------------------
    # Datum konvertieren
    # ------------------------------------------------------------

    data["Datum"] = pd.to_datetime(
        data["Datum"],
        dayfirst=True
    )

    return data

