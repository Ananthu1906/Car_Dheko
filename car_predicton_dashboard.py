import streamlit as st
import numpy as np

# Placeholder function for prediction
def predict_price(features):
    # Dummy prediction logic (replace this with actual model prediction later)
    return np.random.uniform(500000, 1500000)  # Dummy price in INR

# Streamlit app
def main():
    st.title('Used Car Price Predictor')
    st.write('Enter the details of the car to get the estimated price.')

    # Car make and models dictionary
    car_models = {
        'Toyota': ['Corolla', 'Camry', 'Yaris', 'Fortuner'],
        'Honda': ['Civic', 'Accord', 'City', 'CR-V'],
        'Ford': ['Figo', 'EcoSport', 'Mustang', 'Endeavour'],
        'BMW': ['3 Series', '5 Series', 'X1', 'X5'],
        'Audi': ['A4', 'A6', 'Q3', 'Q7']
    }

    # User inputs
    fuel_type = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'Electric', 'Hybrid'])
    body_type = st.selectbox('Body Type', ['Sedan', 'Hatchback', 'SUV', 'Coupe', 'Convertible'])
    km_driven = st.number_input('Kilometers Driven', min_value=1000, max_value=300000, step=1000)
    registration_year = st.number_input('Registration Year', min_value=2000, max_value=2024, step=1)
    
    make = st.selectbox('Car Make', list(car_models.keys()))
    car_model = st.selectbox('Car Model', car_models[make])

    ownership = st.number_input('Number of Previous Owners', min_value=0, max_value=5, step=1)
    engine_power = st.number_input('Engine Power (in BHP)', min_value=50, max_value=500, step=1)
    mileage = st.number_input('Mileage (in km/l)', min_value=10, max_value=24, step=1)
    city = st.selectbox('City', ['Chennai', 'Bangalore', 'Hyderabad', 'Delhi', 'Kolkata', 'Jaipur'])

    # Feature dictionary
    feature_dict = {
        'Fuel Type': fuel_type,
        'Body Type': body_type,
        'Kilometers Driven': km_driven,
        'Registration Year': registration_year,
        'Car Model': car_model,
        'Ownership': ownership,
        'Engine Power': engine_power,
        'Mileage': mileage,
        'City': city
    }

    # Display the selected features for verification
    st.write("### Selected Car Details:")
    for key, value in feature_dict.items():
        st.write(f"- **{key}**: {value}")
    
    # Show predictions
    if st.button('Predict Price'):
        # Example feature processing (replace with actual processing)
        features = list(feature_dict.values())
        
        # Dummy prediction
        price = predict_price(features)
        st.write(f'Estimated Price: ₹{price:,.2f}')

if __name__ == "__main__":
    main()
