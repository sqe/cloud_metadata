FROM python:3.11

RUN mkdir /cloud_metadata
COPY source/ cloud_metadata/
WORKDIR /cloud_metadata

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

ENV PORT 80
EXPOSE 80
ENV FLASK_APP=cloud_metadata.py
#ENTRYPOINT [ "flask", "run", "--host=0.0.0.0", "--port=80" ]
CMD ["FLASK_APP=cloud_metadata.py flask run"]