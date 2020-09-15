#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sys
import numpy as np
import open3d as o3d
sys.path.insert(1, "../data")
from utils import readData, readPointCloud


# In[5]:
ground_truth = readData("../data/01.txt")
ground_truth = ground_truth[:77][:]




# In[11]:


def computeTransformation(point_ind):
#     final_pose = []
    T = ground_truth[point_ind][:]
    T = np.reshape(T, (3,4))
    b = np.array([0,0,0,1])
    T = np.vstack ((T,b)) 
#     print (T.shape)
    return T


# In[8]:


# print (ground_truth.shape)
# res = computeTransformation(76)
# print(np.shape(res[0]))


# In[12]:


def computePoseCameraFrame(point_ind):
    file = "../data/01/" + str(point_ind).zfill(6) + ".bin"
    print (file)
    pcd = readPointCloud(file)
    npts = pcd.shape[0]
    lidar_to_cam = np.array([[0,-1,0,0],[0,0,-1,0],[1,0,0,0],[0,0,0,1]])
    pcd = np.hstack((pcd[:,:3],np.ones((npts,1))))
    poses = np.dot(np.asarray(pcd),lidar_to_cam.T)
    poses = np.dot(poses,computeTransformation(point_ind).T)
    print ("Hello 2.2!")
    return poses


# In[14]:


# pcd_net = o3d.geometry.PointCloud()
# for i in range(77):
#     poses = computePoseCameraFrame(i)
#     pcd = o3d.geometry.PointCloud()
#     pcd.points = o3d.utility.Vector3dVector(poses[:,:3])
#     pcd_net += pcd
# downpcd = pcd_net.voxel_down_sample(voxel_size=1)
# o3d.visualization.draw_geometries([downpcd])

