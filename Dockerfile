FROM node:10-alpine

WORKDIR /home/node/app

RUN npm install

COPY . .

EXPOSE 8080

CMD [ "node", "print_number.js" ]