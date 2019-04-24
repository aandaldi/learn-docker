# learn-docker to run simple project vue-js

1.  Install the vue CLI
    To install the vue-cli npm module, open a command prompt and type sudo npm install --g vue-cli or npm install -g @vue/cli

    This command has installed the vue-cli on our machine as a global (hence the -g) package. This means that the “vue” command is available from the command-line. 

2.  initialization project
    vue init webpack-simple my-vue-app

    Entering the above command will begin the process of creating a new vue application. It will be created in the directory my-vue-app, you just need to wait for the template to download then answer some configuration questions, it is safe to leave the default answers for now.

3.  cd my-vue-app
    npm install
    npm run dev

    These command instruct npm to download all the dependencies your project needs and then launch your application. 

4.  