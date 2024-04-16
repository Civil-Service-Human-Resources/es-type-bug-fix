# ElasticSearch module type fix tool

## Install and prepare environment

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

## Update ElasticSearch database

### 1. Get inside the Docker container

To enter the client container, run this command:

```sh
docker-compose exec es-client bash
```

The following are to be run within the client container:

### 2. Plan

```sh
es-client plan
```

This will create a `plan.json` file:

### 3. Apply

Using the `plan.json` file, this command will apply the updates to the specified ElasticSearch database:

```sh
es-client apply
```

## Revent updates

Using the `plan.json` file, this command will create a new plan, `revert-plan.json` to revert the changes made:

```sh
es-client revert-plan
```

### Apply revert

This command will use `revert-plan.json` to apply the reversion:

```sh
es-client revert-apply
```

## Track logs

The logs are contained in `logs/app.log`.

Use this command in a new tab (outside the container) to track logs live:

```sh
tail -f logs/app.log
```
