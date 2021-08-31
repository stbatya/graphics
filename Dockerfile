# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.8-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED=True

# Copy local code to the container image.
ENV APP_HOME=/flaskr
WORKDIR $APP_HOME
COPY . ./
ENV FLASK_APP=flaskr
ENV FLASK_ENV=development

# Install production dependencies.
RUN pip3 install Flask gunicorn
RUN pip3 install -r requirements.txt
# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
