FROM nginx:alpine

COPY nginx.cfg etc/nginx/sites-available/nginx.cfg

EXPOSE 80