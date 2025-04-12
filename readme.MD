
## Simple airflow setup

### Step 1: Clone repo
```ssh
git clone git@github.com:vinkumdev/airflow-template-docker.git
```

#### Step 2: Setup and update .env

Rename .env.template and update if required

### Step 3: Build with docker
```ssh
docker network create airflow-network
docker compose up -d
```
http://localhost:8083

Username: admin, Password: admin

