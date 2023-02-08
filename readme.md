# Custom Wallpaper Changer
Changes the background image of the desktop after a specified period of time.
**Cannot be used as a plug-in.**

## Table of Contents

* Requirements
* Installation
* Usage

## Requirements
*cachetools==5.3.0
certifi==2022.12.7
charset-normalizer==3.0.1
click==8.1.3
colorama==0.4.6
google-api-core==2.11.0
google-api-python-client==2.48.0
google-auth==2.16.0
google-auth-httplib2==0.1.0
Google-Images-Search==1.4.6
googleapis-common-protos==1.58.0
httplib2==0.21.0
idna==3.4
Pillow==9.4.0
protobuf==4.21.12
pyasn1==0.4.8
pyasn1-modules==0.2.8
pyfiglet==0.8.post1
pyparsing==3.0.9
pystray==0.19.4
python-resize-image==1.1.20
requests==2.28.2
rsa==4.9
six==1.16.0
termcolor==1.1.0
uritemplate==4.1.1
urllib3==1.26.14*


## Installation
To be able to use this program, you need to enable Google Custom Search API, generate API key credentials and set a project:

* Visit https://console.developers.google.com and create a project.

* Visit https://console.developers.google.com/apis/library/customsearch.googleapis.com and enable "Custom Search API" for your project.

* Visit https://console.developers.google.com/apis/credentials and generate API key credentials for your project.

* Visit https://cse.google.com/cse/all and in the web form where you create/edit your custom search engine enable "Image search" option and for "Sites to search" option select "Search the entire web but emphasize included sites".



## Usage
Explain how to use your project
Include code snippets and screenshots if possible
javascript
const projectName = require('project-name');

projectName.run();


