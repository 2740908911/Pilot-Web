# 使用SQL Server基础镜像
FROM postgres:12

ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=fanqie
ENV POSTGRES_DB=postgres

COPY ./sqldata/pgsql.sql /docker-entrypoint-initdb.d/pgsql.sql
EXPOSE 5432
