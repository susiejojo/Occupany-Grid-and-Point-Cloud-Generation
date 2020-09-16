# Instructions to run 

The codes for Assignment 2.1 and 2.2 are written in the notebooks `A21.ipynb` and `A22.ipynb`. Follow the below instructions to navigate to these notebooks and run them:

### How to navigate to jupyter notebook

In your terminal:\
<code>
    git clone https://github.com/Mobile-Robotics-IIITH-2020/assignment-2-18_french-biriyani
</code>
\
<code>
    cd assignment-2-18_french-biriyani
</code>
\
<code>
    conda env create -f env.yml
</code>
\
<code>
    conda activate mr
</code>
\
<code>
    cd Assignment_2.1 
</code>
  or 
<code>
    cd Assignment_2.2 
</code>
\
<code>
    jupyter notebook
 </code>
 
### Running and testing 

After that, Jupyter Notebook should open on localhost in the folder for Assignment 2.1 or 2.2. The code can be found in the notebook 'A21.ipynb' under Assignment_2.1 or 'A22.ipynb' under Assignment_2.2. 

Code for A21.ipynb has also been saved as a Python script in `A21.py`.

The code can be tested locally by running each cell in the notebook.

Make sure that all cells containing functions in the notebook are run to generate the final outputs, as the code has been modularised, and the final output depends on multiple functions defined the cells before it.


### Where to find LiDAR bin files:

The individual LiDAR bin files are stored in `assignment-2-18_french-biriyani/data/01`. 

### Where to find outputs and results:

The individual occupancy grids and the occupancy grid for a net of 5,10,15 point clouds from the LIDAR bin files (Assignment 2.2 parts a) and b)) are stored in `assignment-2-18_french-biriyani/data/imgs/cv`. 
