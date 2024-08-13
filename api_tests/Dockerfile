FROM python:3.12

RUN apt-get update && apt-get install -y \

COPY api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY api/ .

CMD ["pytest", "api/tests/"]