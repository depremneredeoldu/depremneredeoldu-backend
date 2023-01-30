IMAGE_TAG_NAME=depremneredeoldu-api-img
CONTAINER_NAME=depremneredeoldu-api
NETWORK_NAME=swarm

build:
	docker build -t ${IMAGE_TAG_NAME} .

deploy:
	docker rm -f ${CONTAINER_NAME} || true
	docker run --name ${CONTAINER_NAME} -d ${IMAGE_TAG_NAME} --network ${NETWORK_NAME}
