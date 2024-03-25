# ElasticSearch module type fix tool

## Install and run container

Firstly, create a `client.env` file which contains the host, username and password for your ElasticSearch database:

```properties
ES_HOST=<host>
ES_USERNAME=<username>
ES_PASSWORD=<password>
```

Next, build and run the client container:

```sh
docker-compose build
docker-compose up -d
```

## Run tool inside container

To enter the client container, run this command:

```sh
docker-compose exec es-client bash
```

The following are to be run within the client container:

### Plan update

```sh
python main.py plan
```

### Apply update

python main.py plan

## Track logs

The logs are contained in `logs/app.log`.

Use this command in a new tab (outside the container) to track logs live:

```sh
tail -f logs/app.log
```