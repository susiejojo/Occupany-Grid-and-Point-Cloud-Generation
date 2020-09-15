# Assignment 2.2 - Occupancy Grid Construction

## Objective:

- Create an occupancy grid map for each LiDAR scan. For the purpose of this assignment, you do not need to apply bayesian update rules and each individual scan can be assumed as a prior. Save each scan as a binary png
- Using odometry data, concat multiple scans and create a occupancy grid of 5, 10 and 15 scans

## Instructions to test and verify outputs:

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

### Python libraries used:

- numpy (for numerical computations)
- opencv (for saving and reading saved images)
- matplotlib (for displaying the occupancy grids)
- pandas (for processing the data into an organised DataFrame and to observe patterns in data)
- sys (for maintaining directory structures)

### Organisation of the notebook

The first part of the notebook guides step-by-step how the occupancy grid is generated for a given point cloud. Please refer to the notebook for detailed explanation of each cell of code. 
The notebook contains two standalone functions: `computeGrid_individual_pcd` and `computeGrid`.

#### `computeGrid_individual_pcd`: Function to compute occupancy grid for an individual pcd. 
`Input`: pcd (an individual point cloud (or a net_pcd resulting from addition of multiple pcds)

`Output`: An 400*400 array representing the image of the occupancy grid

`Usage`: img = computeGrid_individual_pcd(individual_pcd)

#### `computeGrid`: Function to compute occupancy grid of a LIDAR bin file indicated by a certain index
`Input`: the index of the LIDAR bin file to read and process for creation of occupancy grid

`Output`: An 400*400 array representing the image of the occupancy grid

`Usage`: img = computeGrid(index_of_bin_file)

### Where to find LIDAR bin files:

The individual LIDAR bin files are stored in `assignment-2-18_french-biriyani/data/01`. 

### Where to find outputs and results:

The individual occupancy grids for the LIDAR bin files are stored in `assignment-2-18_french-biriyani/data/imgs/cv`. 

#### Output storage form:

In the directory `assignment-2-18_french-biriyani` you will find images of generated occupancy grids numbered as `grid0.png`, `grid1.png` till `grid76.png`. 
They correspond to each of the individual 77 LIDAR bin files that can be found at the location mentioned above, namely `000000.bin`, `000001.bin` respectively and so on. 

#### Approach: 

#### Example Output for Part a):

Occupancy Grid for 0000000.bin:

![alt text](https://github.com/Mobile-Robotics-IIITH-2020/assignment-2-18_french-biriyani/blob/master/Assignment_2.2/grid.png "Title")

#### Output and results for Part b):

- Results:

We observe that the white patches in the generated occupancy grids become more distinct and prominent as we incorporate a greater no. of LIDAR bins. An analogy of this to the probabilistic Bayesian update would be that the confidence of a grid cell being occupied increases as we consider more LIDAR scans.
