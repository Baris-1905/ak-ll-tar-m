
# -*- coding: utf-8 -*-
import streamlit as st

mahalle_verisi = {
  "Acarköy": {
    "Enlem": 39.3,
    "Boylam": 41.6,
    "Rakım (m)": 1700.0,
    "Sıcaklık (°C)": 8.5
  },
  "Akbayır": {
    "Enlem": 39.300999999999995,
    "Boylam": 41.601,
    "Rakım (m)": 1705.0,
    "Sıcaklık (°C)": 8.4
  },
  "Akçamelik": {
    "Enlem": 39.302,
    "Boylam": 41.602000000000004,
    "Rakım (m)": 1710.0,
    "Sıcaklık (°C)": 8.3
  },
  "Akgelin": {
    "Enlem": 39.303,
    "Boylam": 41.603,
    "Rakım (m)": 1715.0,
    "Sıcaklık (°C)": 8.2
  },
  "Akgöze": {
    "Enlem": 39.303999999999995,
    "Boylam": 41.604,
    "Rakım (m)": 1720.0,
    "Sıcaklık (°C)": 8.1
  },
  "Akören": {
    "Enlem": 39.305,
    "Boylam": 41.605000000000004,
    "Rakım (m)": 1725.0,
    "Sıcaklık (°C)": 8.5
  },
  "Alaca": {
    "Enlem": 39.306,
    "Boylam": 41.606,
    "Rakım (m)": 1730.0,
    "Sıcaklık (°C)": 8.4
  },
  "Alagöz": {
    "Enlem": 39.306999999999995,
    "Boylam": 41.607,
    "Rakım (m)": 1735.0,
    "Sıcaklık (°C)": 8.3
  },
  "Alikırı": {
    "Enlem": 39.308,
    "Boylam": 41.608000000000004,
    "Rakım (m)": 1740.0,
    "Sıcaklık (°C)": 8.2
  },
  "Alınteri": {
    "Enlem": 39.309,
    "Boylam": 41.609,
    "Rakım (m)": 1745.0,
    "Sıcaklık (°C)": 8.1
  },
  "Altınpınar": {
    "Enlem": 39.309999999999995,
    "Boylam": 41.61,
    "Rakım (m)": 1750.0,
    "Sıcaklık (°C)": 8.5
  },
  "Arpadere": {
    "Enlem": 39.311,
    "Boylam": 41.611000000000004,
    "Rakım (m)": 1755.0,
    "Sıcaklık (°C)": 8.4
  },
  "Aşağıkayabaşı": {
    "Enlem": 39.312,
    "Boylam": 41.612,
    "Rakım (m)": 1760.0,
    "Sıcaklık (°C)": 8.3
  },
  "Avcılar": {
    "Enlem": 39.312999999999995,
    "Boylam": 41.613,
    "Rakım (m)": 1765.0,
    "Sıcaklık (°C)": 8.2
  },
  "Bahçe": {
    "Enlem": 39.314,
    "Boylam": 41.614000000000004,
    "Rakım (m)": 1770.0,
    "Sıcaklık (°C)": 8.1
  },
  "Başköy": {
    "Enlem": 39.315,
    "Boylam": 41.615,
    "Rakım (m)": 1775.0,
    "Sıcaklık (°C)": 8.5
  },
  "Bayırköy": {
    "Enlem": 39.315999999999995,
    "Boylam": 41.616,
    "Rakım (m)": 1780.0,
    "Sıcaklık (°C)": 8.4
  },
  "Bellitaş": {
    "Enlem": 39.317,
    "Boylam": 41.617000000000004,
    "Rakım (m)": 1785.0,
    "Sıcaklık (°C)": 8.3
  },
  "Beyyurdu": {
    "Enlem": 39.318,
    "Boylam": 41.618,
    "Rakım (m)": 1790.0,
    "Sıcaklık (°C)": 8.2
  },
  "Burhanköy": {
    "Enlem": 39.318999999999996,
    "Boylam": 41.619,
    "Rakım (m)": 1795.0,
    "Sıcaklık (°C)": 8.1
  },
  "Çakmak": {
    "Enlem": 39.32,
    "Boylam": 41.620000000000005,
    "Rakım (m)": 1800.0,
    "Sıcaklık (°C)": 8.5
  },
  "Çamurlu": {
    "Enlem": 39.321,
    "Boylam": 41.621,
    "Rakım (m)": 1805.0,
    "Sıcaklık (°C)": 8.4
  },
  "Çatak": {
    "Enlem": 39.321999999999996,
    "Boylam": 41.622,
    "Rakım (m)": 1810.0,
    "Sıcaklık (°C)": 8.3
  },
  "Çilligöl": {
    "Enlem": 39.323,
    "Boylam": 41.623000000000005,
    "Rakım (m)": 1815.0,
    "Sıcaklık (°C)": 8.2
  },
  "Dağçayırı": {
    "Enlem": 39.324,
    "Boylam": 41.624,
    "Rakım (m)": 1820.0,
    "Sıcaklık (°C)": 8.1
  },
  "Demirci": {
    "Enlem": 39.324999999999996,
    "Boylam": 41.625,
    "Rakım (m)": 1700.0,
    "Sıcaklık (°C)": 8.5
  },
  "Derince": {
    "Enlem": 39.326,
    "Boylam": 41.626000000000005,
    "Rakım (m)": 1705.0,
    "Sıcaklık (°C)": 8.4
  },
  "Dervişali": {
    "Enlem": 39.327,
    "Boylam": 41.627,
    "Rakım (m)": 1710.0,
    "Sıcaklık (°C)": 8.3
  },
  "Dibekli": {
    "Enlem": 39.327999999999996,
    "Boylam": 41.628,
    "Rakım (m)": 1715.0,
    "Sıcaklık (°C)": 8.2
  },
  "Dikili": {
    "Enlem": 39.329,
    "Boylam": 41.629000000000005,
    "Rakım (m)": 1720.0,
    "Sıcaklık (°C)": 8.1
  },
  "Doğanköy": {
    "Enlem": 39.33,
    "Boylam": 41.63,
    "Rakım (m)": 1725.0,
    "Sıcaklık (°C)": 8.5
  },
  "Döllük": {
    "Enlem": 39.330999999999996,
    "Boylam": 41.631,
    "Rakım (m)": 1730.0,
    "Sıcaklık (°C)": 8.4
  },
  "Dumlu": {
    "Enlem": 39.331999999999994,
    "Boylam": 41.632,
    "Rakım (m)": 1735.0,
    "Sıcaklık (°C)": 8.3
  },
  "Düzce": {
    "Enlem": 39.333,
    "Boylam": 41.633,
    "Rakım (m)": 1740.0,
    "Sıcaklık (°C)": 8.2
  },
  "Ekincik": {
    "Enlem": 39.333999999999996,
    "Boylam": 41.634,
    "Rakım (m)": 1745.0,
    "Sıcaklık (°C)": 8.1
  },
  "Erbeyli": {
    "Enlem": 39.334999999999994,
    "Boylam": 41.635,
    "Rakım (m)": 1750.0,
    "Sıcaklık (°C)": 8.5
  },
  "Erikdere": {
    "Enlem": 39.336,
    "Boylam": 41.636,
    "Rakım (m)": 1755.0,
    "Sıcaklık (°C)": 8.4
  },
  "Esenevler": {
    "Enlem": 39.336999999999996,
    "Boylam": 41.637,
    "Rakım (m)": 1760.0,
    "Sıcaklık (°C)": 8.3
  },
  "Eskiköy": {
    "Enlem": 39.337999999999994,
    "Boylam": 41.638,
    "Rakım (m)": 1765.0,
    "Sıcaklık (°C)": 8.2
  },
  "Gedik": {
    "Enlem": 39.339,
    "Boylam": 41.639,
    "Rakım (m)": 1770.0,
    "Sıcaklık (°C)": 8.1
  },
  "Göller": {
    "Enlem": 39.339999999999996,
    "Boylam": 41.64,
    "Rakım (m)": 1775.0,
    "Sıcaklık (°C)": 8.5
  },
  "Günbatan": {
    "Enlem": 39.340999999999994,
    "Boylam": 41.641,
    "Rakım (m)": 1780.0,
    "Sıcaklık (°C)": 8.4
  },
  "Güzelhisar": {
    "Enlem": 39.342,
    "Boylam": 41.642,
    "Rakım (m)": 1785.0,
    "Sıcaklık (°C)": 8.3
  },
  "Halilçavuş": {
    "Enlem": 39.342999999999996,
    "Boylam": 41.643,
    "Rakım (m)": 1790.0,
    "Sıcaklık (°C)": 8.2
  },
  "Hanköy": {
    "Enlem": 39.343999999999994,
    "Boylam": 41.644,
    "Rakım (m)": 1795.0,
    "Sıcaklık (°C)": 8.1
  },
  "Hızırilyas": {
    "Enlem": 39.345,
    "Boylam": 41.645,
    "Rakım (m)": 1800.0,
    "Sıcaklık (°C)": 8.5
  },
  "İncesu": {
    "Enlem": 39.346,
    "Boylam": 41.646,
    "Rakım (m)": 1805.0,
    "Sıcaklık (°C)": 8.4
  },
  "Karakaya": {
    "Enlem": 39.346999999999994,
    "Boylam": 41.647,
    "Rakım (m)": 1810.0,
    "Sıcaklık (°C)": 8.3
  },
  "Karapınar": {
    "Enlem": 39.348,
    "Boylam": 41.648,
    "Rakım (m)": 1815.0,
    "Sıcaklık (°C)": 8.2
  },
  "Kavaklı": {
    "Enlem": 39.349,
    "Boylam": 41.649,
    "Rakım (m)": 1820.0,
    "Sıcaklık (°C)": 8.1
  },
  "Kazancı": {
    "Enlem": 39.349999999999994,
    "Boylam": 41.65,
    "Rakım (m)": 1700.0,
    "Sıcaklık (°C)": 8.5
  },
  "Keklik": {
    "Enlem": 39.351,
    "Boylam": 41.651,
    "Rakım (m)": 1705.0,
    "Sıcaklık (°C)": 8.4
  },
  "Kılıçören": {
    "Enlem": 39.352,
    "Boylam": 41.652,
    "Rakım (m)": 1710.0,
    "Sıcaklık (°C)": 8.3
  },
  "Kızılören": {
    "Enlem": 39.352999999999994,
    "Boylam": 41.653,
    "Rakım (m)": 1715.0,
    "Sıcaklık (°C)": 8.2
  },
  "Koçköy": {
    "Enlem": 39.354,
    "Boylam": 41.654,
    "Rakım (m)": 1720.0,
    "Sıcaklık (°C)": 8.1
  },
  "Konak": {
    "Enlem": 39.355,
    "Boylam": 41.655,
    "Rakım (m)": 1725.0,
    "Sıcaklık (°C)": 8.5
  },
  "Köprübaşı": {
    "Enlem": 39.355999999999995,
    "Boylam": 41.656,
    "Rakım (m)": 1730.0,
    "Sıcaklık (°C)": 8.4
  },
  "Kurugöl": {
    "Enlem": 39.357,
    "Boylam": 41.657000000000004,
    "Rakım (m)": 1735.0,
    "Sıcaklık (°C)": 8.3
  },
  "Kümbet": {
    "Enlem": 39.358,
    "Boylam": 41.658,
    "Rakım (m)": 1740.0,
    "Sıcaklık (°C)": 8.2
  },
  "Kutluca": {
    "Enlem": 39.358999999999995,
    "Boylam": 41.659,
    "Rakım (m)": 1745.0,
    "Sıcaklık (°C)": 8.1
  },
  "Meşeli": {
    "Enlem": 39.36,
    "Boylam": 41.660000000000004,
    "Rakım (m)": 1750.0,
    "Sıcaklık (°C)": 8.5
  },
  "Mirzaoğlu": {
    "Enlem": 39.361,
    "Boylam": 41.661,
    "Rakım (m)": 1755.0,
    "Sıcaklık (°C)": 8.4
  },
  "Mutluca": {
    "Enlem": 39.361999999999995,
    "Boylam": 41.662,
    "Rakım (m)": 1760.0,
    "Sıcaklık (°C)": 8.3
  },
  "Ortaklar": {
    "Enlem": 39.363,
    "Boylam": 41.663000000000004,
    "Rakım (m)": 1765.0,
    "Sıcaklık (°C)": 8.2
  },
  "Oymak": {
    "Enlem": 39.364,
    "Boylam": 41.664,
    "Rakım (m)": 1770.0,
    "Sıcaklık (°C)": 8.1
  },
  "Öğütlü": {
    "Enlem": 39.364999999999995,
    "Boylam": 41.665,
    "Rakım (m)": 1775.0,
    "Sıcaklık (°C)": 8.5
  },
  "Sağlık": {
    "Enlem": 39.366,
    "Boylam": 41.666000000000004,
    "Rakım (m)": 1780.0,
    "Sıcaklık (°C)": 8.4
  },
  "Saraycık": {
    "Enlem": 39.367,
    "Boylam": 41.667,
    "Rakım (m)": 1785.0,
    "Sıcaklık (°C)": 8.3
  },
  "Söğütlü": {
    "Enlem": 39.367999999999995,
    "Boylam": 41.668,
    "Rakım (m)": 1790.0,
    "Sıcaklık (°C)": 8.2
  },
  "Söğütözü": {
    "Enlem": 39.369,
    "Boylam": 41.669000000000004,
    "Rakım (m)": 1795.0,
    "Sıcaklık (°C)": 8.1
  },
  "Sorkunlu": {
    "Enlem": 39.37,
    "Boylam": 41.67,
    "Rakım (m)": 1800.0,
    "Sıcaklık (°C)": 8.5
  },
  "Sürekli": {
    "Enlem": 39.370999999999995,
    "Boylam": 41.671,
    "Rakım (m)": 1805.0,
    "Sıcaklık (°C)": 8.4
  },
  "Şahinkaya": {
    "Enlem": 39.372,
    "Boylam": 41.672000000000004,
    "Rakım (m)": 1810.0,
    "Sıcaklık (°C)": 8.3
  },
  "Şenlik": {
    "Enlem": 39.373,
    "Boylam": 41.673,
    "Rakım (m)": 1815.0,
    "Sıcaklık (°C)": 8.2
  },
  "Taşbulak": {
    "Enlem": 39.373999999999995,
    "Boylam": 41.674,
    "Rakım (m)": 1820.0,
    "Sıcaklık (°C)": 8.1
  },
  "Taşlıdere": {
    "Enlem": 39.375,
    "Boylam": 41.675000000000004,
    "Rakım (m)": 1700.0,
    "Sıcaklık (°C)": 8.5
  },
  "Tavşanlı": {
    "Enlem": 39.376,
    "Boylam": 41.676,
    "Rakım (m)": 1705.0,
    "Sıcaklık (°C)": 8.4
  },
  "Tekyamaç": {
    "Enlem": 39.376999999999995,
    "Boylam": 41.677,
    "Rakım (m)": 1710.0,
    "Sıcaklık (°C)": 8.3
  },
  "Toprakkale": {
    "Enlem": 39.378,
    "Boylam": 41.678000000000004,
    "Rakım (m)": 1715.0,
    "Sıcaklık (°C)": 8.2
  },
  "Uluköy": {
    "Enlem": 39.379,
    "Boylam": 41.679,
    "Rakım (m)": 1720.0,
    "Sıcaklık (°C)": 8.1
  },
  "Uysal": {
    "Enlem": 39.379999999999995,
    "Boylam": 41.68,
    "Rakım (m)": 1725.0,
    "Sıcaklık (°C)": 8.5
  },
  "Uzunkavak": {
    "Enlem": 39.381,
    "Boylam": 41.681000000000004,
    "Rakım (m)": 1730.0,
    "Sıcaklık (°C)": 8.4
  },
  "Ünlükaya": {
    "Enlem": 39.382,
    "Boylam": 41.682,
    "Rakım (m)": 1735.0,
    "Sıcaklık (°C)": 8.3
  },
  "Yalınca": {
    "Enlem": 39.382999999999996,
    "Boylam": 41.683,
    "Rakım (m)": 1740.0,
    "Sıcaklık (°C)": 8.2
  },
  "Yazılıtaş": {
    "Enlem": 39.384,
    "Boylam": 41.684000000000005,
    "Rakım (m)": 1745.0,
    "Sıcaklık (°C)": 8.1
  },
  "Yelpınar": {
    "Enlem": 39.385,
    "Boylam": 41.685,
    "Rakım (m)": 1750.0,
    "Sıcaklık (°C)": 8.5
  },
  "Yeniçayır": {
    "Enlem": 39.385999999999996,
    "Boylam": 41.686,
    "Rakım (m)": 1755.0,
    "Sıcaklık (°C)": 8.4
  },
  "Yeniköy": {
    "Enlem": 39.387,
    "Boylam": 41.687000000000005,
    "Rakım (m)": 1760.0,
    "Sıcaklık (°C)": 8.3
  },
  "Yeşilbağlar": {
    "Enlem": 39.388,
    "Boylam": 41.688,
    "Rakım (m)": 1765.0,
    "Sıcaklık (°C)": 8.2
  },
  "Yeşildere": {
    "Enlem": 39.388999999999996,
    "Boylam": 41.689,
    "Rakım (m)": 1770.0,
    "Sıcaklık (°C)": 8.1
  },
  "Yeşilyurt": {
    "Enlem": 39.39,
    "Boylam": 41.690000000000005,
    "Rakım (m)": 1775.0,
    "Sıcaklık (°C)": 8.5
  },
  "Yumrutepe": {
    "Enlem": 39.391,
    "Boylam": 41.691,
    "Rakım (m)": 1780.0,
    "Sıcaklık (°C)": 8.4
  },
  "Yumaklı": {
    "Enlem": 39.391999999999996,
    "Boylam": 41.692,
    "Rakım (m)": 1785.0,
    "Sıcaklık (°C)": 8.3
  },
  "Yüceyurt": {
    "Enlem": 39.393,
    "Boylam": 41.693000000000005,
    "Rakım (m)": 1790.0,
    "Sıcaklık (°C)": 8.2
  },
  "Yukarıkayabaşı": {
    "Enlem": 39.394,
    "Boylam": 41.694,
    "Rakım (m)": 1795.0,
    "Sıcaklık (°C)": 8.1
  },
  "Yuva": {
    "Enlem": 39.394999999999996,
    "Boylam": 41.695,
    "Rakım (m)": 1800.0,
    "Sıcaklık (°C)": 8.5
  },
  "Yürektaşı": {
    "Enlem": 39.395999999999994,
    "Boylam": 41.696,
    "Rakım (m)": 1805.0,
    "Sıcaklık (°C)": 8.4
  },
  "Ziyaret": {
    "Enlem": 39.397,
    "Boylam": 41.697,
    "Rakım (m)": 1810.0,
    "Sıcaklık (°C)": 8.3
  }
}

st.title("Akıllı Tarım Karar Destek Sistemi")

secili_mahalle = st.selectbox("Mahalle Seçiniz", list(mahalle_verisi.keys()))
if secili_mahalle:
    v = mahalle_verisi[secili_mahalle]
    st.markdown(f"**Seçilen Mahalle:** {secili_mahalle}")
    st.markdown(f"**Enlem:** {v['Enlem']}")
    st.markdown(f"**Boylam:** {v['Boylam']}")
    st.markdown(f"**Rakım:** {v['Rakım (m)']} m")
    st.markdown(f"**Sıcaklık:** {v['Sıcaklık (°C)']} °C")
