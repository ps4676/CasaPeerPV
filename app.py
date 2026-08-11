import streamlit as st

from modules.data_loader import load_data
from modules.calculations import calculate_values

from modules.overview import show_overview
from modules.monthly import show_monthly
from modules.storage import show_storage
from modules.pv import show_pv
from modules.performance import show_performance
from modules.costs import show_costs
from modules.amortization import show_amortization

from modules.styles import navigation_style


# ============================================================
# EINSTELLUNGEN
# ============================================================

st.set_page_config(
    page_title="Casa Peer PV",
    page_icon="☀️",
    layout="wide"
)


# ============================================================
# NAVIGATION
# ============================================================

st.sidebar.markdown(
    navigation_style(),
    unsafe_allow_html=True
)

st.sidebar.markdown("### ☀️ Casa Peer PV")

seite = st.sidebar.radio(
    "Navigation",
    [
        "📊 Übersicht",
        "📅 Monatsübersicht",
        "🔋 Speicher",
        "☀️ PV-Produktion",
        "📈 Modul-Performance",
        "💶 Stromkosten",
        "💰 Amortisation"
    ],
    label_visibility="collapsed"
)


# ============================================================
# DATEIUPLOAD
# ============================================================

st.sidebar.header("📂 Daten")

uploaded_file = st.sidebar.file_uploader(
    "CSV-Datei hochladen",
    type=["csv"]
)

if uploaded_file is not None:

    st.sidebar.success(
        f"Datei geladen: {uploaded_file.name}"
    )

else:

    st.sidebar.info(
        "Standarddaten werden verwendet."
    )


# ============================================================
# DATEN LADEN
# ============================================================

data = load_data(uploaded_file)


# ============================================================
# BERECHNUNGEN
# ============================================================

werte = calculate_values(data)


# ============================================================
# SEITE ANZEIGEN
# ============================================================

if seite == "📊 Übersicht":

    show_overview(werte)

elif seite == "📅 Monatsübersicht":

    show_monthly(werte)

elif seite == "🔋 Speicher":

    show_storage(werte)

elif seite == "☀️ PV-Produktion":

    show_pv(werte)

elif seite == "📈 Modul-Performance":

    show_performance(werte)

elif seite == "💶 Stromkosten":

    show_costs(werte)

elif seite == "💰 Amortisation":

    show_amortization(werte)