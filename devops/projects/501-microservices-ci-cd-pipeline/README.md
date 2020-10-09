# Project 501: Microservices CI/CD Pipeline

## Description

This project aims to create full CI/CD Pipeline for microservice based applications using [Spring Petclinic Microservices Application](https://github.com/spring-petclinic/spring-petclinic-microservices). Jenkins Server deployed on Elastic Compute Cloud (EC2) Instance is used as CI/CD Server to build pipelines.

## Flow of Tasks for Project Realization

| Epic  | Task  | Students Task |  Task Definition   | Branch  |
| ---   | :---  | ---           |  :---              | :---    |
| Local Development Environment | Prepare Development Server Manually on EC2 Instance| MSP-1 | Prepare development server manually on Amazon Linux 2 for developers, enabled with `Docker`, `Docker-Compose`, `Java 11`, `Git`.  |
| Local Development Environment | Prepare GitHub Repository for the Project | MSP-2-1 | Fork and clone the Petclinic app from the Clarusway repository [Petclinic Microservices Application](https://github.com/clarusway/petclinic-microservices.git) |
| Local Development Environment | Prepare GitHub Repository for the Project | MSP-2-2 | Prepare base branches namely `master`, `dev`, `release` for DevOps cycle. |
| Local Development Environment | Check the Maven Build Setup on Dev Branch | MSP-3 | Check the Maven builds for `test`, `package`, and `install` phases on `dev` branch |
| Local Development Environment | Prepare a Script for Packaging the Application | MSP-4 | Prepare a script to package the application with Maven wrapper | feature/msp-4 |
| Local Development Environment | Prepare Development Server Cloudformation Template | MSP-5 | Prepare development server script with Cloudformation template for developers, enabled with `Docker`, `Docker-Compose`, `Java 11`, `Git`. | feature/msp-5 |
| Local Development Build | Prepare Dockerfiles for Microservices | MSP-6 | Prepare Dockerfiles for each microservices. | feature/msp-6 |
| Local Development Build | Prepare Script for Building Docker Images | MSP-7 | Prepare a script to package and build the docker images for all microservices. | feature/msp-7 |
| Local Development Build | Create Docker Compose File for Local Development | MSP-8-1 | Prepare docker compose file to deploy the application locally. | feature/msp-8 |
| Local Development Build | Create Docker Compose File for Local Development | MSP-8-2 | Prepare a script to test the deployment of the app locally. | feature/msp-8 |

## MSP 1 - Prepare Development Server Manually on EC2 Instance

- Prepare development server manually on Amazon Linux 2 for developers, enabled with `Docker`, `Docker-Compose`, `Java 11`, `Git`.

```bash

```

## MSP 2 - Prepare GitHub Repository for the Project

- Fork the Petclinic app from the Clarusway repository [Petclinic Microservices Application](https://github.com/clarusway/petclinic-microservices.git)

- Rename the forked repo on your GitHub as `microservices-ci-cd-pipeline-with-petclinic-app`.

- Clone the forked repo from your GitHub repo on development server.

```bash

```

- Prepare base branches namely `master`, `dev`, `release` for DevOps cycle.

  - Create `dev` base branch.

    ```bash
    
    ```

  - Create `release` base branch.

    ```bash
  
    ```

## MSP 3 - Check the Maven Build Setup on Dev Branch

- Switch to `dev` branch.

```bash

```

- Test the compiled source code.

```bash

```

- Take the compiled code and package it in its distributable `JAR` format.

```bash

```

- Install distributable `JAR`s into local repository.

```bash

```

## MSP 4 - Prepare a Script for Packaging the Application

- Create `feature/msp-4` branch from `dev`.

```bash

```

- Prepare a script to package the application with maven wrapper and save it as `package-with-mvn-wrapper.sh`.

```bash

```

- Commit and push the new script to remote repo.

```bash

```

## MSP 5 - Prepare Development Server Cloudformation Template

- Create `feature/msp-5` branch from `dev`.

```bash

```

- Create a folder for infrastructure setup with the name of `infrastructure`.

```bash

```

- Prepare development server script with Cloudformation template for developers, enabled with `Docker`, `Docker-Compose`, `Java 11`, `Git` and save it as `dev-server-for-petclinic-app-cfn-template.yml` under `infrastructure` folder.

```bash

```

- Commit and push the new script to remote repo.

```bash

```

## MSP 6 - Prepare Dockerfiles for Microservices

- Create `feature/msp-6` branch from `dev`.

```bash

```

- Prepare a Dockerfile for the `admin-server` microservice with following content and save it under `spring-petclinic-admin-server`.

```Dockerfile

```

- Prepare a Dockerfile for the `api-gateway` microservice with the following content and save it under `spring-petclinic-api-gateway`.

```Dockerfile

```

- Prepare a Dockerfile for the `config-server` microservice with the following content and save it under `spring-petclinic-config-server`.

```Dockerfile

```

- Prepare a Dockerfile for the `customer-service` microservice with the following content and save it under `spring-petclinic-customer-service`.

```Dockerfile

```

- Prepare a Dockerfile for the `discovery-server` microservice with the following content and save it under `spring-petclinic-discovery-server`.

```Dockerfile

```

- Prepare a Dockerfile for the `hystrix-dashboard` microservice with the following content and save it under `spring-petclinic-hystrix-dashboard`.

```Dockerfile

```

- Prepare a Dockerfile for the `vets-service` microservice with the following content and save it under `spring-petclinic-vets-service`.

```Dockerfile

```

- Prepare a Dockerfile for the `visits-service` microservice with the following content and save it under `spring-petclinic-visits-service`.

```Dockerfile

```

- Commit the changes, then push the Dockerfiles to the remote repo.

```bash

```

## MSP 7 - Prepare Script for Building Docker Images

- Create `feature/msp-7` branch from `dev`.

```bash

```

- Prepare a script to build the docker images and save it as `build-dev-docker-images.sh`.

```bash

```

- Commit the changes, then push the new script to the remote repo.

```bash

```

## MSP 8 - Create Docker Compose File for Local Development

- Create `feature/msp-8` branch from `dev`.

```bash

```

- Prepare docker compose file to deploy the application locally and save it as `docker-compose-local.yml`.

```yaml

```

- Prepare a script to test the deployment of the app locally with `docker-compose-local.yml` and save it as `test-local-deployment.sh`.

```bash

```

- Commit the change, then push the docker compose file to the remote repo.

```bash

```
