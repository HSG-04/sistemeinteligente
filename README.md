# Proiect Machine Learning – Gestionarea Grupelor și Patrulelor

## 1. Introducere și Motivație

Acest proiect urmărește dezvoltarea unei aplicații inteligente pentru gestionarea grupelor și patrulelor operative utilizând tehnici de Machine Learning. Ideea proiectului a pornit de la necesitatea organizării eficiente a resurselor umane și logistice în situații reale precum meciuri sportive, concerte, urgențe sau patrule urbane.

În cadrul proiectului au fost simulate date operaționale privind:

* numărul total de angajați;
* angajați liberi;
* personal în concediu;
* personal în rezervă;
* mașini disponibile;
* tipul evenimentului;
* necesarul de patrule.

Scopul principal al aplicației este estimarea automată a numărului necesar de patrule în funcție de situația operativă existentă.

Proiectul utilizează:

* Python;
* Scikit-Learn;
* Pandas;
* Matplotlib;
* Seaborn;
* Tkinter.

---

# 2. Descrierea Datelor și Contextul Proiectului

## 2.1 Structura setului de date

Setul de date este generat artificial pentru simularea activităților operative reale.

Număr de instanțe:

* 500 exemple.

Caracteristici:

* Total_Angajati
* Liberi
* Medical
* Concediu
* Rezerve
* Disponibili
* Masini_Disponibile
* Eveniment
* Patrule_Necesare

## 2.2 Tipuri de evenimente

În proiect au fost definite următoarele tipuri de evenimente:

* Normal
* Meci Fotbal
* Meci Handbal
* Concert
* Parc Auto
* Patrula Oras
* Urgenta

## 2.3 Problema abordată

Problema abordată este una de clasificare supervisată.

Modelul trebuie să determine clasa de patrule necesare pentru o anumită situație operativă.

Clasele sunt:

* 0 = necesar redus;
* 1 = necesar mediu;
* 2 = necesar ridicat;
* 3 = necesar critic.

---

# 3. Aspecte Teoretice

## 3.1 Machine Learning

Machine Learning reprezintă o ramură a inteligenței artificiale care permite sistemelor informatice să învețe din date fără a fi programate explicit.

În acest proiect s-au utilizat algoritmi de clasificare.

---

## 3.2 Decision Tree

Decision Tree construiește o structură arborescentă bazată pe reguli logice.

Avantaje:

* ușor de interpretat;
* rapid;
* explicabil.

Dezavantaje:

* poate produce overfitting.

---

## 3.3 Random Forest

Random Forest utilizează mai mulți arbori de decizie și combină rezultatele acestora.

Avantaje:

* acuratețe ridicată;
* rezistență la overfitting;
* performanțe stabile.

Acesta a fost modelul final ales.

---

## 3.4 Support Vector Machine (SVM)

SVM încearcă să găsească hiperplanul optim pentru separarea claselor.

Avantaje:

* bun pentru clasificări complexe;
* generalizare bună.

Dezavantaje:

* cost computațional ridicat;
* mai greu de interpretat.

---

# 4. Implementarea Proiectului

## 4.1 Prelucrarea datelor

Datele au fost:

* generate;
* validate;
* transformate;
* codificate.

Evenimentele textuale au fost transformate numeric utilizând LabelEncoder.

---

## 4.2 Împărțirea datelor

Datele au fost împărțite:

* 80% training;
* 20% testing.

Funcția utilizată:

```python
train_test_split()
```

---

## 4.3 Algoritmii utilizați

Au fost testați:

* Decision Tree;
* Random Forest;
* SVM.

---

## 4.4 Interfața grafică

Aplicația include:

* meniu cu 3 puncte;
* introducere manuală a turelor;
* adăugare multiple evenimente;
* generare predicții;
* statistici dinamice;
* grafice și heatmap-uri.

---

# 5. Testare și Validare

## 5.1 Metrici utilizate

Pentru evaluare s-au utilizat:

* Accuracy;
* Confusion Matrix;
* Precision;
* Recall;
* F1-Score.

---

## 5.2 Rezultate obținute

Rezultatele aproximative:

* Decision Tree: 85%-90%;
* Random Forest: 92%-97%;
* SVM: 88%-93%.

Random Forest a obținut cele mai bune performanțe.

---

# 6. Rezultate și Discuții

## 6.1 Performanțele modelului

Modelul Random Forest a demonstrat:

* stabilitate;
* acuratețe ridicată;
* rezistență la zgomot.

---

## 6.2 Importanța caracteristicilor

Cele mai importante caracteristici:

* Disponibili;
* Tipul evenimentului;
* Mașini disponibile;
* Rezerve.

---

## 6.3 Analiza erorilor

Modelul poate produce erori:

* în situații extreme;
* la combinații rare de evenimente;
* la valori foarte mari ale patrulelor.

---

# 7. Concluzii

În cadrul proiectului am învățat:

* dezvoltarea unui sistem ML complet;
* prelucrarea datelor;
* evaluarea algoritmilor;
* dezvoltarea unei aplicații GUI;
* interpretarea rezultatelor.

---

# 8. Limitări

Limitările proiectului:

* date generate artificial;
* lipsa unor date reale operative;
* lipsa unei baze de date externe.

---

# 9. Îmbunătățiri viitoare

Posibile îmbunătățiri:

* conectare la baze de date reale;
* utilizarea rețelelor neuronale;
* integrare GPS;
* generare automată de trasee;
* sistem live de monitorizare.

---

# 10. Referințe Bibliografice

1. Tom Mitchell – Machine Learning.
2. Ian Goodfellow – Deep Learning.
3. Christopher Bishop – Pattern Recognition and Machine Learning.
4. Aurélien Géron – Hands-On Machine Learning.
5. Trevor Hastie – The Elements of Statistical Learning.
6. Scikit-Learn Documentation.
7. Pandas Documentation.
8. Python Documentation.
9. Random Forests – Leo Breiman.
10. Support Vector Machines – Cortes & Vapnik.
