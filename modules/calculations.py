import numpy as np


def calculate_values(data):

    # ========================================================
    # ZEITACHSE
    # ========================================================

    t = data["Datum"]


    # ========================================================
    # VERBRAUCH
    # ========================================================

    EigenV = data["Eigenverbrauch (kWh)"]

    NetzImp = data["Netzimport (kWh)"]

    genSolE = data["Genutzte Solarenergie (kWh)"]


    # ========================================================
    # PV
    # ========================================================

    PV_spalte = [
        spalte
        for spalte in data.columns
        if "Gesamterzeugung" in spalte
        and "Solarbank" in spalte
    ][0]

    PV = data[PV_spalte]


    PV1_spalte = [
        spalte
        for spalte in data.columns
        if "PV1" in spalte
    ][0]

    PV2_spalte = [
        spalte
        for spalte in data.columns
        if "PV2" in spalte
    ][0]

    PV3_spalte = [
        spalte
        for spalte in data.columns
        if "PV3" in spalte
    ][0]

    PV4_spalte = [
        spalte
        for spalte in data.columns
        if "PV4" in spalte
    ][0]

    PV1 = data[PV1_spalte]
    PV2 = data[PV2_spalte]
    PV3 = data[PV3_spalte]
    PV4 = data[PV4_spalte]


    # ========================================================
    # SPEICHER
    # ========================================================

    E_geladen = data["Speicherladung (kWh)"]

    E_entladen = data["Speicherentladung (kWh)"]


    # ========================================================
    # MONATSSUMMEN
    # ========================================================

    monat = data["Datum"].dt.to_period("M")


    EigenV_months = data.groupby(
        monat
    )["Eigenverbrauch (kWh)"].sum()


    NetzImp_months = data.groupby(
        monat
    )["Netzimport (kWh)"].sum()


    genSolE_months = data.groupby(
        monat
    )["Genutzte Solarenergie (kWh)"].sum()


    PV_months = data.groupby(
        monat
    )[PV_spalte].sum()


    PV1_months = data.groupby(
        monat
    )[PV1_spalte].sum()


    PV2_months = data.groupby(
        monat
    )[PV2_spalte].sum()


    PV3_months = data.groupby(
        monat
    )[PV3_spalte].sum()


    PV4_months = data.groupby(
        monat
    )[PV4_spalte].sum()


    E_geladen_months = data.groupby(
        monat
    )["Speicherladung (kWh)"].sum()


    E_entladen_months = data.groupby(
        monat
    )["Speicherentladung (kWh)"].sum()


    # ========================================================
    # WIRKUNGSGRAD
    # ========================================================

    Q_Sonne = 1361

    A = (1.95 * 1.13) * 4

    P_Sonne = Q_Sonne * A / 1e3

    P_Sol_peak = 2

    eta = 100 / P_Sonne * P_Sol_peak


    # ========================================================
    # STROMKOSTEN
    # ========================================================

    P = 0.33

    K_ges = P * EigenV

    K_gesp = P * genSolE

    K_NI = P * NetzImp


    K_ges_sum = K_ges.sum()

    K_gesp_sum = K_gesp.sum()

    K_NI_sum = K_NI.sum()


    if K_ges_sum != 0:

        K_gesp_p = (
            100 / K_ges_sum * K_gesp_sum
        )

    else:

        K_gesp_p = 0


    # Monatliche Kosten

    K_ges_months = P * EigenV_months

    K_gesp_months = P * genSolE_months

    K_NI_months = P * NetzImp_months


    # Prozentuale monatliche Kosten

    K_ges_months_p = (
        100 * K_ges_months / K_ges_months
    )

    K_gesp_months_p = (
        100 * K_gesp_months / K_ges_months
    )

    K_NI_months_p = (
        100 * K_NI_months / K_ges_months
    )


    # ========================================================
    # SPEICHERZYKLEN
    # ========================================================

    cap = 8.6

    N_laden = E_geladen.sum() / cap

    N_entladen = E_entladen.sum() / cap


    # ========================================================
    # MODUL-PERFORMANCE
    # ========================================================

    perf_module = np.array([
        PV1.median(),
        PV2.median(),
        PV3.median(),
        PV4.median()
    ])


    pvID = np.array([
        "PV1",
        "PV2",
        "PV3",
        "PV4"
    ])


    idx = np.argsort(
        perf_module
    )[::-1]


    modulranking = {
        "Modul": pvID[idx],
        "Median in kWh": perf_module[idx]
    }


    # ========================================================
    # AMORTISATION
    # ========================================================

    KP = 3500

    amortisation = (
        100 / KP * K_gesp_sum
    )


    # ========================================================
    # AMORTISATIONSPROGNOSE
    # ========================================================

    if len(t) > 0 and K_gesp_sum > 0:

        kGain = K_gesp_sum / len(t)

        T_amort_prog = (
            (KP - K_ges_sum) / kGain
        )

    else:

        kGain = 0
        T_amort_prog = 0


    # ========================================================
    # ALLES ZURÜCKGEBEN
    # ========================================================

    return {

        # Zeit
        "t": t,

        # Verbrauch
        "EigenV": EigenV,
        "NetzImp": NetzImp,
        "genSolE": genSolE,

        # PV
        "PV": PV,
        "PV1": PV1,
        "PV2": PV2,
        "PV3": PV3,
        "PV4": PV4,

        # Speicher
        "E_geladen": E_geladen,
        "E_entladen": E_entladen,

        # Monate
        "EigenV_months": EigenV_months,
        "NetzImp_months": NetzImp_months,
        "genSolE_months": genSolE_months,

        "PV_months": PV_months,
        "PV1_months": PV1_months,
        "PV2_months": PV2_months,
        "PV3_months": PV3_months,
        "PV4_months": PV4_months,

        "E_geladen_months": E_geladen_months,
        "E_entladen_months": E_entladen_months,

        # Wirkungsgrad
        "Q_Sonne": Q_Sonne,
        "A": A,
        "P_Sonne": P_Sonne,
        "P_Sol_peak": P_Sol_peak,
        "eta": eta,

        # Speicherzyklen
        "cap": cap,
        "N_laden": N_laden,
        "N_entladen": N_entladen,

        # Modulranking
        "modulranking": modulranking,

        # Stromkosten
        "P": P,
        "K_ges": K_ges,
        "K_gesp": K_gesp,
        "K_NI": K_NI,

        "K_ges_sum": K_ges_sum,
        "K_gesp_sum": K_gesp_sum,
        "K_NI_sum": K_NI_sum,

        "K_gesp_p": K_gesp_p,

        "K_ges_months": K_ges_months,
        "K_gesp_months": K_gesp_months,
        "K_NI_months": K_NI_months,

        "K_ges_months_p": K_ges_months_p,
        "K_gesp_months_p": K_gesp_months_p,
        "K_NI_months_p": K_NI_months_p,

        # Amortisation
        "KP": KP,
        "amortisation": amortisation,

        # Prognose
        "kGain": kGain,
        "T_amort_prog": T_amort_prog,
    }