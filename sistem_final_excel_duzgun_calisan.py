import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Akıllı Tarım Karar Destek Sistemi", layout="centered")

st.title("Akıllı Tarım Karar Destek Sistemi")

veri_turu = st.radio("Veri giriş türünü seçin:", ["Manuel Veri Girişi", "Excel ile Geçmiş Veriler"])

if veri_turu == "Manuel Veri Girişi":
    # Buraya manuel veri girişi ekranı koyulacak (orijinal koddan alınarak)
    st.header("🧑‍🌾 Manuel Veri Girişi")
    # ... (devam eden manuel giriş kodları)

elif veri_turu == "Excel ile Geçmiş Veriler":
    # Buraya excel veri yükleme ve analiz kısmı yazılacak
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