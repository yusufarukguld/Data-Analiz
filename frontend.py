import streamlit as st
import requests
import pandas as pd

st.title('Veri Analizi Uygulaması')

st.write("""
Bu uygulama, dosya yükleyip basit bir veri analizi yapmanızı sağlar. 
Sağladığımız hizmetin en basit gösterimidir ve asıl olarak çok daha kapsamlı çözümler sunmaktayız.
Hizmetlerimizin sunduğu temel avantajlardan bazıları şunlardır:

1. **Kolay veri yükleme**: İşletmenizin verilerini hızlı ve güvenli bir şekilde analiz edebilirsiniz.
2. **Anlamlı bilgiler**: Verilerinizden çıkarılan önemli bilgilerle stratejik kararlar alabilirsiniz.
3. **Otomatik raporlamalar**: Özel ihtiyaçlarınıza göre raporlar oluşturup sunuyoruz.
4. **Görselleştirilmiş analizler**: Verilerinizi daha iyi anlamak için grafikler ve görselleştirmeler sağlıyoruz.
5. **İşletmenizi geliştirme**: Verilerinizin analiziyle operasyonel iyileştirmeler yaparak rekabette öne geçebilirsiniz.

Bu, sunduğumuz hizmetlerin en basit gösterimidir. Daha detaylı analizler ve çözümlerle işletmenizi en iyi hale getirmek için buradayız.
""")

uploaded_file = st.file_uploader("Dosya yükleyin", type=['csv', 'xlsx'])
if uploaded_file is not None:
    # Dosyanın uzantısına göre veriyi oku
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
    else:
        st.error("Desteklenmeyen dosya formatı.")
        st.stop()

    # Veri çerçevesini göster
    st.write("Yüklenen Veri:", df)

    # Temel istatistikleri hesapla ve göster
    st.write("Temel İstatistikler:", df.describe())

    # Veri tiplerini göster
    st.write("Veri Tipleri:", df.dtypes)

    # Eksik değerlerin sayısını göster
    st.write("Eksik Değerlerin Sayısı:", df.isnull().sum())

st.write("Dosya yükleyerek verileriniz üzerinde temel analizler yapabilirsiniz.")

