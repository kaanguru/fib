import yfinance as yf
import pandas as pd

tickers_dosya = pd.read_csv("./data/BistList.csv")
tum_hisseler = tickers_dosya["kod"]
uyumluHisseler = []
kaldirilmisHisseler = []


def fib_seviyeler_arasinda(hisse):
    # hisse için bir yıllık verileri çek
    try:
        df = yf.download(
            hisse + ".IS",
            period="1y",
            # interval="1h",
        )

        # Fibonacci sabitleri
        max_deger = df["Close"].max()
        min_deger = df["Close"].min()
        fark = max_deger - min_deger

        # Fibonacci seviyelerini belirle

        dorduncu_seviye = max_deger - fark * 0.618
        besinci_seviye = max_deger - fark * 0.786
        son_fiyat = df["Close"].iloc[-1]
        if son_fiyat > besinci_seviye and son_fiyat < dorduncu_seviye:
            return True
    except:
        kaldirilmisHisseler.append(hisse)


for hisse in tum_hisseler:
    if fib_seviyeler_arasinda(hisse):
        uyumluHisseler.append(hisse)

# Raporlama

print("Uyumlu hisseler:" + str(uyumluHisseler))
print(str(len(uyumluHisseler)) + " adet hisse fib uyumlu")

print("Kaldırılanlar hisseler:" + str(kaldirilmisHisseler))
print(str(len(kaldirilmisHisseler)) + " adet hisse kalkmış")

uyumluHisSerisi = pd.Series(uyumluHisseler)
uyumluHisSerisi.to_csv("./data/uyumlu-bist.csv")
kaldHisSerisi = pd.Series(kaldirilmisHisseler)
kaldHisSerisi.to_csv("./data/kalkmis-bist.csv")
