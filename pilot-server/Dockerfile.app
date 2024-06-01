FROM python:3.10.12-slim

COPY ./pilot-server /pilot-server
COPY ./pypi /pypi

RUN dpkg -i pypi/*.deb
RUN pip install pypi/*.whl
RUN pip install pypi/*.tar.gz

WORKDIR /pilot-server
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV NET_IP=192.168.79.143

ENV MYSQL_PORT=3306
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=fanqie
ENV MYSQL_DATABASE=pilot

ENV ACCEPT_EULA=Y
ENV MSSQL_PORT=1433
ENV MSSQL_USER=sa
ENV MSSQL_DATABASE=pilot
ENV MSSQL_PASSWORD=Fanqie.1433

ENV POSTGRES_PORT=5432
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=fanqie
ENV POSTGRES_DB=postgres

CMD ["flask", "run"]
EXPOSE 5000
