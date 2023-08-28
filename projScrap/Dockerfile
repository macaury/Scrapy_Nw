FROM python:alpine3.17
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
EXPOSE 8080
COPY . /code

CMD [ "python","api.py" ]