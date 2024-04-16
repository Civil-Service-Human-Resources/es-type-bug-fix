# ElasticSearch module type fix tool

## Install and run container

Firstly, create a `client.env` file which contains the host, username and password for your ElasticSearch database:

```properties
ES_HOST=<host>
# The host URL must include protocol and port. For example http://localhost:9200
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
es-client plan
```

### Apply update

```sh
es-client apply
```

### Plan revert

```sh
es-client revert-plan
```

### Apply revert

```sh
es-client revert-apply
```

## Track logs

The logs are contained in `logs/app.log`.

Use this command in a new tab (outside the container) to track logs live:

```sh
tail -f logs/app.log
```
