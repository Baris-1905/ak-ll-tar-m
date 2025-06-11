
# -*- coding: utf-8 -*-
import streamlit as st

# 📌 Mahalle + Toprak Türü bazlı tüm veriler
veri = {
  "ACARKÖY|Killi": {
    "Enlem": 39.4,
    "Boylam": 41.5,
    "Rakım": 1650,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ACARKÖY|Tınlı": {
    "Enlem": 39.4,
    "Boylam": 41.5,
    "Rakım": 1650,
    "Sıcaklık": 7.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "ACARKÖY|Kumlu": {
    "Enlem": 39.4,
    "Boylam": 41.5,
    "Rakım": 1650,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ACARKÖY|Kireçli": {
    "Enlem": 39.4,
    "Boylam": 41.5,
    "Rakım": 1650,
    "Sıcaklık": 7.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "AKBAYIR|Killi": {
    "Enlem": 39.401,
    "Boylam": 41.501,
    "Rakım": 1656,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "AKBAYIR|Tınlı": {
    "Enlem": 39.401,
    "Boylam": 41.501,
    "Rakım": 1656,
    "Sıcaklık": 7.7,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "AKBAYIR|Kumlu": {
    "Enlem": 39.401,
    "Boylam": 41.501,
    "Rakım": 1656,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "AKBAYIR|Kireçli": {
    "Enlem": 39.401,
    "Boylam": 41.501,
    "Rakım": 1656,
    "Sıcaklık": 7.7,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "AKÇAMELİK|Killi": {
    "Enlem": 39.402,
    "Boylam": 41.502,
    "Rakım": 1662,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "AKÇAMELİK|Tınlı": {
    "Enlem": 39.402,
    "Boylam": 41.502,
    "Rakım": 1662,
    "Sıcaklık": 7.9,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "AKÇAMELİK|Kumlu": {
    "Enlem": 39.402,
    "Boylam": 41.502,
    "Rakım": 1662,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "AKÇAMELİK|Kireçli": {
    "Enlem": 39.402,
    "Boylam": 41.502,
    "Rakım": 1662,
    "Sıcaklık": 7.9,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "AKGELİN|Killi": {
    "Enlem": 39.403,
    "Boylam": 41.503,
    "Rakım": 1668,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "AKGELİN|Tınlı": {
    "Enlem": 39.403,
    "Boylam": 41.503,
    "Rakım": 1668,
    "Sıcaklık": 8.1,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "AKGELİN|Kumlu": {
    "Enlem": 39.403,
    "Boylam": 41.503,
    "Rakım": 1668,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "AKGELİN|Kireçli": {
    "Enlem": 39.403,
    "Boylam": 41.503,
    "Rakım": 1668,
    "Sıcaklık": 8.1,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "AKGÖZE|Killi": {
    "Enlem": 39.404,
    "Boylam": 41.504,
    "Rakım": 1674,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "AKGÖZE|Tınlı": {
    "Enlem": 39.404,
    "Boylam": 41.504,
    "Rakım": 1674,
    "Sıcaklık": 8.3,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "AKGÖZE|Kumlu": {
    "Enlem": 39.404,
    "Boylam": 41.504,
    "Rakım": 1674,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "AKGÖZE|Kireçli": {
    "Enlem": 39.404,
    "Boylam": 41.504,
    "Rakım": 1674,
    "Sıcaklık": 8.3,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "AKÖREN|Killi": {
    "Enlem": 39.405,
    "Boylam": 41.505,
    "Rakım": 1680,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "AKÖREN|Tınlı": {
    "Enlem": 39.405,
    "Boylam": 41.505,
    "Rakım": 1680,
    "Sıcaklık": 8.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "AKÖREN|Kumlu": {
    "Enlem": 39.405,
    "Boylam": 41.505,
    "Rakım": 1680,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "AKÖREN|Kireçli": {
    "Enlem": 39.405,
    "Boylam": 41.505,
    "Rakım": 1680,
    "Sıcaklık": 8.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ALACA|Killi": {
    "Enlem": 39.406,
    "Boylam": 41.506,
    "Rakım": 1686,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ALACA|Tınlı": {
    "Enlem": 39.406,
    "Boylam": 41.506,
    "Rakım": 1686,
    "Sıcaklık": 7.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "ALACA|Kumlu": {
    "Enlem": 39.406,
    "Boylam": 41.506,
    "Rakım": 1686,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ALACA|Kireçli": {
    "Enlem": 39.406,
    "Boylam": 41.506,
    "Rakım": 1686,
    "Sıcaklık": 7.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ALAGÖZ|Killi": {
    "Enlem": 39.407,
    "Boylam": 41.507,
    "Rakım": 1692,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ALAGÖZ|Tınlı": {
    "Enlem": 39.407,
    "Boylam": 41.507,
    "Rakım": 1692,
    "Sıcaklık": 7.7,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "ALAGÖZ|Kumlu": {
    "Enlem": 39.407,
    "Boylam": 41.507,
    "Rakım": 1692,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ALAGÖZ|Kireçli": {
    "Enlem": 39.407,
    "Boylam": 41.507,
    "Rakım": 1692,
    "Sıcaklık": 7.7,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ALINTERİ|Killi": {
    "Enlem": 39.408,
    "Boylam": 41.508,
    "Rakım": 1698,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ALINTERİ|Tınlı": {
    "Enlem": 39.408,
    "Boylam": 41.508,
    "Rakım": 1698,
    "Sıcaklık": 7.9,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "ALINTERİ|Kumlu": {
    "Enlem": 39.408,
    "Boylam": 41.508,
    "Rakım": 1698,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ALINTERİ|Kireçli": {
    "Enlem": 39.408,
    "Boylam": 41.508,
    "Rakım": 1698,
    "Sıcaklık": 7.9,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ALİKIRI|Killi": {
    "Enlem": 39.409,
    "Boylam": 41.509,
    "Rakım": 1704,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ALİKIRI|Tınlı": {
    "Enlem": 39.409,
    "Boylam": 41.509,
    "Rakım": 1704,
    "Sıcaklık": 8.1,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "ALİKIRI|Kumlu": {
    "Enlem": 39.409,
    "Boylam": 41.509,
    "Rakım": 1704,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ALİKIRI|Kireçli": {
    "Enlem": 39.409,
    "Boylam": 41.509,
    "Rakım": 1704,
    "Sıcaklık": 8.1,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ALTINPINAR|Killi": {
    "Enlem": 39.41,
    "Boylam": 41.51,
    "Rakım": 1710,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ALTINPINAR|Tınlı": {
    "Enlem": 39.41,
    "Boylam": 41.51,
    "Rakım": 1710,
    "Sıcaklık": 8.3,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "ALTINPINAR|Kumlu": {
    "Enlem": 39.41,
    "Boylam": 41.51,
    "Rakım": 1710,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ALTINPINAR|Kireçli": {
    "Enlem": 39.41,
    "Boylam": 41.51,
    "Rakım": 1710,
    "Sıcaklık": 8.3,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ARPADERESİ|Killi": {
    "Enlem": 39.411,
    "Boylam": 41.511,
    "Rakım": 1716,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ARPADERESİ|Tınlı": {
    "Enlem": 39.411,
    "Boylam": 41.511,
    "Rakım": 1716,
    "Sıcaklık": 8.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "ARPADERESİ|Kumlu": {
    "Enlem": 39.411,
    "Boylam": 41.511,
    "Rakım": 1716,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ARPADERESİ|Kireçli": {
    "Enlem": 39.411,
    "Boylam": 41.511,
    "Rakım": 1716,
    "Sıcaklık": 8.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "AŞAĞIKAYABAŞI|Killi": {
    "Enlem": 39.412,
    "Boylam": 41.512,
    "Rakım": 1722,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "AŞAĞIKAYABAŞI|Tınlı": {
    "Enlem": 39.412,
    "Boylam": 41.512,
    "Rakım": 1722,
    "Sıcaklık": 7.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "AŞAĞIKAYABAŞI|Kumlu": {
    "Enlem": 39.412,
    "Boylam": 41.512,
    "Rakım": 1722,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "AŞAĞIKAYABAŞI|Kireçli": {
    "Enlem": 39.412,
    "Boylam": 41.512,
    "Rakım": 1722,
    "Sıcaklık": 7.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "AVCILAR|Killi": {
    "Enlem": 39.413,
    "Boylam": 41.513,
    "Rakım": 1728,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "AVCILAR|Tınlı": {
    "Enlem": 39.413,
    "Boylam": 41.513,
    "Rakım": 1728,
    "Sıcaklık": 7.7,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "AVCILAR|Kumlu": {
    "Enlem": 39.413,
    "Boylam": 41.513,
    "Rakım": 1728,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "AVCILAR|Kireçli": {
    "Enlem": 39.413,
    "Boylam": 41.513,
    "Rakım": 1728,
    "Sıcaklık": 7.7,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "BAHÇE|Killi": {
    "Enlem": 39.414,
    "Boylam": 41.514,
    "Rakım": 1734,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "BAHÇE|Tınlı": {
    "Enlem": 39.414,
    "Boylam": 41.514,
    "Rakım": 1734,
    "Sıcaklık": 7.9,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "BAHÇE|Kumlu": {
    "Enlem": 39.414,
    "Boylam": 41.514,
    "Rakım": 1734,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "BAHÇE|Kireçli": {
    "Enlem": 39.414,
    "Boylam": 41.514,
    "Rakım": 1734,
    "Sıcaklık": 7.9,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "BAŞKÖY|Killi": {
    "Enlem": 39.415,
    "Boylam": 41.515,
    "Rakım": 1740,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "BAŞKÖY|Tınlı": {
    "Enlem": 39.415,
    "Boylam": 41.515,
    "Rakım": 1740,
    "Sıcaklık": 8.1,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "BAŞKÖY|Kumlu": {
    "Enlem": 39.415,
    "Boylam": 41.515,
    "Rakım": 1740,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "BAŞKÖY|Kireçli": {
    "Enlem": 39.415,
    "Boylam": 41.515,
    "Rakım": 1740,
    "Sıcaklık": 8.1,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "BAYIRKÖY|Killi": {
    "Enlem": 39.416,
    "Boylam": 41.516,
    "Rakım": 1746,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "BAYIRKÖY|Tınlı": {
    "Enlem": 39.416,
    "Boylam": 41.516,
    "Rakım": 1746,
    "Sıcaklık": 8.3,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "BAYIRKÖY|Kumlu": {
    "Enlem": 39.416,
    "Boylam": 41.516,
    "Rakım": 1746,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "BAYIRKÖY|Kireçli": {
    "Enlem": 39.416,
    "Boylam": 41.516,
    "Rakım": 1746,
    "Sıcaklık": 8.3,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "BELLİTAŞ|Killi": {
    "Enlem": 39.417,
    "Boylam": 41.517,
    "Rakım": 1752,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "BELLİTAŞ|Tınlı": {
    "Enlem": 39.417,
    "Boylam": 41.517,
    "Rakım": 1752,
    "Sıcaklık": 8.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "BELLİTAŞ|Kumlu": {
    "Enlem": 39.417,
    "Boylam": 41.517,
    "Rakım": 1752,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "BELLİTAŞ|Kireçli": {
    "Enlem": 39.417,
    "Boylam": 41.517,
    "Rakım": 1752,
    "Sıcaklık": 8.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "BEYYURDU|Killi": {
    "Enlem": 39.418,
    "Boylam": 41.518,
    "Rakım": 1758,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "BEYYURDU|Tınlı": {
    "Enlem": 39.418,
    "Boylam": 41.518,
    "Rakım": 1758,
    "Sıcaklık": 7.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "BEYYURDU|Kumlu": {
    "Enlem": 39.418,
    "Boylam": 41.518,
    "Rakım": 1758,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "BEYYURDU|Kireçli": {
    "Enlem": 39.418,
    "Boylam": 41.518,
    "Rakım": 1758,
    "Sıcaklık": 7.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "BURHANKÖY|Killi": {
    "Enlem": 39.419,
    "Boylam": 41.519,
    "Rakım": 1764,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "BURHANKÖY|Tınlı": {
    "Enlem": 39.419,
    "Boylam": 41.519,
    "Rakım": 1764,
    "Sıcaklık": 7.7,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "BURHANKÖY|Kumlu": {
    "Enlem": 39.419,
    "Boylam": 41.519,
    "Rakım": 1764,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "BURHANKÖY|Kireçli": {
    "Enlem": 39.419,
    "Boylam": 41.519,
    "Rakım": 1764,
    "Sıcaklık": 7.7,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ÇAKMAK|Killi": {
    "Enlem": 39.42,
    "Boylam": 41.52,
    "Rakım": 1650,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ÇAKMAK|Tınlı": {
    "Enlem": 39.42,
    "Boylam": 41.52,
    "Rakım": 1650,
    "Sıcaklık": 7.9,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "ÇAKMAK|Kumlu": {
    "Enlem": 39.42,
    "Boylam": 41.52,
    "Rakım": 1650,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ÇAKMAK|Kireçli": {
    "Enlem": 39.42,
    "Boylam": 41.52,
    "Rakım": 1650,
    "Sıcaklık": 7.9,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ÇAMURLU|Killi": {
    "Enlem": 39.421,
    "Boylam": 41.521,
    "Rakım": 1656,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ÇAMURLU|Tınlı": {
    "Enlem": 39.421,
    "Boylam": 41.521,
    "Rakım": 1656,
    "Sıcaklık": 8.1,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "ÇAMURLU|Kumlu": {
    "Enlem": 39.421,
    "Boylam": 41.521,
    "Rakım": 1656,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ÇAMURLU|Kireçli": {
    "Enlem": 39.421,
    "Boylam": 41.521,
    "Rakım": 1656,
    "Sıcaklık": 8.1,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ÇATAK|Killi": {
    "Enlem": 39.422,
    "Boylam": 41.522,
    "Rakım": 1662,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ÇATAK|Tınlı": {
    "Enlem": 39.422,
    "Boylam": 41.522,
    "Rakım": 1662,
    "Sıcaklık": 8.3,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "ÇATAK|Kumlu": {
    "Enlem": 39.422,
    "Boylam": 41.522,
    "Rakım": 1662,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ÇATAK|Kireçli": {
    "Enlem": 39.422,
    "Boylam": 41.522,
    "Rakım": 1662,
    "Sıcaklık": 8.3,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ÇİLLİGÖL|Killi": {
    "Enlem": 39.423,
    "Boylam": 41.523,
    "Rakım": 1668,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ÇİLLİGÖL|Tınlı": {
    "Enlem": 39.423,
    "Boylam": 41.523,
    "Rakım": 1668,
    "Sıcaklık": 8.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "ÇİLLİGÖL|Kumlu": {
    "Enlem": 39.423,
    "Boylam": 41.523,
    "Rakım": 1668,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ÇİLLİGÖL|Kireçli": {
    "Enlem": 39.423,
    "Boylam": 41.523,
    "Rakım": 1668,
    "Sıcaklık": 8.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "DAĞÇAYIRI|Killi": {
    "Enlem": 39.424,
    "Boylam": 41.524,
    "Rakım": 1674,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "DAĞÇAYIRI|Tınlı": {
    "Enlem": 39.424,
    "Boylam": 41.524,
    "Rakım": 1674,
    "Sıcaklık": 7.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "DAĞÇAYIRI|Kumlu": {
    "Enlem": 39.424,
    "Boylam": 41.524,
    "Rakım": 1674,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "DAĞÇAYIRI|Kireçli": {
    "Enlem": 39.424,
    "Boylam": 41.524,
    "Rakım": 1674,
    "Sıcaklık": 7.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "DEMİRCİ|Killi": {
    "Enlem": 39.425,
    "Boylam": 41.525,
    "Rakım": 1680,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "DEMİRCİ|Tınlı": {
    "Enlem": 39.425,
    "Boylam": 41.525,
    "Rakım": 1680,
    "Sıcaklık": 7.7,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "DEMİRCİ|Kumlu": {
    "Enlem": 39.425,
    "Boylam": 41.525,
    "Rakım": 1680,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "DEMİRCİ|Kireçli": {
    "Enlem": 39.425,
    "Boylam": 41.525,
    "Rakım": 1680,
    "Sıcaklık": 7.7,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "DERİNCE|Killi": {
    "Enlem": 39.426,
    "Boylam": 41.526,
    "Rakım": 1686,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "DERİNCE|Tınlı": {
    "Enlem": 39.426,
    "Boylam": 41.526,
    "Rakım": 1686,
    "Sıcaklık": 7.9,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "DERİNCE|Kumlu": {
    "Enlem": 39.426,
    "Boylam": 41.526,
    "Rakım": 1686,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "DERİNCE|Kireçli": {
    "Enlem": 39.426,
    "Boylam": 41.526,
    "Rakım": 1686,
    "Sıcaklık": 7.9,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "DERVİŞALİ|Killi": {
    "Enlem": 39.427,
    "Boylam": 41.527,
    "Rakım": 1692,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "DERVİŞALİ|Tınlı": {
    "Enlem": 39.427,
    "Boylam": 41.527,
    "Rakım": 1692,
    "Sıcaklık": 8.1,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "DERVİŞALİ|Kumlu": {
    "Enlem": 39.427,
    "Boylam": 41.527,
    "Rakım": 1692,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "DERVİŞALİ|Kireçli": {
    "Enlem": 39.427,
    "Boylam": 41.527,
    "Rakım": 1692,
    "Sıcaklık": 8.1,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "DİBEKLİ|Killi": {
    "Enlem": 39.428,
    "Boylam": 41.528,
    "Rakım": 1698,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "DİBEKLİ|Tınlı": {
    "Enlem": 39.428,
    "Boylam": 41.528,
    "Rakım": 1698,
    "Sıcaklık": 8.3,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "DİBEKLİ|Kumlu": {
    "Enlem": 39.428,
    "Boylam": 41.528,
    "Rakım": 1698,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "DİBEKLİ|Kireçli": {
    "Enlem": 39.428,
    "Boylam": 41.528,
    "Rakım": 1698,
    "Sıcaklık": 8.3,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "DİKİLİ|Killi": {
    "Enlem": 39.429,
    "Boylam": 41.529,
    "Rakım": 1704,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "DİKİLİ|Tınlı": {
    "Enlem": 39.429,
    "Boylam": 41.529,
    "Rakım": 1704,
    "Sıcaklık": 8.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "DİKİLİ|Kumlu": {
    "Enlem": 39.429,
    "Boylam": 41.529,
    "Rakım": 1704,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "DİKİLİ|Kireçli": {
    "Enlem": 39.429,
    "Boylam": 41.529,
    "Rakım": 1704,
    "Sıcaklık": 8.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "DİVANHÜSEYİN|Killi": {
    "Enlem": 39.43,
    "Boylam": 41.53,
    "Rakım": 1710,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "DİVANHÜSEYİN|Tınlı": {
    "Enlem": 39.43,
    "Boylam": 41.53,
    "Rakım": 1710,
    "Sıcaklık": 7.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "DİVANHÜSEYİN|Kumlu": {
    "Enlem": 39.43,
    "Boylam": 41.53,
    "Rakım": 1710,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "DİVANHÜSEYİN|Kireçli": {
    "Enlem": 39.43,
    "Boylam": 41.53,
    "Rakım": 1710,
    "Sıcaklık": 7.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ELMADALI|Killi": {
    "Enlem": 39.431,
    "Boylam": 41.531,
    "Rakım": 1716,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ELMADALI|Tınlı": {
    "Enlem": 39.431,
    "Boylam": 41.531,
    "Rakım": 1716,
    "Sıcaklık": 7.7,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "ELMADALI|Kumlu": {
    "Enlem": 39.431,
    "Boylam": 41.531,
    "Rakım": 1716,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ELMADALI|Kireçli": {
    "Enlem": 39.431,
    "Boylam": 41.531,
    "Rakım": 1716,
    "Sıcaklık": 7.7,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ERBEYLİ|Killi": {
    "Enlem": 39.432,
    "Boylam": 41.532,
    "Rakım": 1722,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ERBEYLİ|Tınlı": {
    "Enlem": 39.432,
    "Boylam": 41.532,
    "Rakım": 1722,
    "Sıcaklık": 7.9,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "ERBEYLİ|Kumlu": {
    "Enlem": 39.432,
    "Boylam": 41.532,
    "Rakım": 1722,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ERBEYLİ|Kireçli": {
    "Enlem": 39.432,
    "Boylam": 41.532,
    "Rakım": 1722,
    "Sıcaklık": 7.9,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ERDURAN|Killi": {
    "Enlem": 39.433,
    "Boylam": 41.533,
    "Rakım": 1728,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ERDURAN|Tınlı": {
    "Enlem": 39.433,
    "Boylam": 41.533,
    "Rakım": 1728,
    "Sıcaklık": 8.1,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "ERDURAN|Kumlu": {
    "Enlem": 39.433,
    "Boylam": 41.533,
    "Rakım": 1728,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ERDURAN|Kireçli": {
    "Enlem": 39.433,
    "Boylam": 41.533,
    "Rakım": 1728,
    "Sıcaklık": 8.1,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ERENCE|Killi": {
    "Enlem": 39.434,
    "Boylam": 41.534,
    "Rakım": 1734,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ERENCE|Tınlı": {
    "Enlem": 39.434,
    "Boylam": 41.534,
    "Rakım": 1734,
    "Sıcaklık": 8.3,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "ERENCE|Kumlu": {
    "Enlem": 39.434,
    "Boylam": 41.534,
    "Rakım": 1734,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ERENCE|Kireçli": {
    "Enlem": 39.434,
    "Boylam": 41.534,
    "Rakım": 1734,
    "Sıcaklık": 8.3,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ESENLİ|Killi": {
    "Enlem": 39.435,
    "Boylam": 41.535,
    "Rakım": 1740,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ESENLİ|Tınlı": {
    "Enlem": 39.435,
    "Boylam": 41.535,
    "Rakım": 1740,
    "Sıcaklık": 8.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "ESENLİ|Kumlu": {
    "Enlem": 39.435,
    "Boylam": 41.535,
    "Rakım": 1740,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ESENLİ|Kireçli": {
    "Enlem": 39.435,
    "Boylam": 41.535,
    "Rakım": 1740,
    "Sıcaklık": 8.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "GÖLLER|Killi": {
    "Enlem": 39.436,
    "Boylam": 41.536,
    "Rakım": 1746,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "GÖLLER|Tınlı": {
    "Enlem": 39.436,
    "Boylam": 41.536,
    "Rakım": 1746,
    "Sıcaklık": 7.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "GÖLLER|Kumlu": {
    "Enlem": 39.436,
    "Boylam": 41.536,
    "Rakım": 1746,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "GÖLLER|Kireçli": {
    "Enlem": 39.436,
    "Boylam": 41.536,
    "Rakım": 1746,
    "Sıcaklık": 7.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "GÜLİSTAN|Killi": {
    "Enlem": 39.437,
    "Boylam": 41.537,
    "Rakım": 1752,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "GÜLİSTAN|Tınlı": {
    "Enlem": 39.437,
    "Boylam": 41.537,
    "Rakım": 1752,
    "Sıcaklık": 7.7,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "GÜLİSTAN|Kumlu": {
    "Enlem": 39.437,
    "Boylam": 41.537,
    "Rakım": 1752,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "GÜLİSTAN|Kireçli": {
    "Enlem": 39.437,
    "Boylam": 41.537,
    "Rakım": 1752,
    "Sıcaklık": 7.7,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "GÜLLÜÇİMEN|Killi": {
    "Enlem": 39.438,
    "Boylam": 41.538,
    "Rakım": 1758,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "GÜLLÜÇİMEN|Tınlı": {
    "Enlem": 39.438,
    "Boylam": 41.538,
    "Rakım": 1758,
    "Sıcaklık": 7.9,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "GÜLLÜÇİMEN|Kumlu": {
    "Enlem": 39.438,
    "Boylam": 41.538,
    "Rakım": 1758,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "GÜLLÜÇİMEN|Kireçli": {
    "Enlem": 39.438,
    "Boylam": 41.538,
    "Rakım": 1758,
    "Sıcaklık": 7.9,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "GÜRÇAYIR|Killi": {
    "Enlem": 39.439,
    "Boylam": 41.539,
    "Rakım": 1764,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "GÜRÇAYIR|Tınlı": {
    "Enlem": 39.439,
    "Boylam": 41.539,
    "Rakım": 1764,
    "Sıcaklık": 8.1,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "GÜRÇAYIR|Kumlu": {
    "Enlem": 39.439,
    "Boylam": 41.539,
    "Rakım": 1764,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "GÜRÇAYIR|Kireçli": {
    "Enlem": 39.439,
    "Boylam": 41.539,
    "Rakım": 1764,
    "Sıcaklık": 8.1,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "GÜZELDERE|Killi": {
    "Enlem": 39.44,
    "Boylam": 41.54,
    "Rakım": 1650,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "GÜZELDERE|Tınlı": {
    "Enlem": 39.44,
    "Boylam": 41.54,
    "Rakım": 1650,
    "Sıcaklık": 8.3,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "GÜZELDERE|Kumlu": {
    "Enlem": 39.44,
    "Boylam": 41.54,
    "Rakım": 1650,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "GÜZELDERE|Kireçli": {
    "Enlem": 39.44,
    "Boylam": 41.54,
    "Rakım": 1650,
    "Sıcaklık": 8.3,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "HALİLÇAVUŞ|Killi": {
    "Enlem": 39.441,
    "Boylam": 41.541,
    "Rakım": 1656,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "HALİLÇAVUŞ|Tınlı": {
    "Enlem": 39.441,
    "Boylam": 41.541,
    "Rakım": 1656,
    "Sıcaklık": 8.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "HALİLÇAVUŞ|Kumlu": {
    "Enlem": 39.441,
    "Boylam": 41.541,
    "Rakım": 1656,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "HALİLÇAVUŞ|Kireçli": {
    "Enlem": 39.441,
    "Boylam": 41.541,
    "Rakım": 1656,
    "Sıcaklık": 8.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "HAYRAN|Killi": {
    "Enlem": 39.442,
    "Boylam": 41.542,
    "Rakım": 1662,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "HAYRAN|Tınlı": {
    "Enlem": 39.442,
    "Boylam": 41.542,
    "Rakım": 1662,
    "Sıcaklık": 7.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "HAYRAN|Kumlu": {
    "Enlem": 39.442,
    "Boylam": 41.542,
    "Rakım": 1662,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "HAYRAN|Kireçli": {
    "Enlem": 39.442,
    "Boylam": 41.542,
    "Rakım": 1662,
    "Sıcaklık": 7.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ILICAKÖY|Killi": {
    "Enlem": 39.443,
    "Boylam": 41.543,
    "Rakım": 1668,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ILICAKÖY|Tınlı": {
    "Enlem": 39.443,
    "Boylam": 41.543,
    "Rakım": 1668,
    "Sıcaklık": 7.7,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "ILICAKÖY|Kumlu": {
    "Enlem": 39.443,
    "Boylam": 41.543,
    "Rakım": 1668,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ILICAKÖY|Kireçli": {
    "Enlem": 39.443,
    "Boylam": 41.543,
    "Rakım": 1668,
    "Sıcaklık": 7.7,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "İSMAİL|Killi": {
    "Enlem": 39.444,
    "Boylam": 41.544,
    "Rakım": 1674,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "İSMAİL|Tınlı": {
    "Enlem": 39.444,
    "Boylam": 41.544,
    "Rakım": 1674,
    "Sıcaklık": 7.9,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "İSMAİL|Kumlu": {
    "Enlem": 39.444,
    "Boylam": 41.544,
    "Rakım": 1674,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "İSMAİL|Kireçli": {
    "Enlem": 39.444,
    "Boylam": 41.544,
    "Rakım": 1674,
    "Sıcaklık": 7.9,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KALECİK|Killi": {
    "Enlem": 39.445,
    "Boylam": 41.545,
    "Rakım": 1680,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KALECİK|Tınlı": {
    "Enlem": 39.445,
    "Boylam": 41.545,
    "Rakım": 1680,
    "Sıcaklık": 8.1,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "KALECİK|Kumlu": {
    "Enlem": 39.445,
    "Boylam": 41.545,
    "Rakım": 1680,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KALECİK|Kireçli": {
    "Enlem": 39.445,
    "Boylam": 41.545,
    "Rakım": 1680,
    "Sıcaklık": 8.1,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KARAAĞAÇ|Killi": {
    "Enlem": 39.446,
    "Boylam": 41.546,
    "Rakım": 1686,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KARAAĞAÇ|Tınlı": {
    "Enlem": 39.446,
    "Boylam": 41.546,
    "Rakım": 1686,
    "Sıcaklık": 8.3,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "KARAAĞAÇ|Kumlu": {
    "Enlem": 39.446,
    "Boylam": 41.546,
    "Rakım": 1686,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KARAAĞAÇ|Kireçli": {
    "Enlem": 39.446,
    "Boylam": 41.546,
    "Rakım": 1686,
    "Sıcaklık": 8.3,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KARABUDAK|Killi": {
    "Enlem": 39.447,
    "Boylam": 41.547,
    "Rakım": 1692,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KARABUDAK|Tınlı": {
    "Enlem": 39.447,
    "Boylam": 41.547,
    "Rakım": 1692,
    "Sıcaklık": 8.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "KARABUDAK|Kumlu": {
    "Enlem": 39.447,
    "Boylam": 41.547,
    "Rakım": 1692,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KARABUDAK|Kireçli": {
    "Enlem": 39.447,
    "Boylam": 41.547,
    "Rakım": 1692,
    "Sıcaklık": 8.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KARAKULA|Killi": {
    "Enlem": 39.448,
    "Boylam": 41.548,
    "Rakım": 1698,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KARAKULA|Tınlı": {
    "Enlem": 39.448,
    "Boylam": 41.548,
    "Rakım": 1698,
    "Sıcaklık": 7.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "KARAKULA|Kumlu": {
    "Enlem": 39.448,
    "Boylam": 41.548,
    "Rakım": 1698,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KARAKULA|Kireçli": {
    "Enlem": 39.448,
    "Boylam": 41.548,
    "Rakım": 1698,
    "Sıcaklık": 7.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KARAMOLLA|Killi": {
    "Enlem": 39.449,
    "Boylam": 41.549,
    "Rakım": 1704,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KARAMOLLA|Tınlı": {
    "Enlem": 39.449,
    "Boylam": 41.549,
    "Rakım": 1704,
    "Sıcaklık": 7.7,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "KARAMOLLA|Kumlu": {
    "Enlem": 39.449,
    "Boylam": 41.549,
    "Rakım": 1704,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KARAMOLLA|Kireçli": {
    "Enlem": 39.449,
    "Boylam": 41.549,
    "Rakım": 1704,
    "Sıcaklık": 7.7,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KAZANCI|Killi": {
    "Enlem": 39.45,
    "Boylam": 41.55,
    "Rakım": 1710,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KAZANCI|Tınlı": {
    "Enlem": 39.45,
    "Boylam": 41.55,
    "Rakım": 1710,
    "Sıcaklık": 7.9,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "KAZANCI|Kumlu": {
    "Enlem": 39.45,
    "Boylam": 41.55,
    "Rakım": 1710,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KAZANCI|Kireçli": {
    "Enlem": 39.45,
    "Boylam": 41.55,
    "Rakım": 1710,
    "Sıcaklık": 7.9,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KETENCİ|Killi": {
    "Enlem": 39.451,
    "Boylam": 41.551,
    "Rakım": 1716,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KETENCİ|Tınlı": {
    "Enlem": 39.451,
    "Boylam": 41.551,
    "Rakım": 1716,
    "Sıcaklık": 8.1,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "KETENCİ|Kumlu": {
    "Enlem": 39.451,
    "Boylam": 41.551,
    "Rakım": 1716,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KETENCİ|Kireçli": {
    "Enlem": 39.451,
    "Boylam": 41.551,
    "Rakım": 1716,
    "Sıcaklık": 8.1,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KISIK|Killi": {
    "Enlem": 39.452,
    "Boylam": 41.552,
    "Rakım": 1722,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KISIK|Tınlı": {
    "Enlem": 39.452,
    "Boylam": 41.552,
    "Rakım": 1722,
    "Sıcaklık": 8.3,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "KISIK|Kumlu": {
    "Enlem": 39.452,
    "Boylam": 41.552,
    "Rakım": 1722,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KISIK|Kireçli": {
    "Enlem": 39.452,
    "Boylam": 41.552,
    "Rakım": 1722,
    "Sıcaklık": 8.3,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KIZILAHMET|Killi": {
    "Enlem": 39.453,
    "Boylam": 41.553,
    "Rakım": 1728,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KIZILAHMET|Tınlı": {
    "Enlem": 39.453,
    "Boylam": 41.553,
    "Rakım": 1728,
    "Sıcaklık": 8.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "KIZILAHMET|Kumlu": {
    "Enlem": 39.453,
    "Boylam": 41.553,
    "Rakım": 1728,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KIZILAHMET|Kireçli": {
    "Enlem": 39.453,
    "Boylam": 41.553,
    "Rakım": 1728,
    "Sıcaklık": 8.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KIZMUSA|Killi": {
    "Enlem": 39.454,
    "Boylam": 41.554,
    "Rakım": 1734,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KIZMUSA|Tınlı": {
    "Enlem": 39.454,
    "Boylam": 41.554,
    "Rakım": 1734,
    "Sıcaklık": 7.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "KIZMUSA|Kumlu": {
    "Enlem": 39.454,
    "Boylam": 41.554,
    "Rakım": 1734,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KIZMUSA|Kireçli": {
    "Enlem": 39.454,
    "Boylam": 41.554,
    "Rakım": 1734,
    "Sıcaklık": 7.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KOLHİSAR|Killi": {
    "Enlem": 39.455,
    "Boylam": 41.555,
    "Rakım": 1740,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KOLHİSAR|Tınlı": {
    "Enlem": 39.455,
    "Boylam": 41.555,
    "Rakım": 1740,
    "Sıcaklık": 7.7,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "KOLHİSAR|Kumlu": {
    "Enlem": 39.455,
    "Boylam": 41.555,
    "Rakım": 1740,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KOLHİSAR|Kireçli": {
    "Enlem": 39.455,
    "Boylam": 41.555,
    "Rakım": 1740,
    "Sıcaklık": 7.7,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KONGUR|Killi": {
    "Enlem": 39.456,
    "Boylam": 41.556,
    "Rakım": 1746,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KONGUR|Tınlı": {
    "Enlem": 39.456,
    "Boylam": 41.556,
    "Rakım": 1746,
    "Sıcaklık": 7.9,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "KONGUR|Kumlu": {
    "Enlem": 39.456,
    "Boylam": 41.556,
    "Rakım": 1746,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KONGUR|Kireçli": {
    "Enlem": 39.456,
    "Boylam": 41.556,
    "Rakım": 1746,
    "Sıcaklık": 7.9,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KÖPRÜBAŞI|Killi": {
    "Enlem": 39.457,
    "Boylam": 41.557,
    "Rakım": 1752,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KÖPRÜBAŞI|Tınlı": {
    "Enlem": 39.457,
    "Boylam": 41.557,
    "Rakım": 1752,
    "Sıcaklık": 8.1,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "KÖPRÜBAŞI|Kumlu": {
    "Enlem": 39.457,
    "Boylam": 41.557,
    "Rakım": 1752,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "KÖPRÜBAŞI|Kireçli": {
    "Enlem": 39.457,
    "Boylam": 41.557,
    "Rakım": 1752,
    "Sıcaklık": 8.1,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "MEYDANKÖY|Killi": {
    "Enlem": 39.458,
    "Boylam": 41.558,
    "Rakım": 1758,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "MEYDANKÖY|Tınlı": {
    "Enlem": 39.458,
    "Boylam": 41.558,
    "Rakım": 1758,
    "Sıcaklık": 8.3,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "MEYDANKÖY|Kumlu": {
    "Enlem": 39.458,
    "Boylam": 41.558,
    "Rakım": 1758,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "MEYDANKÖY|Kireçli": {
    "Enlem": 39.458,
    "Boylam": 41.558,
    "Rakım": 1758,
    "Sıcaklık": 8.3,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "MEZRA|Killi": {
    "Enlem": 39.459,
    "Boylam": 41.559,
    "Rakım": 1764,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "MEZRA|Tınlı": {
    "Enlem": 39.459,
    "Boylam": 41.559,
    "Rakım": 1764,
    "Sıcaklık": 8.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "MEZRA|Kumlu": {
    "Enlem": 39.459,
    "Boylam": 41.559,
    "Rakım": 1764,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "MEZRA|Kireçli": {
    "Enlem": 39.459,
    "Boylam": 41.559,
    "Rakım": 1764,
    "Sıcaklık": 8.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "MOLLACELİL|Killi": {
    "Enlem": 39.46,
    "Boylam": 41.56,
    "Rakım": 1650,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "MOLLACELİL|Tınlı": {
    "Enlem": 39.46,
    "Boylam": 41.56,
    "Rakım": 1650,
    "Sıcaklık": 7.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "MOLLACELİL|Kumlu": {
    "Enlem": 39.46,
    "Boylam": 41.56,
    "Rakım": 1650,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "MOLLACELİL|Kireçli": {
    "Enlem": 39.46,
    "Boylam": 41.56,
    "Rakım": 1650,
    "Sıcaklık": 7.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "MOLLAKULAÇ|Killi": {
    "Enlem": 39.461,
    "Boylam": 41.561,
    "Rakım": 1656,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "MOLLAKULAÇ|Tınlı": {
    "Enlem": 39.461,
    "Boylam": 41.561,
    "Rakım": 1656,
    "Sıcaklık": 7.7,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "MOLLAKULAÇ|Kumlu": {
    "Enlem": 39.461,
    "Boylam": 41.561,
    "Rakım": 1656,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "MOLLAKULAÇ|Kireçli": {
    "Enlem": 39.461,
    "Boylam": 41.561,
    "Rakım": 1656,
    "Sıcaklık": 7.7,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "MUTLUCA|Killi": {
    "Enlem": 39.462,
    "Boylam": 41.562,
    "Rakım": 1662,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "MUTLUCA|Tınlı": {
    "Enlem": 39.462,
    "Boylam": 41.562,
    "Rakım": 1662,
    "Sıcaklık": 7.9,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "MUTLUCA|Kumlu": {
    "Enlem": 39.462,
    "Boylam": 41.562,
    "Rakım": 1662,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "MUTLUCA|Kireçli": {
    "Enlem": 39.462,
    "Boylam": 41.562,
    "Rakım": 1662,
    "Sıcaklık": 7.9,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ORTAKÖY|Killi": {
    "Enlem": 39.463,
    "Boylam": 41.563,
    "Rakım": 1668,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ORTAKÖY|Tınlı": {
    "Enlem": 39.463,
    "Boylam": 41.563,
    "Rakım": 1668,
    "Sıcaklık": 8.1,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "ORTAKÖY|Kumlu": {
    "Enlem": 39.463,
    "Boylam": 41.563,
    "Rakım": 1668,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ORTAKÖY|Kireçli": {
    "Enlem": 39.463,
    "Boylam": 41.563,
    "Rakım": 1668,
    "Sıcaklık": 8.1,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "OVAÇEVİRME|Killi": {
    "Enlem": 39.464,
    "Boylam": 41.564,
    "Rakım": 1674,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "OVAÇEVİRME|Tınlı": {
    "Enlem": 39.464,
    "Boylam": 41.564,
    "Rakım": 1674,
    "Sıcaklık": 8.3,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "OVAÇEVİRME|Kumlu": {
    "Enlem": 39.464,
    "Boylam": 41.564,
    "Rakım": 1674,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "OVAÇEVİRME|Kireçli": {
    "Enlem": 39.464,
    "Boylam": 41.564,
    "Rakım": 1674,
    "Sıcaklık": 8.3,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "OVAKOZLU|Killi": {
    "Enlem": 39.465,
    "Boylam": 41.565,
    "Rakım": 1680,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "OVAKOZLU|Tınlı": {
    "Enlem": 39.465,
    "Boylam": 41.565,
    "Rakım": 1680,
    "Sıcaklık": 8.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "OVAKOZLU|Kumlu": {
    "Enlem": 39.465,
    "Boylam": 41.565,
    "Rakım": 1680,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "OVAKOZLU|Kireçli": {
    "Enlem": 39.465,
    "Boylam": 41.565,
    "Rakım": 1680,
    "Sıcaklık": 8.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "PARMAKSIZ|Killi": {
    "Enlem": 39.466,
    "Boylam": 41.566,
    "Rakım": 1686,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "PARMAKSIZ|Tınlı": {
    "Enlem": 39.466,
    "Boylam": 41.566,
    "Rakım": 1686,
    "Sıcaklık": 7.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "PARMAKSIZ|Kumlu": {
    "Enlem": 39.466,
    "Boylam": 41.566,
    "Rakım": 1686,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "PARMAKSIZ|Kireçli": {
    "Enlem": 39.466,
    "Boylam": 41.566,
    "Rakım": 1686,
    "Sıcaklık": 7.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "PINARBAŞI|Killi": {
    "Enlem": 39.467,
    "Boylam": 41.567,
    "Rakım": 1692,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "PINARBAŞI|Tınlı": {
    "Enlem": 39.467,
    "Boylam": 41.567,
    "Rakım": 1692,
    "Sıcaklık": 7.7,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "PINARBAŞI|Kumlu": {
    "Enlem": 39.467,
    "Boylam": 41.567,
    "Rakım": 1692,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "PINARBAŞI|Kireçli": {
    "Enlem": 39.467,
    "Boylam": 41.567,
    "Rakım": 1692,
    "Sıcaklık": 7.7,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "PINARKÖY|Killi": {
    "Enlem": 39.468,
    "Boylam": 41.568,
    "Rakım": 1698,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "PINARKÖY|Tınlı": {
    "Enlem": 39.468,
    "Boylam": 41.568,
    "Rakım": 1698,
    "Sıcaklık": 7.9,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "PINARKÖY|Kumlu": {
    "Enlem": 39.468,
    "Boylam": 41.568,
    "Rakım": 1698,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "PINARKÖY|Kireçli": {
    "Enlem": 39.468,
    "Boylam": 41.568,
    "Rakım": 1698,
    "Sıcaklık": 7.9,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "SALTEPE|Killi": {
    "Enlem": 39.469,
    "Boylam": 41.569,
    "Rakım": 1704,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "SALTEPE|Tınlı": {
    "Enlem": 39.469,
    "Boylam": 41.569,
    "Rakım": 1704,
    "Sıcaklık": 8.1,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "SALTEPE|Kumlu": {
    "Enlem": 39.469,
    "Boylam": 41.569,
    "Rakım": 1704,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "SALTEPE|Kireçli": {
    "Enlem": 39.469,
    "Boylam": 41.569,
    "Rakım": 1704,
    "Sıcaklık": 8.1,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "SANAYİ|Killi": {
    "Enlem": 39.47,
    "Boylam": 41.57,
    "Rakım": 1710,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "SANAYİ|Tınlı": {
    "Enlem": 39.47,
    "Boylam": 41.57,
    "Rakım": 1710,
    "Sıcaklık": 8.3,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "SANAYİ|Kumlu": {
    "Enlem": 39.47,
    "Boylam": 41.57,
    "Rakım": 1710,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "SANAYİ|Kireçli": {
    "Enlem": 39.47,
    "Boylam": 41.57,
    "Rakım": 1710,
    "Sıcaklık": 8.3,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "SARILI|Killi": {
    "Enlem": 39.471,
    "Boylam": 41.571,
    "Rakım": 1716,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "SARILI|Tınlı": {
    "Enlem": 39.471,
    "Boylam": 41.571,
    "Rakım": 1716,
    "Sıcaklık": 8.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "SARILI|Kumlu": {
    "Enlem": 39.471,
    "Boylam": 41.571,
    "Rakım": 1716,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "SARILI|Kireçli": {
    "Enlem": 39.471,
    "Boylam": 41.571,
    "Rakım": 1716,
    "Sıcaklık": 8.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "SILDIZ|Killi": {
    "Enlem": 39.472,
    "Boylam": 41.572,
    "Rakım": 1722,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "SILDIZ|Tınlı": {
    "Enlem": 39.472,
    "Boylam": 41.572,
    "Rakım": 1722,
    "Sıcaklık": 7.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "SILDIZ|Kumlu": {
    "Enlem": 39.472,
    "Boylam": 41.572,
    "Rakım": 1722,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "SILDIZ|Kireçli": {
    "Enlem": 39.472,
    "Boylam": 41.572,
    "Rakım": 1722,
    "Sıcaklık": 7.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "SÖĞÜTLÜ|Killi": {
    "Enlem": 39.473,
    "Boylam": 41.573,
    "Rakım": 1728,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "SÖĞÜTLÜ|Tınlı": {
    "Enlem": 39.473,
    "Boylam": 41.573,
    "Rakım": 1728,
    "Sıcaklık": 7.7,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "SÖĞÜTLÜ|Kumlu": {
    "Enlem": 39.473,
    "Boylam": 41.573,
    "Rakım": 1728,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "SÖĞÜTLÜ|Kireçli": {
    "Enlem": 39.473,
    "Boylam": 41.573,
    "Rakım": 1728,
    "Sıcaklık": 7.7,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "SULTANLI|Killi": {
    "Enlem": 39.474,
    "Boylam": 41.574,
    "Rakım": 1734,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "SULTANLI|Tınlı": {
    "Enlem": 39.474,
    "Boylam": 41.574,
    "Rakım": 1734,
    "Sıcaklık": 7.9,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "SULTANLI|Kumlu": {
    "Enlem": 39.474,
    "Boylam": 41.574,
    "Rakım": 1734,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "SULTANLI|Kireçli": {
    "Enlem": 39.474,
    "Boylam": 41.574,
    "Rakım": 1734,
    "Sıcaklık": 7.9,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "SUVARAN|Killi": {
    "Enlem": 39.475,
    "Boylam": 41.575,
    "Rakım": 1740,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "SUVARAN|Tınlı": {
    "Enlem": 39.475,
    "Boylam": 41.575,
    "Rakım": 1740,
    "Sıcaklık": 8.1,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "SUVARAN|Kumlu": {
    "Enlem": 39.475,
    "Boylam": 41.575,
    "Rakım": 1740,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "SUVARAN|Kireçli": {
    "Enlem": 39.475,
    "Boylam": 41.575,
    "Rakım": 1740,
    "Sıcaklık": 8.1,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ŞAHABETTİNKÖY|Killi": {
    "Enlem": 39.476,
    "Boylam": 41.576,
    "Rakım": 1746,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ŞAHABETTİNKÖY|Tınlı": {
    "Enlem": 39.476,
    "Boylam": 41.576,
    "Rakım": 1746,
    "Sıcaklık": 8.3,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "ŞAHABETTİNKÖY|Kumlu": {
    "Enlem": 39.476,
    "Boylam": 41.576,
    "Rakım": 1746,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ŞAHABETTİNKÖY|Kireçli": {
    "Enlem": 39.476,
    "Boylam": 41.576,
    "Rakım": 1746,
    "Sıcaklık": 8.3,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ŞAHVERDİ|Killi": {
    "Enlem": 39.477,
    "Boylam": 41.577,
    "Rakım": 1752,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ŞAHVERDİ|Tınlı": {
    "Enlem": 39.477,
    "Boylam": 41.577,
    "Rakım": 1752,
    "Sıcaklık": 8.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "ŞAHVERDİ|Kumlu": {
    "Enlem": 39.477,
    "Boylam": 41.577,
    "Rakım": 1752,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ŞAHVERDİ|Kireçli": {
    "Enlem": 39.477,
    "Boylam": 41.577,
    "Rakım": 1752,
    "Sıcaklık": 8.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ŞALGAMKÖY|Killi": {
    "Enlem": 39.478,
    "Boylam": 41.578,
    "Rakım": 1758,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ŞALGAMKÖY|Tınlı": {
    "Enlem": 39.478,
    "Boylam": 41.578,
    "Rakım": 1758,
    "Sıcaklık": 7.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "ŞALGAMKÖY|Kumlu": {
    "Enlem": 39.478,
    "Boylam": 41.578,
    "Rakım": 1758,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ŞALGAMKÖY|Kireçli": {
    "Enlem": 39.478,
    "Boylam": 41.578,
    "Rakım": 1758,
    "Sıcaklık": 7.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "TANIR|Killi": {
    "Enlem": 39.479,
    "Boylam": 41.579,
    "Rakım": 1764,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "TANIR|Tınlı": {
    "Enlem": 39.479,
    "Boylam": 41.579,
    "Rakım": 1764,
    "Sıcaklık": 7.7,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "TANIR|Kumlu": {
    "Enlem": 39.479,
    "Boylam": 41.579,
    "Rakım": 1764,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "TANIR|Kireçli": {
    "Enlem": 39.479,
    "Boylam": 41.579,
    "Rakım": 1764,
    "Sıcaklık": 7.7,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "TAPUKÖY|Killi": {
    "Enlem": 39.48,
    "Boylam": 41.58,
    "Rakım": 1650,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "TAPUKÖY|Tınlı": {
    "Enlem": 39.48,
    "Boylam": 41.58,
    "Rakım": 1650,
    "Sıcaklık": 7.9,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "TAPUKÖY|Kumlu": {
    "Enlem": 39.48,
    "Boylam": 41.58,
    "Rakım": 1650,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "TAPUKÖY|Kireçli": {
    "Enlem": 39.48,
    "Boylam": 41.58,
    "Rakım": 1650,
    "Sıcaklık": 7.9,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "TAŞBUDAK|Killi": {
    "Enlem": 39.481,
    "Boylam": 41.581,
    "Rakım": 1656,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "TAŞBUDAK|Tınlı": {
    "Enlem": 39.481,
    "Boylam": 41.581,
    "Rakım": 1656,
    "Sıcaklık": 8.1,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "TAŞBUDAK|Kumlu": {
    "Enlem": 39.481,
    "Boylam": 41.581,
    "Rakım": 1656,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "TAŞBUDAK|Kireçli": {
    "Enlem": 39.481,
    "Boylam": 41.581,
    "Rakım": 1656,
    "Sıcaklık": 8.1,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "TELLİTEPE|Killi": {
    "Enlem": 39.482,
    "Boylam": 41.582,
    "Rakım": 1662,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "TELLİTEPE|Tınlı": {
    "Enlem": 39.482,
    "Boylam": 41.582,
    "Rakım": 1662,
    "Sıcaklık": 8.3,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "TELLİTEPE|Kumlu": {
    "Enlem": 39.482,
    "Boylam": 41.582,
    "Rakım": 1662,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "TELLİTEPE|Kireçli": {
    "Enlem": 39.482,
    "Boylam": 41.582,
    "Rakım": 1662,
    "Sıcaklık": 8.3,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "TİPİDERESİ|Killi": {
    "Enlem": 39.483,
    "Boylam": 41.583,
    "Rakım": 1668,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "TİPİDERESİ|Tınlı": {
    "Enlem": 39.483,
    "Boylam": 41.583,
    "Rakım": 1668,
    "Sıcaklık": 8.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "TİPİDERESİ|Kumlu": {
    "Enlem": 39.483,
    "Boylam": 41.583,
    "Rakım": 1668,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "TİPİDERESİ|Kireçli": {
    "Enlem": 39.483,
    "Boylam": 41.583,
    "Rakım": 1668,
    "Sıcaklık": 8.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "TOPRAKKALE|Killi": {
    "Enlem": 39.484,
    "Boylam": 41.584,
    "Rakım": 1674,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "TOPRAKKALE|Tınlı": {
    "Enlem": 39.484,
    "Boylam": 41.584,
    "Rakım": 1674,
    "Sıcaklık": 7.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "TOPRAKKALE|Kumlu": {
    "Enlem": 39.484,
    "Boylam": 41.584,
    "Rakım": 1674,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "TOPRAKKALE|Kireçli": {
    "Enlem": 39.484,
    "Boylam": 41.584,
    "Rakım": 1674,
    "Sıcaklık": 7.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "TORAMAN|Killi": {
    "Enlem": 39.485,
    "Boylam": 41.585,
    "Rakım": 1680,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "TORAMAN|Tınlı": {
    "Enlem": 39.485,
    "Boylam": 41.585,
    "Rakım": 1680,
    "Sıcaklık": 7.7,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "TORAMAN|Kumlu": {
    "Enlem": 39.485,
    "Boylam": 41.585,
    "Rakım": 1680,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "TORAMAN|Kireçli": {
    "Enlem": 39.485,
    "Boylam": 41.585,
    "Rakım": 1680,
    "Sıcaklık": 7.7,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ULUÇAYIR|Killi": {
    "Enlem": 39.486,
    "Boylam": 41.586,
    "Rakım": 1686,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ULUÇAYIR|Tınlı": {
    "Enlem": 39.486,
    "Boylam": 41.586,
    "Rakım": 1686,
    "Sıcaklık": 7.9,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "ULUÇAYIR|Kumlu": {
    "Enlem": 39.486,
    "Boylam": 41.586,
    "Rakım": 1686,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ULUÇAYIR|Kireçli": {
    "Enlem": 39.486,
    "Boylam": 41.586,
    "Rakım": 1686,
    "Sıcaklık": 7.9,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "UYANIK|Killi": {
    "Enlem": 39.487,
    "Boylam": 41.587,
    "Rakım": 1692,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "UYANIK|Tınlı": {
    "Enlem": 39.487,
    "Boylam": 41.587,
    "Rakım": 1692,
    "Sıcaklık": 8.1,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "UYANIK|Kumlu": {
    "Enlem": 39.487,
    "Boylam": 41.587,
    "Rakım": 1692,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "UYANIK|Kireçli": {
    "Enlem": 39.487,
    "Boylam": 41.587,
    "Rakım": 1692,
    "Sıcaklık": 8.1,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ÜNLÜCE|Killi": {
    "Enlem": 39.488,
    "Boylam": 41.588,
    "Rakım": 1698,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ÜNLÜCE|Tınlı": {
    "Enlem": 39.488,
    "Boylam": 41.588,
    "Rakım": 1698,
    "Sıcaklık": 8.3,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "ÜNLÜCE|Kumlu": {
    "Enlem": 39.488,
    "Boylam": 41.588,
    "Rakım": 1698,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "ÜNLÜCE|Kireçli": {
    "Enlem": 39.488,
    "Boylam": 41.588,
    "Rakım": 1698,
    "Sıcaklık": 8.3,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "YAMANLAR|Killi": {
    "Enlem": 39.489,
    "Boylam": 41.589,
    "Rakım": 1704,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "YAMANLAR|Tınlı": {
    "Enlem": 39.489,
    "Boylam": 41.589,
    "Rakım": 1704,
    "Sıcaklık": 8.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "YAMANLAR|Kumlu": {
    "Enlem": 39.489,
    "Boylam": 41.589,
    "Rakım": 1704,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "YAMANLAR|Kireçli": {
    "Enlem": 39.489,
    "Boylam": 41.589,
    "Rakım": 1704,
    "Sıcaklık": 8.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "YAYLAKONAK|Killi": {
    "Enlem": 39.49,
    "Boylam": 41.59,
    "Rakım": 1710,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "YAYLAKONAK|Tınlı": {
    "Enlem": 39.49,
    "Boylam": 41.59,
    "Rakım": 1710,
    "Sıcaklık": 7.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "YAYLAKONAK|Kumlu": {
    "Enlem": 39.49,
    "Boylam": 41.59,
    "Rakım": 1710,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "YAYLAKONAK|Kireçli": {
    "Enlem": 39.49,
    "Boylam": 41.59,
    "Rakım": 1710,
    "Sıcaklık": 7.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "YELPİZ|Killi": {
    "Enlem": 39.491,
    "Boylam": 41.591,
    "Rakım": 1716,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "YELPİZ|Tınlı": {
    "Enlem": 39.491,
    "Boylam": 41.591,
    "Rakım": 1716,
    "Sıcaklık": 7.7,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "YELPİZ|Kumlu": {
    "Enlem": 39.491,
    "Boylam": 41.591,
    "Rakım": 1716,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "YELPİZ|Kireçli": {
    "Enlem": 39.491,
    "Boylam": 41.591,
    "Rakım": 1716,
    "Sıcaklık": 7.7,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "YENİKENT|Killi": {
    "Enlem": 39.492,
    "Boylam": 41.592,
    "Rakım": 1722,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "YENİKENT|Tınlı": {
    "Enlem": 39.492,
    "Boylam": 41.592,
    "Rakım": 1722,
    "Sıcaklık": 7.9,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "YENİKENT|Kumlu": {
    "Enlem": 39.492,
    "Boylam": 41.592,
    "Rakım": 1722,
    "Sıcaklık": 7.9,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "YENİKENT|Kireçli": {
    "Enlem": 39.492,
    "Boylam": 41.592,
    "Rakım": 1722,
    "Sıcaklık": 7.9,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "YENİKÖY|Killi": {
    "Enlem": 39.493,
    "Boylam": 41.593,
    "Rakım": 1728,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "YENİKÖY|Tınlı": {
    "Enlem": 39.493,
    "Boylam": 41.593,
    "Rakım": 1728,
    "Sıcaklık": 8.1,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "YENİKÖY|Kumlu": {
    "Enlem": 39.493,
    "Boylam": 41.593,
    "Rakım": 1728,
    "Sıcaklık": 8.1,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "YENİKÖY|Kireçli": {
    "Enlem": 39.493,
    "Boylam": 41.593,
    "Rakım": 1728,
    "Sıcaklık": 8.1,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "YEŞİLBAHÇE|Killi": {
    "Enlem": 39.494,
    "Boylam": 41.594,
    "Rakım": 1734,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "YEŞİLBAHÇE|Tınlı": {
    "Enlem": 39.494,
    "Boylam": 41.594,
    "Rakım": 1734,
    "Sıcaklık": 8.3,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "YEŞİLBAHÇE|Kumlu": {
    "Enlem": 39.494,
    "Boylam": 41.594,
    "Rakım": 1734,
    "Sıcaklık": 8.3,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "YEŞİLBAHÇE|Kireçli": {
    "Enlem": 39.494,
    "Boylam": 41.594,
    "Rakım": 1734,
    "Sıcaklık": 8.3,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "YEŞİLYAZI|Killi": {
    "Enlem": 39.495,
    "Boylam": 41.595,
    "Rakım": 1740,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "YEŞİLYAZI|Tınlı": {
    "Enlem": 39.495,
    "Boylam": 41.595,
    "Rakım": 1740,
    "Sıcaklık": 8.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "YEŞİLYAZI|Kumlu": {
    "Enlem": 39.495,
    "Boylam": 41.595,
    "Rakım": 1740,
    "Sıcaklık": 8.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "YEŞİLYAZI|Kireçli": {
    "Enlem": 39.495,
    "Boylam": 41.595,
    "Rakım": 1740,
    "Sıcaklık": 8.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "YOLÜSTÜ|Killi": {
    "Enlem": 39.496,
    "Boylam": 41.596,
    "Rakım": 1746,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "YOLÜSTÜ|Tınlı": {
    "Enlem": 39.496,
    "Boylam": 41.596,
    "Rakım": 1746,
    "Sıcaklık": 7.5,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "YOLÜSTÜ|Kumlu": {
    "Enlem": 39.496,
    "Boylam": 41.596,
    "Rakım": 1746,
    "Sıcaklık": 7.5,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "YOLÜSTÜ|Kireçli": {
    "Enlem": 39.496,
    "Boylam": 41.596,
    "Rakım": 1746,
    "Sıcaklık": 7.5,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "YUKARIKAYABAŞI|Killi": {
    "Enlem": 39.497,
    "Boylam": 41.597,
    "Rakım": 1752,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "YUKARIKAYABAŞI|Tınlı": {
    "Enlem": 39.497,
    "Boylam": 41.597,
    "Rakım": 1752,
    "Sıcaklık": 7.7,
    "pH": 6.8,
    "Azot": "Orta",
    "Fosfor": "Yüksek"
  },
  "YUKARIKAYABAŞI|Kumlu": {
    "Enlem": 39.497,
    "Boylam": 41.597,
    "Rakım": 1752,
    "Sıcaklık": 7.7,
    "pH": 6.7,
    "Azot": "Orta",
    "Fosfor": "Orta"
  },
  "YUKARIKAYABAŞI|Kireçli": {
    "Enlem": 39.497,
    "Boylam": 41.597,
    "Rakım": 1752,
    "Sıcaklık": 7.7,
    "pH": 7.0,
    "Azot": "Orta",
    "Fosfor": "Orta"
  }
}

st.set_page_config(page_title="Akıllı Tarım Karar Destek Sistemi", layout="centered")
st.title("🌾 Akıllı Tarım Karar Destek Sistemi")

st.markdown("Bu sistem Hınıs ilçesindeki 98 mahallenin toprak ve iklim bilgilerine dayalı olarak sulama, gübreleme, hastalık ve ürün önerileri sunar.")

# MAHALLE + TOPRAK TÜRÜ SEÇİMİ
mahalle = st.selectbox("Mahalle Seçiniz", sorted(set(m.split("|")[0] for m in veri.keys())))
toprak_turu = st.selectbox("Toprak Türü Seçiniz", ["Killi", "Tınlı", "Kumlu", "Kireçli"])
anahtar = f"{mahalle}|{toprak_turu}"

if anahtar in veri:
    v = veri[anahtar]
    st.markdown(f"**Enlem:** {v['Enlem']}")
    st.markdown(f"**Boylam:** {v['Boylam']}")
    st.markdown(f"**Rakım:** {v['Rakım']} m")
    st.markdown(f"**Sıcaklık:** {v['Sıcaklık']} °C")

    st.subheader("🧪 Tahmini Toprak Değerleri (Bölgesel Verilere Göre)")
    st.markdown(f"- **pH:** {v['pH']}")
    st.markdown(f"- **Azot Durumu:** {v['Azot']}")
    st.markdown(f"- **Fosfor Durumu:** {v['Fosfor']}")

    urun = st.selectbox("Ürün Seçiniz", ["Buğday", "Arpa", "Fasulye"])
    sulama_yapildi = st.radio("Sulama yapılıyor mu?", ["Evet", "Hayır"])
    arazi = st.number_input("Arazi büyüklüğü (dekar):", min_value=1)

    # SULAMA UYARISI
    if urun in ["Buğday", "Fasulye"] and sulama_yapildi == "Hayır":
        st.error("⚠️ Bu ürün için sulama yapılmalıdır. Lütfen sulama yapınız.")

    # GÜBRE TAVSİYESİ
    st.subheader("🌿 Gübreleme Tavsiyesi")
    if urun == "Buğday":
        st.markdown("- Üre: 25-30 kg/da")
        st.markdown("- Ahır Gübresi: 2 ton/da")
    elif urun == "Arpa":
        st.markdown("- Amonyum Sülfat: 20 kg/da")
        st.markdown("- Ahır Gübresi: 2-3 ton/da")
    elif urun == "Fasulye":
        st.markdown("- TSP: 20 kg/da")
        st.markdown("- Ahır Gübresi: 2.5 ton/da")

    # HASTALIK MODÜLÜ
    st.subheader("🦠 Hastalık ve İlaçlama Önerisi")
    if urun == "Buğday":
        if v["Sıcaklık"] > 8:
            st.warning("Septorya riski! → Tebuconazole")
    elif urun == "Fasulye":
        if v["Sıcaklık"] > 8 and v["Rakım"] < 1800:
            st.warning("Külleme riski! → Karathane")
    elif urun == "Arpa":
        if v["Rakım"] > 1850:
            st.warning("Yaprak lekesi riski! → Mancozeb")

    # ALTERNATİF ÜRÜN ÖNERİSİ
    st.subheader("🌱 Alternatif Ürün Önerisi")
    def alternatif_urun(urun, rakim, sicaklik, toprak):
        if urun == "Fasulye" and rakim < 1800 and sicaklik > 8:
            return "Mısır veya Ayçiçeği"
        if urun == "Buğday" and sicaklik > 8 and toprak == "Tınlı":
            return "Korunga veya Çavdar"
        if urun == "Arpa" and rakim > 1850 and sicaklik < 7:
            return "Mercimek veya Nohut"
        return "Fiğ veya Yulaf"
    st.success("Alternatif: " + alternatif_urun(urun, v["Rakım"], v["Sıcaklık"], toprak_turu))
else:
    st.error("Veri bulunamadı.")
