# LookingAtSound
## Introduction
For my Data Analysis project, I decided to analyize sound. This project consists of a Jupyter notebook file and a python file. 

## Prerequisites
Before being able to use this project, you first need to have python 3 installed running the latest version (I'm currently using version 3.8.9). 

### Python packages needed
Use pip3 to install the following modules. 
Example:
> pip3 install librosa
- librosa
- numpy
- matplotlib
- scipy
- pylab
- pandas
- seaborn
- wave
- pydub
  * Note: For pydub, I also had to install ffmpeg using homebrew to silence an error I was receiving. The code still runs, but if you want to silence any errors.
    > brew install ffmpeg

### Anaconda or Visual Studio Code with Jupyter Notebook extension
Because this project uses a Jupyter notebook file for the graphs, either install Anaconda and launch a new environment, or use Visual Studio Code and install the Jupyter notebook package (see [*this page*](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) for setting up your Visual Studio Code environment for Jupyter Notebook)

## Project Specifications
1.) In order to view some sounds, we need a sound file. The first feature of this project reads a .wav sound file that will be used for analyizing.

2.) After we have our sound file, we can take a look at it and manipulate it. We will do this with a Fast Fourier Transofrorm and taking samples of the file. 

3.) We then analyize the data from the audio file using various functions from the different packages installed.  

4.) The data is visualized in various spots throughout the Jupyter notebook. 

5.) Interpretation takes place along with visulization of the graphs. 