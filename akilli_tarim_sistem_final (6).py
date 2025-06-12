
# Akıllı Tarım Karar Destek Sistemi - Final Sürüm

import streamlit as st

st.set_page_config(page_title="Akıllı Tarım Karar Destek Sistemi")
st.title("🌱 Akıllı Tarım Karar Destek Sistemi")

st.markdown("""
Bu sistem, Erzurum Hınıs ilçesinin 98 mahallesi için:
- Mahalleye göre otomatik pH, azot, fosfor tahmini
- FAO56 sulama takvimi (evre bazlı)
- Hastalık + ilaç önerisi
- Dinamik alternatif ürün önerisi
- Gübre tavsiyesi + ahır gübresi desteği
- Arazi büyüklüğüne göre dozajlama
sunmaktadır.
""")

st.warning("⚠️ Bu bir demo şablondur. Sistem modülleri bir sonraki adımda yüklenecek.")
