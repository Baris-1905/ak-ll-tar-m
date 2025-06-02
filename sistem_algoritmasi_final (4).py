
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Akıllı Tarım Karar Destek Sistemi", layout="centered")
st.title("🌱 Akıllı Tarım Karar Destek Sistemi")

# Simülasyon senaryoları
simulasyon_senaryolari = {
    "Senaryo 1": {
        "urun": "Buğday",
        "konum": "Erbeyli",
        "rakim": 1750,
        "sicaklik": 17,
        "toprak": "Killi",
        "organik_madde": "Orta",
        "sulama_var": True,
        "sulama_turu": "Yağmurlama",
        "gubreleme_var": True,
        "gubre_turu": "20-20-20",
        "arazi_buyuklugu": 5
    },
    "Senaryo 2": {
        "urun": "Fasulye",
        "konum": "Aşağıkayabaşı",
        "rakim": 1700,
        "sicaklik": 16,
        "toprak": "Tınlı",
        "organik_madde": "Yüksek",
        "sulama_var": False,
        "sulama_turu": "",
        "gubreleme_var": False,
        "gubre_turu": "",
        "arazi_buyuklugu": 3
    }
}

# Sulama takvimi
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



# Hınıs köy listesi (örnek 15 adet)
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

urunler = ["Arpa", "Buğday", "Fasulye"]
gubre_aciklamalari = {
    "Ahır Gübresi": "Organik bir gübre türüdür. Toprağın yapısını iyileştirir.",
    "20-20-20": "Dengeli kompoze gübredir. %20 Azot, %20 Fosfor, %20 Potasyum içerir.",
    "15-15-30": "Potasyum ağırlıklı gübredir. Meyve gelişimi ve kaliteyi artırır.",
    "Kompoze": "Genel amaçlı, farklı oranlarda NPK içerebilir."
}
verim_katsayi = {"Arpa": 280, "Buğday": 320, "Fasulye": 250}

if "veri_turu" not in st.session_state:
    st.session_state.veri_turu = None

if st.session_state.veri_turu is None:
    st.subheader("📊 Veri Girişi Türünü Seçin")
    st.session_state.veri_turu = st.radio("Seçim yapın:", ["Manuel Veri Girişi", "Otomatik Veri (Drone)", "Excel ile Geçmiş Veriler"])
    st.stop()

veri_turu = st.session_state.veri_turu


if veri_turu == "Manuel Veri Girişi":
    st.subheader("🌾 Manuel Veri Girişi")

    urun = st.selectbox("Yetiştirilecek ürünü seçin:", urunler)
    konum = st.selectbox("Ekim yapılacak köy/mahalle:", list(hinos_koyleri.keys()))
    rakim = hinos_koyleri[konum]["rakim"]
    sicaklik = hinos_koyleri[konum]["sicaklik"]
    st.success(f"Rakım: {rakim} m | Ortalama Sıcaklık: {sicaklik} °C")

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
        gubre_turu = st.selectbox("Gübre türünü seçin:", list(gubre_aciklamalari.keys()))
        st.info(f"{gubre_turu}: {gubre_aciklamalari[gubre_turu]}")
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
        verim = verim_katsayi[urun] * arazi
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

        st.subheader("💧 FAO56 Sulama Takvimi")
        for satir in fao56_sulama_detaylari[veri["urun"]]:
            st.write(satir)

        if veri["urun"] in ["Buğday", "Fasulye"] and not veri["sulama_var"]:
            st.warning("⚠️ Bu ürün için sulama yapılması önerilir.")
        if veri["urun"] == "Fasulye" and not veri["gubreleme_var"]:
            st.warning("⚠️ Fasulye için gübreleme yapılması önerilir.")

        st.subheader("📈 Verim Tahmini")
        verim = verim_katsayi[veri["urun"]] * veri["arazi_buyuklugu"]
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
