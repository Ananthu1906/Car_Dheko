import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Placeholder function for prediction
def predict_price(features):
    # Dummy prediction logic (replace this with actual model prediction later)
    return np.random.uniform(500000, 1500000)  # Dummy price in INR

# Streamlit app
def main():
    st.title('Used Car Price Predictor Dashboard')

    # Layout for the dashboard
    col1, col2 = st.columns([1, 3])

    # Left column - Inputs
    with col1:
        st.header("Car Details")
        
        car_models = {
            'Toyota': ['Corolla', 'Camry', 'Yaris', 'Fortuner'],
            'Honda': ['Civic', 'Accord', 'City', 'CR-V'],
            'Ford': ['Figo', 'EcoSport', 'Mustang', 'Endeavour'],
            'BMW': ['3 Series', '5 Series', 'X1', 'X5'],
            'Audi': ['A4', 'A6', 'Q3', 'Q7']
        }
        
        make = st.selectbox('Car Make', list(car_models.keys()))
        car_model = st.selectbox('Car Model', car_models[make])
        registration_year = st.number_input('Registration Year', min_value=2000, max_value=2024, step=1)
        car_price = st.number_input('Car Price (in INR)', min_value=100000, max_value=10000000, step=50000)
        car_condition = st.selectbox('Car Condition', ['Excellent', 'Good', 'Fair', 'Poor'])
        
    # Right column - Dashboard
    with col2:
        st.header("Dashboard & Analysis")
        
        # Display the selected features
        st.subheader("Selected Car Details")
        st.write(f"**Make**: {make}")
        st.write(f"**Model**: {car_model}")
        st.write(f"**Registration Year**: {registration_year}")
        st.write(f"**Price**: ₹{car_price:,.2f}")
        st.write(f"**Condition**: {car_condition}")
        
        # Predictive Analysis
        if st.button('Predict Price'):
            features = [make, car_model, registration_year, car_price, car_condition]
            price_prediction = predict_price(features)
            st.write(f"**Predicted Price**: ₹{price_prediction:,.2f}")
        
        # Data Visualization
        st.subheader("Data Visualization")
        
        # Dummy data for visualization
        data = pd.DataFrame({
            'Model': ['Corolla', 'Camry', 'Civic', 'Accord', 'Figo'],
            'Price': [800000, 1500000, 900000, 1200000, 700000],
            'Year': [2018, 2019, 2017, 2020, 2016],
            'Mileage': [15, 14, 16, 13, 18]
        })

        # Bar Chart: Car Model vs Price
        st.write("### Car Model vs Price")
        fig1, ax1 = plt.subplots()
        ax1.barh(data['Model'], data['Price'], color='skyblue')
        ax1.set_xlabel('Price (INR)')
        ax1.set_title('Car Model vs Price')
        st.pyplot(fig1)

        # Line Chart: Year vs Price
        st.write("### Year vs Price")
        fig2, ax2 = plt.subplots()
        ax2.plot(data['Year'], data['Price'], marker='o', linestyle='-', color='green')
        ax2.set_xlabel('Year')
        ax2.set_ylabel('Price (INR)')
        ax2.set_title('Year vs Price')
        st.pyplot(fig2)

        # Scatter Plot: Mileage vs Price
        st.write("### Mileage vs Price")
        fig3, ax3 = plt.subplots()
        ax3.scatter(data['Mileage'], data['Price'], color='red')
        ax3.set_xlabel('Mileage (km/l)')
        ax3.set_ylabel('Price (INR)')
        ax3.set_title('Mileage vs Price')
        st.pyplot(fig3)

if __name__ == "__main__":
    main()
