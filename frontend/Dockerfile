





# Use an official Node.js runtime as a parent image
FROM node:latest

# Set the working directory to /app
WORKDIR /app

ENV NODE_ENV production

# Copy package.json and package-lock.json to the container
COPY package.json /app/package.json
COPY package-lock.json /app/package-lock.json

# Install dependencies
RUN npm install

# Copy the current directory contents into the container at /app
COPY . /app
RUN touch /app/.env


RUN npm run build

# Expose port 3000
EXPOSE 3000

CMD ["npm", "run", "start"]