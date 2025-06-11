
# -*- coding: utf-8 -*-
import streamlit as st

mahalle_verisi = {
  "ACARKÖY": {
    "Enlem": 39.4,
    "Boylam": 41.5,
    "Rakım (m)": 1650.0,
    "Sıcaklık (°C)": 7.5
  },
  "ALİKIRI": {
    "Enlem": 39.409,
    "Boylam": 41.509,
    "Rakım (m)": 1704.0,
    "Sıcaklık (°C)": 8.5
  }
}

st.title("Akıllı Tarım Karar Destek Sistemi")

secili_mahalle = st.selectbox("Mahalle Seçiniz", list(mahalle_verisi.keys()))
if secili_mahalle:
    v = mahalle_verisi[secili_mahalle]
    st.markdown(f"**Seçilen Mahalle:** {secili_mahalle}")
    st.markdown(f"**Enlem:** {v['Enlem']}")
    st.markdown(f"**Boylam:** {v['Boylam']}")
    st.markdown(f"**Rakım:** {v['Rakım (m)']} m")
    st.markdown(f"**Sıcaklık:** {v['Sıcaklık (°C)']} °C")

    urun = st.selectbox("Ürün Seçiniz", ["Arpa", "Buğday", "Fasulye"])
    toprak_turu = st.selectbox("Toprak Türü", ["Killi", "Kumlu", "Tınlı", "Kireçli"])
    sulama_yapildi = st.radio("Bu sezon sulama yaptınız mı?", ["Evet", "Hayır"])
    arazi_buyuklugu = st.number_input("Araziniz kaç dekar?", min_value=1)

    def tahmini_toprak_degerleri(toprak):
        if toprak == "Killi":
            return 6.4, "Düşük", "Orta"
        elif toprak == "Tınlı":
            return 6.8, "Orta", "Yüksek"
        elif toprak == "Kumlu":
            return 7.2, "Düşük", "Düşük"
        else:
            return 7.0, "Orta", "Orta"

    pH, azot, fosfor = tahmini_toprak_degerleri(toprak_turu)

    st.subheader("Tahmini Toprak Değerleri")
    st.markdown(f"- pH: {pH}")
    st.markdown(f"- Azot Durumu: {azot}")
    st.markdown(f"- Fosfor Durumu: {fosfor}")

    if urun in ["Fasulye", "Buğday"] and sulama_yapildi == "Hayır":
        st.error("⚠️ Bu ürün için sulama yapılması gereklidir. Lütfen sulama yapınız.")

    st.subheader("Gübreleme Tavsiyesi")
    if urun == "Arpa":
        st.markdown("- Azotlu Gübre: 20-25 kg/da")
        st.markdown("- Ahır Gübresi: 2-3 ton/da")
    elif urun == "Buğday":
        st.markdown("- Üre (46% N): 25-30 kg/da")
        st.markdown("- Ahır Gübresi: 2 ton/da")
    elif urun == "Fasulye":
        st.markdown("- Triple Süper Fosfat (43-44% P₂O₅): 20 kg/da")
        st.markdown("- Ahır Gübresi: 2.5 ton/da")

    st.subheader("Hastalık ve İlaçlama Önerisi")
    if urun == "Buğday":
        if v['Sıcaklık (°C)'] > 8:
            st.warning("Septorya riski yüksek. Tavsiye: Tebuconazole.")
        if toprak_turu == "Killi":
            st.warning("Kök hastalıkları riski. Tavsiye: Azoxystrobin.")
    elif urun == "Fasulye":
        if v['Rakım (m)'] < 1800:
            st.warning("Antraknoz riski. Tavsiye: Azoxystrobin.")
        if v['Sıcaklık (°C)'] > 8:
            st.warning("Külleme riski. Tavsiye: Karathane.")
    elif urun == "Arpa":
        if toprak_turu == "Killi":
            st.warning("Kök çürüklüğü riski. Tavsiye: Propiconazole.")
        if v['Rakım (m)'] > 1850:
            st.warning("Yaprak lekesi riski. Tavsiye: Mancozeb.")

    st.subheader("Alternatif Ürün Önerisi")
    def alternatif_urun_oner(urun, rakim, sicaklik, toprak):
        if urun == "Arpa":
            if rakim > 1850 and sicaklik < 7:
                return "Mercimek veya Nohut"
            else:
                return "Yulaf veya Fiğ"
        elif urun == "Buğday":
            if sicaklik > 8 and toprak == "Tınlı":
                return "Korunga veya Çavdar"
            else:
                return "Tritikale veya Fiğ"
        elif urun == "Fasulye":
            if rakim < 1800 and sicaklik > 8:
                return "Mısır veya Ayçiçeği"
            else:
                return "Patates veya Fiğ"
        return "Fiğ veya Yulaf"

    onerilen = alternatif_urun_oner(urun, v['Rakım (m)'], v['Sıcaklık (°C)'], toprak_turu)
    st.success(f"Alternatif olarak: {onerilen}")
