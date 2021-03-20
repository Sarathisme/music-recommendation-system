# Music Recommendation System
A unsupervised learning model which analyses playlists and gives recommendations. Dataset used is <a href="https://github.com/mdeff/fma#data">FMA</a>.


<img width="300px" src="https://media.giphy.com/media/tqfS3mgQU28ko/giphy.gif" />

### Why
We created this project to see if we can actually understand the musical patterns of a listener with their playlist as source and what factors are really useful in determining the taste and interest of the listener.

## Table of Contents
1. [Next Steps](https://github.com/Sarathisme/music-recommendation-system/blob/readme-changes/README.md#next-steps)
2. [Installation](https://github.com/Sarathisme/music-recommendation-system/blob/readme-changes/README.md#installation)
3. [Run it](https://github.com/Sarathisme/music-recommendation-system/blob/readme-changes/README.md#run-it)

### Next steps
If do not have jupyter and python visit [Install Jupyter and Python](https://github.com/Sarathisme/music-recommendation-system/tree/readme-changes#instal-jupyter-and-python)

If you have them, proceed with the below steps.

1. Clone the repo 

   ```shell
   $ git clone https://github.com/Sarathisme/music-recommendation-system.git
   ````
2. Visit the [Run It](https://github.com/Sarathisme/music-recommendation-system/blob/readme-changes/README.md#run-it) section

### Instal Jupyter and Python
1. Clone this repo to get the .ipynb files
   ```shell
   $ git clone https://github.com/Sarathisme/music-recommendation-system.git
   ```
2. Install python from <a href="https://www.python.org/downloads/"/>https://www.python.org/downloads</a>

3. If you already have jupyter in your machine, skip the next step.

4. Install jupyter either from conda or pip
    
   >If you dont have conda installed, get it from <a href="https://docs.continuum.io/anaconda/install/">https://docs.continuum.io/anaconda/install/</a>
   
   From conda  
    ```shell 
    $ conda install -c conda-forge jupyterlab
    $ conda install -c conda-forge notebook
    ```
    From pip (pip is auto installed when you install python)
    ```shell 
    $ pip install jupyterlab
    $ pip install notebook
    ```

### Run it
Unfortunately at this point we do not have a .tar or a pickle file for you to quickly plug and play the code.

1. Go to the cloned folder

   ```shell
   $ cd path/to/code
   ```
2. Run setup.py to get the dataset installed and extracted into the project folder.
   
   ```shell
   $ python setup.py
   ```

3. Open jupyter notebook

   ```shell
   $ jupyter notebook
   ```
 
3. Open `Music Recommendation System (Data Processing and Analysis).ipynb` for data processing and analysis
4. Open `Music Recommendation System (Machine Learning).ipynb` for machine learning. This also has the recommendations code.
