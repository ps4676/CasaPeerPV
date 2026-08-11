import numpy as np

# ============================================================
# FARBEN
# ============================================================

sblau = np.array([56, 58, 107]) / 255
smag = np.array([203, 31, 115]) / 255
srot = np.array([224, 58, 60]) / 255
soran = np.array([242, 136, 1]) / 255


# ============================================================
# NAVIGATIONSKACHELN
# ============================================================

def navigation_style():

    return """
    <style>

    div[role="radiogroup"] {
        gap: 10px;
    }

    div[role="radiogroup"] label {
        background-color: #f5f5f7;
        border-radius: 12px;
        padding: 12px 15px;
        margin-bottom: 8px;
        border: 1px solid #e0e0e0;
        transition: all 0.2s ease;
        cursor: pointer;
    }

    div[role="radiogroup"] label:hover {
        background-color: #eaeaf0;
        transform: translateX(3px);
    }

    div[role="radiogroup"] label[data-checked="true"] {
        background-color: #383a6b;
        color: white;
        border-color: #383a6b;
    }

    div[role="radiogroup"] label[data-checked="true"] p {
        color: white;
        font-weight: 600;
    }

    div[role="radiogroup"] label p {
        font-size: 15px;
        margin: 0;
    }

    </style>
    """