FROM python:3.7.3-stretch

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt
    
EXPOSE 5000

CMD ["python", "app.py"]
