
# Geliştirilmiş Akıllı Tarım Karar Destek Sistemi (v2)

import streamlit as st
import pandas as pd
from datetime import datetime
from geopy.geocoders import Nominatim
import firebase_admin
from firebase_admin import credentials, auth

# Firebase entegrasyonu
if not firebase_admin._apps:
    cred = credentials.Certificate({
        "type": st.secrets["firebase"]["type"],
        "project_id": st.secrets["firebase"]["project_id"],
        "private_key_id": st.secrets["firebase"]["private_key_id"],
        "private_key": st.secrets["firebase"]["private_key"].replace("\\n", "\n"),
        "client_email": st.secrets["firebase"]["client_email"],
        "client_id": st.secrets["firebase"]["client_id"],
        "auth_uri": st.secrets["firebase"]["auth_uri"],
        "token_uri": st.secrets["firebase"]["token_uri"],
        "auth_provider_x509_cert_url": st.secrets["firebase"]["auth_provider_x509_cert_url"],
        "client_x509_cert_url": st.secrets["firebase"]["client_x509_cert_url"]
    })
    firebase_admin.initialize_app(cred)

st.set_page_config(page_title="Akıllı Tarım KDS", layout="centered")
st.title("🌾 Akıllı Tarım Karar Destek Sistemi")

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# Giriş/Kayıt Paneli
if not st.session_state["authenticated"]:
    secim = st.sidebar.selectbox("İşlem Seçin", ["Giriş Yap", "Kaydol"])

    if secim == "Kaydol":
        st.subheader("🆕 Kayıt Ol")
        email = st.text_input("E-posta")
        password = st.text_input("Parola", type="password")
        if st.button("Kaydol"):
            try:
                auth.create_user(email=email, password=password)
                st.success("✅ Kayıt başarılı, şimdi giriş yapabilirsiniz.")
            except Exception as e:
                st.error(f"Hata: {str(e)}")

    if secim == "Giriş Yap":
        st.subheader("🔐 Giriş Yap")
        email = st.text_input("E-posta")
        password = st.text_input("Parola", type="password")
        if st.button("Giriş"):
            try:
                st.session_state["authenticated"] = True
                st.experimental_rerun()
            except:
                st.error("Giriş başarısız.")
else:
    st.success("✅ Giriş başarılı.")

    veri_turu = st.radio("📂 Veri Giriş Türü Seç", ["Manuel Veri Girişi", "Drone Verisi", "Geçmiş Veriler (Excel)"])

    if veri_turu == "Geçmiş Veriler (Excel)":
        uploaded_file = st.file_uploader("📤 Excel/CSV Dosyası Yükleyin", type=["csv", "xlsx"])
        if uploaded_file:
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            st.write("Yüklenen Veri:")
            st.dataframe(df)

    elif veri_turu == "Manuel Veri Girişi":
        urun = st.selectbox("Ürün Seçimi", ["arpa", "buğday", "fasulye"])
        ekim_tavsiye = {
            "arpa": "15 Nisan - 1 Mayıs",
            "buğday": "1 Ekim - 15 Ekim",
            "fasulye": "10 Mayıs - 25 Mayıs"
        }
        st.info(f"💡 Tavsiye edilen ekim tarihi: {ekim_tavsiye[urun]}")
        ekim_tarihi = st.date_input("Ekim Tarihi")
        tohum = st.selectbox("Tohum Türü", ["yerli", "erkenci", "geççi"])
        arazi = st.number_input("Arazi Büyüklüğü (dekar)", min_value=1)

        toprak = st.selectbox("Toprak Tipi", ["tınlı", "killi", "kumlu"])
        sulama_durumu = st.selectbox("Sulama Var mı?", ["var", "yok"])
        sulama_yontemi = st.selectbox("Sulama Yöntemi", ["yağmurlama", "salma", "damlama"])

        hinis_koyleri = [
            "Aşağıkayabaşı", "Ballı", "Başköy", "Bellitaş", "Camiişerif", "Dağyurdu",
            "Deliktaş", "Erbeyli", "Göller", "Halilçavuş", "Karakale", "Karlıca",
            "Kızılkale", "Konakkale", "Murat", "Ovaçevirme", "Söğütlü", "Topraklı",
            "Yaprakbaşı", "Yukarıkayabaşı"
        ]
        lokasyon = st.selectbox("Köy/Mahalle Seç", hinis_koyleri)

        if st.button("📊 Hesapla"):
            st.subheader("💧 Sulama Takvimi")
            if urun == "arpa":
                st.markdown("- İlk 2 hafta: 3 günde bir sulama\n- Sonraki haftalar: haftalık sulama")
            elif urun == "buğday":
                st.markdown("- Çimlenme sonrası 7 günde bir\n- Başaklanma döneminde sıklaştır")
            elif urun == "fasulye":
                st.markdown("- 10 günde bir sulama\n- Bakla döneminde 5 günde bir")

            st.subheader("🌿 Gübre Tavsiyesi")
            if urun == "arpa":
                st.write("20-20-20 gübre - dekara 50 kg")
            elif urun == "buğday":
                st.write("Üre gübresi + Amonyum Sülfat - toplam 60 kg/da")
            elif urun == "fasulye":
                st.write("Triple Süper Fosfat + Potasyum - 40 kg/da")

            st.subheader("🌾 Alternatif Ürün Önerisi")
            if urun == "arpa":
                st.write("Alternatif: Mercimek, nohut")
            elif urun == "buğday":
                st.write("Alternatif: Tritikale, yulaf")
            elif urun == "fasulye":
                st.write("Alternatif: Barbunya, bezelye")

            st.subheader("📝 Geri Bildirim")
            st.markdown("[Google Forms ile ilet](https://forms.gle/yourformlink)")
