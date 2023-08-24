FROM python:3.9-slim

WORKDIR /app

COPY . .

# Make
RUN apt-get update && apt-get install -y make
RUN make setup

CMD ["make", "run"]
