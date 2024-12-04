import pickle
from flask import Flask, request, jsonify
import numpy as np

# Create a Flask instance
app = Flask(__name__)

# Load your trained model
with open('classifier.pkl', 'rb') as f:
    model = pickle.load(f)

# Define a route
@app.route('/')
def home():
    return "Hello, World!"

# Create an endpoint for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from the POST request
        data = request.get_json(force=True)
        
        # Extract features from the input data
        age = data['age']
        test_score = data['test_score']
        high_school_percentage = data['high_school_percentage']
        
        #print(f"Received features - Age: {age}, Test Score: {test_score}, High School Percentage: {high_school_percentage}")
         
 
        # Prepare the features as a NumPy array
        features = np.array([age, test_score, high_school_percentage]).reshape(1, -1)
        
         # Log the reshaped features to ensure it's in the correct format
        #print(f"Features shape: {features.shape}")
        
        # Make prediction using the loaded model
        prediction = model.predict(features)
        print(f"Model prediction: {prediction}")
        
        # The output prediction might be 0 (Not Admitted) or 1 (Admitted)
        admission_status = "Admitted" if prediction[0] == "Accepted" else "Not Admitted"
        
        # Return the prediction as a JSON response
        return jsonify({
            'admission_status': admission_status
        })
    except Exception as e:
        # Handle any errors
        return jsonify({'error': str(e)})



if __name__ == '__main__':
    app.run(debug=True)
