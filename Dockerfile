FROM python:3.13

WORKDIR /app

COPY requirement.txt .

RUN pip install --no-cache-dir -r requirement.txt

COPY . .


EXPOSE 5000


CMD ["python3", "croApi.py"]
FROM python:3.13

WORKDIR /app

COPY requirement.txt .

RUN pip install --no-cache-dir -r requirement.txt

COPY . .


EXPOSE 5000


CMD ["python3", "croApi.py"]
FROM python:3.13

WORKDIR /app

COPY requirement.txt .

RUN pip install --no-cache-dir -r requirement.txt

COPY . .


EXPOSE 5000


CMD ["python3", "croApi.py"]
FROM python:3.13

WORKDIR /app

COPY requirement.txt .

RUN pip install --no-cache-dir -r requirement.txt

COPY . .


EXPOSE 5000


CMD ["python3", "croApi.py"]
