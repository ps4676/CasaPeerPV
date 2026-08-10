import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from modules.styles import sblau, smag, soran


def show_costs(werte):

    st.title("💶 Stromkosten")


    t = werte["t"]

    K_ges = werte["K_ges"]

    K_gesp = werte["K_gesp"]

    K_NI = werte["K_NI"]


    K_ges_sum = werte["K_ges_sum"]

    K_gesp_sum = werte["K_gesp_sum"]

    K_NI_sum = werte["K_NI_sum"]

    K_gesp_p = werte["K_gesp_p"]


    # ========================================================
    # PREIS
    # ========================================================

    st.info(
        f"Angenommener Strompreis: "
        f"{werte['P']:.2f} €/kWh"
    )


    # ========================================================
    # KENNZAHLEN
    # ========================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Kosten ohne PV",
            f"{K_ges_sum:.2f} €"
        )

    with col2:

        st.metric(
            "Kosten mit PV",
            f"{K_NI_sum:.2f} €"
        )

    with col3:

        st.metric(
            "Gesparte Kosten",
            f"{K_gesp_sum:.2f} €"
        )

    with col4:

        st.metric(
            "Ersparnis",
            f"{K_gesp_p:.2f} %"
        )


    st.metric(
        "Median gesparte Kosten pro Tag",
        f"{np.median(K_gesp):.2f} €"
    )


    # ========================================================
    # KOSTENVERLAUF
    # ========================================================

    st.subheader("Kostenverlauf")

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.plot(
        t,
        K_ges,
        color=sblau,
        marker="o",
        label="Gesamt"
    )

    ax.plot(
        t,
        K_gesp,
        color=soran,
        marker="v",
        label="Gespart"
    )

    ax.plot(
        t,
        K_NI,
        color=smag,
        marker="x",
        label="Gekauft"
    )

    ax.grid(True)

    ax.set_xlabel("t in Tagen")

    ax.set_ylabel("K in €")

    ax.legend()

    fig.autofmt_xdate()

    st.pyplot(fig)

    plt.close(fig)


    # ========================================================
    # MONATLICHE KOSTEN
    # ========================================================

    st.subheader("Monatlicher Kostenverlauf")

    K_ges_months = werte["K_ges_months"]

    K_gesp_months = werte["K_gesp_months"]

    K_NI_months = werte["K_NI_months"]


    fig, ax = plt.subplots(figsize=(12, 5))

    ax.plot(
        K_ges_months.index.astype(str),
        K_ges_months.values,
        color=sblau,
        marker="o",
        label="Gesamt"
    )

    ax.plot(
        K_gesp_months.index.astype(str),
        K_gesp_months.values,
        color=soran,
        marker="v",
        label="Gespart"
    )

    ax.plot(
        K_NI_months.index.astype(str),
        K_NI_months.values,
        color=smag,
        marker="x",
        label="Gekauft"
    )

    ax.grid(True)

    ax.set_xlabel("t in Monaten")

    ax.set_ylabel("K in €")

    ax.legend()

    st.pyplot(fig)

    plt.close(fig)


    # ========================================================
    # MONATLICHE ENERGIEAUFTEILUNG
    # ========================================================

    st.subheader("Monatliche Energieaufteilung")

    K_ges_months_p = werte["K_ges_months_p"]

    K_gesp_months_p = werte["K_gesp_months_p"]

    K_NI_months_p = werte["K_NI_months_p"]


    x = np.arange(
        len(K_ges_months)
    )

    width = 0.25


    fig, ax = plt.subplots(figsize=(12, 5))

    ax.bar(
        x - width,
        K_ges_months_p.values,
        color=sblau,
        width=width,
        label="Gesamt"
    )

    ax.bar(
        x,
        K_gesp_months_p.values,
        color=soran,
        width=width,
        label="Gespart"
    )

    ax.bar(
        x + width,
        K_NI_months_p.values,
        color=smag,
        width=width,
        label="Gekauft"
    )

    ax.set_xticks(
        x,
        K_ges_months.index.astype(str)
    )

    ax.grid(True)

    ax.set_xlabel("t in Monaten")

    ax.set_ylabel(
        "Relativer Kostenanteil in %"
    )

    ax.legend()

    st.pyplot(fig)

    plt.close(fig)


    # ========================================================
    # GESAMTENERGIEAUFTEILUNG
    # ========================================================

    st.subheader("Gesamtenergieaufteilung")

    namen = [
        "Gesamt",
        "Gespart",
        "Gekauft"
    ]

    werte_balken = [
        K_ges_sum,
        K_gesp_sum,
        K_NI_sum
    ]


    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar(
        namen,
        werte_balken,
        width=0.4,
        color=[sblau, soran, smag]
    )

    ax.grid(True)

    ax.set_ylabel("K in €")

    st.pyplot(fig)

    plt.close(fig)