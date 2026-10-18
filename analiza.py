import pandas as pd

def wczytaj_dane(sciezka):
    return pd.read_csv(
        sciezka,
        sep=";"
    )

def wyczysc_dane(df):
    wynik = df.copy()
    
    wynik["kanal"] = wynik["kanal"].str.strip().str.lower()
    return wynik

def podsumowanie(df):
    
    return {
        "liczba": int(df["wartosc"].count()),
        "suma": float(df["wartosc"].sum()),
        "srednia": float(df["wartosc"].mean()),
        "mediana": float(df["wartosc"].median())
    }

def sprzedaz_wg_kanalu(df):
    
    wynik = (
        df.groupby("kanal", as_index=False)["wartosc"]
        .sum()
        .rename(columns={"wartosc": "suma_sprzedazy"})
    )
    return wynik