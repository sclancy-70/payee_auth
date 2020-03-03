FROM python:3

Expose 8080

WORKDIR /usr/src/app

COPY requirements.txt . 

RUN pip install --no-cache-dir -r requirements.txt waitress

COPY . .

CMD [  "waitress-serve", "--call", "payee_auth_api.app:create_app"]
