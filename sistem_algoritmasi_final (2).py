
# sistem_algoritmasi_final.py
# Akıllı Tarım Karar Destek Sistemi - Tümleşik Sürüm (import hatası yok)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Simülasyon verileri ve FAO56 takvimi doğrudan bu dosyada tanımlanıyor
simulasyon_senaryolari = {
    "Senaryo 1 - Buğday - Aşağıkayabaşı": {
        "urun": "Buğday", "konum": "Aşağıkayabaşı", "rakim": 1700, "sicaklik": 16,
        "toprak": "Killi", "drenaj": "Orta", "organik_madde": "Orta",
        "sulama_var": True, "sulama_turu": "Yağmurlama",
        "gubreleme_var": True, "gubre_turu": "20-20-20",
        "arazi_buyuklugu": 5
    },
    "Senaryo 2 - Fasulye - Erbeyli": {
        "urun": "Fasulye", "konum": "Erbeyli", "rakim": 1750, "sicaklik": 17,
        "toprak": "Tınlı", "drenaj": "İyi", "organik_madde": "Yüksek",
        "sulama_var": False,
        "gubreleme_var": True, "gubre_turu": "Ahır Gübresi",
        "arazi_buyuklugu": 3
    }
}

fao56_sulama_detaylari = {
    "Buğday": [
        "1. Hafta - Çimlenme Dönemi: 20 mm",
        "2. Hafta - Kardeşlenme Dönemi: 30 mm",
        "3. Hafta - Sapa Kalkma: 40 mm",
        "4. Hafta - Başaklanma: 35 mm",
        "5. Hafta - Süt Olum: 25 mm"
    ],
    "Fasulye": [
        "1. Hafta - Çimlenme: 25 mm",
        "2. Hafta - İlk Yaprak: 30 mm",
        "3. Hafta - Çiçeklenme: 35 mm",
        "4. Hafta - Bakla Oluşumu: 30 mm",
        "5. Hafta - Olgunluk: 20 mm"
    ],
    "Arpa": [
        "1. Hafta - Çimlenme: 15 mm",
        "2. Hafta - Sapa Kalkma: 25 mm",
        "3. Hafta - Başaklanma: 30 mm",
        "4. Hafta - Olgunluk: 20 mm"
    ]
}
