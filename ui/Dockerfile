FROM python:3.12

COPY api_tests/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY api_tests/ ./

CMD ["pytest"]