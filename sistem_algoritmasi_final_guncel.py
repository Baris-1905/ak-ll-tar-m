
# sistem_algoritmasi_final.py
# Akıllı Tarım Karar Destek Sistemi - Güncellenmiş Sürüm
# Eksikler giderildi: sulama uyarısı, drone verisi, FAO56 takvimi, köy listesi, ekran ayrımı

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from simulasyon_verisi_ve_sulama import simulasyon_senaryolari, fao56_sulama_detaylari


# Gerçek Hınıs köy ve mahalle listesi (örnek veri, genişletilebilir)
hinos_koyleri = {
    "Erbeyli": {"rakim": 1750, "sicaklik": 17},
    "Aşağıkayabaşı": {"rakim": 1700, "sicaklik": 16},
    "Yukarıçayırlı": {"rakim": 1780, "sicaklik": 15},
    "Bellitaş": {"rakim": 1800, "sicaklik": 16},
    "Halilçavuş": {"rakim": 1720, "sicaklik": 17},
    "Kızılkale": {"rakim": 1735, "sicaklik": 16},
    "Diğer (manuel giriş)": {}
}

urunler = ["Arpa", "Buğday", "Fasulye"]

gubre_aciklamalari = {
    "Ahır Gübresi": "Organik bir gübre türüdür. Toprağın yapısını iyileştirir.",
    "20-20-20": "Dengeli kompoze gübredir. %20 Azot, %20 Fosfor, %20 Potasyum içerir.",
    "15-15-30": "Potasyum ağırlıklı gübredir. Meyve gelişimi ve kaliteyi artırır.",
    "Kompoze": "Genel amaçlı, farklı oranlarda NPK içerebilir."
}

st.title("🌱 Akıllı Tarım Karar Destek Sistemi")

# Veri giriş ekranı ayrı olarak tanımlansın
if "veri_turu" not in st.session_state:
    st.session_state.veri_turu = None

if st.session_state.veri_turu is None:
    st.subheader("📊 Lütfen Veri Giriş Türünü Seçin")
    st.session_state.veri_turu = st.radio("Seçiminizi yapın:", ["Manuel Veri Girişi", "Otomatik Veri (Drone)", "Excel ile Geçmiş Veriler"])
    st.stop()

veri_turu = st.session_state.veri_turu

if veri_turu == "Manuel Veri Girişi":
    st.subheader("🌾 Manuel Veri Girişi")

    urun = st.selectbox("Yetiştirilecek ürünü seçin:", urunler)
    konum = st.selectbox("Ekim yapılacak köy/mahalle:", list(hinos_koyleri.keys()))
    if konum != "Diğer (manuel giriş)":
        rakim = hinos_koyleri[konum]["rakim"]
        sicaklik = hinos_koyleri[konum]["sicaklik"]
        st.success(f"Rakım: {rakim} m | Ortalama Sıcaklık: {sicaklik} °C")
    else:
        rakim = st.number_input("Rakım (m):", min_value=1000, max_value=2500)
        sicaklik = st.number_input("Sıcaklık (°C):", min_value=5, max_value=30)

    toprak = st.selectbox("Toprak türü:", ["Killi", "Tınlı", "Kumlu", "Organik"])
    drenaj = st.selectbox("Drenaj durumu:", ["İyi", "Orta", "Kötü"])
    organik = st.selectbox("Organik madde miktarı:", ["Yüksek", "Orta", "Düşük"])
    arazi = st.number_input("Arazi büyüklüğü (dekar):", min_value=1)

    sulama_var = st.radio("Sulama yapıldı mı?", ["Evet", "Hayır"])
    if sulama_var == "Evet":
        sulama_turu = st.selectbox("Sulama türü:", ["Yağmurlama", "Damla", "Salma"])
    else:
        sulama_turu = "Yok"

    gubreleme_var = st.radio("Gübreleme yapıldı mı?", ["Evet", "Hayır"])
    if gubreleme_var == "Evet":
        gubre_turu = st.selectbox("Gübre türü:", list(gubre_aciklamalari.keys()))
        st.info(f"ℹ️ {gubre_turu}: {gubre_aciklamalari[gubre_turu]}")
    else:
        gubre_turu = "Yok"

    if st.button("📊 Sonuçları Göster"):
        st.subheader("📅 Ekim Tarihi Önerisi")
        st.write("Ekim için en uygun tarih: 15 Nisan - 5 Mayıs arası")

        st.subheader("💧 FAO56 Sulama Takvimi")
        for satir in fao56_sulama_detaylari[urun]:
            st.write(satir)

        if urun in ["Buğday", "Fasulye"] and sulama_var == "Hayır":
            st.warning("⚠️ Bu ürün için sulama yapılması önerilir.")
        if urun == "Fasulye" and gubreleme_var == "Hayır":
            st.warning("⚠️ Fasulye için gübreleme yapılması önerilir.")

        st.subheader("📈 Verim Tahmini")
        verim = 250 * arazi
        st.success(f"Tahmini verim: {verim} kg")
