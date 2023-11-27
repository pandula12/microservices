FROM python:3.9
WORKDIR /app
COPY gateway.py .
RUN pip install requests flask
CMD ["python", "gateway.py"]
