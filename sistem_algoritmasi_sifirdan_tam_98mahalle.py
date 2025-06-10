
# -*- coding: utf-8 -*-
import streamlit as st

# 98 Mahallelik gömülü veri
mahalle_verisi = {
  "Mahalle_1": {
    "Enlem": 39.3,
    "Boylam": 41.6,
    "Rakım (m)": 1700.0,
    "Sıcaklık (°C)": 8.5
  },
  "Mahalle_2": {
    "Enlem": 39.300999999999995,
    "Boylam": 41.601,
    "Rakım (m)": 1705.0,
    "Sıcaklık (°C)": 8.4
  },
  "Mahalle_3": {
    "Enlem": 39.302,
    "Boylam": 41.602000000000004,
    "Rakım (m)": 1710.0,
    "Sıcaklık (°C)": 8.3
  },
  "Mahalle_4": {
    "Enlem": 39.303,
    "Boylam": 41.603,
    "Rakım (m)": 1715.0,
    "Sıcaklık (°C)": 8.2
  },
  "Mahalle_5": {
    "Enlem": 39.303999999999995,
    "Boylam": 41.604,
    "Rakım (m)": 1720.0,
    "Sıcaklık (°C)": 8.1
  },
  "Mahalle_6": {
    "Enlem": 39.305,
    "Boylam": 41.605000000000004,
    "Rakım (m)": 1725.0,
    "Sıcaklık (°C)": 8.5
  },
  "Mahalle_7": {
    "Enlem": 39.306,
    "Boylam": 41.606,
    "Rakım (m)": 1730.0,
    "Sıcaklık (°C)": 8.4
  },
  "Mahalle_8": {
    "Enlem": 39.306999999999995,
    "Boylam": 41.607,
    "Rakım (m)": 1735.0,
    "Sıcaklık (°C)": 8.3
  },
  "Mahalle_9": {
    "Enlem": 39.308,
    "Boylam": 41.608000000000004,
    "Rakım (m)": 1740.0,
    "Sıcaklık (°C)": 8.2
  },
  "Mahalle_10": {
    "Enlem": 39.309,
    "Boylam": 41.609,
    "Rakım (m)": 1745.0,
    "Sıcaklık (°C)": 8.1
  },
  "Mahalle_11": {
    "Enlem": 39.309999999999995,
    "Boylam": 41.61,
    "Rakım (m)": 1750.0,
    "Sıcaklık (°C)": 8.5
  },
  "Mahalle_12": {
    "Enlem": 39.311,
    "Boylam": 41.611000000000004,
    "Rakım (m)": 1755.0,
    "Sıcaklık (°C)": 8.4
  },
  "Mahalle_13": {
    "Enlem": 39.312,
    "Boylam": 41.612,
    "Rakım (m)": 1760.0,
    "Sıcaklık (°C)": 8.3
  },
  "Mahalle_14": {
    "Enlem": 39.312999999999995,
    "Boylam": 41.613,
    "Rakım (m)": 1765.0,
    "Sıcaklık (°C)": 8.2
  },
  "Mahalle_15": {
    "Enlem": 39.314,
    "Boylam": 41.614000000000004,
    "Rakım (m)": 1770.0,
    "Sıcaklık (°C)": 8.1
  },
  "Mahalle_16": {
    "Enlem": 39.315,
    "Boylam": 41.615,
    "Rakım (m)": 1775.0,
    "Sıcaklık (°C)": 8.5
  },
  "Mahalle_17": {
    "Enlem": 39.315999999999995,
    "Boylam": 41.616,
    "Rakım (m)": 1780.0,
    "Sıcaklık (°C)": 8.4
  },
  "Mahalle_18": {
    "Enlem": 39.317,
    "Boylam": 41.617000000000004,
    "Rakım (m)": 1785.0,
    "Sıcaklık (°C)": 8.3
  },
  "Mahalle_19": {
    "Enlem": 39.318,
    "Boylam": 41.618,
    "Rakım (m)": 1790.0,
    "Sıcaklık (°C)": 8.2
  },
  "Mahalle_20": {
    "Enlem": 39.318999999999996,
    "Boylam": 41.619,
    "Rakım (m)": 1795.0,
    "Sıcaklık (°C)": 8.1
  },
  "Mahalle_21": {
    "Enlem": 39.32,
    "Boylam": 41.620000000000005,
    "Rakım (m)": 1800.0,
    "Sıcaklık (°C)": 8.5
  },
  "Mahalle_22": {
    "Enlem": 39.321,
    "Boylam": 41.621,
    "Rakım (m)": 1805.0,
    "Sıcaklık (°C)": 8.4
  },
  "Mahalle_23": {
    "Enlem": 39.321999999999996,
    "Boylam": 41.622,
    "Rakım (m)": 1810.0,
    "Sıcaklık (°C)": 8.3
  },
  "Mahalle_24": {
    "Enlem": 39.323,
    "Boylam": 41.623000000000005,
    "Rakım (m)": 1815.0,
    "Sıcaklık (°C)": 8.2
  },
  "Mahalle_25": {
    "Enlem": 39.324,
    "Boylam": 41.624,
    "Rakım (m)": 1820.0,
    "Sıcaklık (°C)": 8.1
  },
  "Mahalle_26": {
    "Enlem": 39.324999999999996,
    "Boylam": 41.625,
    "Rakım (m)": 1700.0,
    "Sıcaklık (°C)": 8.5
  },
  "Mahalle_27": {
    "Enlem": 39.326,
    "Boylam": 41.626000000000005,
    "Rakım (m)": 1705.0,
    "Sıcaklık (°C)": 8.4
  },
  "Mahalle_28": {
    "Enlem": 39.327,
    "Boylam": 41.627,
    "Rakım (m)": 1710.0,
    "Sıcaklık (°C)": 8.3
  },
  "Mahalle_29": {
    "Enlem": 39.327999999999996,
    "Boylam": 41.628,
    "Rakım (m)": 1715.0,
    "Sıcaklık (°C)": 8.2
  },
  "Mahalle_30": {
    "Enlem": 39.329,
    "Boylam": 41.629000000000005,
    "Rakım (m)": 1720.0,
    "Sıcaklık (°C)": 8.1
  },
  "Mahalle_31": {
    "Enlem": 39.33,
    "Boylam": 41.63,
    "Rakım (m)": 1725.0,
    "Sıcaklık (°C)": 8.5
  },
  "Mahalle_32": {
    "Enlem": 39.330999999999996,
    "Boylam": 41.631,
    "Rakım (m)": 1730.0,
    "Sıcaklık (°C)": 8.4
  },
  "Mahalle_33": {
    "Enlem": 39.331999999999994,
    "Boylam": 41.632,
    "Rakım (m)": 1735.0,
    "Sıcaklık (°C)": 8.3
  },
  "Mahalle_34": {
    "Enlem": 39.333,
    "Boylam": 41.633,
    "Rakım (m)": 1740.0,
    "Sıcaklık (°C)": 8.2
  },
  "Mahalle_35": {
    "Enlem": 39.333999999999996,
    "Boylam": 41.634,
    "Rakım (m)": 1745.0,
    "Sıcaklık (°C)": 8.1
  },
  "Mahalle_36": {
    "Enlem": 39.334999999999994,
    "Boylam": 41.635,
    "Rakım (m)": 1750.0,
    "Sıcaklık (°C)": 8.5
  },
  "Mahalle_37": {
    "Enlem": 39.336,
    "Boylam": 41.636,
    "Rakım (m)": 1755.0,
    "Sıcaklık (°C)": 8.4
  },
  "Mahalle_38": {
    "Enlem": 39.336999999999996,
    "Boylam": 41.637,
    "Rakım (m)": 1760.0,
    "Sıcaklık (°C)": 8.3
  },
  "Mahalle_39": {
    "Enlem": 39.337999999999994,
    "Boylam": 41.638,
    "Rakım (m)": 1765.0,
    "Sıcaklık (°C)": 8.2
  },
  "Mahalle_40": {
    "Enlem": 39.339,
    "Boylam": 41.639,
    "Rakım (m)": 1770.0,
    "Sıcaklık (°C)": 8.1
  },
  "Mahalle_41": {
    "Enlem": 39.339999999999996,
    "Boylam": 41.64,
    "Rakım (m)": 1775.0,
    "Sıcaklık (°C)": 8.5
  },
  "Mahalle_42": {
    "Enlem": 39.340999999999994,
    "Boylam": 41.641,
    "Rakım (m)": 1780.0,
    "Sıcaklık (°C)": 8.4
  },
  "Mahalle_43": {
    "Enlem": 39.342,
    "Boylam": 41.642,
    "Rakım (m)": 1785.0,
    "Sıcaklık (°C)": 8.3
  },
  "Mahalle_44": {
    "Enlem": 39.342999999999996,
    "Boylam": 41.643,
    "Rakım (m)": 1790.0,
    "Sıcaklık (°C)": 8.2
  },
  "Mahalle_45": {
    "Enlem": 39.343999999999994,
    "Boylam": 41.644,
    "Rakım (m)": 1795.0,
    "Sıcaklık (°C)": 8.1
  },
  "Mahalle_46": {
    "Enlem": 39.345,
    "Boylam": 41.645,
    "Rakım (m)": 1800.0,
    "Sıcaklık (°C)": 8.5
  },
  "Mahalle_47": {
    "Enlem": 39.346,
    "Boylam": 41.646,
    "Rakım (m)": 1805.0,
    "Sıcaklık (°C)": 8.4
  },
  "Mahalle_48": {
    "Enlem": 39.346999999999994,
    "Boylam": 41.647,
    "Rakım (m)": 1810.0,
    "Sıcaklık (°C)": 8.3
  },
  "Mahalle_49": {
    "Enlem": 39.348,
    "Boylam": 41.648,
    "Rakım (m)": 1815.0,
    "Sıcaklık (°C)": 8.2
  },
  "Mahalle_50": {
    "Enlem": 39.349,
    "Boylam": 41.649,
    "Rakım (m)": 1820.0,
    "Sıcaklık (°C)": 8.1
  },
  "Mahalle_51": {
    "Enlem": 39.349999999999994,
    "Boylam": 41.65,
    "Rakım (m)": 1700.0,
    "Sıcaklık (°C)": 8.5
  },
  "Mahalle_52": {
    "Enlem": 39.351,
    "Boylam": 41.651,
    "Rakım (m)": 1705.0,
    "Sıcaklık (°C)": 8.4
  },
  "Mahalle_53": {
    "Enlem": 39.352,
    "Boylam": 41.652,
    "Rakım (m)": 1710.0,
    "Sıcaklık (°C)": 8.3
  },
  "Mahalle_54": {
    "Enlem": 39.352999999999994,
    "Boylam": 41.653,
    "Rakım (m)": 1715.0,
    "Sıcaklık (°C)": 8.2
  },
  "Mahalle_55": {
    "Enlem": 39.354,
    "Boylam": 41.654,
    "Rakım (m)": 1720.0,
    "Sıcaklık (°C)": 8.1
  },
  "Mahalle_56": {
    "Enlem": 39.355,
    "Boylam": 41.655,
    "Rakım (m)": 1725.0,
    "Sıcaklık (°C)": 8.5
  },
  "Mahalle_57": {
    "Enlem": 39.355999999999995,
    "Boylam": 41.656,
    "Rakım (m)": 1730.0,
    "Sıcaklık (°C)": 8.4
  },
  "Mahalle_58": {
    "Enlem": 39.357,
    "Boylam": 41.657000000000004,
    "Rakım (m)": 1735.0,
    "Sıcaklık (°C)": 8.3
  },
  "Mahalle_59": {
    "Enlem": 39.358,
    "Boylam": 41.658,
    "Rakım (m)": 1740.0,
    "Sıcaklık (°C)": 8.2
  },
  "Mahalle_60": {
    "Enlem": 39.358999999999995,
    "Boylam": 41.659,
    "Rakım (m)": 1745.0,
    "Sıcaklık (°C)": 8.1
  },
  "Mahalle_61": {
    "Enlem": 39.36,
    "Boylam": 41.660000000000004,
    "Rakım (m)": 1750.0,
    "Sıcaklık (°C)": 8.5
  },
  "Mahalle_62": {
    "Enlem": 39.361,
    "Boylam": 41.661,
    "Rakım (m)": 1755.0,
    "Sıcaklık (°C)": 8.4
  },
  "Mahalle_63": {
    "Enlem": 39.361999999999995,
    "Boylam": 41.662,
    "Rakım (m)": 1760.0,
    "Sıcaklık (°C)": 8.3
  },
  "Mahalle_64": {
    "Enlem": 39.363,
    "Boylam": 41.663000000000004,
    "Rakım (m)": 1765.0,
    "Sıcaklık (°C)": 8.2
  },
  "Mahalle_65": {
    "Enlem": 39.364,
    "Boylam": 41.664,
    "Rakım (m)": 1770.0,
    "Sıcaklık (°C)": 8.1
  },
  "Mahalle_66": {
    "Enlem": 39.364999999999995,
    "Boylam": 41.665,
    "Rakım (m)": 1775.0,
    "Sıcaklık (°C)": 8.5
  },
  "Mahalle_67": {
    "Enlem": 39.366,
    "Boylam": 41.666000000000004,
    "Rakım (m)": 1780.0,
    "Sıcaklık (°C)": 8.4
  },
  "Mahalle_68": {
    "Enlem": 39.367,
    "Boylam": 41.667,
    "Rakım (m)": 1785.0,
    "Sıcaklık (°C)": 8.3
  },
  "Mahalle_69": {
    "Enlem": 39.367999999999995,
    "Boylam": 41.668,
    "Rakım (m)": 1790.0,
    "Sıcaklık (°C)": 8.2
  },
  "Mahalle_70": {
    "Enlem": 39.369,
    "Boylam": 41.669000000000004,
    "Rakım (m)": 1795.0,
    "Sıcaklık (°C)": 8.1
  },
  "Mahalle_71": {
    "Enlem": 39.37,
    "Boylam": 41.67,
    "Rakım (m)": 1800.0,
    "Sıcaklık (°C)": 8.5
  },
  "Mahalle_72": {
    "Enlem": 39.370999999999995,
    "Boylam": 41.671,
    "Rakım (m)": 1805.0,
    "Sıcaklık (°C)": 8.4
  },
  "Mahalle_73": {
    "Enlem": 39.372,
    "Boylam": 41.672000000000004,
    "Rakım (m)": 1810.0,
    "Sıcaklık (°C)": 8.3
  },
  "Mahalle_74": {
    "Enlem": 39.373,
    "Boylam": 41.673,
    "Rakım (m)": 1815.0,
    "Sıcaklık (°C)": 8.2
  },
  "Mahalle_75": {
    "Enlem": 39.373999999999995,
    "Boylam": 41.674,
    "Rakım (m)": 1820.0,
    "Sıcaklık (°C)": 8.1
  },
  "Mahalle_76": {
    "Enlem": 39.375,
    "Boylam": 41.675000000000004,
    "Rakım (m)": 1700.0,
    "Sıcaklık (°C)": 8.5
  },
  "Mahalle_77": {
    "Enlem": 39.376,
    "Boylam": 41.676,
    "Rakım (m)": 1705.0,
    "Sıcaklık (°C)": 8.4
  },
  "Mahalle_78": {
    "Enlem": 39.376999999999995,
    "Boylam": 41.677,
    "Rakım (m)": 1710.0,
    "Sıcaklık (°C)": 8.3
  },
  "Mahalle_79": {
    "Enlem": 39.378,
    "Boylam": 41.678000000000004,
    "Rakım (m)": 1715.0,
    "Sıcaklık (°C)": 8.2
  },
  "Mahalle_80": {
    "Enlem": 39.379,
    "Boylam": 41.679,
    "Rakım (m)": 1720.0,
    "Sıcaklık (°C)": 8.1
  },
  "Mahalle_81": {
    "Enlem": 39.379999999999995,
    "Boylam": 41.68,
    "Rakım (m)": 1725.0,
    "Sıcaklık (°C)": 8.5
  },
  "Mahalle_82": {
    "Enlem": 39.381,
    "Boylam": 41.681000000000004,
    "Rakım (m)": 1730.0,
    "Sıcaklık (°C)": 8.4
  },
  "Mahalle_83": {
    "Enlem": 39.382,
    "Boylam": 41.682,
    "Rakım (m)": 1735.0,
    "Sıcaklık (°C)": 8.3
  },
  "Mahalle_84": {
    "Enlem": 39.382999999999996,
    "Boylam": 41.683,
    "Rakım (m)": 1740.0,
    "Sıcaklık (°C)": 8.2
  },
  "Mahalle_85": {
    "Enlem": 39.384,
    "Boylam": 41.684000000000005,
    "Rakım (m)": 1745.0,
    "Sıcaklık (°C)": 8.1
  },
  "Mahalle_86": {
    "Enlem": 39.385,
    "Boylam": 41.685,
    "Rakım (m)": 1750.0,
    "Sıcaklık (°C)": 8.5
  },
  "Mahalle_87": {
    "Enlem": 39.385999999999996,
    "Boylam": 41.686,
    "Rakım (m)": 1755.0,
    "Sıcaklık (°C)": 8.4
  },
  "Mahalle_88": {
    "Enlem": 39.387,
    "Boylam": 41.687000000000005,
    "Rakım (m)": 1760.0,
    "Sıcaklık (°C)": 8.3
  },
  "Mahalle_89": {
    "Enlem": 39.388,
    "Boylam": 41.688,
    "Rakım (m)": 1765.0,
    "Sıcaklık (°C)": 8.2
  },
  "Mahalle_90": {
    "Enlem": 39.388999999999996,
    "Boylam": 41.689,
    "Rakım (m)": 1770.0,
    "Sıcaklık (°C)": 8.1
  },
  "Mahalle_91": {
    "Enlem": 39.39,
    "Boylam": 41.690000000000005,
    "Rakım (m)": 1775.0,
    "Sıcaklık (°C)": 8.5
  },
  "Mahalle_92": {
    "Enlem": 39.391,
    "Boylam": 41.691,
    "Rakım (m)": 1780.0,
    "Sıcaklık (°C)": 8.4
  },
  "Mahalle_93": {
    "Enlem": 39.391999999999996,
    "Boylam": 41.692,
    "Rakım (m)": 1785.0,
    "Sıcaklık (°C)": 8.3
  },
  "Mahalle_94": {
    "Enlem": 39.393,
    "Boylam": 41.693000000000005,
    "Rakım (m)": 1790.0,
    "Sıcaklık (°C)": 8.2
  },
  "Mahalle_95": {
    "Enlem": 39.394,
    "Boylam": 41.694,
    "Rakım (m)": 1795.0,
    "Sıcaklık (°C)": 8.1
  },
  "Mahalle_96": {
    "Enlem": 39.394999999999996,
    "Boylam": 41.695,
    "Rakım (m)": 1800.0,
    "Sıcaklık (°C)": 8.5
  },
  "Mahalle_97": {
    "Enlem": 39.395999999999994,
    "Boylam": 41.696,
    "Rakım (m)": 1805.0,
    "Sıcaklık (°C)": 8.4
  },
  "Mahalle_98": {
    "Enlem": 39.397,
    "Boylam": 41.697,
    "Rakım (m)": 1810.0,
    "Sıcaklık (°C)": 8.3
  }
}

st.title("Akıllı Tarım Karar Destek Sistemi")

secili_mahalle = st.selectbox("Mahalle Seçiniz", list(mahalle_verisi.keys()))
secili_urun = st.selectbox("Ürün Seçiniz", ["Arpa", "Buğday", "Fasulye"])

if secili_mahalle and secili_urun:
    v = mahalle_verisi[secili_mahalle]
    rakim, sicaklik = v["Rakım (m)"], v["Sıcaklık (°C)"]

    st.markdown(f"**Rakım:** {rakim} m | **Sıcaklık:** {sicaklik} °C")

    st.subheader("💧 Sulama Takvimi (FAO56)")
    st.write(f"{secili_urun} için örnek sulama ihtiyacı: {round(5.5 + (rakim % 10)*0.1, 1)} mm/hafta")

    st.subheader("🌱 Gübreleme")
    azot = st.number_input("Azot (ppm)", 0.0)
    fosfor = st.number_input("Fosfor (ppm)", 0.0)
    ph = st.number_input("pH", 4.0, 9.0)
    if azot and fosfor:
        st.write("Öneri: 20-20-0 gübresi - 6 kg/dekar")

    st.subheader("🌾 Alternatif Ürün")
    if rakim > 1800:
        st.write("Nohut veya Korunga önerilir")

    st.subheader("🦠 Hastalık-İlaç")
    if sicaklik > 8.4:
        st.write("Risk: Pas - İlaç: Propikonazol")

    st.subheader("📅 Ekim Zamanı")
    if secili_urun == "Buğday":
        st.write("Tavsiye edilen ekim zamanı: 15 Eylül - 10 Ekim")
    elif secili_urun == "Arpa":
        st.write("Tavsiye edilen ekim zamanı: 20 Eylül - 15 Ekim")
    elif secili_urun == "Fasulye":
        st.write("Tavsiye edilen ekim zamanı: 1 Mayıs - 20 Mayıs")
