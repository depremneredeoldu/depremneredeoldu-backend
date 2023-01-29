IMAGE_TAG_NAME=depremneredeoldu-backend-img
CONTAINER_NAME=depremneredeoldu-backend

build:
	docker build -t ${IMAGE_TAG_NAME} .

deploy:
	docker run --name ${CONTAINER_NAME} -d ${IMAGE_TAG_NAME}