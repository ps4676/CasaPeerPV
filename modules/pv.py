import streamlit as st
import matplotlib.pyplot as plt


from modules.styles import (
    sblau,
    smag,
    srot,
    soran
)


def show_pv(werte):

    st.title("☀️ PV-Produktion")


    t = werte["t"]

    PV = werte["PV"]
    PV1 = werte["PV1"]
    PV2 = werte["PV2"]
    PV3 = werte["PV3"]
    PV4 = werte["PV4"]


    # ========================================================
    # KENNZAHL
    # ========================================================
    st.subheader(f"Gesamtwerte bis {t.max().strftime('%d.%m.%Y')}:")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("PV Gesamt",f"{PV.sum():.2f} kWh")

    with col2:
        st.metric("PV1",f"{PV1.sum():.2f} kWh")

    with col3:
        st.metric("PV2",f"{PV2.sum():.2f} kWh")

    with col4:
        st.metric("PV3",f"{PV3.sum():.2f} kWh")

    with col5:
        st.metric("PV4",f"{PV4.sum():.2f} kWh")


    # ========================================================
    # TAGESVERLAUF
    # ========================================================

    st.subheader("PV-Produktion über Tage")

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.plot(
        t,
        PV,
        marker="o",
        label="PV Gesamt"
    )

    ax.plot(
        t,
        PV1,
        marker="x",
        color=sblau,
        label="PV1"
    )

    ax.plot(
        t,
        PV2,
        marker="v",
        color=smag,
        label="PV2"
    )

    ax.plot(
        t,
        PV3,
        marker="*",
        color=srot,
        label="PV3"
    )

    ax.plot(
        t,
        PV4,
        marker="D",
        color=soran,
        label="PV4"
    )

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

    st.subheader("PV-Produktion über Monate")

    PV_months = werte["PV_months"]

    PV1_months = werte["PV1_months"]

    PV2_months = werte["PV2_months"]

    PV3_months = werte["PV3_months"]

    PV4_months = werte["PV4_months"]


    fig, ax = plt.subplots(figsize=(12, 5))

    ax.plot(
        PV_months.index.astype(str),
        PV_months.values,
        marker="o",
        label="PV Gesamt"
    )

    ax.plot(
        PV1_months.index.astype(str),
        PV1_months.values,
        color=sblau,
        marker="x",
        label="PV1"
    )

    ax.plot(
        PV2_months.index.astype(str),
        PV2_months.values,
        color=smag,
        marker="v",
        label="PV2"
    )

    ax.plot(
        PV3_months.index.astype(str),
        PV3_months.values,
        color=srot,
        marker="*",
        label="PV3"
    )

    ax.plot(
        PV4_months.index.astype(str),
        PV4_months.values,
        color=soran,
        marker="D",
        label="PV4"
    )

    ax.grid(True)

    ax.set_xlabel("t in Monaten")

    ax.set_ylabel("E in kWh")

    ax.legend()

    st.pyplot(fig)

    plt.close(fig)


    # ========================================================
    # PRODUKTION PRO MODUL
    # ========================================================

    st.subheader("Gesamtproduktion pro Modul")

    namen = [
        "Gesamt",
        "PV1",
        "PV2",
        "PV3",
        "PV4"
    ]

    werte_modul = [
        PV.sum(),
        PV1.sum(),
        PV2.sum(),
        PV3.sum(),
        PV4.sum()
    ]


    fig, ax = plt.subplots(figsize=(10, 5))

    ax.bar(
        namen,
        werte_modul,
        width=0.4,
        color=[
            "tab:blue",
            sblau,
            smag,
            srot,
            soran
        ]
    )

    ax.grid(True)

    ax.set_ylabel("E in kWh")

    st.pyplot(fig)

    plt.close(fig)


    # ========================================================
    # MEDIAN
    # ========================================================

    st.metric(
        "Median PV-Produktion pro Tag",
        f"{PV.median():.2f} kWh"
    )


    # ========================================================
    # WIRKUNGSGRAD
    # ========================================================

    st.subheader("Wirkungsgrad der Anlage")

    P_Sonne = werte["P_Sonne"]

    P_Sol_peak = werte["P_Sol_peak"]

    eta = werte["eta"]


    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Sonnenleistung",
            f"{P_Sonne:.2f} kW"
        )

    with col2:

        st.metric(
            "Anlagenleistung",
            f"{P_Sol_peak:.2f} kW"
        )

    with col3:

        st.metric(
            "Wirkungsgrad",
            f"{eta:.2f} %"
        )