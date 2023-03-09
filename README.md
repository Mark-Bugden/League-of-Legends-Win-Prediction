# League-of-Legends-Win-Prediction
A repository for my League of Legends Win Prediction project.

## Description
Coming soon!

## Folder structure
    - **Data Collection** : Tools and instructions for using API to query match data from RIOT Games
    - **img**: Images for Champion icons, scraped from web
    - **Preprocessing**: Notebook and output of preprocessing step converting raw match data into features and labels for machine learning use
    - **src**: Main folder, containing all important Machine Learning analyses of the match data
    - **streamlit app**: Files for streamlit app
    - **utils**: Utility scripts that are used by the notebooks in the repository.
    - Instructions.txt: Instructions on how to set up the environment
    - README.md: This readme file
    - requirements.txt: Requirements file for various packages in environment
    - riot.txt: Identifying file required by RIOT Games to obtain a development API
        

## How to setup the environment:

1. Create a Conda environment with
    ```
    conda create --name LoL python=3.7
    ```
2. Activate the environment with
    ```
    conda activate LoL
    ```

3. Install the following packages, in this order.
    ```python 
    conda install pip
    ```
    ``` 
    conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
    ```    
    ``` 
    pip install -r requirements.txt
    ``` 
   

Once you have the environment set up, you can run the Win_prediction.ipnb file in that environment (using, for instance, Jupyter Lab). 

### *Why the cudatools package?*
The cudatools package ensures that tensorflow runs on the GPU and not on the CPU, significantly speeding up the training process. You can probably run the notebook just fine using a CPU installation of tensorflow, but it will be a bit slower. 

## TO DO
1. Clean up Data Collection folder, organise into raw+sorted+preprocessed subfolders
2. Move Preprocessing into utils
3. Fix ANN notebook so it actually works
4. Streamline Data Collection pipeline
5. Run Data Collection Pipeline to get more data
6. Clean up deprecated imports in files
7. Add gitignore for ipythoncheckpoints
