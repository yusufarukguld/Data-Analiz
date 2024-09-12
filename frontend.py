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


uploaded_file = st.file_uploader("Dosya Seçiniz", type=['csv', 'xlsx'], )
if uploaded_file is not None:
    # Backend'e dosyayı gönderme
    print(uploaded_file)
    files = {'file': uploaded_file}
    response = requests.post("http://127.0.0.1:8000/upload", files=files)
    if response.status_code == 200:
        # Sonuçları alıp gösterme
        description = pd.read_json(response.json()['description'])
        st.write(description)
    else:
        st.error("An error occurred. " + response.json()['message'])


