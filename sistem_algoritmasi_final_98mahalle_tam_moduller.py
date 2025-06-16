
# -*- coding: utf-8 -*-
import streamlit as st

# Mahalle verisi
mahalle_verisi = {
  "ACARKÖY": {
    "Enlem": 39.4,
    "Boylam": 41.5,
    "Rakım (m)": 1650.0,
    "Sıcaklık (°C)": 7.5
  },
  "AKBAYIR": {
    "Enlem": 39.400999999999996,
    "Boylam": 41.501,
    "Rakım (m)": 1656.0,
    "Sıcaklık (°C)": 7.7
  },
  "AKÇAMELİK": {
    "Enlem": 39.402,
    "Boylam": 41.502,
    "Rakım (m)": 1662.0,
    "Sıcaklık (°C)": 7.9
  },
  "AKGELİN": {
    "Enlem": 39.403,
    "Boylam": 41.503,
    "Rakım (m)": 1668.0,
    "Sıcaklık (°C)": 8.1
  },
  "AKGÖZE": {
    "Enlem": 39.403999999999996,
    "Boylam": 41.504,
    "Rakım (m)": 1674.0,
    "Sıcaklık (°C)": 8.3
  },
  "AKÖREN": {
    "Enlem": 39.405,
    "Boylam": 41.505,
    "Rakım (m)": 1680.0,
    "Sıcaklık (°C)": 8.5
  },
  "ALACA": {
    "Enlem": 39.406,
    "Boylam": 41.506,
    "Rakım (m)": 1686.0,
    "Sıcaklık (°C)": 7.5
  },
  "ALAGÖZ": {
    "Enlem": 39.407,
    "Boylam": 41.507,
    "Rakım (m)": 1692.0,
    "Sıcaklık (°C)": 7.7
  },
  "ALINTERİ": {
    "Enlem": 39.408,
    "Boylam": 41.508,
    "Rakım (m)": 1698.0,
    "Sıcaklık (°C)": 7.9
  },
  "ALİKIRI ": {
    "Enlem": 39.409,
    "Boylam": 41.509,
    "Rakım (m)": 1704.0,
    "Sıcaklık (°C)": 8.1
  },
  "ALTINPINAR": {
    "Enlem": 39.41,
    "Boylam": 41.51,
    "Rakım (m)": 1710.0,
    "Sıcaklık (°C)": 8.3
  },
  "ARPADERESİ": {
    "Enlem": 39.411,
    "Boylam": 41.511,
    "Rakım (m)": 1716.0,
    "Sıcaklık (°C)": 8.5
  },
  "AŞAĞIKAYABAŞI": {
    "Enlem": 39.412,
    "Boylam": 41.512,
    "Rakım (m)": 1722.0,
    "Sıcaklık (°C)": 7.5
  },
  "AVCILAR": {
    "Enlem": 39.413,
    "Boylam": 41.513,
    "Rakım (m)": 1728.0,
    "Sıcaklık (°C)": 7.7
  },
  "BAHÇE": {
    "Enlem": 39.414,
    "Boylam": 41.514,
    "Rakım (m)": 1734.0,
    "Sıcaklık (°C)": 7.9
  },
  "BAŞKÖY": {
    "Enlem": 39.415,
    "Boylam": 41.515,
    "Rakım (m)": 1740.0,
    "Sıcaklık (°C)": 8.1
  },
  "BAYIRKÖY": {
    "Enlem": 39.416,
    "Boylam": 41.516,
    "Rakım (m)": 1746.0,
    "Sıcaklık (°C)": 8.3
  },
  "BELLİTAŞ": {
    "Enlem": 39.417,
    "Boylam": 41.517,
    "Rakım (m)": 1752.0,
    "Sıcaklık (°C)": 8.5
  },
  "BEYYURDU": {
    "Enlem": 39.418,
    "Boylam": 41.518,
    "Rakım (m)": 1758.0,
    "Sıcaklık (°C)": 7.5
  },
  "BURHANKÖY": {
    "Enlem": 39.419,
    "Boylam": 41.519,
    "Rakım (m)": 1764.0,
    "Sıcaklık (°C)": 7.7
  },
  "ÇAKMAK": {
    "Enlem": 39.42,
    "Boylam": 41.52,
    "Rakım (m)": 1650.0,
    "Sıcaklık (°C)": 7.9
  },
  "ÇAMURLU": {
    "Enlem": 39.421,
    "Boylam": 41.521,
    "Rakım (m)": 1656.0,
    "Sıcaklık (°C)": 8.1
  },
  "ÇATAK": {
    "Enlem": 39.422,
    "Boylam": 41.522,
    "Rakım (m)": 1662.0,
    "Sıcaklık (°C)": 8.3
  },
  "ÇİLLİGÖL": {
    "Enlem": 39.423,
    "Boylam": 41.523,
    "Rakım (m)": 1668.0,
    "Sıcaklık (°C)": 8.5
  },
  "DAĞÇAYIRI": {
    "Enlem": 39.424,
    "Boylam": 41.524,
    "Rakım (m)": 1674.0,
    "Sıcaklık (°C)": 7.5
  },
  "DEMİRCİ": {
    "Enlem": 39.425,
    "Boylam": 41.525,
    "Rakım (m)": 1680.0,
    "Sıcaklık (°C)": 7.7
  },
  "DERİNCE": {
    "Enlem": 39.426,
    "Boylam": 41.526,
    "Rakım (m)": 1686.0,
    "Sıcaklık (°C)": 7.9
  },
  "DERVİŞALİ": {
    "Enlem": 39.427,
    "Boylam": 41.527,
    "Rakım (m)": 1692.0,
    "Sıcaklık (°C)": 8.1
  },
  "DİBEKLİ": {
    "Enlem": 39.428,
    "Boylam": 41.528,
    "Rakım (m)": 1698.0,
    "Sıcaklık (°C)": 8.3
  },
  "DİKİLİ": {
    "Enlem": 39.429,
    "Boylam": 41.529,
    "Rakım (m)": 1704.0,
    "Sıcaklık (°C)": 8.5
  },
  "DİVANHÜSEYİN": {
    "Enlem": 39.43,
    "Boylam": 41.53,
    "Rakım (m)": 1710.0,
    "Sıcaklık (°C)": 7.5
  },
  "ELMADALI": {
    "Enlem": 39.431,
    "Boylam": 41.531,
    "Rakım (m)": 1716.0,
    "Sıcaklık (°C)": 7.7
  },
  "ERBEYLİ": {
    "Enlem": 39.431999999999995,
    "Boylam": 41.532,
    "Rakım (m)": 1722.0,
    "Sıcaklık (°C)": 7.9
  },
  "ERDURAN": {
    "Enlem": 39.433,
    "Boylam": 41.533,
    "Rakım (m)": 1728.0,
    "Sıcaklık (°C)": 8.1
  },
  "ERENCE": {
    "Enlem": 39.434,
    "Boylam": 41.534,
    "Rakım (m)": 1734.0,
    "Sıcaklık (°C)": 8.3
  },
  "ESENLİ": {
    "Enlem": 39.434999999999995,
    "Boylam": 41.535,
    "Rakım (m)": 1740.0,
    "Sıcaklık (°C)": 8.5
  },
  "GÖLLER": {
    "Enlem": 39.436,
    "Boylam": 41.536,
    "Rakım (m)": 1746.0,
    "Sıcaklık (°C)": 7.5
  },
  "GÜLİSTAN": {
    "Enlem": 39.437,
    "Boylam": 41.537,
    "Rakım (m)": 1752.0,
    "Sıcaklık (°C)": 7.7
  },
  "GÜLLÜÇİMEN": {
    "Enlem": 39.437999999999995,
    "Boylam": 41.538,
    "Rakım (m)": 1758.0,
    "Sıcaklık (°C)": 7.9
  },
  "GÜRÇAYIR": {
    "Enlem": 39.439,
    "Boylam": 41.539,
    "Rakım (m)": 1764.0,
    "Sıcaklık (°C)": 8.1
  },
  "GÜZELDERE": {
    "Enlem": 39.44,
    "Boylam": 41.54,
    "Rakım (m)": 1650.0,
    "Sıcaklık (°C)": 8.3
  },
  "HALİLÇAVUŞ": {
    "Enlem": 39.440999999999995,
    "Boylam": 41.541,
    "Rakım (m)": 1656.0,
    "Sıcaklık (°C)": 8.5
  },
  "HAYRAN": {
    "Enlem": 39.442,
    "Boylam": 41.542,
    "Rakım (m)": 1662.0,
    "Sıcaklık (°C)": 7.5
  },
  "ILICAKÖY": {
    "Enlem": 39.443,
    "Boylam": 41.543,
    "Rakım (m)": 1668.0,
    "Sıcaklık (°C)": 7.7
  },
  "İSMAİL": {
    "Enlem": 39.443999999999996,
    "Boylam": 41.544,
    "Rakım (m)": 1674.0,
    "Sıcaklık (°C)": 7.9
  },
  "KALECİK": {
    "Enlem": 39.445,
    "Boylam": 41.545,
    "Rakım (m)": 1680.0,
    "Sıcaklık (°C)": 8.1
  },
  "KARAAĞAÇ": {
    "Enlem": 39.446,
    "Boylam": 41.546,
    "Rakım (m)": 1686.0,
    "Sıcaklık (°C)": 8.3
  },
  "KARABUDAK": {
    "Enlem": 39.446999999999996,
    "Boylam": 41.547,
    "Rakım (m)": 1692.0,
    "Sıcaklık (°C)": 8.5
  },
  "KARAKULA": {
    "Enlem": 39.448,
    "Boylam": 41.548,
    "Rakım (m)": 1698.0,
    "Sıcaklık (°C)": 7.5
  },
  "KARAMOLLA": {
    "Enlem": 39.449,
    "Boylam": 41.549,
    "Rakım (m)": 1704.0,
    "Sıcaklık (°C)": 7.7
  },
  "KAZANCI": {
    "Enlem": 39.449999999999996,
    "Boylam": 41.55,
    "Rakım (m)": 1710.0,
    "Sıcaklık (°C)": 7.9
  },
  "KETENCİ": {
    "Enlem": 39.451,
    "Boylam": 41.551,
    "Rakım (m)": 1716.0,
    "Sıcaklık (°C)": 8.1
  },
  "KISIK": {
    "Enlem": 39.452,
    "Boylam": 41.552,
    "Rakım (m)": 1722.0,
    "Sıcaklık (°C)": 8.3
  },
  "KIZILAHMET": {
    "Enlem": 39.452999999999996,
    "Boylam": 41.553,
    "Rakım (m)": 1728.0,
    "Sıcaklık (°C)": 8.5
  },
  "KIZMUSA": {
    "Enlem": 39.454,
    "Boylam": 41.554,
    "Rakım (m)": 1734.0,
    "Sıcaklık (°C)": 7.5
  },
  "KOLHİSAR": {
    "Enlem": 39.455,
    "Boylam": 41.555,
    "Rakım (m)": 1740.0,
    "Sıcaklık (°C)": 7.7
  },
  "KONGUR": {
    "Enlem": 39.455999999999996,
    "Boylam": 41.556,
    "Rakım (m)": 1746.0,
    "Sıcaklık (°C)": 7.9
  },
  "KÖPRÜBAŞI": {
    "Enlem": 39.457,
    "Boylam": 41.557,
    "Rakım (m)": 1752.0,
    "Sıcaklık (°C)": 8.1
  },
  "MEYDANKÖY": {
    "Enlem": 39.458,
    "Boylam": 41.558,
    "Rakım (m)": 1758.0,
    "Sıcaklık (°C)": 8.3
  },
  "MEZRA": {
    "Enlem": 39.458999999999996,
    "Boylam": 41.559,
    "Rakım (m)": 1764.0,
    "Sıcaklık (°C)": 8.5
  },
  "MOLLACELİL": {
    "Enlem": 39.46,
    "Boylam": 41.56,
    "Rakım (m)": 1650.0,
    "Sıcaklık (°C)": 7.5
  },
  "MOLLAKULAÇ": {
    "Enlem": 39.461,
    "Boylam": 41.561,
    "Rakım (m)": 1656.0,
    "Sıcaklık (°C)": 7.7
  },
  "MUTLUCA": {
    "Enlem": 39.461999999999996,
    "Boylam": 41.562,
    "Rakım (m)": 1662.0,
    "Sıcaklık (°C)": 7.9
  },
  "ORTAKÖY": {
    "Enlem": 39.463,
    "Boylam": 41.563,
    "Rakım (m)": 1668.0,
    "Sıcaklık (°C)": 8.1
  },
  "OVAÇEVİRME": {
    "Enlem": 39.464,
    "Boylam": 41.564,
    "Rakım (m)": 1674.0,
    "Sıcaklık (°C)": 8.3
  },
  "OVAKOZLU": {
    "Enlem": 39.464999999999996,
    "Boylam": 41.565,
    "Rakım (m)": 1680.0,
    "Sıcaklık (°C)": 8.5
  },
  "PARMAKSIZ": {
    "Enlem": 39.466,
    "Boylam": 41.566,
    "Rakım (m)": 1686.0,
    "Sıcaklık (°C)": 7.5
  },
  "PINARBAŞI": {
    "Enlem": 39.467,
    "Boylam": 41.567,
    "Rakım (m)": 1692.0,
    "Sıcaklık (°C)": 7.7
  },
  "PINARKÖY": {
    "Enlem": 39.467999999999996,
    "Boylam": 41.568,
    "Rakım (m)": 1698.0,
    "Sıcaklık (°C)": 7.9
  },
  "SALTEPE": {
    "Enlem": 39.469,
    "Boylam": 41.569,
    "Rakım (m)": 1704.0,
    "Sıcaklık (°C)": 8.1
  },
  "SANAYİ": {
    "Enlem": 39.47,
    "Boylam": 41.57,
    "Rakım (m)": 1710.0,
    "Sıcaklık (°C)": 8.3
  },
  "SARILI": {
    "Enlem": 39.471,
    "Boylam": 41.571,
    "Rakım (m)": 1716.0,
    "Sıcaklık (°C)": 8.5
  },
  "SILDIZ": {
    "Enlem": 39.472,
    "Boylam": 41.572,
    "Rakım (m)": 1722.0,
    "Sıcaklık (°C)": 7.5
  },
  "SÖĞÜTLÜ": {
    "Enlem": 39.473,
    "Boylam": 41.573,
    "Rakım (m)": 1728.0,
    "Sıcaklık (°C)": 7.7
  },
  "SULTANLI": {
    "Enlem": 39.474,
    "Boylam": 41.574,
    "Rakım (m)": 1734.0,
    "Sıcaklık (°C)": 7.9
  },
  "SUVARAN": {
    "Enlem": 39.475,
    "Boylam": 41.575,
    "Rakım (m)": 1740.0,
    "Sıcaklık (°C)": 8.1
  },
  "ŞAHABETTİNKÖY": {
    "Enlem": 39.476,
    "Boylam": 41.576,
    "Rakım (m)": 1746.0,
    "Sıcaklık (°C)": 8.3
  },
  "ŞAHVERDİ": {
    "Enlem": 39.477,
    "Boylam": 41.577,
    "Rakım (m)": 1752.0,
    "Sıcaklık (°C)": 8.5
  },
  "ŞALGAMKÖY": {
    "Enlem": 39.478,
    "Boylam": 41.578,
    "Rakım (m)": 1758.0,
    "Sıcaklık (°C)": 7.5
  },
  "TANIR": {
    "Enlem": 39.479,
    "Boylam": 41.579,
    "Rakım (m)": 1764.0,
    "Sıcaklık (°C)": 7.7
  },
  "TAPUKÖY": {
    "Enlem": 39.48,
    "Boylam": 41.58,
    "Rakım (m)": 1650.0,
    "Sıcaklık (°C)": 7.9
  },
  "TAŞBUDAK": {
    "Enlem": 39.481,
    "Boylam": 41.581,
    "Rakım (m)": 1656.0,
    "Sıcaklık (°C)": 8.1
  },
  "TELLİTEPE": {
    "Enlem": 39.482,
    "Boylam": 41.582,
    "Rakım (m)": 1662.0,
    "Sıcaklık (°C)": 8.3
  },
  "TİPİDERESİ": {
    "Enlem": 39.483,
    "Boylam": 41.583,
    "Rakım (m)": 1668.0,
    "Sıcaklık (°C)": 8.5
  },
  "TOPRAKKALE": {
    "Enlem": 39.484,
    "Boylam": 41.584,
    "Rakım (m)": 1674.0,
    "Sıcaklık (°C)": 7.5
  },
  "TORAMAN": {
    "Enlem": 39.485,
    "Boylam": 41.585,
    "Rakım (m)": 1680.0,
    "Sıcaklık (°C)": 7.7
  },
  "ULUÇAYIR": {
    "Enlem": 39.486,
    "Boylam": 41.586,
    "Rakım (m)": 1686.0,
    "Sıcaklık (°C)": 7.9
  },
  "UYANIK": {
    "Enlem": 39.487,
    "Boylam": 41.587,
    "Rakım (m)": 1692.0,
    "Sıcaklık (°C)": 8.1
  },
  "ÜNLÜCE": {
    "Enlem": 39.488,
    "Boylam": 41.588,
    "Rakım (m)": 1698.0,
    "Sıcaklık (°C)": 8.3
  },
  "YAMANLAR": {
    "Enlem": 39.489,
    "Boylam": 41.589,
    "Rakım (m)": 1704.0,
    "Sıcaklık (°C)": 8.5
  },
  "YAYLAKONAK": {
    "Enlem": 39.49,
    "Boylam": 41.59,
    "Rakım (m)": 1710.0,
    "Sıcaklık (°C)": 7.5
  },
  "YELPİZ": {
    "Enlem": 39.491,
    "Boylam": 41.591,
    "Rakım (m)": 1716.0,
    "Sıcaklık (°C)": 7.7
  },
  "YENİKENT": {
    "Enlem": 39.492,
    "Boylam": 41.592,
    "Rakım (m)": 1722.0,
    "Sıcaklık (°C)": 7.9
  },
  "YENİKÖY": {
    "Enlem": 39.493,
    "Boylam": 41.593,
    "Rakım (m)": 1728.0,
    "Sıcaklık (°C)": 8.1
  },
  "YEŞİLBAHÇE": {
    "Enlem": 39.494,
    "Boylam": 41.594,
    "Rakım (m)": 1734.0,
    "Sıcaklık (°C)": 8.3
  },
  "YEŞİLYAZI": {
    "Enlem": 39.495,
    "Boylam": 41.595,
    "Rakım (m)": 1740.0,
    "Sıcaklık (°C)": 8.5
  },
  "YOLÜSTÜ": {
    "Enlem": 39.495999999999995,
    "Boylam": 41.596,
    "Rakım (m)": 1746.0,
    "Sıcaklık (°C)": 7.5
  },
  "YUKARIKAYABAŞI": {
    "Enlem": 39.497,
    "Boylam": 41.597,
    "Rakım (m)": 1752.0,
    "Sıcaklık (°C)": 7.7
  }
}

st.title("Akıllı Tarım Karar Destek Sistemi")

# Mahalle seçimi
secili_mahalle = st.selectbox("Mahalle Seçiniz", list(mahalle_verisi.keys()))
if secili_mahalle:
    v = mahalle_verisi[secili_mahalle]
    st.markdown(f"**Seçilen Mahalle:** {secili_mahalle}")
    st.markdown(f"**Enlem:** {v['Enlem']}")
    st.markdown(f"**Boylam:** {v['Boylam']}")
    st.markdown(f"**Rakım:** {v['Rakım (m)']} m")
    st.markdown(f"**Sıcaklık:** {v['Sıcaklık (°C)']} °C")

# Ürün seçimi
urun = st.selectbox("Ürün Seçiniz", ["Arpa", "Buğday", "Fasulye"])
toprak_turu = st.selectbox("Toprak Türü", ["Killi", "Kumlu", "Tınlı", "Kireçli"])
sulama_yapildi = st.radio("Bu sezon sulama yaptınız mı?", ["Evet", "Hayır"])

# Sulama uyarısı
sulama_gereken_urunler = ["Fasulye", "Buğday"]
if urun in sulama_gereken_urunler and sulama_yapildi == "Hayır":
    st.error("⚠️ Bu ürün için sulama yapılması gereklidir. Lütfen sulama yapınız.")

# Gübreleme önerisi
st.subheader("Gübreleme Tavsiyesi")
if urun == "Arpa":
    st.markdown("- Azotlu Gübre: 20-25 kg/da")
    st.markdown("- Ahır Gübresi: 2-3 ton/da")
elif urun == "Buğday":
    st.markdown("- Üre (46% N): 25-30 kg/da")
    st.markdown("- Ahır Gübresi: 2 ton/da")
elif urun == "Fasulye":
    st.markdown("- Triple Süper Fosfat (43-44% P₂O₅): 20 kg/da")
    st.markdown("- Ahır Gübresi: 2.5 ton/da")

st.markdown(f"*Toprak Türü: **{toprak_turu}** olduğu için organik madde katkısı önemlidir.*")


# Arazi büyüklüğü girişi
st.subheader("Arazi Büyüklüğü")
arazi_buyuklugu = st.number_input("Araziniz kaç dekar?", min_value=1)

# FAO56 sulama takvimi (örnek evre bazlı)
st.subheader("FAO56 Sulama Takvimi")
if urun == "Buğday":
    evreler = [
        ("Çimlenme", 15),
        ("Kardeşlenme", 25),
        ("Sapa kalkma", 30),
        ("Başaklanma", 35),
        ("Olgunlaşma", 10)
    ]
elif urun == "Arpa":
    evreler = [
        ("Çimlenme", 10),
        ("Sapa kalkma", 20),
        ("Başaklanma", 25),
        ("Dolum", 30),
        ("Olgunlaşma", 8)
    ]
else:  # Fasulye
    evreler = [
        ("Çimlenme", 20),
        ("Vejetatif gelişim", 30),
        ("Çiçeklenme", 40),
        ("Bakla oluşumu", 35),
        ("Olgunlaşma", 15)
    ]
for evre, ihtiyac in evreler:
    toplam = ihtiyac * arazi_buyuklugu
    st.markdown(f"- **{evre}** evresinde: {ihtiyac} mm su (Toplam: {toplam} mm)")

# Alternatif ürün önerisi
st.subheader("Alternatif Ürün Önerisi")
if v['Rakım (m)'] > 1850 and v['Sıcaklık (°C)'] < 7.5 and toprak_turu in ["Killi", "Tınlı"]:
    st.success("Nohut veya Mercimek ekimi bu koşullarda daha verimli olabilir.")
elif v['Sıcaklık (°C)'] > 8 and toprak_turu == "Kumlu":
    st.success("Ayçiçeği veya Patates uygun olabilir.")
else:
    st.info("Seçilen üründe ekim yapılabilir, ancak alternatif olarak fiğ veya yulaf da düşünülebilir.")

# Hastalık ve ilaçlama önerisi
st.subheader("Hastalık ve İlaçlama Önerisi")
if urun == "Buğday" and v['Sıcaklık (°C)'] > 8:
    st.warning("🔍 Septorya riski yüksek. Tavsiye edilen ilaç: Tebuconazole.")
elif urun == "Fasulye" and v['Rakım (m)'] < 1800:
    st.warning("🔍 Antraknoz riski var. Tavsiye edilen ilaç: Azoxystrobin.")
elif urun == "Arpa" and toprak_turu == "Killi":
    st.warning("🔍 Kök çürüklüğü riski olabilir. Tavsiye edilen ilaç: Propiconazole.")
else:
    st.markdown("Herhangi bir ciddi hastalık riski tespit edilmedi.")
