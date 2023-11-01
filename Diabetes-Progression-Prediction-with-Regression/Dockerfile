# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy Pipfiles to the container
COPY Pipfile Pipfile.lock /app/

# Install Pipenv
RUN pip install pipenv

# Install application dependencies using Pipenv
RUN pipenv install --deploy --ignore-pipfile

# Expose the port that Streamlit will run on (8501 by default)
EXPOSE 8501

# Copy your Streamlit app code to the container
COPY . /app/

# Copy your trained model to the container
COPY model.bin /app/

# Run the Streamlit app
CMD ["pipenv", "run", "streamlit", "run", "app.py"]
