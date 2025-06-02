
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Akıllı Tarım Karar Destek Sistemi", layout="centered")
st.title("🌱 Akıllı Tarım Karar Destek Sistemi")

# Başlangıçta veri türü seçilmediği sürece durdur
if "veri_turu" not in st.session_state:
    st.session_state.veri_turu = None

if st.session_state.veri_turu is None:
    st.subheader("📊 Merhaba, Hoş Geldiniz. Lütfen veri giriş türünü seçin:")
    st.session_state.veri_turu = st.radio("Veri Giriş Türü", ["Manuel Veri Girişi", "Otomatik Veri (Drone)", "Excel ile Geçmiş Veriler"])
    st.stop()

veri_turu = st.session_state.veri_turu

# Veriler
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
simulasyon_senaryolari = {
    "Senaryo 1: Buğday – Aşağıkayabaşı – 1700 m – 16°C": {
        "urun": "Buğday", "konum": "Aşağıkayabaşı", "rakim": 1700, "sicaklik": 16,
        "toprak": "Killi", "organik_madde": "Orta", "sulama_var": True, "sulama_turu": "Yağmurlama",
        "gubreleme_var": True, "gubre_turu": "20-20-20", "arazi_buyuklugu": 5
    }
}

# === MANUEL VERİ GİRİŞİ EKRANI ===
if veri_turu == "Manuel Veri Girişi":
    st.header("🧑‍🌾 Manuel Veri Girişi")

    urun = st.selectbox("Ürün Seçin:", urunler)
    konum = st.selectbox("Ekim Yapılacak Köy/Mahalle:", list(hinos_koyleri.keys()))
    rakim = hinos_koyleri[konum]["rakim"]
    sicaklik = hinos_koyleri[konum]["sicaklik"]
    st.info(f"Rakım: {rakim} m, Sıcaklık: {sicaklik} °C")

    toprak = st.selectbox("Toprak Türü:", ["Killi", "Tınlı", "Kumlu", "Organik"])
    organik_madde = st.selectbox("Organik Madde Miktarı:", ["Düşük", "Orta", "Yüksek"])
    arazi_buyuklugu = st.number_input("Arazi Büyüklüğü (dekar):", min_value=1)

    sulama_var = st.radio("Sulama Yapıldı mı?", ["Evet", "Hayır"])
    if sulama_var == "Evet":
        sulama_turu = st.selectbox("Sulama Türü:", ["Yağmurlama", "Damla", "Salma"])
    else:
        sulama_turu = "Yok"

    gubreleme_var = st.radio("Gübreleme Yapıldı mı?", ["Evet", "Hayır"])
    if gubreleme_var == "Evet":
        gubre_turu = st.selectbox("Gübre Türü:", list(gubre_aciklamalari.keys()))
        st.caption(gubre_aciklamalari[gubre_turu])
    else:
        gubre_turu = "Yok"

    if st.button("📊 Sonuçları Göster"):
        st.subheader("📅 Ekim Tarihi Önerisi")
        st.success("Ekim için en uygun tarih: 10 Nisan - 25 Nisan arası")

        st.subheader("💧 FAO56 Sulama Takvimi")
        for evre in fao56_sulama_detaylari[urun]:
            st.write(f"• {evre}")

        if urun in ["Buğday", "Fasulye"] and sulama_var == "Hayır":
            st.warning("⚠️ Bu ürün için sulama gereklidir. Sulama yapılmazsa verim düşer.")
        if urun == "Fasulye" and gubreleme_var == "Hayır":
            st.warning("⚠️ Fasulye için gübreleme önerilir.")

        verim = verim_katsayi[urun] * arazi_buyuklugu
        st.subheader("📈 Verim Tahmini")
        st.success(f"Tahmini verim: {verim} kg")


# === DRONE VERİSİ (Simülasyon) ===
elif veri_turu == "Otomatik Veri (Drone)":
    st.header("🤖 Otomatik Drone Verisi Simülasyonu")
    senaryo = st.selectbox("Senaryo Seçin:", list(simulasyon_senaryolari.keys()))
    veri = simulasyon_senaryolari[senaryo]

    st.markdown(f"""
    **Ürün:** {veri['urun']}  
    **Konum:** {veri['konum']}  
    **Rakım:** {veri['rakim']} m  
    **Sıcaklık:** {veri['sicaklik']} °C  
    **Toprak Türü:** {veri['toprak']}  
    **Organik Madde:** {veri['organik_madde']}  
    **Sulama:** {"Var (" + veri['sulama_turu'] + ")" if veri['sulama_var'] else "Yok"}  
    **Gübreleme:** {"Var (" + veri['gubre_turu'] + ")" if veri['gubreleme_var'] else "Yok"}  
    **Arazi:** {veri['arazi_buyuklugu']} dekar
    """)

    if st.button("📊 Sonuçları Göster - Simülasyon"):
        st.subheader("📅 Ekim Tarihi Önerisi")
        st.success("Ekim için en uygun tarih: 10 Nisan - 25 Nisan arası")

        st.subheader("💧 FAO56 Sulama Takvimi")
        for evre in fao56_sulama_detaylari[veri['urun']]:
            st.write(f"• {evre}")

        if veri["urun"] in ["Buğday", "Fasulye"] and not veri["sulama_var"]:
            st.warning("⚠️ Bu ürün için sulama gereklidir.")

        if veri["urun"] == "Fasulye" and not veri["gubreleme_var"]:
            st.warning("⚠️ Fasulye için gübreleme önerilir.")

        verim = verim_katsayi[veri['urun']] * veri['arazi_buyuklugu']
        st.subheader("📈 Verim Tahmini")
        st.success(f"Tahmini verim: {verim} kg")


# === EXCEL YÜKLEME (Geçmiş Veriler) ===
elif veri_turu == "Excel ile Geçmiş Veriler":
    st.header("📂 Geçmiş Verileri Yükleyin")
    dosya = st.file_uploader("Excel Dosyası Yükleyin (.xlsx, .xls)", type=["xlsx", "xls"])
    if dosya:
        try:
            df = pd.read_excel(dosya)
            st.dataframe(df)

            if "Yıl" in df.columns and "Verim" in df.columns:
                st.line_chart(df.set_index("Yıl")["Verim"])
            else:
                st.error("⚠️ Dosyada 'Yıl' ve 'Verim' sütunları bulunmalı.")
        except Exception as e:
            st.error(f"Hata oluştu: {e}")
