
# Akıllı Tarım Karar Destek Sistemi - Firebase Yorum Satırı Versiyonu

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from io import BytesIO
from geopy.geocoders import Nominatim
# import firebase_admin
# from firebase_admin import credentials, auth

# Firebase bağlantısı geçici olarak devre dışı
# if not firebase_admin._apps:
#     cred = credentials.Certificate({
#         "type": st.secrets["firebase"]["type"],
#         "project_id": st.secrets["firebase"]["project_id"],
#         "private_key_id": st.secrets["firebase"]["private_key_id"],
#         "private_key": st.secrets["firebase"]["private_key"].replace("\\n", "\n"),
#         "client_email": st.secrets["firebase"]["client_email"],
#         "client_id": st.secrets["firebase"]["client_id"],
#         "auth_uri": st.secrets["firebase"]["auth_uri"],
#         "token_uri": st.secrets["firebase"]["token_uri"],
#         "auth_provider_x509_cert_url": st.secrets["firebase"]["auth_provider_x509_cert_url"],
#         "client_x509_cert_url": st.secrets["firebase"]["client_x509_cert_url"]
#     })
#     firebase_admin.initialize_app(cred)

st.set_page_config(page_title="Akıllı Tarım KDS", layout="centered")
st.title("🌾 Akıllı Tarım Karar Destek Sistemi")

st.success("Firebase geçici olarak devre dışı bırakıldı. Settings > Secrets sekmesini etkinleştirmek için.")    
