FROM python:3.8-buster
COPY . /app/practice
WORKDIR /app/practice
RUN pip install -r requirements.txt
CMD ["python3", "main.py"]
