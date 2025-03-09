# HSA13_hw15_logging
Set up Graylog and ELK stasks to collect slow MySQL logs. Compare MySQL performance with different long_query_time values
Setup a cluster


Insert 1 million users

```bash
docker exec -it app python insert_db.py
```

Create inputs for Graylog

```bash
chmod 775 graylog/setup-inputs.sh
./graylog/setup-inputs.sh
```

Run tests

```bash
docker exec -it app siege -c10 -t30s "http://127.0.0.1:5000/search?name=test"
```

Test results:

| long_query_time | transactions | longest_transaction |
|:---------------:|:------------:|:-------------------:|
|        0        |      295     |        1.62         |
|        5        |      315     |        1.42         |
|       10        |      328     |        1.37         |
