# SVM Labs Environments

Follow the instructions below corresponding to your operating system.

## Linux

First make sure you have a working <a href="https://www.anaconda.com/download/#linux">Python 3 Conda Linux distribution</a>, then follow the next steps.

### With shell

Follow these steps:

1. Download the environment file *environment.yml* to your computer.
2. Open a shell terminal. Then type this (*<route_yml>* in the route where you downloaded *environment.yml*):
  ```
  conda env create -f <route_yml>
  ```

3. Wait for the environment to install (it may take some minutes to install all packages and dependencies).
4. Type the following. The terminal should reflect the activation and prompt afterwards *(svm_labs)*.
  ```
  source activate svm_labs
  ```
  
5. Start the Jupyter notebook server by typing:
  ```
  jupyter notebook
  ```
  
### Manually

If the above fails for whichever reason or notebooks do not work, do as follows:
   
1. Open a shell terminal.
2. Remove the previously created conda environment (if any) with:
  ```
  conda env remove -n svm_labs
  ```
3. Create the environment from scratch with:
  ```
  conda env create -n svm_labs python=3.6
  ```
4. Activate the environment by doing:
  ```
  source activate svm_labs
  ```

5. Install the packages specified in *environment.yml* file one by one, first trying with *conda* and if that does not work with *pip*. For example, the first package in the file is *jupyter=1.0.0*, so we try first:
  ```
  conda install jupyter=1.0.0
  ```
  And if that doesn't work:
  ```
  pip install jupyter==1.0.0
  ```
  Beware that *pip* requires double *==* signs for versions, while *conda* just expects one *=*. Note also that with *conda* some packages are not present in the default repositories, and you have to specify the *conda_forge* channel by hand via:
  ```
  conda install <package>=<version> -c conda-forge
  ```

6. When finished with all packages, launch Jupyter notebook:
  ```
  jupyter notebook
  ```  


## Windows

First make sure you have a working <a href="https://www.anaconda.com/download/#windows">Python 3 Conda Windows distribution</a>, then follow the next steps.

### With Anaconda Navigator

If you want to use Anaconda Navigator, follow these steps:

1. Download the environment file *environment.yml* to your computer.
2. Open Anaconda Navigator.
3. In the left menu, click on *Environments* (between *Home* and *Learning*).
4. In the middle menu, click on *Import* (at the bottom, between *Clone* and *Remove*).
5. A dialog appears. Click on the black folder to the right of *Specification file*.
6. Locate and select the *environment.yml* you just downloaded.
7. The dialog should have filled the *Name* field automatically to *svm_labs*. Click on *Import*.
8. Wait for the environment to install (it may take some minutes to install all packages and dependencies).
9. The new *svm_labs* environment should now be available in the list of environments and be active (with a triangle next to it). If not, click on it to activate.
10. In the left menu, click on *Home*, locate *Jupyter notebook* and click on *Launch*.

### With Anaconda Prompt

Follow these steps:

1. Download the environment file *environment.yml* to your computer.
2. Open an Anaconda Prompt terminal. Then type this (*<route_yml>* in the route where you downloaded *environment.yml*):
  ```
  conda env create -f <route_yml>
  ```

3. Wait for the environment to install (it may take some minutes to install all packages and dependencies).
4. Type the following. The terminal should reflect the activation and prompt afterwards *(svm_labs)*.
  ```
  activate svm_labs
  ```
  
5. Start the Jupyter notebook server by typing:
  ```
  jupyter notebook
  ```

### Manually

If the above fails for whichever reason or notebooks do not work, do as follows:
   
1. Open an Anaconda Prompt terminal.
2. Remove the previously created conda environment (if any) with:
  ```
  conda env remove -n svm_labs
  ```
3. Create the environment from scratch with:
  ```
  conda env create -n svm_labs python=3.6
  ```
4. Activate the environment by doing:
  ```
  activate svm_labs
  ```

5. Install the packages specified in *environment.yml* file one by one, first trying with *conda* and if that does not work with *pip*. For example, the first package in the file is *jupyter=1.0.0*, so we try first:
  ```
  conda install jupyter=1.0.0
  ```
  And if that doesn't work:
  ```
  pip install jupyter==1.0.0
  ```
  Beware that *pip* requires double *==* signs for versions, while *conda* just expects one *=*.

6. When finished with all packages, launch Jupyter notebook:
  ```
  jupyter notebook
  ```

