
import streamlit as st

st.title("🔐 Firebase Bağlantı Testi")

try:
    api_key = st.secrets["firebase"]["api_key"]
    db_url = st.secrets["firebase"]["database_url"]
    st.success("✅ Firebase bilgileri başarıyla yüklendi.")
    st.write("API Key:", api_key)
    st.write("Database URL:", db_url)
except KeyError as e:
    st.error(f"❌ Firebase yapılandırması hatalı veya eksik: {e}")
