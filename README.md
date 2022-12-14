# League-of-Legends-Win-Prediction
A repository for my League of Legends Win Prediction project

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
