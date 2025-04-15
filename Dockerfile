#we want a base image
FROM python:3.10-alpine3.20
# install system dependencies
RUN apk add --no-cache build-base gcc musl-dev libffi-dev \
    nodejs npm
#make new folder and go in there
WORKDIR /app
#install tailwind
COPY package.json package-lock.json* ./
RUN npm install
#install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt
#copy files to this image
COPY . .
# build tailwind (if you have a build script in package.json)
RUN npm run tw-build
#expose port
EXPOSE 5000
# run the server
CMD ["python", "main.py"]