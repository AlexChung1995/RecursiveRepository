To deploy and use RecursiveRepository

0.) Install python


1.) Install Google Cloud SDK and add it to your path

- follow the instructions here: https://cloud.google.com/sdk/docs/
- add it to your path with "./google-cloud-sdk/install.sh"


2.) Create a new Google Cloud App project

- create a new project with this command "gcloud projects create [YOUR_PROJECT_ID] --set-as-default"
    - I called my project "recursive-repo" so my command was "gcloud projects create recursive-repo --set-as-default"
- verify your project was created with "gcloud projects describe [YOUR_PROJECT_ID]"
    - my command was "gcloud projects describe recursive-repo"
- initialize the web app with "gcloud app create --project=[YOUR_PROJECT_ID]"
    - my command was "gcloud app create --project=recursive-repo"
- install the gcloud python app engine "gcloud components install app-engine-python"


3.) Enable Billing for your Google Cloud app

- you will have to enable billing at the address here: https://console.cloud.google.com/projectselector/billing?lang=python3&st=true&_ga=2.220467096.-1609744369.1567999366
- more detailed instructions are here: https://cloud.google.com/appengine/docs/standard/python3/quickstart


3.) Clone the RecursiveRepo project so you have it locally

- If you have already used the RecursiveRepo web application, you can clone from your Github user account
- If not, write "git clone https://github.com/AlexChung1995/RecursiveRepository.git" in your terminal


4.) Register your GitHub App

- For this app to access Github User profiles, it must be registered with Github
- When the app is deployed on Google Cloud it will be accessible at http://YOUR_PROJECT_ID.appspot.com
    - because my project_id is recursive-repo, my web app can be accessed at http://recursive-repo.appspot.com  
    - go to https://github.com/settings/applications/new
    - set Application Name to anything
    - set Homepage URL to http://YOUR_PROJECT_ID.appspot.com/
        - i set my Homepage URL to http://recursive-repo.appspot.com
    - set Authorization Callback URL to http://YOUR_PROJECT_ID.appspot.com/callback
        - i set my Authorization Callback URL to http://recursive-repo.appspot.com/callback


5.) Put client ID and client Secret into a secrets file

- Once you have registered a new app with Github, you will be given a client ID and client Secret credentials
- in the RecursiveRepo project directory that you cloned earlier, in /self_replicating create a text file called secrets.ini

-secrets.ini should look like

    ['GITHUB']
    client_ID = <the client ID provided by GitHub> 
    client_Secret = <the client secret provided by GitHub>


6.) Deploy on Google cloud

- go to your terminal and navigate to your RecursiveRepo/self_replicating directory
- write "gcloud app deploy"
- the web app will now be available at http://YOUR_PROJECT_ID.appspot.com