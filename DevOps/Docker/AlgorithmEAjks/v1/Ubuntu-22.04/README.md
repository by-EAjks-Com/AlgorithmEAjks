# Building and Deploying for Ubuntu 22.04

```powershell
cd /Path/To/AlgorithmEAjks
$timestamp = (get-date -format 'yyyyMMdd')
```

## Build

```powershell
docker build --pull --no-cache `
    --file DevOps/Docker/AlgorithmEAjks/v1/Ubuntu-22.04/Dockerfile `
    --tag docker.io/eajkseajks/algorithmeajks:v1-ubuntu-22.04-$timestamp `
    --tag docker.io/eajkseajks/algorithmeajks:v1-ubuntu-22.04-latest `
    .
```

## Deploy to Docker.IO

```powershell
docker login
docker push docker.io/eajkseajks/algorithmeajks:v1-ubuntu-22.04-$timestamp
docker push docker.io/eajkseajks/algorithmeajks:v1-ubuntu-22.04-latest
```
