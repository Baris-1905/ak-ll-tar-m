
# sistem_algoritmasi_final.py
# Akıllı Tarım Karar Destek Sistemi
# Oluşturuluyor...

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Kodun devamı burada olacak...
st.title("🌱 Akıllı Tarım Karar Destek Sistemi")

# Köy verileri
hinos_koyleri = {
    "Erbeyli": {"rakim": 1750, "sicaklik": 17},
    "Aşağıkayabaşı": {"rakim": 1700, "sicaklik": 16},
    "Karabudak": {"rakim": 1800, "sicaklik": 15},
    "Ortaderik": {"rakim": 1780, "sicaklik": 16},
    "Yukarıhakim": {"rakim": 1720, "sicaklik": 17},
    "Diğer (manuel giriş)": {}
}

urunler = ["Arpa", "Buğday", "Fasulye"]

gubre_aciklamalari = {
    "Ahır Gübresi": "Organik bir gübre türüdür. Toprağın yapısını iyileştirir.",
    "20-20-20": "Dengeli kompoze gübredir. %20 Azot, %20 Fosfor, %20 Potasyum içerir.",
    "15-15-30": "Potasyum ağırlıklı gübredir. Meyve gelişimi ve kaliteyi artırır.",
    "Kompoze": "Genel amaçlı, farklı oranlarda NPK içerebilir."
}

veri_turu = st.radio("📌 Lütfen veri giriş türünü seçin:", ["Manuel Veri Girişi", "Otomatik Veri (Drone)", "Excel ile Geçmiş Veriler"])

if veri_turu == "Manuel Veri Girişi":
    st.subheader("🌾 Manuel Veri Girişi")

    urun = st.selectbox("Yetiştirilecek ürünü seçin:", urunler)

    konum = st.selectbox("Ekim yapılacak köy/mahalle:", list(hinos_koyleri.keys()))
    if konum != "Diğer (manuel giriş)":
        rakim = hinos_koyleri[konum]["rakim"]
        sicaklik = hinos_koyleri[konum]["sicaklik"]
        st.success(f"Rakım: {rakim} m | Ortalama Sıcaklık: {sicaklik} °C")
    else:
        rakim = st.number_input("Rakım bilgisini girin (metre):", min_value=1000, max_value=2500)
        sicaklik = st.number_input("Ortalama sıcaklık bilgisini girin (°C):", min_value=5, max_value=30)

    toprak = st.selectbox("Toprak türünü seçin:", ["Killi", "Tınlı", "Kumlu", "Organik"])
    drenaj = st.selectbox("Drenaj durumu:", ["İyi", "Orta", "Kötü"])
    organik = st.selectbox("Organik madde miktarı:", ["Yüksek", "Orta", "Düşük"])
    arazi = st.number_input("Arazi büyüklüğü (dekar):", min_value=1)

    sulama_var = st.radio("Sulama yapıldı mı?", ["Evet", "Hayır"])
    if sulama_var == "Evet":
        sulama_turu = st.selectbox("Sulama türünü seçin:", ["Yağmurlama", "Damla", "Salma"])
    else:
        sulama_turu = "Yok"

    gubreleme_var = st.radio("Gübreleme yapıldı mı?", ["Evet", "Hayır"])
    if gubreleme_var == "Evet":
        gubre_turu = st.selectbox("Gübre türünü seçin:", list(gubre_aciklamalari.keys()))
        st.info(f"ℹ️ {gubre_turu}: {gubre_aciklamalari[gubre_turu]}")
    else:
        gubre_turu = "Yok"

    if st.button("📊 Sonuçları Göster"):
        st.subheader("📅 Ekim Tarihi Önerisi")
        st.write("Ekim için en uygun tarih: 15 Nisan - 5 Mayıs arası")

        st.subheader("💧 FAO56 Sulama Takvimi (Örnek)")
        st.write("Hafta 1: 25 mm, Hafta 2: 30 mm, Hafta 3: 35 mm...")

        if urun in ["Buğday", "Fasulye"] and sulama_var == "Hayır":
            st.warning("⚠️ Bu ürün için sulama önerilir. Sulama yapılmaması verimi düşürebilir.")
        if urun == "Fasulye" and gubreleme_var == "Hayır":
            st.warning("⚠️ Fasulye için gübreleme yapılması önerilir.")

        st.subheader("📈 Verim Tahmini")
        verim = 250 * arazi  # örnek hesap
        st.success(f"Tahmini verim: {verim} kg")

elif veri_turu == "Otomatik Veri (Drone)":
    st.subheader("🤖 Drone Simülasyonu Verisi")

    senaryo = st.selectbox("Simülasyon senaryosu seçin:", list(simulasyon_senaryolari.keys()))
    veri = simulasyon_senaryolari[senaryo]

    st.write(f"📌 Ürün: {veri['urun']}")
    st.write(f"📍 Konum: {veri['konum']}")
    st.write(f"📈 Rakım: {veri['rakim']} m, Sıcaklık: {veri['sicaklik']} °C")
    st.write(f"🧱 Toprak Türü: {veri['toprak']}, Organik Madde: {veri['organik_madde']}")
    st.write(f"💧 Sulama: {'Var - ' + veri['sulama_turu'] if veri['sulama_var'] else 'Yok'}")
    st.write(f"💩 Gübreleme: {'Var - ' + veri['gubre_turu'] if veri['gubreleme_var'] else 'Yok'}")
    st.write(f"📐 Arazi Büyüklüğü: {veri['arazi_buyuklugu']} dekar")

    if st.button("📊 Sonuçları Göster", key="simulasyon_sonuc"):
        st.subheader("📅 Ekim Tarihi Önerisi")
        st.write("Ekim için en uygun tarih: 10 Nisan - 25 Nisan arası")

        st.subheader("💧 FAO56 Sulama Takvimi (Örnek)")
        st.write("Hafta 1: 30 mm, Hafta 2: 35 mm, Hafta 3: 40 mm...")

        if veri["urun"] in ["Buğday", "Fasulye"] and not veri["sulama_var"]:
            st.warning("⚠️ Bu ürün için sulama yapılması önerilir.")

        if veri["urun"] == "Fasulye" and not veri["gubreleme_var"]:
            st.warning("⚠️ Fasulye için gübreleme yapılması önerilir.")

        st.subheader("📈 Verim Tahmini")
        verim = 260 * veri["arazi_buyuklugu"]
        st.success(f"Tahmini verim: {verim} kg")

elif veri_turu == "Excel ile Geçmiş Veriler":
    st.subheader("📂 Geçmiş Verileri Yükleyin")
    yuklenen_dosya = st.file_uploader("Excel dosyasını yükleyin (.xlsx veya .xls):", type=["xlsx", "xls"])
    if yuklenen_dosya is not None:
        try:
            df = pd.read_excel(yuklenen_dosya)
            st.write("📊 Yüklenen Veri:")
            st.dataframe(df)

            if 'Yıl' in df.columns and 'Verim' in df.columns:
                st.subheader("📈 Yıllara Göre Verim Grafiği")
                df_sorted = df.sort_values("Yıl")
                st.line_chart(df_sorted.set_index("Yıl")["Verim"])
            else:
                st.info("ℹ️ 'Yıl' ve 'Verim' sütunlarının olduğundan emin olun.")

        except Exception as e:
            st.error(f"Hata oluştu: {e}")
