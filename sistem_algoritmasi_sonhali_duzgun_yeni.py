
# Akıllı Tarım Karar Destek Sistemi - Firebase Entegre Edilmiş Sürüm

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from io import BytesIO
from geopy.geocoders import Nominatim
import firebase_admin
from firebase_admin import credentials, auth

# Firebase bağlantısı (Streamlit Secrets üzerinden)
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

menu = ["Giriş Yap", "Kaydol"]
choice = st.sidebar.selectbox("İşlem Seçin", menu)

if choice == "Kaydol":
    st.subheader("🆕 Kayıt Ol")
    email = st.text_input("E-posta")
    password = st.text_input("Parola", type="password")
    if st.button("Kaydol"):
        try:
            auth.create_user(email=email, password=password)
            st.success("Kayıt başarılı. Şimdi giriş yapabilirsiniz.")
        except:
            st.error("Bu e-posta zaten kayıtlı veya parola zayıf.")

elif choice == "Giriş Yap":
    st.subheader("🔐 Giriş Yap")
    email = st.text_input("E-posta")
    password = st.text_input("Parola", type="password")
    if st.button("Giriş"):
        st.session_state["authenticated"] = True

if st.session_state.get("authenticated"):
    st.success("✅ Giriş başarılı. Sisteme erişim sağlandı.")

    st.header("📋 Üretim Bilgileri")
    urun = st.selectbox("Ürün Seçimi", ["arpa", "buğday", "fasulye"])
    ekim_tarihi = st.date_input("Ekim Tarihi")
    tohum = st.selectbox("Tohum Türü", ["yerli", "erkenci", "geççi"])
    arazi = st.number_input("Arazi Büyüklüğü (dekar)", min_value=1)

    st.header("🌱 Toprak ve Sulama Bilgileri")
    toprak = st.selectbox("Toprak Tipi", ["tınlı", "killi", "kumlu"])
    sulama = st.selectbox("Sulama Durumu", ["var", "yok"])

    st.header("📍 Lokasyon ve Veriler")
    hinis_koyleri = [
    "Aşağıkayabaşı", "Ballı", "Başköy", "Bellitaş", "Camiişerif", "Dağyurdu",
    "Deliktaş", "Erbeyli", "Göller", "Halilçavuş", "Karakale", "Karlıca",
    "Kızılkale", "Konakkale", "Murat", "Ovaçevirme", "Söğütlü", "Topraklı",
    "Yaprakbaşı", "Yukarıkayabaşı"
]
lokasyon = st.selectbox("Köy/Mahalle Seç", hinis_koyleri)
    verim_dosya = st.file_uploader("Verim Verisi (CSV)", type="csv")

    rakim = None
    if st.button("Rakımı Hesapla"):
        geo = Nominatim(user_agent="tarim-app")
        loc = geo.geocode(lokasyon)
        if loc:
            rakim = loc.altitude or 1700
            st.success(f"Rakım: {rakim:.0f} m")
        else:
            st.warning("Lokasyon bulunamadı.")

    if st.button("📊 Hesapla"):
        st.subheader("💧 Sulama Takvimi")
        if urun == "arpa":
            st.markdown("- 1. Hafta: Nemli tut\n- 2. Hafta: İlk sulama\n- 3-6. Hafta: Haftalık sulama\n- 7. Hafta: Sulama yapılmaz")

        st.subheader("🌿 Gübre Tavsiyesi")
        if urun == "arpa" and toprak == "tınlı":
            st.write("20-20-20 kompoze gübre - dekara 50 kg")

        st.subheader("🌾 Alternatif Ürün Önerisi")
        if rakim and rakim > 1700:
            st.write("Nohut veya mercimek önerilir")
        else:
            st.write("Ayçiçeği veya fiğ alternatif olabilir")

        if verim_dosya:
            df = pd.read_csv(verim_dosya)
            if urun in df.columns:
                ort = df[urun].mean()
                st.subheader("📈 Tahmini Verim")
                st.write(f"Ortalama Verim: {ort:.2f} kg/dekar")
            else:
                st.warning(f"CSV içinde '{urun}' sütunu bulunamadı.")

        st.subheader("📝 Geri Bildirim")
        st.markdown("[Google Forms üzerinden bize ulaşın](https://forms.gle/yourformlink)")
