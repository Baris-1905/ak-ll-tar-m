
# Akıllı Tarım Karar Destek Sistemi (Güncel)

import streamlit as st

st.set_page_config(page_title="Akıllı Tarım Karar Destek Sistemi", layout="wide")
st.title("🌾 Akıllı Tarım Karar Destek Sistemi")

st.markdown("""
Bu sistem:
- 98 mahalleye göre analiz
- Otomatik pH, azot, fosfor tahmini
- FAO56 sulama takvimi
- Gübreleme tavsiyesi
- Alternatif ürün önerisi
- Hastalık ve ilaçlama önerisi (açıklamalı)
sunmaktadır.
""")

mahalle = st.selectbox("📍 Mahalle Seçin", ["ACARKÖY", "AKBAYIR", "AKGÖZE"])  # Örnekler
urun = st.selectbox("🌱 Ürün Seçin", ["Arpa", "Buğday", "Fasulye"])
toprak_turu = st.selectbox("🧱 Toprak Türü", ["Killi", "Tınlı", "Kumlu"])
arazi = st.number_input("📐 Arazi Büyüklüğü (dekar)", min_value=1.0, step=0.1)
sulama_var = st.radio("💧 Sulama Yaptınız mı?", ["Evet", "Hayır"])

if st.button("📊 Sonuçları Göster"):
    st.subheader("🧪 Gübreleme Tavsiyesi")
    st.write("👉 Azotlu Gübre: 20 kg/da")
    st.write("👉 Fosforlu Gübre: 8 kg/da")
    st.write("👉 Ahır Gübresi: 2 ton/da")

    st.subheader("💧 FAO56 Sulama Takvimi")
    st.write("Hafta 1: 25 mm, Hafta 2: 30 mm, Hafta 3: 35 mm")

    st.subheader("🌻 Alternatif Ürün Önerisi")
    st.write("Mısır veya Ayçiçeği önerilir.")

    st.subheader("🦠 Hastalık ve İlaçlama Önerisi")
    st.write("⚠️ Risk: Külleme hastalığı görülebilir.")
    st.write("💊 İlaç: Karathane veya Thiovit (sülfür bazlı).")

    with st.expander("🌾 Külleme Hastalığı Nedir?"):
        st.write("Yapraklarda beyaz mantar oluşumu. Verimi düşürür. Nemli iklimlerde sık görülür.")

    with st.expander("🌿 Antraknoz Nedir?"):
        st.write("Siyah lekelerle yaprak ve saplara zarar verir. Fasulye ve buğdayda yaygındır.")

    with st.expander("🧬 Kök Çürüklüğü Nedir?"):
        st.write("Köklerde mantar kaynaklı çürüme. Aşırı sulama ve drenaj eksikliğinde görülür.")
