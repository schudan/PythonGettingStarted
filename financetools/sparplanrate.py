def sparplan(stueckzahl, eurKurs, eurUsdKurs):
    """Berechnet die Eingaben vom TradeRepublic-Ausdruck für die Eintragung 
    in PortfolioPerformance """
    #ausgabe der Parameter
    print("Berechne Sparplandaten für PortfolioPerformance")
    print ("es wurden " + str(stueckzahl) + " Aktien zu " + str(eurKurs) + " gekauft.")
    print ("dabei war der aktuel EUR/USD Umrechnungskurs " + str(eurUsdKurs))
    #berechnungen
    dollarKurs= eurKurs * eurUsdKurs
    eurKosten = stueckzahl * eurKurs
    #ausgabe der Ergebnisse
    print("Kurs der Aktie in Dollar: " + str(dollarKurs))
    print("Kosten in EUR: " + str(eurKosten))

#programmstart
#eingabe erfragen
print("Stückzahl der Aktie") 
stueckzahl = float(input())
print ("EUR Kurs der Aktie") 
eurKurs = float(input())
print ("EUR/USD Kurs")
eurUsdKurs = float(input())

#berechnen per funktion
sparplan(stueckzahl, eurKurs, eurUsdKurs)