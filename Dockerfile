FROM python:3.8-slim
RUN mkdir app
WORKDIR "/app/"
RUN apt-get update && apt-get install curl -y
COPY . .
RUN curl -o "model/houseregressor.joblib" "http://akeyro.eu/downloads/houseregressor.joblib"
RUN curl -o "model/apartmentregressor.joblib" "http://akeyro.eu/downloads/apartmentregressor.joblib"
RUN pip3 install -r requirements.txt
CMD waitress-serve --port=${PORT} app:app