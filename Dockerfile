FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./

RUN if [ -s requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

COPY main.py .

CMD ["python", "main.py"]