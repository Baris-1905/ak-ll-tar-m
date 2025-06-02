import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Akıllı Tarım KDS", layout="centered")

# Giriş ekranı
if "veri_turu_secildi" not in st.session_state:
    st.session_state["veri_turu_secildi"] = False

if not st.session_state["veri_turu_secildi"]:
    st.subheader("📊 Merhaba, Hoş Geldiniz. Lütfen veri giriş türünü seçin:")
    secim = st.radio("Veri Giriş Türü", ["Manuel Veri Girişi", "Excel ile Geçmiş Veriler"])
    if st.button("Devam Et"):
        st.session_state["veri_turu"] = secim
        st.session_state["veri_turu_secildi"] = True
        st.experimental_rerun()
    st.stop()

veri_turu = st.session_state["veri_turu"]

# Ürünler ve açıklamalar
urunler = ["Arpa", "Buğday", "Fasulye"]
gubre_aciklamalari = {
    "Ahır Gübresi": "Organik bir gübre türüdür. Toprağın yapısını iyileştirir.",
    "20-20-20": "Dengeli kompoze gübredir. %20 Azot, %20 Fosfor, %20 Potasyum içerir.",
    "15-15-30": "Potasyum ağırlıklı gübredir. Meyve gelişimi ve kaliteyi artırır.",
    "Kompoze": "Genel amaçlı, farklı oranlarda NPK içerebilir."
}

# Köy verileri (Hınıs köylerinden örnekler)
hinos_koyleri = {
    "Erbeyli": {"rakim": 1750, "sicaklik": 17},
    "Aşağıkayabaşı": {"rakim": 1700, "sicaklik": 16}
}

if veri_turu == "Manuel Veri Girişi":
    st.subheader("🌾 Manuel Veri Girişi")

    urun = st.selectbox("Yetiştirilecek ürünü seçin:", urunler)

    konum = st.selectbox("Ekim yapılacak köy/mahalle:", list(hinos_koyleri.keys()))
    rakim = hinos_koyleri[konum]["rakim"]
    sicaklik = hinos_koyleri[konum]["sicaklik"]
    st.success(f"Rakım: {rakim} m | Ortalama Sıcaklık: {sicaklik} °C")

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
        verim = 250 * arazi
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
