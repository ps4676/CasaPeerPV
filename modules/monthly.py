import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from modules.styles import sblau, smag, soran


def show_monthly(werte):

    st.title("📅 Monatsübersicht")

    
    EigenV_months = werte["EigenV_months"]

    NetzImp_months = werte["NetzImp_months"]

    genSolE_months = werte["genSolE_months"]


    # ========================================================
    # MONATLICHE KENNZAHLEN
    # ========================================================



    # ========================================================
    # DIAGRAMM
    # ========================================================

    st.subheader("Monatliche Energieübersicht")

    x = np.arange(len(EigenV_months))

    width = 0.25

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.bar(
        x - width,
        EigenV_months.values,
        color=sblau,
        width=width,
        label="Eigenverbrauch"
    )

    ax.bar(
        x,
        genSolE_months.values,
        color=soran,
        width=width,
        label="Genutzte Solarenergie"
    )

    ax.bar(
        x + width,
        NetzImp_months.values,
        color=smag,
        width=width,
        label="Netzimport"
    )

    ax.set_xticks(
        x,
        EigenV_months.index.astype(str)
    )

    ax.grid(True)

    ax.set_xlabel("t in Monaten")

    ax.set_ylabel("E in kWh")

    ax.legend()

    st.pyplot(fig)

    plt.close(fig)