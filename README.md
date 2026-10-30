# Canadian Beer – Datenanalyse 🍺

Analyse des **Canadian-Beer-Datensatzes** im Rahmen einer Statistik- und Datenvisualisierungsaufgabe.

## Ziel

Wir untersuchen unter anderem die Verteilung von Bierarten und Brauereien, Kennzahlen, Unterschiede zwischen Ale und Stout sowie die Zusammenhänge von Score, Ranking und Alkoholgehalt. Die Ergebnisse werden mit statistischen Auswertungen und Diagrammen dargestellt.

## Datensatz

- **Quelle:** [Top 100 Canadian Beers – Kaggle](https://www.kaggle.com/datasets/shwong/top-100-canadian-beers)
- **Datei:** `canadian_beers.csv`

## Verwendete Python-Bibliotheken

| Bibliothek | Zweck |
| --- | --- |
| `pandas` | Daten einlesen, aufbereiten und auswerten |
| `numpy` | Numerische Berechnungen |
| `seaborn` | Statistische Visualisierungen |
| `matplotlib` | Diagramme erstellen und anpassen |
| `scipy` | Statistische Verfahren und Tests |

## Installation

**Voraussetzung:** Python 3 und pip.

#### Bibliotheken installieren:

   ```bash
   python3 -m pip install -r requirements.txt
   ```

In der `requirements.txt` stehen bewusst **keine festen Versionsnummern**. Bei einer Neuinstallation wählt pip die neuesten verfügbaren stabilen Versionen aus, soweit sie mit der verwendeten Python-Version und den übrigen Abhängigkeiten kompatibel sind.

Um **bereits installierte Bibliotheken zu aktualisieren**:

```bash
python3 -m pip install --upgrade -r requirements.txt
```