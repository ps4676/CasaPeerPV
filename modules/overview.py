import streamlit as st
import matplotlib.pyplot as plt

from modules.styles import sblau, smag, soran


def show_overview(werte):

    st.title("☀️ Solaranlage Casa Peer")

    st.write("Energie- und PV-Auswertung")


    # ========================================================
    # DATEN
    # ========================================================

    t = werte["t"]

    EigenV = werte["EigenV"]

    NetzImp = werte["NetzImp"]

    genSolE = werte["genSolE"]

    PV = werte["PV"]

    K_gesp_sum = werte["K_gesp_sum"]


    # ========================================================
    # KENNZAHLEN
    # ========================================================
    st.subheader("Gesamtwerte bis gestern:")
    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Gesamtverbrauch:",
            f"{EigenV.sum():.2f} kWh"
        )

    with col2:

        st.metric(
            "PV-Erzeugung:",
            f"{PV.sum():.2f} kWh"
        )

    with col3:

        st.metric(
            "Netzimport:",
            f"{NetzImp.sum():.2f} kWh"
        )

    with col4:

        st.metric(
            "Gesparte Kohle:",
            f"{K_gesp_sum:.2f} €"
        )


    # ========================================================
    # ZEITRAUM
    # ========================================================

    st.info(
        f"Auswertungszeitraum: "
        f"{t.min().strftime('%d.%m.%Y')} – "
        f"{t.max().strftime('%d.%m.%Y')}"
    )


    # ========================================================
    # TAGESVERLAUF
    # ========================================================

    st.subheader("Energieverbrauch über Tage")

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.plot(t,EigenV,color=sblau,marker="o",label="Eigenverbrauch")
    ax.plot(t,NetzImp,color=smag,marker="o",label="Netzimport")
    ax.plot(t,genSolE,color=soran,marker="o",label="Genutzte Solarenergie")
    ax.grid(True)
    ax.set_xlabel("t in Tagen")
    ax.set_ylabel("E in kWh")
    ax.legend()

    fig.autofmt_xdate()
    st.pyplot(fig)
    plt.close(fig)


    # ========================================================
    # MONATSVERLAUF
    # ========================================================

    st.subheader("Energieverbrauch über Monate")

    EigenV_months = werte["EigenV_months"]

    NetzImp_months = werte["NetzImp_months"]

    genSolE_months = werte["genSolE_months"]


    fig, ax = plt.subplots(figsize=(12, 5))

    ax.plot(
        EigenV_months.index.astype(str),
        EigenV_months.values,
        color=sblau,
        marker="o",
        label="Eigenverbrauch"
    )

    ax.plot(
        NetzImp_months.index.astype(str),
        NetzImp_months.values,
        color=smag,
        marker="o",
        label="Netzimport"
    )

    ax.plot(
        genSolE_months.index.astype(str),
        genSolE_months.values,
        color=soran,
        marker="o",
        label="Genutzte Solarenergie"
    )

    ax.grid(True)

    ax.set_xlabel("t in Monaten")

    ax.set_ylabel("E in kWh")

    ax.legend()

    st.pyplot(fig)

    plt.close(fig)


    # ========================================================
    # EIGENVERBRAUCH
    # ========================================================

    st.subheader("Eigenverbrauch pro Tag")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Median",
            f"{EigenV.median():.2f} kWh"
        )

    with col2:

        st.metric(
            "Mittelwert",
            f"{EigenV.mean():.2f} kWh"
        )