# Use the official Nginx Alpine image
FROM nginx:alpine

# Copy the Nginx configuration file into the container
COPY nginx.cfg /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

# Start Nginx when the container starts
CMD ["nginx", "-g", "daemon off;"]