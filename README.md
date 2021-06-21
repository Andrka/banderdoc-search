It`s a written in Python (using FastAPI) API for upload and search 'pieces of text'.

### Prerequisites

Before you continue, ensure you have installed the latest versions of Python and pip on your computer.

This project uses [Poetry](https://python-poetry.org/) for dependency and virtual environment management. 

### Installation

1) Clone the repo:

`git clone https://github.com/Andrka/banderdoc-search.git`

2) To install the required dependencies and set up a virtual environment run in the cloned directory (using poetry):

`poetry install`

or install requirements using requirements.txt by yourself:

`pip install --user --upgrade -r requirements.txt`

### Run Docker container

1) Install Docker

2) Build Docker image using

`make image-build`

3) Run Docker container using

`make image-run`

4) Go to [http://127.0.0.1:80/docs](http://127.0.0.1:80/docs) to see all available methods of the API