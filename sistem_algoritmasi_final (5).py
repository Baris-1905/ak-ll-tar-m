
if veri_turu == "Manuel Veri Girişi":
    st.header("🌾 Manuel Veri Girişi")

    urun = st.selectbox("Yetiştirilecek ürünü seçin:", urunler)
    konum = st.selectbox("Ekim yapılacak köy/mahalle:", list(hinos_koyleri.keys()))
    rakim = hinos_koyleri[konum]["rakim"]
    sicaklik = hinos_koyleri[konum]["sicaklik"]
    st.success(f"Rakım: {rakim} m | Ortalama Sıcaklık: {sicaklik} °C")

    toprak = st.selectbox("Toprak türü:", ["Killi", "Tınlı", "Kumlu", "Organik"])
    drenaj = st.selectbox("Drenaj durumu:", ["İyi", "Orta", "Kötü"])
    organik = st.selectbox("Organik madde miktarı:", ["Yüksek", "Orta", "Düşük"])
    arazi = st.number_input("Arazi büyüklüğü (dekar):", min_value=1)

    sulama_var = st.radio("Sulama yapıldı mı?", ["Evet", "Hayır"])
    if sulama_var == "Evet":
        sulama_turu = st.selectbox("Sulama türünü seçin:", ["Yağmurlama", "Damla", "Salma"])
    else:
        sulama_turu = "Yok"

    gubreleme_var = st.radio("Gübreleme yapıldı mı?", ["Evet", "Hayır"])
    if gubreleme_var == "Evet":
        gubre_turu = st.selectbox("Gübre türünü seçin:", list(gubre_aciklamalari.keys()))
        st.info(f"{gubre_turu}: {gubre_aciklamalari[gubre_turu]}")
    else:
        gubre_turu = "Yok"

    if st.button("📊 Sonuçları Göster"):
        st.subheader("📅 Ekim Tarihi Önerisi")
        st.write("Ekim için en uygun tarih: 15 Nisan - 5 Mayıs arası")

        st.subheader("💧 FAO56 Sulama Takvimi")
        for satir in fao56_sulama_detaylari[urun]:
            st.write(satir)

        if urun in ["Buğday", "Fasulye"] and sulama_var == "Hayır":
            st.warning("⚠️ Bu ürün için sulama yapılması önerilir.")
        if urun == "Fasulye" and gubreleme_var == "Hayır":
            st.warning("⚠️ Fasulye için gübreleme yapılması önerilir.")

        st.subheader("📈 Verim Tahmini")
        verim = verim_katsayi[urun] * arazi
        st.success(f"Tahmini verim: {verim} kg")


elif veri_turu == "Otomatik Veri (Drone)":
    st.header("🤖 Drone Simülasyonu Verisi")

    senaryo = st.selectbox("Simülasyon senaryosu seçin:", list(simulasyon_senaryolari.keys()))
    veri = simulasyon_senaryolari[senaryo]

    st.write(f"📌 Ürün: {veri['urun']}")
    st.write(f"📍 Konum: {veri['konum']}")
    st.write(f"📈 Rakım: {veri['rakim']} m, Sıcaklık: {veri['sicaklik']} °C")
    st.write(f"🧱 Toprak Türü: {veri['toprak']}, Organik Madde: {veri['organik_madde']}")
    st.write(f"💧 Sulama: {'Var - ' + veri['sulama_turu'] if veri['sulama_var'] else 'Yok'}")
    st.write(f"💩 Gübreleme: {'Var - ' + veri['gubre_turu'] if veri['gubreleme_var'] else 'Yok'}")
    st.write(f"📐 Arazi Büyüklüğü: {veri['arazi_buyuklugu']} dekar")

    if st.button("📊 Sonuçları Göster", key="simulasyon_sonuc"):
        st.subheader("📅 Ekim Tarihi Önerisi")
        st.write("Ekim için en uygun tarih: 10 Nisan - 25 Nisan arası")

        st.subheader("💧 FAO56 Sulama Takvimi")
        for satir in fao56_sulama_detaylari[veri["urun"]]:
            st.write(satir)

        if veri["urun"] in ["Buğday", "Fasulye"] and not veri["sulama_var"]:
            st.warning("⚠️ Bu ürün için sulama yapılması önerilir.")
        if veri["urun"] == "Fasulye" and not veri["gubreleme_var"]:
            st.warning("⚠️ Fasulye için gübreleme yapılması önerilir.")

        st.subheader("📈 Verim Tahmini")
        verim = verim_katsayi[veri["urun"]] * veri["arazi_buyuklugu"]
        st.success(f"Tahmini verim: {verim} kg")

elif veri_turu == "Excel ile Geçmiş Veriler":
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
                st.info("ℹ️ 'Yıl' ve 'Verim' sütunlarının olduğundan emin olun.")

        except Exception as e:
            st.error(f"Hata oluştu: {e}")
