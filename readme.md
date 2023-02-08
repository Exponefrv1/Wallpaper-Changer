# Custom Wallpaper Changer
Changes the background image of the desktop after a specified period of time.
**Cannot be used as a plug-in.**

## Installation
To be able to use this program, you need to enable Google Custom Search API, generate API key credentials and set a project:

* Visit https://console.developers.google.com and create a project.

* Visit https://console.developers.google.com/apis/library/customsearch.googleapis.com and enable "Custom Search API" for your project.

* Visit https://console.developers.google.com/apis/credentials and generate API key credentials for your project.

* Visit https://cse.google.com/cse/all and in the web form where you create/edit your custom search engine enable "Image search" option and for "Sites to search" option select "Search the entire web but emphasize included sites".

* Add api key and cx key in config.ini (src/)

Launch a install.bat script for create venv and install requirements.


## Usage
Explain how to use your project
Include code snippets and screenshots if possible
javascript
const projectName = require('project-name');

projectName.run();


