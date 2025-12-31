- the auth service docker file needs some updates, refer in this repo
- `docker build -t gokulkris/auth_service:latest .`use this command to tag your image

- `docker push gokulkris/auth_service:latest` to push we need to login to docker hub

- `docker login` to login to docker hub or `docker login -u gokulkris`
 
- how to run k9s in ubuntu
    - `sudo snap install k9s` to install k9s
    - `k9s` to run k9s 