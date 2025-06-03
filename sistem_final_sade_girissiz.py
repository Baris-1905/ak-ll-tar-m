
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="AkÄ±llÄ± TarÄ±m Karar Destek Sistemi", layout="centered")
st.title("ð¾ AkÄ±llÄ± TarÄ±m Karar Destek Sistemi")

if "veri_turu" not in st.session_state:
    st.session_state.veri_turu = None

if st.session_state.veri_turu is None:
    st.subheader("ð Merhaba, HoÅ Geldiniz. LÃ¼tfen veri giriÅ tÃ¼rÃ¼nÃ¼ seÃ§in:")
    st.session_state.veri_turu = st.radio("Veri GiriÅ TÃ¼rÃ¼", ["Manuel Veri GiriÅi", "Excel ile GeÃ§miÅ Veriler"])
    st.stop()

veri_turu = st.session_state.veri_turu

urunler = ["Arpa", "BuÄday", "Fasulye"]
verim_katsayi = {"Arpa": 280, "BuÄday": 320, "Fasulye": 250}
gubre_aciklamalari = {
    "AhÄ±r GÃ¼bresi": "Organik gÃ¼bre. Toprak yapÄ±sÄ±nÄ± iyileÅtirir.",
    "20-20-20": "Dengeli gÃ¼bre. %20 N, %20 P, %20 K.",
    "15-15-30": "Potasyum aÄÄ±rlÄ±klÄ±. Kaliteyi artÄ±rÄ±r.",
    "Kompoze": "Genel amaÃ§lÄ± farklÄ± oranlarda NPK iÃ§erir."
}
fao56_sulama_detaylari = {
    "BuÄday": [
        "Ãimlenme (1-2. hafta): 25 mm",
        "KardeÅlenme (3-4. hafta): 30 mm",
        "Sapa kalkma (5-6. hafta): 35 mm",
        "BaÅaklanma (7-8. hafta): 40 mm",
        "OlgunlaÅma (9-10. hafta): 20 mm"
    ],
    "Arpa": [
        "Ãimlenme (1-2. hafta): 20 mm",
        "KardeÅlenme (3-4. hafta): 25 mm",
        "Sapa kalkma (5-6. hafta): 30 mm",
        "BaÅaklanma (7-8. hafta): 35 mm",
        "OlgunlaÅma (9-10. hafta): 15 mm"
    ],
    "Fasulye": [
        "Ãimlenme (1-2. hafta): 30 mm",
        "Yapraklanma (3-4. hafta): 35 mm",
        "ÃiÃ§eklenme (5-6. hafta): 40 mm",
        "Bakla oluÅumu (7-8. hafta): 45 mm",
        "OlgunlaÅma (9-10. hafta): 25 mm"
    ]
}
hinos_koyleri = {
    "Erbeyli": {"rakim": 1750, "sicaklik": 17},
    "AÅaÄÄ±kayabaÅÄ±": {"rakim": 1700, "sicaklik": 16},
    "BellitaÅ": {"rakim": 1780, "sicaklik": 15},
    "YukarÄ±Ã§ayÄ±rlÄ±": {"rakim": 1790, "sicaklik": 16},
    "KÄ±zÄ±lkale": {"rakim": 1745, "sicaklik": 17},
    "HalilÃ§avuÅ": {"rakim": 1710, "sicaklik": 18},
    "Karabudak": {"rakim": 1800, "sicaklik": 16},
    "Ortaderik": {"rakim": 1770, "sicaklik": 15},
    "SÃ¼tlÃ¼ce": {"rakim": 1690, "sicaklik": 17},
    "YukarÄ±aktaÅ": {"rakim": 1810, "sicaklik": 14},
    "Sergen": {"rakim": 1760, "sicaklik": 15},
    "ÃayÄ±rlÄ±": {"rakim": 1705, "sicaklik": 16},
    "BaÅarÄ±": {"rakim": 1725, "sicaklik": 17},
    "GÃ¶ller": {"rakim": 1755, "sicaklik": 16},
    "TatarcÄ±k": {"rakim": 1795, "sicaklik": 15}
}

if veri_turu == "Manuel Veri GiriÅi":
    st.header("ð§âð¾ Manuel Veri GiriÅi")

    urun = st.selectbox("YetiÅtirilecek ÃrÃ¼n:", urunler)
    konum = st.selectbox("Ekim YapÄ±lacak KÃ¶y/Mahalle:", list(hinos_koyleri.keys()))
    rakim = hinos_koyleri[konum]["rakim"]
    sicaklik = hinos_koyleri[konum]["sicaklik"]
    st.success(f"RakÄ±m: {rakim} m | SÄ±caklÄ±k: {sicaklik} Â°C")

    toprak = st.selectbox("Toprak TÃ¼rÃ¼:", ["Killi", "TÄ±nlÄ±", "Kumlu", "Organik"])
    organik = st.selectbox("Organik Madde MiktarÄ±:", ["DÃ¼ÅÃ¼k", "Orta", "YÃ¼ksek"])
    azot = st.slider("Topraktaki Azot OranÄ± (mg/kg)", 0, 100, 30)
    fosfor = st.slider("Topraktaki Fosfor OranÄ± (mg/kg)", 0, 100, 25)
    ph = st.slider("Toprak pH DeÄeri", 4.5, 9.0, 6.5)

    arazi = st.number_input("Arazi BÃ¼yÃ¼klÃ¼ÄÃ¼ (dekar):", min_value=1)

    sulama_var = st.radio("Sulama yapÄ±ldÄ± mÄ±?", ["Evet", "HayÄ±r"])
    if sulama_var == "Evet":
        sulama_turu = st.selectbox("Sulama TÃ¼rÃ¼:", ["YaÄmurlama", "Damla", "Salma"])
    else:
        sulama_turu = "Yok"

    gubreleme_var = st.radio("GÃ¼breleme yapÄ±ldÄ± mÄ±?", ["Evet", "HayÄ±r"])
    if gubreleme_var == "Evet":
        gubre_turu = st.selectbox("GÃ¼bre TÃ¼rÃ¼:", list(gubre_aciklamalari.keys()))
        st.caption(gubre_aciklamalari[gubre_turu])
    else:
        gubre_turu = "Yok"

    if st.button("ð SonuÃ§larÄ± GÃ¶ster"):
        st.subheader("ð Ekim Tarihi Ãnerisi")
        st.info("En uygun ekim tarihi: 10 Nisan - 25 Nisan arasÄ±")

        st.subheader("ð§ FAO56 Sulama Takvimi")
        for evre in fao56_sulama_detaylari[urun]:
            st.write("â¢ " + evre)

        if urun in ["Fasulye", "BuÄday"] and sulama_var == "HayÄ±r":
            st.warning("â ï¸ Bu Ã¼rÃ¼n iÃ§in sulama yapÄ±lmasÄ± gereklidir.")

        if urun == "Fasulye" and gubreleme_var == "HayÄ±r":
            st.warning("â ï¸ Fasulye iÃ§in gÃ¼breleme yapÄ±lmasÄ± Ã¶nerilir.")

        st.subheader("ð¦  OlasÄ± HastalÄ±klar ve Ä°laÃ§lama")
        hastaliklar = []
        if urun == "BuÄday":
            if rakim > 1700 and sicaklik < 17 and toprak == "Killi":
                hastaliklar.append("KÃ¶k BoÄazÄ± ÃÃ¼rÃ¼klÃ¼ÄÃ¼")
            if ph < 6.0 or azot < 20:
                hastaliklar.append("Pas HastalÄ±ÄÄ±")
        elif urun == "Arpa":
            if rakim > 1750 or ph > 8.0:
                hastaliklar.append("Arpa Mozaik VirÃ¼sÃ¼")
            if organik == "DÃ¼ÅÃ¼k":
                hastaliklar.append("Yaprak YanÄ±klÄ±ÄÄ±")
        elif urun == "Fasulye":
            if sicaklik > 18 and ph > 7.5:
                hastaliklar.append("KÃ¶k ÃÃ¼rÃ¼klÃ¼ÄÃ¼")
            if azot < 25:
                hastaliklar.append("Antraknoz")

        if hastaliklar:
            for h in hastaliklar:
                st.error(f"â ï¸ OlasÄ± HastalÄ±k: {h}")
            st.warning("ð§ª Tavsiye: TarÄ±m ilacÄ± kullanÄ±mÄ± iÃ§in ziraat mÃ¼hendisine danÄ±ÅÄ±nÄ±z.")
        else:
            st.success("â HastalÄ±k riski dÃ¼ÅÃ¼k. Ãretime devam edilebilir.")

        st.subheader("ð Tahmini Verim")
        verim = verim_katsayi[urun] * arazi
        st.success(f"{urun} iÃ§in tahmini verim: {verim} kg")

elif veri_turu == "Excel ile GeÃ§miÅ Veriler":
    st.header("ð Excel ile GeÃ§miÅ Verileri YÃ¼kleyin")

    yuklenen_dosya = st.file_uploader("Excel dosyanÄ±zÄ± yÃ¼kleyin (.xlsx):", type=["xlsx"])

    if yuklenen_dosya is not None:
        try:
            df = pd.read_excel(yuklenen_dosya)
            st.success("â Dosya baÅarÄ±yla yÃ¼klendi.")
            st.dataframe(df)

            if 'YÄ±l' in df.columns and 'Verim' in df.columns:
                st.subheader("ð YÄ±llara GÃ¶re Verim GrafiÄi")
                df_sorted = df.sort_values("YÄ±l")
                st.line_chart(df_sorted.set_index("YÄ±l")["Verim"])

                st.subheader("ð Temel Ä°statistikler")
                st.write(df["Verim"].describe())
            else:
                st.warning("â ï¸ 'YÄ±l' ve 'Verim' sÃ¼tunlarÄ±nÄ±n dosyada bulunduÄundan emin olun.")

        except Exception as e:
            st.error(f"Hata oluÅtu: {e}")
