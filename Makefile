IMAGE_TAG_NAME=depremneredeoldu-api-img
CONTAINER_NAME=depremneredeoldu-api
DEV_DB_DIR=/home/production/deprem-db
NETWORK_NAME=swarm

build:
	docker build -t ${IMAGE_TAG_NAME} .

deploy:
	docker rm -f ${CONTAINER_NAME} || true
	docker run --name ${CONTAINER_NAME} -v ${DEV_DB_DIR}:/app/db --network ${NETWORK_NAME} -d ${IMAGE_TAG_NAME}

reload-nginx:
	docker exec nginx nginx -s reload