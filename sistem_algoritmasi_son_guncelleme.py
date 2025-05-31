
import streamlit as st
import pandas as pd
import numpy as np
import json
from datetime import datetime
import base64
from io import BytesIO
from geopy.geocoders import Nominatim
import pyrebase

st.set_page_config(page_title="Akıllı Tarım Karar Destek Sistemi", layout="wide")

# --- Firebase Ayarları ---
firebase_config = {
    "apiKey": st.secrets["firebase"]["api_key"],
    "authDomain": st.secrets["firebase"]["auth_domain"],
    "databaseURL": st.secrets["firebase"]["database_url"],
    "projectId": st.secrets["firebase"]["project_id"],
    "storageBucket": st.secrets["firebase"]["storage_bucket"],
    "messagingSenderId": st.secrets["firebase"]["messaging_sender_id"],
    "appId": st.secrets["firebase"]["app_id"],
    "measurementId": st.secrets["firebase"]["measurement_id"],
    "type": st.secrets["firebase"]["type"],
    "private_key_id": st.secrets["firebase"]["private_key_id"],
    "private_key": st.secrets["firebase"]["private_key"].replace("\n", "\n"),
    "client_email": st.secrets["firebase"]["client_email"],
    "client_id": st.secrets["firebase"]["client_id"],
    "auth_uri": st.secrets["firebase"]["auth_uri"],
    "token_uri": st.secrets["firebase"]["token_uri"],
    "auth_provider_x509_cert_url": st.secrets["firebase"]["auth_provider_x509_cert_url"],
    "client_x509_cert_url": st.secrets["firebase"]["client_x509_cert_url"]
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

# --- Kullanıcı oturumu ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

def giris_ekrani():
    secim = st.radio("Giriş yap veya kayıt ol", ["Giriş Yap", "Kayıt Ol"])

    if secim == "Giriş Yap":
        kullanici_adi = st.text_input("Kullanıcı Adı")
        sifre = st.text_input("Şifre", type="password")
        if st.button("Giriş Yap"):
            try:
                user = auth.sign_in_with_email_and_password(f"{kullanici_adi}@tarim.com", sifre)
                st.session_state.authenticated = True
                st.session_state.user_email = f"{kullanici_adi}@tarim.com"
            except Exception as e:
                st.error("Giriş başarısız. Kullanıcı adı veya şifre hatalı.")

    elif secim == "Kayıt Ol":
        yeni_kullanici = st.text_input("Yeni Kullanıcı Adı")
        yeni_sifre = st.text_input("Yeni Şifre", type="password")
        if st.button("Kayıt Ol"):
            try:
                auth.create_user_with_email_and_password(f"{yeni_kullanici}@tarim.com", yeni_sifre)
                st.success("Kayıt başarılı. Giriş yapabilirsiniz.")
            except Exception as e:
                st.error("Kayıt başarısız. Kullanıcı adı zaten kullanılıyor veya şifre zayıf.")

if not st.session_state.authenticated:
    giris_ekrani()
    st.stop()

# --- Kullanıcı Girişi Başarılı, Devam ---
st.title("🌾 Akıllı Tarım Karar Destek Sistemi")

# 1. Veri Giriş Türü
veri_turu = st.radio("📥 Veri Giriş Türü Seçin", ["Manuel Giriş", "Drone Verisi", "Geçmiş Veriler (Excel)"])
if veri_turu == "Geçmiş Veriler (Excel)":
    excel_dosya = st.file_uploader("Excel Dosyası Yükle", type=["xls", "xlsx", "csv"])
    if excel_dosya:
        df = pd.read_excel(excel_dosya) if "xls" in excel_dosya.name else pd.read_csv(excel_dosya)
        st.write("Yüklenen Veri:")
        st.dataframe(df)
    st.stop()
elif veri_turu == "Drone Verisi":
    st.info("Drone verisi örneği kullanılıyor. Bu özellik demo moddadır.")
    # Drone senaryosu buraya entegre edilecek
    st.stop()

# Manuel Veri Girişi
st.subheader("Ürün ve Üretim Bilgileri")
urun = st.selectbox("Ürün Seçiniz", ["Buğday", "Arpa", "Fasulye"])
tohum_turu = st.radio("Tohum Türü", ["Yerli", "Erkenci", "Geççi"])

st.subheader("Tarla ve Toprak Bilgileri")
arazi_buyuklugu = st.number_input("Arazi Büyüklüğü (dekar)", min_value=1.0)
gubre_tipi_kullanici = st.text_input("Kullandığınız Gübre Türü")

secilen_koy = st.selectbox("Köy veya Mahalle Seçin (Hınıs)", ["Yelpınar", "Bellitaş", "Erbeyli", "Kızılkale", "Karakale", "Aşağı Tüylü", "Yukarı Tüylü"])
rakimlar = {
    "Yelpınar": 1780,
    "Bellitaş": 1830,
    "Erbeyli": 1765,
    "Kızılkale": 1805,
    "Karakale": 1775,
    "Aşağı Tüylü": 1790,
    "Yukarı Tüylü": 1820
}
rakim = rakimlar.get(secilen_koy, 1800)

sicaklik = st.slider("Mevcut Ortalama Sıcaklık (°C)", 5, 40, 20)
sulama_yontemi = st.radio("Sulama Yöntemi", ["Yağmurlama", "Damlama", "Salma"])

if st.button("Hesapla"):
    st.success(f"Seçilen Ürün: {urun}")
    st.write(f"Tohum Türü: {tohum_turu}")
    st.write(f"Arazi Büyüklüğü: {arazi_buyuklugu} dekar")
    st.write(f"Kullanılan Gübre: {gubre_tipi_kullanici}")
    st.write(f"Köy: {secilen_koy} | Rakım: {rakim} m")
    st.write(f"Sıcaklık: {sicaklik}°C | Sulama: {sulama_yontemi}")

    # Öneriler
    st.subheader("🌱 Gübre Tavsiyesi")
    if urun == "Buğday":
        st.write("Önerilen Gübre: 20-20-0 veya ÜRE")
    elif urun == "Arpa":
        st.write("Önerilen Gübre: 18-46-0 DAP")
    elif urun == "Fasulye":
        st.write("Önerilen Gübre: Triple Süper Fosfat + Potasyum Nitrat")

    st.subheader("📅 Tavsiye Edilen Ekim Tarihi")
    if urun == "Buğday":
        st.info("Ekim Zamanı: 15 Eylül - 15 Ekim")
    elif urun == "Arpa":
        st.info("Ekim Zamanı: 20 Eylül - 20 Ekim")
    elif urun == "Fasulye":
        st.info("Ekim Zamanı: 1 Mayıs - 20 Mayıs")

    st.subheader("💧 Sulama Takvimi (FAO56 tahmini)")
    if sulama_yontemi == "Damlama":
        st.write("Haftada 2 kez, 12 mm sulama")
    elif sulama_yontemi == "Yağmurlama":
        st.write("Haftada 1 kez, 20 mm sulama")
    elif sulama_yontemi == "Salma":
        st.write("10 günde bir, 30 mm sulama")
