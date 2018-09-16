# SVM Labs Environments

First make sure you have a working Python 3 Conda distribution, then follow the next steps depending on your operative system.

## Windows

### With Anaconda Navigator

If you want to use Anaconda Navigator, follow these steps:

1. Download the environment file *environment_windows.yml* to your computer.
2. Open Anaconda Navigator.
3. In the left menu, click on *Environments* (between *Home* and *Learning*).
4. In the middle menu, click on *Import* (at the bottom, between *Clone* and *Remove*).
5. A dialog appears. Click on the black folder to the right of *Specification file*.
6. Locate and select the *environment_windows.yml* you just downloaded.
7. The dialog should have filled the *Name* field automatically to *svm_labs*. Click on *Import*.
8. Wait for the environment to install (it may take some minutes to install all packages and dependencies).
9. The new *svm_labs* environment should now be available in the list of environments and be active (with a triangle next to it). If not, click on it to activate.
10. In the left menu, click on *Home*, locate *Jupyter notebook* and click on *Launch*.

### With Anaconda Prompt

Follow these steps:

1. Download the environment file *environment_windows.yml* to your computer.
2. Open an Anaconda Prompt terminal. Then type this (*<route_yml>* in the route where you downloaded *environment_windows.yml*):
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
  
