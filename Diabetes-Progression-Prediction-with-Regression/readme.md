# Diabetes Progression Prediction App

This application predicts the progression of diabetes based on various health factors. It's built with Python and Streamlit, and can be run locally, in a Docker container, or deployed with Kubernetes.

![app.py](https://github.com/ajinkyavbhandare/projects/blob/main/Diabetes-Progression-Prediction-with-Regression/images/app.png)

## Deploying the App With Streamlit

Follow these steps to run the app without Docker:

1. Install the dependencies from the Pipfile:
    ```bash
    pip install pipenv
    pipenv install --deploy --ignore-pipfile
    ```
2. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Deploying the App With Docker

Follow these steps to run the app with Docker:

1. Save the Dockerfile. If you're using Windows, you can create a new text file named "Dockerfile" in Notepad.
2. Build the Docker image:
    ```bash
    cd ..
    docker build -t diabetic_pred .
    ```
3. Run the Docker container:
    ```bash
    docker run -p 8501:8501 diabetic_pred
    ```

## Deploying the App With Kubernetes

Follow these steps to deploy the app with Kubernetes:

1. Change the name of the image in the deploy.yaml file.
2. Apply the deployment configuration:
    ```bash
    kubectl apply -f deploy.yaml
    ```
Access the app at: http://localhost:8501/

