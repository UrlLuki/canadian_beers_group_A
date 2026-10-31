import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
import scipy

beers_original = pd.read_csv("canadian_beers.csv")
print(beers_original.head())

# 1. (1 Punkt) Aus welchen Beobachtungen setzen sich die Daten zusammen? Beschreiben Sie diese
# kurz und überlegen Sie sich, welches Skalenniveau die einzelnen Beobachtungen haben.
# 2. (2 Punkte) Wie setzen sich die einzelnen Beobachtungen zusammen? Verwenden Sie Methoden
# für univariate Datensätze sinnvoll.
# 3. (1 Punkt) Ermitteln Sie Kennzahlen für die einzelnen Beobachtungen, die Ihnen sinnvoll
# erscheinen. (Lokation, Modus, Varianzen, Quantile…)
# 4. (2 Punkte) Ermitteln Sie die 3 häufigsten Brauereien und Bier Arten, die in diesem Datensatz
# vorkommen. Wie verteilen sich Rang und Score auf diese Brauereien und Arten von Bier? Das
# Bier welcher Brauerei und welcher Art würden Sie jemandem empfehlen, wenn Sie sich nach dem
# Score richten? (Betrachten Sie hier nur die 3 häufigsten Arten)
# 5. (2 Punkte) Fügen Sie eine Variable ein, die anzeigt, ob es sich um ein american style beer handelt
# (Tipp: Variable style). Wie siehen scores und rank in diesem Fall aus?
# 6. (3 Punkte) Untersuchen Sie die Unterschiede zwischen ‘Ale’ und ‘Stout’ Bieren.
# 7. (1 Punkt) Wie verhält sich das Ranking in Abhängigkeit vom Score und Alkoholgehalt? Ermitteln
# Sie, falls passend, den Korrelationskoeffizienten.
# 8. (3 Punkte) Untersuchen Sie den Score in Abhängigkeit der anderen Variablen. Welche Variablen
# haben Ihrer Meinung nach einen Einfluss?