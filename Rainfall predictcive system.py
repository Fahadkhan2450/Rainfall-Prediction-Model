import streamlit as st
import pandas as pd
import pickle


loaded_model = pickle.load(open("C:/Users/Crown Tech/Desktop/Pandas projects/scikit learn learning material/rainfall prediction/rainfall_prediction.sav", 'rb'))


columns = ["pressure", "dewpoint", "humidity", "cloud", "sunshine", "winddirection", "windspeed"]


st.title("Rainfall Prediction System")

# Input fields
pressure = st.number_input("Pressure (hPa)")
dewpoint = st.number_input("Dew Point (°C)")
humidity = st.number_input("Humidity (%)")
cloud = st.number_input("Cloud Cover (%)")
sunshine = st.number_input("Sunshine Hours")
winddirection = st.number_input("Wind Direction (°)")
windspeed = st.number_input("Wind Speed (km/h)")


if st.button("Predict Rainfall"):
    input_data = [[pressure, dewpoint, humidity, cloud, sunshine, winddirection, windspeed]]
    input_df = pd.DataFrame(input_data, columns=columns)

  
    if isinstance(loaded_model, dict):
        model = loaded_model['model']
    else:
        model = loaded_model

   
    prediction = model.predict(input_df)

  
    result = "Rainfall Expected" if prediction[0] == 1 else " No Rainfall Expected"
    st.success(f"Prediction: {result}")
