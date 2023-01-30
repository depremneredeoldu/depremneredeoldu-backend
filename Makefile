IMAGE_TAG_NAME=depremneredeoldu-api-img
CONTAINER_NAME=depremneredeoldu-api

build:
	docker build -t ${IMAGE_TAG_NAME} .

deploy:
	docker run --name ${CONTAINER_NAME} -d ${IMAGE_TAG_NAME}