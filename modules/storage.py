import streamlit as st
import matplotlib.pyplot as plt


from modules.styles import sblau, smag


def show_storage(werte):

    st.title("🔋 Speicher")


    t = werte["t"]

    E_geladen = werte["E_geladen"]

    E_entladen = werte["E_entladen"]

    N_laden = werte["N_laden"]

    N_entladen = werte["N_entladen"]


    # ========================================================
    # KENNZAHLEN
    # ========================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Geladen",
            f"{E_geladen.sum():.2f} kWh"
        )

    with col2:

        st.metric(
            "Entladen",
            f"{E_entladen.sum():.2f} kWh"
        )

    with col3:

        st.metric(
            "Ladezyklen",
            f"{N_laden:.2f}"
        )

    with col4:

        st.metric(
            "Entladezyklen",
            f"{N_entladen:.2f}"
        )


    # ========================================================
    # TAGESVERLAUF
    # ========================================================

    st.subheader("Speicher über Tage")

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.plot(
        t,
        E_geladen,
        color=sblau,
        marker="o",
        label="Geladen"
    )

    ax.plot(
        t,
        E_entladen,
        color=smag,
        marker="D",
        label="Entladen"
    )

    ax.grid(True)

    ax.set_xlabel("t in Tagen")

    ax.set_ylabel("E in kWh")

    ax.legend()

    fig.autofmt_xdate()

    st.pyplot(fig)

    plt.close(fig)


    # ========================================================
    # SPEICHERZYKLEN
    # ========================================================

    st.subheader("Speicherzyklen")

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar(
        ["Aufladungen", "Entladungen"],
        [N_laden, N_entladen],
        width=0.4,
        color=[sblau, smag]
    )

    ax.grid(True)

    ax.set_ylabel("# Zyklen")

    st.pyplot(fig)

    plt.close(fig)


    # ========================================================
    # MONATSVERLAUF
    # ========================================================

    st.subheader("Speicher über Monate")

    E_geladen_months = werte["E_geladen_months"]

    E_entladen_months = werte["E_entladen_months"]


    fig, ax = plt.subplots(figsize=(12, 5))

    ax.plot(
        E_geladen_months.index.astype(str),
        E_geladen_months.values,
        color=sblau,
        marker="o",
        label="Geladen"
    )

    ax.plot(
        E_entladen_months.index.astype(str),
        E_entladen_months.values,
        color=smag,
        marker="D",
        label="Entladen"
    )

    ax.grid(True)

    ax.set_xlabel("t in Monaten")

    ax.set_ylabel("E in kWh")

    ax.legend()

    st.pyplot(fig)

    plt.close(fig)


    # ========================================================
    # MEDIAN
    # ========================================================

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Median Aufladung",
            f"{E_geladen.median():.2f} kWh"
        )

    with col2:

        st.metric(
            "Median Entladung",
            f"{E_entladen.median():.2f} kWh"
        )