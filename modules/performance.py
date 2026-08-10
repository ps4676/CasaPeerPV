import streamlit as st
import pandas as pd


def show_performance(werte):

    st.title("📈 Performance der PV-Module")


    PV1 = werte["PV1"]
    PV2 = werte["PV2"]
    PV3 = werte["PV3"]
    PV4 = werte["PV4"]


    # ========================================================
    # MODULRANKING
    # ========================================================

    modulranking = pd.DataFrame(
        werte["modulranking"]
    )


    st.subheader("Modulranking")


    st.dataframe(
        modulranking,
        hide_index=True,
        use_container_width=True
    )


    # ========================================================
    # KENNZAHLEN
    # ========================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "PV1 Median",
            f"{PV1.median():.2f} kWh"
        )

    with col2:

        st.metric(
            "PV2 Median",
            f"{PV2.median():.2f} kWh"
        )

    with col3:

        st.metric(
            "PV3 Median",
            f"{PV3.median():.2f} kWh"
        )

    with col4:

        st.metric(
            "PV4 Median",
            f"{PV4.median():.2f} kWh"
        )