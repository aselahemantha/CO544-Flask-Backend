FROM python:3
LABEL authors="Asela H Premawansha"

ENTRYPOINT ["top", "-b"]

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0"]
