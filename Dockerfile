#Use an official pyhtom image
FROM python:3.11.11-slim

#set the working directory in the container
WORKDIR /network_anomaly

#upgrade pip
RUN python3 -m pip install --upgrade pip

#copy the files into the container
COPY . /network_anomaly

#install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#set environment variable for Flask
ENV FLASK_APP=app.py

#command to run the Flask app
CMD [ "python", "app.py" ]