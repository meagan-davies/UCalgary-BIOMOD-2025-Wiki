# UCalgary BIOMOD 2025 Wiki

## About this Template

### Files

The static assets are in the `static` directory. The layout and templates are in the `wiki` directory, and the pages live in the `wiki > pages` directory. Unless you are an experienced and/or adventurous human, you probably shouldn't change other files.

    |__ docs/               -> Static copy of wiki for deployment on GitHub Pages
    |__ static/             -> static assets (CSS and JavaScript files only)
    |__ wiki/               -> Main directory for the pages and layouts
        |__ footer.html     -> Footer that will appear in all the pages
        |__ layout.html     -> Main layout of your wiki. All the pages will follow its structure
        |__ menu.html       -> Menu that will appear in all the pages
        |__ pages/          -> Directory for all the pages
            |__ *.html      -> Actual pages of your wiki
    |__ .gitignore          -> Tells GitLab which files/directories should not be uploaded to the repository
    |__ .gitlab-ci.yml      -> Automated flow for building, testing and deploying your website.
    |__ app.py              -> Python code managing your wiki
    |__ dependencies.txt    -> Software dependencies from the Python code
    |__ README.md           -> File containing the text you are reading right now

### Technologies

  * [GitLab Pages](https://docs.gitlab.com/ee/user/project/pages/)
  * [Python](https://www.python.org): Programming language
  * [Flask](https://palletsprojects.com/p/flask/): Python framework
  * [Frozen-Flask](https://frozen-flask.readthedocs.io/en/latest/): Library that builds the wiki to be deployed as a static website
  * [Bootstrap](https://getbootstrap.com/docs/5.0/components): CSS and JS components used

### Building Locally

To work locally with this project, follow the steps below:

#### Install

* Using vscode the repository can be cloned from github
* Next create a virtual environment by running:
```bash
python3 -m venv venv
. venv/bin/activate # on Linux, MacOS; or
. venv\Scripts\activate # on Windows
pip install -r dependencies.txt
```

#### Execute

* To run the website open a terminal and run:
```bash
python app.py
```
* In browser of choice run http://0.0.0.0:8080 or http://localhost:8080/

### Using GitHub

* Note when using GitHub Git commands are used to control the movement of data
* To push and pull code in the repository
    - To push code: Use Source Control in side panel to commit changes to the respository and label updates
    - To pull code: Open a bash terminal and run
```bash
git pull
```
* Note branches can be used to contain updates and prevent overwriting updates
    - When merging branches it is important to avoiding overwriting code

#### Vscode Extensions

* Note to simplify the use of GitHub in Vscode the following extensions are utlised:
    - Git Extension Pack
    - GitHub Codespaces
    - GitHub Pull Requests

### Deploying to GitHub Pages

This project is set up with Frozen Flask to freeze the dynamic flask pages to allow for deployment. To utlise this method to update the deployed pages the following can be run:
```bash
python app.py build
```
 