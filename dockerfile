FROM python:3.10.16

WORKDIR /work
COPY . /work
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000"]
