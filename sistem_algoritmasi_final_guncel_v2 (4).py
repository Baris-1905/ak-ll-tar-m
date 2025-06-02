import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Akıllı Tarım KDS", layout="centered")

# Uygulama durumu yönetimi
if "veri_turu_secildi" not in st.session_state:
    st.session_state.veri_turu_secildi = False

if not st.session_state.veri_turu_secildi:
    st.subheader("📊 Merhaba, Hoş Geldiniz. Lütfen veri giriş türünü seçin:")
    secim = st.radio("Veri Giriş Türü", ["Manuel Veri Girişi", "Excel ile Geçmiş Veriler"])
    if st.button("Devam Et"):
        st.session_state.veri_turu = secim
        st.session_state.veri_turu_secildi = True
        st.experimental_rerun()
    st.stop()

veri_turu = st.session_state.veri_turu
import pandas as pd
import matplotlib.pyplot as plt


# Uygulama durumu yönetimi

    st.subheader("📊 Merhaba, Hoş Geldiniz. Lütfen veri giriş türünü seçin:")


# Açılış ekranı

    st.subheader("📊 Merhaba, Hoş Geldiniz. Lütfen veri giriş türünü seçin:")

import pandas as pd
import matplotlib.pyplot as plt

st.title("🌾 Akıllı Tarım Karar Destek Sistemi")


    st.subheader("📊 Merhaba, Hoş Geldiniz. Lütfen veri giriş türünü seçin:")


urunler = ["Arpa", "Buğday", "Fasulye"]
verim_katsayi = {"Arpa": 280, "Buğday": 320, "Fasulye": 250}
gubre_aciklamalari = {
    "Ahır Gübresi": "Organik gübre. Toprak yapısını iyileştirir.",
    "20-20-20": "Dengeli gübre. %20 N, %20 P, %20 K.",
    "15-15-30": "Potasyum ağırlıklı. Kaliteyi artırır.",
    "Kompoze": "Genel amaçlı farklı oranlarda NPK içerir."
}
fao56_sulama_detaylari = {
    "Buğday": [
        "Çimlenme (1-2. hafta): 25 mm",
        "Kardeşlenme (3-4. hafta): 30 mm",
        "Sapa kalkma (5-6. hafta): 35 mm",
        "Başaklanma (7-8. hafta): 40 mm",
        "Olgunlaşma (9-10. hafta): 20 mm"
    ],
    "Arpa": [
        "Çimlenme (1-2. hafta): 20 mm",
        "Kardeşlenme (3-4. hafta): 25 mm",
        "Sapa kalkma (5-6. hafta): 30 mm",
        "Başaklanma (7-8. hafta): 35 mm",
        "Olgunlaşma (9-10. hafta): 15 mm"
    ],
    "Fasulye": [
        "Çimlenme (1-2. hafta): 30 mm",
        "Yapraklanma (3-4. hafta): 35 mm",
        "Çiçeklenme (5-6. hafta): 40 mm",
        "Bakla oluşumu (7-8. hafta): 45 mm",
        "Olgunlaşma (9-10. hafta): 25 mm"
    ]
}
hinos_koyleri = {
    "Erbeyli": {"rakim": 1750, "sicaklik": 17},
    "Aşağıkayabaşı": {"rakim": 1700, "sicaklik": 16},
    "Bellitaş": {"rakim": 1780, "sicaklik": 15},
    "Yukarıçayırlı": {"rakim": 1790, "sicaklik": 16},
    "Kızılkale": {"rakim": 1745, "sicaklik": 17},
    "Halilçavuş": {"rakim": 1710, "sicaklik": 18},
    "Karabudak": {"rakim": 1800, "sicaklik": 16},
    "Ortaderik": {"rakim": 1770, "sicaklik": 15},
    "Sütlüce": {"rakim": 1690, "sicaklik": 17},
    "Yukarıaktaş": {"rakim": 1810, "sicaklik": 14},
    "Sergen": {"rakim": 1760, "sicaklik": 15},
    "Çayırlı": {"rakim": 1705, "sicaklik": 16},
    "Başarı": {"rakim": 1725, "sicaklik": 17},
    "Göller": {"rakim": 1755, "sicaklik": 16},
    "Tatarcık": {"rakim": 1795, "sicaklik": 15}
}

if veri_turu == "Manuel Veri Girişi":
    st.header("🧑‍🌾 Manuel Veri Girişi")

    urun = st.selectbox("Yetiştirilecek Ürün:", urunler)
    konum = st.selectbox("Ekim Yapılacak Köy/Mahalle:", list(hinos_koyleri.keys()))
    rakim = hinos_koyleri[konum]["rakim"]
    sicaklik = hinos_koyleri[konum]["sicaklik"]
    st.success(f"Rakım: {rakim} m | Sıcaklık: {sicaklik} °C")

    toprak = st.selectbox("Toprak Türü:", ["Killi", "Tınlı", "Kumlu", "Organik"])
    organik = st.selectbox("Organik Madde Miktarı:", ["Düşük", "Orta", "Yüksek"])
    azot = st.slider("Topraktaki Azot Oranı (mg/kg)", 0, 100, 30)
    fosfor = st.slider("Topraktaki Fosfor Oranı (mg/kg)", 0, 100, 25)
    ph = st.slider("Toprak pH Değeri", 4.5, 9.0, 6.5)

    arazi = st.number_input("Arazi Büyüklüğü (dekar):", min_value=1)

    if sulama_var == "Evet":
        sulama_turu = st.selectbox("Sulama Türü:", ["Yağmurlama", "Damla", "Salma"])
    else:
        sulama_turu = "Yok"

    if gubreleme_var == "Evet":
        gubre_turu = st.selectbox("Gübre Türü:", list(gubre_aciklamalari.keys()))
        st.caption(gubre_aciklamalari[gubre_turu])
    else:
        gubre_turu = "Yok"

        st.subheader("📅 Ekim Tarihi Önerisi")
        st.info("En uygun ekim tarihi: 10 Nisan - 25 Nisan arası")

        st.subheader("💧 FAO56 Sulama Takvimi")
        for evre in fao56_sulama_detaylari[urun]:
            st.write("• " + evre)

        if urun in ["Fasulye", "Buğday"] and sulama_var == "Hayır":
            st.warning("⚠️ Bu ürün için sulama yapılması gereklidir.")

        if urun == "Fasulye" and gubreleme_var == "Hayır":
            st.warning("⚠️ Fasulye için gübreleme yapılması önerilir.")

        st.subheader("🦠 Olası Hastalıklar ve İlaçlama")
        hastaliklar = []
        if urun == "Buğday":
            if rakim > 1700 and sicaklik < 17 and toprak == "Killi":
                hastaliklar.append("Kök Boğazı Çürüklüğü")
            if ph < 6.0 or azot < 20:
                hastaliklar.append("Pas Hastalığı")
        elif urun == "Arpa":
            if rakim > 1750 or ph > 8.0:
                hastaliklar.append("Arpa Mozaik Virüsü")
            if organik == "Düşük":
                hastaliklar.append("Yaprak Yanıklığı")
        elif urun == "Fasulye":
            if sicaklik > 18 and ph > 7.5:
                hastaliklar.append("Kök Çürüklüğü")
            if azot < 25:
                hastaliklar.append("Antraknoz")

        if hastaliklar:
            for h in hastaliklar:
                st.error(f"⚠️ Olası Hastalık: {h}")
            st.warning("🧪 Tavsiye: Tarım ilacı kullanımı için ziraat mühendisine danışınız.")
        else:
            st.success("✅ Hastalık riski düşük. Üretime devam edilebilir.")

        st.subheader("📈 Tahmini Verim")
        verim = verim_katsayi[urun] * arazi
        st.success(f"{urun} için tahmini verim: {verim} kg")

elif veri_turu == "Excel ile Geçmiş Veriler":
    st.header("📂 Excel ile Geçmiş Verileri Yükleyin")

    yuklenen_dosya = st.file_uploader("Excel dosyanızı yükleyin (.xlsx):", type=["xlsx"])

    if yuklenen_dosya is not None:
        try:
            df = pd.read_excel(yuklenen_dosya)
            st.success("✅ Dosya başarıyla yüklendi.")
            st.dataframe(df)

            if 'Yıl' in df.columns and 'Verim' in df.columns:
                st.subheader("📊 Yıllara Göre Verim Grafiği")
                df_sorted = df.sort_values("Yıl")
                st.line_chart(df_sorted.set_index("Yıl")["Verim"])

                st.subheader("📉 Temel İstatistikler")
                st.write(df["Verim"].describe())
            else:
                st.warning("⚠️ 'Yıl' ve 'Verim' sütunlarının dosyada bulunduğundan emin olun.")

        except Exception as e:
            st.error(f"Hata oluştu: {e}")
