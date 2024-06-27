import streamlit as st
import requests

st.title("Deteksi Harga Mobil Bekas")

# Input features from user
model = st.selectbox("Model", ["Toyota Agya", "Honda Civic", "Toyota Innova", "Mitsubishi Pajero"])
tahun = st.number_input("Tahun", min_value=2000, max_value=2023, value=2020)
transmisi = st.selectbox("Transmisi", ["Manual", "Automatic"])
jarak_tempuh = st.number_input("Jarak Tempuh (km)", min_value=0, value=20000)
bahan_bakar = st.selectbox("Bahan Bakar", ["Petrol/Gasoline/Bensin", "Diesel/Solar"])
pajak = st.number_input("Pajak (Rp)", min_value=0, value=1500000)
mpg = st.number_input("MPG (Miles Per Gallon)", min_value=0, value=25)
ukuran_mesin = st.number_input("Ukuran Mesin (L)", min_value=0.0, value=1.2, step=0.1)

if st.button("Prediksi Harga"):
    # Prepare the input data
    input_data = {
        "model": model,
        "tahun": tahun,
        "transmisi": transmisi,
        "jarak_tempuh": jarak_tempuh,
        "bahan_bakar": bahan_bakar,
        "pajak": pajak,
        "mpg": mpg,
        "ukuran_mesin": ukuran_mesin
    }
    
    # Send a request to the FastAPI backend
    response = requests.post("https://<YOUR_BACKEND_URL>/predict", json=input_data)
    result = response.json()
    
    # Display the predicted price
    st.write(f"Predicted Price: {result['predicted_price']}")
