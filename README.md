# Flask Admission Prediction API with Machine Learning Model

This project provides a web API built with **Flask** that predicts the **admission status** based on the features **Age**, **Admission Test Score**, and **High School Percentage** using a trained **Machine Learning Model**. The model is trained on historical admission records, and the API exposes an endpoint to make predictions for new student data.

## Features
- **Flask Web API**: A RESTful API to interact with the trained machine learning model.
- **Machine Learning Model**: Predicts whether a student will be admitted based on their age, admission test score, and high school percentage.
- **Prediction Endpoint**: A POST endpoint `/predict` where users can submit data and receive admission predictions.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [API Endpoints](#api-endpoints)
4. [Model Details](#model-details)

## Installation

### Prerequisites
Make sure you have the following installed:
- **Python 3.x** (preferably Python 3.7+)
- **pip** (Python package manager)

### Steps to install

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/repository-name.git
   cd repository-name

2.  manually install the dependencies:
    ```bash
    pip install flask scikit-learn numpy pandas
    
## Usage

### 1. Running the Flask App

- To start the Flask server and run the API, use the following command:
   ```bash
   python app.py

### 2. Testing the API with Postman
- You can use Postman to test the API by sending a POST request to the /predict endpoint.

- URL: http://127.0.0.1:5000/predict

- Method: POST

- Headers:

- Content-Type: application/json
- Request Body (JSON):
{
  "age": 17,
  "test_score": 89,
  "high_school_percentage": 77
}

- Example Response:
{
  "admission_status": "Admitted"
}
## API Endpoints
- /predict
- Method: POST
- Description: Predicts admission status based on the provided features.
- Request Body (JSON):

## Model Details
- The model uses Age, Test Score, and High School Percentage to predict whether a student will be admitted. The model was trained on historical admission data.
