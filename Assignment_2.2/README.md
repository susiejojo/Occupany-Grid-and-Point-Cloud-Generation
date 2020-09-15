# Assignment 2.2 - Occupancy Grid Construction

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
    cd Assignment_2.2
</code>
\
<code>
    jupyter notebook
 </code>

### Running and testing 

After that, Jupyter Notebook should open locally. Tbe code can be found in the notebook `A22.ipynb`. The code can be tested locally by running each cell in the notebook. 

### Where to find LIDAR bin files:

The individual LIDAR bin files are stored in `assignment-2-18_french-biriyani/data/01`. 


### Where to find outputs and results:

The individual occupancy grids for the LIDAR bin files are stored in `assignment-2-18_french-biriyani/data/imgs/cv`. 

#### Output storage form:

In the directory `assignment-2-18_french-biriyani` you will find images of generated occupancy grids numbered as `grid0.png`, `grid1.png` till `grid76.png`. 
They correspond to each of the individual 77 LIDAR bin files that can be found at the location mentioned above, namely `000000.bin`, `000001.bin` respectively and so on. 
