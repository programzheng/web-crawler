dev:
	docker compose build
	docker compose up 
build-image:
	docker build -t programzheng/web-crawler -f Dockerfile --platform linux/amd64 .
push-image:
	docker push programzheng/web-crawler:latest