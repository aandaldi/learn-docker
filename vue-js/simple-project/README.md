# learn-docker to run simple project vue-js

1.  Install the vue CLI
    To install the vue-cli npm module, open a command prompt and type sudo npm install --g vue-cli or npm install -g @vue/cli

    This command has installed the vue-cli on our machine as a global (hence the -g) package. This means that the “vue” command is available from the command-line. 

2.  initialization project
    vue init webpack-simple my-vue-app

    Entering the above command will begin the process of creating a new vue application. It will be created in the directory my-vue-app, you just need to wait for the template to download then answer some configuration questions, it is safe to leave the default answers for now.

3.  cd my-vue-app
    npm install
    npm run dev         #this code to run app on local machine

    These command instruct npm to download all the dependencies your project needs and then launch your application. 

4.  Create dockerfile
    ==========================================
    # build stage
    FROM node:lts-alpine as build-stage
    WORKDIR /app
    COPY package*.json ./
    RUN npm install
    COPY . .
    RUN npm run build

    # production stage
    FROM nginx:stable-alpine as production-stage
    COPY --from=build-stage /app/dist /usr/share/nginx/html
    EXPOSE 80
    CMD ["nginx", "-g", "daemon off;"]
    =================================================
    Ok, let’s see what’s going on here:
    we have split our original Dockerfile in multiple stages by leveraging the Docker multi-stage builds feature;
    the first stage is responsible for building a production-ready artifact of our Vue.js app;
    the second stage is responsible for serving such artifact using NGINX.

    Nevertheless, for realistically complex production use cases, it may be wiser to stand on the shoulders of some giant like NGINX or Apache and that is exactly what we are going to do next: we are about to leverage NGINX to serve our Vue.js app because it is considered to be one of the most performant and battle-tested solutions out there.

5.  build docker image
    docker build -t simple-vue-js .

6.  run docker image 
    docker run -d -p 8080:80 --rm --name simple-vue-js1 simple-vue-js
