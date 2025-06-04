
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Akıllı Tarım Karar Destek Sistemi", layout="wide")

st.title("Akıllı Tarım Karar Destek Sistemi")
st.header("🧑‍🌾 Manuel Veri Girişi")

urunler = ["Arpa", "Buğday", "Fasulye"]

urun = st.selectbox("Yetiştirilecek Ürün:", urunler)

koyler = {
    "Erbeyli": {"rakim": 1750, "sicaklik": 17},
    "Aşağıkayabaşı": {"rakim": 1700, "sicaklik": 16},
    "Karabudak": {"rakim": 1800, "sicaklik": 15},
}

konum = st.selectbox("Ekim yapılacak köy/mahalle:", list(koyler.keys()))
rakim = koyler[konum]["rakim"]
sicaklik = koyler[konum]["sicaklik"]
st.success(f"Rakım: {rakim} m | Ortalama Sıcaklık: {sicaklik} °C")

toprak_turu = st.selectbox("Toprak Türü:", ["Killi", "Tınlı", "Kumlu", "Organik"])
drenaj = st.selectbox("Drenaj Durumu:", ["İyi", "Orta", "Kötü"])
organik = st.selectbox("Organik Madde Miktarı:", ["Yüksek", "Orta", "Düşük"])
arazi = st.number_input("Arazi Büyüklüğü (dekar):", min_value=1)

sulama_var = st.radio("Sulama yapıldı mı?", ["Evet", "Hayır"])
if sulama_var == "Evet":
    sulama_turu = st.selectbox("Sulama Türü:", ["Yağmurlama", "Damla", "Salma"])
else:
    sulama_turu = "Yok"

gubreleme_var = st.radio("Gübreleme yapıldı mı?", ["Evet", "Hayır"])
if gubreleme_var == "Evet":
    gubre_turu = st.selectbox("Gübre Türü:", ["Ahır", "20-20-20", "15-15-30", "Kompoze"])
else:
    gubre_turu = "Yok"

azot = st.number_input("Topraktaki Azot Miktarı (mg/kg):", min_value=0)
fosfor = st.number_input("Topraktaki Fosfor Miktarı (mg/kg):", min_value=0)
ph = st.number_input("Toprak pH Değeri:", min_value=3.5, max_value=9.5, step=0.1)

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
    verim = 250 * arazi
    st.success(f"Tahmini verim: {verim} kg")
