#!/bin/sh

TARGET_HTML="/usr/share/nginx/pilot-client/pages"
TARGET_JS="/usr/share/nginx/pilot-client/dist/js"

find "$TARGET_HTML" -type f -name '*.html' | while read FILE; do
    echo "Replacing ${NET_IP} and ${FLASK_PORT} in $FILE"
    sed -i "s/{ENV:NET_IP}/${NET_IP}/g" "$FILE"
    sed -i "s/{ENV:NGINX_PORT}/${NGINX_PORT}/g" "$FILE"
    sed -i "s/{ENV:FLASK_PORT}/${FLASK_PORT}/g" "$FILE"
done

find "$TARGET_JS" -type f -name '*.js' | while read FILE; do
    echo "Replacing ${NET_IP} and ${FLASK_PORT} in $FILE"
    sed -i "s/{ENV:NET_IP}/${NET_IP}/g" "$FILE"
    sed -i "s/{ENV:NGINX_PORT}/${NGINX_PORT}/g" "$FILE"
    sed -i "s/{ENV:FLASK_PORT}/${FLASK_PORT}/g" "$FILE"
done

echo "Pilot-Nginx initialization complete."
nginx -g 'daemon off;'

