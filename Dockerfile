FROM python:3.10 AS builder
COPY _requirements.txt .
RUN pip install --user -r _requirements.txt

FROM python:3.10-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY src . 
ENV PATH=/root/.local:$PATH

CMD ["python3", "main.py"]