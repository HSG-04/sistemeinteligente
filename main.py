# =========================================================
# PROIECT MACHINE LEARNING
# Gestionarea Grupelor si Patrulelor
# Varianta COMPLETA
# =========================================================

import tkinter as tk
from tkinter import messagebox

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

# =========================================================
# GENERARE DATE
# =========================================================

np.random.seed(42)

numar_zile = 365
zile = []

tipuri_evenimente = [
    "Normal",
    "Meci Fotbal",
    "Meci Handbal",
    "Concert",
    "Parc Auto",
    "Urgenta",
    "Patrula Oras"
]

for i in range(numar_zile):

    total_angajati = np.random.randint(40, 80)

    liberi = np.random.randint(0, 15)
    medical = np.random.randint(0, 8)
    concediu = np.random.randint(0, 10)
    rezerve = np.random.randint(2, 10)

    disponibili = total_angajati - liberi - medical - concediu

    masini_disponibile = np.random.randint(2, 15)

    eveniment = np.random.choice(tipuri_evenimente)

    if eveniment == "Normal":
        necesar_patrule = max(4, disponibili // 8)

    elif eveniment == "Meci Fotbal":
        necesar_patrule = max(8, disponibili // 3)

    elif eveniment == "Meci Handbal":
        necesar_patrule = max(6, disponibili // 4)

    elif eveniment == "Concert":
        necesar_patrule = max(7, disponibili // 4)

    elif eveniment == "Parc Auto":
        necesar_patrule = max(5, disponibili // 5)

    elif eveniment == "Patrula Oras":
        necesar_patrule = max(5, disponibili // 6)

    else:
        necesar_patrule = max(9, disponibili // 2)

    zile.append([
        total_angajati,
        liberi,
        medical,
        concediu,
        rezerve,
        disponibili,
        masini_disponibile,
        eveniment,
        necesar_patrule
    ])

columns = [
    "Total_Angajati",
    "Liberi",
    "Medical",
    "Concediu",
    "Rezerve",
    "Disponibili",
    "Masini_Disponibile",
    "Eveniment",
    "Patrule_Necesare"
]

df = pd.DataFrame(zile, columns=columns)

# =========================================================
# ENCODARE EVENIMENT
# =========================================================

encoder = LabelEncoder()

df["Eveniment"] = encoder.fit_transform(df["Eveniment"])

# =========================================================
# PREGATIRE DATE
# =========================================================

X = df.drop("Patrule_Necesare", axis=1)

y = df["Patrule_Necesare"]

bins = [0, 5, 10, 20, 100]
labels = [0, 1, 2, 3]

y_clasa = pd.cut(y, bins=bins, labels=labels)

mask = y_clasa.notna()

X = X[mask]
y_clasa = y_clasa[mask]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_clasa,
    test_size=0.2,
    random_state=42
)

# =========================================================
# MODELE ML
# =========================================================

dt_model = DecisionTreeClassifier(max_depth=5)

dt_model.fit(X_train, y_train)

dt_pred = dt_model.predict(X_test)

dt_acc = accuracy_score(y_test, dt_pred)

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)

rf_acc = accuracy_score(y_test, rf_pred)

svm_model = SVC()

svm_model.fit(X_train, y_train)

svm_pred = svm_model.predict(X_test)

svm_acc = accuracy_score(y_test, svm_pred)

# =========================================================
# FUNCTII
# =========================================================

def afisare_statistici():

    text.delete(1.0, tk.END)

    text.insert(tk.END, "=== STATISTICI ACTUALIZATE ===\n\n")

    text.insert(tk.END, str(df.describe()))

# =========================================================
# FORMULAR
# =========================================================

def deschide_formular():

    fereastra = tk.Toplevel(root)

    fereastra.title("Planificare Tura")

    fereastra.geometry("700x750")

    labels = [
        "Total Angajati",
        "Liberi",
        "Medical",
        "Concediu",
        "Rezerve",
        "Disponibili",
        "Masini Disponibile"
    ]

    entries = []

    for label in labels:

        tk.Label(
            fereastra,
            text=label,
            font=("Arial", 10, "bold")
        ).pack(pady=4)

        entry = tk.Entry(fereastra, width=30)

        entry.pack()

        entries.append(entry)

    # =====================================================
    # EVENIMENTE
    # =====================================================

    tk.Label(
        fereastra,
        text="Evenimente pentru tura",
        font=("Arial", 12, "bold")
    ).pack(pady=10)

    frame_evenimente = tk.Frame(fereastra)

    frame_evenimente.pack()

    evenimente = []

    def adauga_eveniment():

        frame = tk.Frame(frame_evenimente)

        frame.pack(pady=5)

        tip_var = tk.StringVar(value="Meci Fotbal")

        tip_menu = tk.OptionMenu(
            frame,
            tip_var,
            "Meci Fotbal",
            "Meci Handbal",
            "Concert",
            "Parc Auto",
            "Patrula Oras",
            "Urgenta"
        )

        tip_menu.pack(side=tk.LEFT, padx=5)

        ora_entry = tk.Entry(frame, width=10)

        ora_entry.insert(0, "Ora")

        ora_entry.pack(side=tk.LEFT, padx=5)

        patrule_entry = tk.Entry(frame, width=12)

        patrule_entry.insert(0, "Patrule")

        patrule_entry.pack(side=tk.LEFT, padx=5)

        evenimente.append({
            "tip": tip_var,
            "ora": ora_entry,
            "patrule": patrule_entry
        })

    tk.Button(
        fereastra,
        text="+ Adauga Eveniment",
        command=adauga_eveniment,
        bg="blue",
        fg="white"
    ).pack(pady=10)

    adauga_eveniment()

    # =====================================================
    # PREDICTIE
    # =====================================================

    def predictie_custom():

        global df

        try:

            total = int(entries[0].get())
            liberi = int(entries[1].get())
            medical = int(entries[2].get())
            concediu = int(entries[3].get())
            rezerve = int(entries[4].get())
            disponibili = int(entries[5].get())
            masini = int(entries[6].get())

            scor_evenimente = 0

            descriere = []

            for ev in evenimente:

                tip = ev["tip"].get()

                ora = ev["ora"].get()

                patrule = int(ev["patrule"].get())

                descriere.append(
                    f"{tip} - {ora} - {patrule} patrule"
                )

                scor_evenimente += patrule

            eveniment_principal = "Meci Fotbal"

            eveniment_encoded = encoder.transform(
                [eveniment_principal]
            )[0]

            date_noi = pd.DataFrame({

                "Total_Angajati": [total],
                "Liberi": [liberi],
                "Medical": [medical],
                "Concediu": [concediu],
                "Rezerve": [rezerve],
                "Disponibili": [disponibili],
                "Masini_Disponibile": [masini],
                "Eveniment": [eveniment_encoded]

            })

            predictie = rf_model.predict(date_noi)

            # =============================================
            # ACTUALIZARE AUTOMATA STATISTICI
            # =============================================

            df.loc[len(df)] = [
                total,
                liberi,
                medical,
                concediu,
                rezerve,
                disponibili,
                masini,
                eveniment_encoded,
                scor_evenimente
            ]

            mesaj = (
                f"Predictie Clasa Patrule: {predictie[0]}\n\n"
                f"Evenimente Introduse:\n\n"
                + "\n".join(descriere)
            )

            messagebox.showinfo(
                "Planificare Tura",
                mesaj
            )

        except Exception as eroare:

            messagebox.showerror(
                "Eroare",
                f"Date invalide!\n\n{eroare}"
            )

    tk.Button(
        fereastra,
        text="Genereaza Planificare",
        command=predictie_custom,
        bg="green",
        fg="white",
        font=("Arial", 11, "bold")
    ).pack(pady=20)

# =========================================================
# GRAFICE
# =========================================================

def distributie_patrule():

    plt.figure(figsize=(10, 6))

    sns.histplot(df["Patrule_Necesare"], bins=15)

    plt.title("Distributia Patrulelor Necesare")

    plt.xlabel("Numar Patrule")

    plt.ylabel("Frecventa")

    plt.show()

def heatmap_corelatii():

    plt.figure(figsize=(10, 7))

    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")

    plt.title("Corelatii")

    plt.show()

def comparatie_modele():

    rezultate = {
        "Decision Tree": dt_acc,
        "Random Forest": rf_acc,
        "SVM": svm_acc
    }

    plt.figure(figsize=(8, 5))

    plt.bar(rezultate.keys(), rezultate.values())

    plt.title("Comparatie Algoritmi")

    plt.ylabel("Accuracy")

    plt.show()

def matrice_confuzie():

    cm = confusion_matrix(y_test, rf_pred)

    plt.figure(figsize=(6, 5))

    sns.heatmap(
        cm,
        annot=True,
        fmt='d',
        cmap='Blues'
    )

    plt.title("Matrice Confuzie")

    plt.show()

def raport_final():

    raport = classification_report(y_test, rf_pred)

    text.delete(1.0, tk.END)

    text.insert(tk.END, raport)

# =========================================================
# GUI
# =========================================================

root = tk.Tk()

root.title("Gestionarea Grupelor si Patrulelor")

root.geometry("1000x650")

# =========================================================
# MENIU
# =========================================================

menubar = tk.Menu(root)

meniul_principal = tk.Menu(
    menubar,
    tearoff=0
)

meniul_principal.add_command(
    label="Statistici",
    command=afisare_statistici
)

meniul_principal.add_command(
    label="Introducere Date Manual",
    command=deschide_formular
)

meniul_principal.add_command(
    label="Distributie Patrule",
    command=distributie_patrule
)

meniul_principal.add_command(
    label="Heatmap Corelatii",
    command=heatmap_corelatii
)

meniul_principal.add_command(
    label="Comparatie Modele",
    command=comparatie_modele
)

meniul_principal.add_command(
    label="Matrice Confuzie",
    command=matrice_confuzie
)

meniul_principal.add_command(
    label="Raport Final",
    command=raport_final
)

meniul_principal.add_separator()

meniul_principal.add_command(
    label="Iesire",
    command=root.quit
)

menubar.add_cascade(
    label="⋮",
    menu=meniul_principal
)

root.config(menu=menubar)

# =========================================================
# ZONA TEXT
# =========================================================

text = tk.Text(
    root,
    font=("Consolas", 11)
)

text.pack(
    fill=tk.BOTH,
    expand=True,
    padx=10,
    pady=10
)

# =========================================================
# START
# =========================================================

root.mainloop()