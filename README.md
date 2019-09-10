# RecursiveRepository

## What RecursiveRepository does

RecursiveRepository replicates it's code onto your Github user profile by forking from the original repository.

This web application accepts requests using a Python Flask app deployed on Google Cloud. 

The backend Flask app serves html files to your web browser to move you through the web flow.

It first authenticates and requests access to your profile through the Github API, then sends another request to the Github API to fork
https://github.com/AlexChung1995/RecursiveRepository.git onto your authenticated user profile.

## To deploy and use RecursiveRepository


### 1.) Install Google Cloud SDK and add it to your path

- follow the instructions here: https://cloud.google.com/sdk/docs/
- add the gcloud bash command to your path by going to the directory where you downloaded the sdk to
    - then, write "./google-cloud-sdk/install.sh" in your terminal


### 2.) Create a new Google Cloud App project

- create a new project with this terminal command "gcloud projects create [YOUR_PROJECT_ID] --set-as-default"
    - I called my project "recursive-repo" so my command was "gcloud projects create recursive-repo --set-as-default"
- verify your project was created with "gcloud projects describe [YOUR_PROJECT_ID]"
    - my command was "gcloud projects describe recursive-repo"
- initialize the web app with "gcloud app create --project=[YOUR_PROJECT_ID]"
    - my command was "gcloud app create --project=recursive-repo"
    - you will also have to choose which region you want your cloud app deployed on, so follow the command prompt instructions after you run this command
- install the gcloud python app engine "gcloud components install app-engine-python"
- more detailed instructions are here: https://cloud.google.com/appengine/docs/standard/python3/quickstart


### 3.) Enable Billing for your Google Cloud app

- you will have to enable billing at the address here: https://console.cloud.google.com/projectselector/billing?lang=python3&st=true&_ga=2.220467096.-1609744369.1567999366
- you will get 300$ in free credit so this app will not charge you
- you can avoid incurring charges by deleting the project afterwards if you wish


### 4.) Clone the RecursiveRepository project so you have it locally

- If you have already used the RecursiveRepository web application, you can clone from your Github user account
- If not, write "git clone https://github.com/AlexChung1995/RecursiveRepository.git" in your terminal


### 5.) Register your GitHub App

- For this app to access Github User profiles, it must be registered with Github
- When your app is deployed on Google Cloud it will be accessible at http://YOUR_PROJECT_ID.appspot.com
    - because my project_id is recursive-repo, my web app can be accessed at http://recursive-repo.appspot.com  
- go to https://github.com/settings/applications/new
    - set Application Name to anything
    - set Homepage URL to http://YOUR_PROJECT_ID.appspot.com/
        - i set my Homepage URL to http://recursive-repo.appspot.com/
    - set Authorization Callback URL to http://YOUR_PROJECT_ID.appspot.com/callback
        - i set my Authorization Callback URL to http://recursive-repo.appspot.com/callback


### 6.) Put client ID and client Secret into a secrets file

- Once you have registered a new app with Github, you will be given a client ID and client Secret credentials
- in the RecursiveRepository project directory that you cloned earlier, in /self_replicating create a text file called secrets.ini

- secrets.ini should look like

```
    [GITHUB]
    client_ID = <the client ID provided by GitHub>
    client_Secret = <the client secret provided by GitHub>
```

- i have included an example .ini file called example.ini, you may change the values within and rename it to "secrets.ini"


### 7.) Add a Flask app secret key to secrets.ini

- The flask app that maintains the backend server for this application requires a secret key to maintain sessions
- you may chose any key that you like, it cannot have whitespaces within it and should be as random as possible
- add it to the secrets.ini file so that the flask app can read it

- secrets.ini should now look like

```
    [GITHUB]
    client_ID = <the client ID provided by GitHub>
    client_Secret = <the client secret provided by GitHub>
    
    [APP_SECRET]
    secret_key = <your_secret_key>
```

### 8.) Deploy on Google cloud

- go to your terminal and navigate to your RecursiveRepository/self_replicating directory
- write "gcloud app deploy"
- the web app will now be available at http://YOUR_PROJECT_ID.appspot.com