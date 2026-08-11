import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from modules.styles import sblau, srot, soran


def show_amortization(werte):

    st.title("💰 Amortisation")


    KP = werte["KP"]

    K_gesp_sum = werte["K_gesp_sum"]

    amortisation = werte["amortisation"]

    kGain = werte["kGain"]

    T_amort_prog = werte["T_amort_prog"]
    t = werte["t"]

    # ========================================================
    # KENNZAHL
    # ========================================================
    letztes_datum = t.max()
    st.subheader(f"Gesamtwerte bis {letztes_datum.strftime('%d.%m.%Y')}")
    
    st.metric(f"{amortisation:.2f} %")


    # ========================================================
    # KAUFPREIS VS. ERSPARNIS
    # ========================================================

    st.subheader(
        "Kaufpreis vs. gesparte Kosten"
    )


    fig, ax = plt.subplots(
        figsize=(8, 5)
    )

    ax.bar(
        ["Kaufpreis", "Gesparte Kosten"],
        [KP, K_gesp_sum],
        width=0.4,
        color=["tab:red", soran]
    )

    ax.grid(True)

    ax.set_ylabel("€")

    ax.set_title(
        "Amortisation der Anlage"
    )

    st.pyplot(fig)

    plt.close(fig)


    # ========================================================
    # PROGNOSE
    # ========================================================

    st.subheader(
        "Lineare Amortisationsprognose"
    )


    if T_amort_prog > 0 and kGain > 0:

        time = np.arange(
            0,
            T_amort_prog,
            1
        )


        fig, ax = plt.subplots(
            figsize=(10, 5)
        )


        ax.plot(
            time / 365,
            kGain * time,
            color=sblau,
            label="Prognose"
        )


        ax.axhline(
            KP,
            color=srot,
            linestyle="--",
            label="Kaufpreis"
        )


        ax.grid(True)

        ax.set_xlabel(
            "t in Jahren"
        )

        ax.set_ylabel(
            "€"
        )

        ax.set_title(
            f"Lineare Amortisationsprognose: "
            f"{T_amort_prog / 365:.2f} Jahre ab jetzt"
        )

        ax.legend()


        st.pyplot(fig)

        plt.close(fig)

    else:

        st.warning(
            "Eine Amortisationsprognose "
            "ist mit den aktuellen Daten "
            "nicht möglich."
        )