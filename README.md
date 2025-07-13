# Rainfall-Prediction-Model


Project Overview:
This project aims to predict the likelihood of rainfall using machine learning techniques. It was developed as a hands-on learning project, combining data preprocessing, model building, and deployment using modern Python libraries and tools.

Dataset & Preprocessing:

The dataset used contains historical weather data with features like temperature, humidity, pressure, dew point, cloud cover, sunshine, wind speed, and wind direction.

Data cleaning and exploration were done using Pandas, where missing values were handled and unnecessary columns were removed.

Seaborn and Matplotlib were used for visualizing data trends and understanding feature relationships, which helped in selecting useful features.

Model Building:
The model was trained using RandomForestClassifier from Scikit-learn.

Initially, the model was tested with default parameters. Later, hyperparameter tuning was performed to improve accuracy.

Scikit-learn was also used for:

Train-test splitting

Model evaluation (accuracy, confusion matrix)

Saving the trained model using  pickle

User Interface with Streamlit
A simple and interactive Streamlit UI was built for users to enter weather parameters.

On submitting the inputs, the app displays the prediction: whether it will rain or not.



Backend Integration with FastAPI:
The trained model was also integrated with FastAPI, allowing prediction through REST API.

This separation of backend and UI made the project more modular and closer to real-world deployment.

The /rainfall_prediction route accepts POST requests with input data and returns prediction results in JSON format.

Tools & Libraries Used:
pandas – for data cleaning and manipulation

matplotlib, seaborn – for visualizing feature patterns and correlations

scikit-learn – for training the Random Forest model and evaluation

streamlit – to design the interactive front-end

fastapi – to create a RESTful API for predictions

pickle – for saving and loading the model

google Colab

Summary:
The project successfully predicts rainfall with good accuracy and is accessible via both a web interface (Streamlit) and an API (FastAPI). It showcases the complete cycle of a machine learning project from data cleaning to deployment.

