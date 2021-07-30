FROM python:3.8-alpine
RUN mkdir app
WORKDIR "/app/"
RUN pip3 install -r requirements.txt
CMD ["waitress-serve", "--port=8080", "app:app"]