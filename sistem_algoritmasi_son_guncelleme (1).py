
# Akıllı Tarım Karar Destek Sistemi (Güncel Sürüm)
# pyrebase kaldırıldı, REST API üzerinden Firebase ile giriş/kayıt sağlanıyor
# Diğer modüller: sulama, gübre önerisi, veri analizi vs. dahil

import streamlit as st
import requests
import pandas as pd
import numpy as np
from datetime import datetime
from geopy.geocoders import Nominatim

# Firebase yapılandırması
FIREBASE_API_KEY = st.secrets["firebase"]["api_key"]
FIREBASE_PROJECT_URL = st.secrets["firebase"]["database_url"]

# Firebase kimlik doğrulama endpointleri
FIREBASE_SIGNUP_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={FIREBASE_API_KEY}"
FIREBASE_SIGNIN_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}"

def kayit_ol(username, password):
    payload = {"email": f"{username}@example.com", "password": password, "returnSecureToken": True}
    response = requests.post(FIREBASE_SIGNUP_URL, data=payload)
    return response

def giris_yap(username, password):
    payload = {"email": f"{username}@example.com", "password": password, "returnSecureToken": True}
    response = requests.post(FIREBASE_SIGNIN_URL, data=payload)
    return response

# Giriş/Kayıt Arayüzü
if "giris_yapildi" not in st.session_state:
    st.session_state.giris_yapildi = False

if not st.session_state.giris_yapildi:
    st.title("🔐 Giriş Yap / Kayıt Ol")
    secenek = st.radio("Seçiminiz:", ["Giriş Yap", "Kayıt Ol"])
    kullanici_adi = st.text_input("Kullanıcı Adı")
    parola = st.text_input("Parola", type="password")

    if secenek == "Kayıt Ol":
        if st.button("Kaydol"):
            sonuc = kayit_ol(kullanici_adi, parola)
            if sonuc.status_code == 200:
                st.success("Kayıt başarılı, şimdi giriş yapabilirsin.")
            else:
                st.error("Kayıt başarısız. Kullanıcı zaten kayıtlı olabilir ya da parola zayıf.")
    else:
        if st.button("Giriş Yap"):
            sonuc = giris_yap(kullanici_adi, parola)
            if sonuc.status_code == 200:
                st.session_state.giris_yapildi = True
                st.session_state.kullanici = kullanici_adi
                st.experimental_rerun()
            else:
                st.error("Giriş başarısız. Bilgileri kontrol et.")
else:
    st.success(f"Hoş geldin, {st.session_state.kullanici}!")

    # Buraya sonrası: veri girişi, analiz, sulama, gübre önerisi vs.
    st.subheader("🌱 Akıllı Tarım Sistemine Hoş Geldin")

    veri_turu = st.selectbox("Veri giriş türünü seç:", ["Manuel Veri Girişi", "Drone Verisi", "Geçmiş Veriler (Excel)"])
    if veri_turu == "Geçmiş Veriler (Excel)":
        dosya = st.file_uploader("Excel dosyasını yükle (.xlsx, .csv)", type=["xlsx", "csv"])
        if dosya:
            if dosya.name.endswith(".csv"):
                df = pd.read_csv(dosya)
            else:
                df = pd.read_excel(dosya)
            st.dataframe(df)
            st.info("Veri yüklendi, analiz başlayabilir.")
    else:
        st.write("Bu bölüm geliştirilmeye devam ediyor...")
