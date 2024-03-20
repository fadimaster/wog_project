FROM python:alpine3.11

WORKDIR .

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "main_score.py", "host=0.0.0.0"]
