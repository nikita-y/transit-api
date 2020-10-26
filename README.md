# Endpoint returns list of ETA and ETD for gitven orgin and destination bus/rail stop codes

## Notes
- Docker image is avalible on DockerHub [here](https://hub.docker.com/repository/docker/nikitany/transit-api)
- Github Action is set up to build a new image and push it to DockerHub.
- Github Action is trigred by pushing new code to the `master` branch.
- The solution covers bus schedule only

## To build, run and deploy
`make build`  - to build a docker image
`make run`    - to run a docker container
`make deploy` - to deploy transit-api service on a local kubernetes cluster (2 replicas)

## To test
The endpoint takes 2 parameters `origin_station_id` and `destination_station_id`
```
 curl -X GET "http://localhost:5000/transit/api/v1/next?origin_station_id=2204&destination_station_id=2399"
```

