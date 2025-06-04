import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Akıllı Tarım Karar Destek Sistemi", layout="centered")

st.title("Akıllı Tarım Karar Destek Sistemi")

veri_turu = st.radio("Veri giriş türünü seçin:", ["Manuel Veri Girişi", "Excel ile Geçmiş Veriler"])

if veri_turu == "Manuel Veri Girişi":
    # Buraya manuel veri girişi ekranı koyulacak (orijinal koddan alınarak)
    st.header("🧑‍🌾 Manuel Veri Girişi")
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

    sulama_var = st.radio("Sulama yapıldı mı?", ["Evet", "Hayır"])
    if sulama_var == "Evet":
        sulama_turu = st.selectbox("Sulama Türü:", ["Yağmurlama", "Damla", "Salma"])
    else:
        sulama_turu = "Yok"

    gubreleme_var = st.radio("Gübreleme yapıldı mı?", ["Evet", "Hayır"])
    if gubreleme_var == "Evet":
        gubre_turu = st.selectbox("Gübre Türü:", list(gubre_aciklamalari.keys()))
        st.caption(gubre_aciklamalari[gubre_turu])
    else:
        gubre_turu = "Yok"

    if st.button("📊 Sonuçları Göster"):
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
    st.header("📂 Geçmiş Verileri Yükleyin")
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
                st.warning("Excel dosyasında 'Yıl' ve 'Verim' sütunları olmalı.")
        except Exception as e:
            st.error(f"Hata oluştu: {e}")