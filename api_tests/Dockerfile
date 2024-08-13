FROM python:3.12

RUN apt-get update && apt-get install -y \
    allure-commandline

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY api_tests /app/api_tests

WORKDIR /app/api_tests

CMD ["pytest", "--alluredir=allure-results"]