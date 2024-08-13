FROM mcr.microsoft.com/playwright:v1.28.0-focal

RUN apt-get update && apt-get install -y \
    allure-commandline

COPY ui/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ui/ .

CMD ["pytest", "--alluredir=allure-results"]
