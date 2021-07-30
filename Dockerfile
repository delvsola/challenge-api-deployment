FROM python:3.8-slim
RUN mkdir app
WORKDIR "/app/"
COPY . .
RUN pip3 install -r requirements.txt
CMD ["waitress-serve", "--port=8080", "app:app"]