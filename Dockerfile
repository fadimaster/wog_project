FROM python:alpine3.11

WORKDIR .

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY ../Downloads/wog_project%20 .

EXPOSE 5000

CMD ["python", "main_score.py", "host=0.0.0.0"]
