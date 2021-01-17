# Music Recommendation System
A unsupervised learning model which analyses playlists and gives recommendations. Dataset used is <a href="https://github.com/mdeff/fma#data">FMA</a>.


<img width="300px" src="https://media.giphy.com/media/tqfS3mgQU28ko/giphy.gif" />

### Why
We created this project to see if we can actually understand the musical patterns of a user with his playlist as the source and what factors are really useful in determining the taste and interest of the listener.

## Table of Contents
1. [Next Steps]()
2. [Installation]()
3. [Run it]()
4. [Approach]()
5. [Improvements]()

### Next steps
If you have jupyter installed, 

1. Clone the repo 
   ```shell
   $ git clone https://github.com/Sarathisme/music-recommendation-system.git
   ````
2. Visit the [Run It]() section

### Installation
1. Clone this repo to get the .ipynb files
   ```shell
   $ git clone https://github.com/Sarathisme/music-recommendation-system.git
   ```
2. Install python from <a href="https://www.python.org/downloads/"/>https://www.python.org/downloads</a>

3. Run setup.py to get the dataset
   ```shell 
   $ cd path/to/setup.py
   $ python setup.py
   ```

3. If you already have jupyter in your machine, skip the next step.

4. Install jupyter either from conda or pip
    
   If you dont have conda installed, get it from <a href="https://docs.continuum.io/anaconda/install/">https://docs.continuum.io/anaconda/install/</a>
   
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
2. Open jupyter notebook

   ```shell
   $ jupyter notebook
   ```
 
3. Open `Music Recommendation System (Data Processing and Analysis).ipynb` for data processing and analysis
4. Open `Music Recommendation System (Machine Learning).ipynb` for machine learning. This also has the recommendations code.

### Approach

