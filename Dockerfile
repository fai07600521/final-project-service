FROM node:14.15.0 as img-service
WORKDIR /app
COPY . /app
RUN npm install
COPY . /app
EXPOSE 3000
CMD ["npm","start"]

