# Custom Wallpaper Changer for Windows
![Example](wpchanger.gif)

Changes the background image of the desktop after a specified period of time.
**Cannot be used as a plug-in.**

## Installation
To be able to use this program, you need to enable Google Custom Search API, generate API key credentials and set a project:

*   Visit https://console.developers.google.com and create a project.

*   Visit https://console.developers.google.com/apis/library/customsearch.googleapis.com and enable "Custom Search API" for your project.

*   Visit https://console.developers.google.com/apis/credentials and generate API key credentials for your project.

*   Visit https://cse.google.com/cse/all and in the web form where you create/edit your custom search engine enable "Image search" option and for "Sites to search" option select "Search the entire web but emphasize included sites".

*   Add api key and cx key in config.ini (src/)

Run an install.bat script for create venv and install requirements.


## Usage
*   Add 3 or more images to the 'images' folder.
You can do this by running find_images.bat or SearchEngine.py.

If python is added in PATH variable:
```bash 
python SearchEngine.py
```

Enter the search query and the number of images you want to download.

If you want to add your own images (already on your pc) - just upload them to the images folder

*   Run 'run_WPChanger.bat' or 'WPChanger.py'
**Script will be minimized to tray.**


*That's all! Very easy, isn't it?*

**You can set image change timeout by yourself in file 'config.ini' in src folder.**
