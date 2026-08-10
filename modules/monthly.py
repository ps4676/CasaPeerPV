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

    st.subheader("Monatliche Kennzahlen")

    for monat in EigenV_months.index:

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                f"{monat} – Eigenverbrauch",
                f"{EigenV_months.loc[monat]:.2f} kWh"
            )

        with col2:

            st.metric(
                f"{monat} – Solarenergie",
                f"{genSolE_months.loc[monat]:.2f} kWh"
            )

        with col3:

            st.metric(
                f"{monat} – Netzimport",
                f"{NetzImp_months.loc[monat]:.2f} kWh"
            )


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