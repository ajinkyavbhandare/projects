import numpy as np
import streamlit as st
import pickle

with open('model.bin', 'rb') as f_in:
    loaded_model = pickle.load(f_in)

def main():
    st.title('Diabetes Progression Prediction App')
    st.write('Enter feature values to predict diabetes progression.')

    # Create two columns
    col1, col2 = st.columns(2)

    # Create input fields for user to enter feature values in each column
    age = col1.number_input('Age', min_value=-0.1, max_value=0.1, value=0.0)
    sex = col1.number_input('Sex', min_value=-0.1, max_value=0.1, value=0.0)
    bmi = col1.number_input('BMI', min_value=-0.1, max_value=0.1, value=0.0)
    bp = col1.number_input('Average Blood Pressure', min_value=-0.1, max_value=0.1, value=0.0)
    s1 = col1.number_input('S1', min_value=-0.1, max_value=0.2, value=0.0)

    s2 = col2.number_input('S2', min_value=-0.1, max_value=0.2, value=0.0)
    s3 = col2.number_input('S3', min_value=-0.1, max_value=0.2, value=0.0)
    s4 = col2.number_input('S4', min_value=-0.1, max_value=0.2, value=0.0)
    s5 = col2.number_input('S5', min_value=-0.1, max_value=0.2, value=0.0)
    s6 = col2.number_input('S6', min_value=-0.1, max_value=0.2, value=0.0)

    # Create a button to make predictions
    if st.button('Predict'):
        # Create a new data point with user input
        new_data_point = np.array([[age, sex, bmi, bp, s1, s2, s3, s4, s5, s6]])

        # Use the loaded model to make predictions
        predicted_progression = loaded_model.predict(new_data_point)

        # Categorize the predicted progression
        if predicted_progression[0] < 115:
            category = 'low'
        elif predicted_progression[0] < 205:
            category = 'mid'
        else:
            category = 'high'

        # Display the prediction and category to the user
        st.write(f'Predicted Progression: {predicted_progression[0]}')
        st.write(f'Category: {category}')

if __name__ == '__main__':
    main()
