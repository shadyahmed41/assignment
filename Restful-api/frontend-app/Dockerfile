# Use a lightweight web server as the base image
FROM nginx:alpine

# Copy your HTML, CSS, and JS files to the nginx default public directory
COPY index.html /usr/share/nginx/html/

COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80 for HTTP traffic
EXPOSE 80

# Start the nginx server
CMD ["nginx", "-g", "daemon off;"]
