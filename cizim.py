import yfinance as yf
import matplotlib.pyplot as plt

def fib_seviyeleri(hisse):
    # hisse için bir yıllık verileri çek
  df = yf.download( hisse, period = "1y" )

  # Fibonacci sabitleri
  max_value = df['Close'].max()
  min_value = df['Close'].min()
  difference = max_value - min_value

  # Fibonacci seviyelerini belirle
  first_level = max_value - difference * 0.236
  second_level = max_value - difference * 0.382
  third_level = max_value - difference * 0.5
  fourth_level = max_value - difference * 0.618

  # tam değerleri yazdır
  print('Yüzde Seviyeleri \t Fiyat')
  print('0.00%\t\t', round(max_value, 3))
  print('23.6\t\t', round(first_level, 3))
  print('38.2%\t\t', round(second_level, 3))
  print('50%\t\t', round(third_level, 3))
  print('61.8%\t\t', round(fourth_level, 3))
  print('100.00%\t\t', round(min_value, 3))

  # Fibonacci grafiğini çiz
  plot_title =   hisse +' İçin Fibonacci Geri Çekilmesi '
  fig = plt.figure(figsize=(22.5, 12.5))
  plt.title(plot_title, fontsize=30)
  ax = fig.add_subplot(111)
  plt.plot(df.index, df['Close'])
  plt.axhline(max_value, linestyle='--', alpha=0.5, color='purple')
  ax.fill_between(df.index, max_value, first_level, color='purple', alpha=0.2)

  # alanları doldur
  plt.axhline(first_level, linestyle='--', alpha=0.5, color='blue')
  ax.fill_between(df.index, first_level, second_level, color='blue', alpha=0.2)

  plt.axhline(second_level, linestyle='--', alpha=0.5, color='green')
  ax.fill_between(df.index, second_level, third_level, color='green', alpha=0.2)

  plt.axhline(third_level, linestyle='--', alpha=0.5, color='red')
  ax.fill_between(df.index, third_level, fourth_level, color='red', alpha=0.2)

  plt.axhline(fourth_level, linestyle='--', alpha=0.5, color='orange')
  ax.fill_between(df.index, fourth_level, min_value, color='orange', alpha=0.2)

  plt.axhline(min_value, linestyle='--', alpha=0.5, color='yellow')
  plt.xlabel('Tarih', fontsize=20)
  plt.ylabel('Kapanış fiyatı $', fontsize=20)
  plt.show()

fib_seviyeleri('TSLA')

