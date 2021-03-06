
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from numpy import newaxis, r_, c_, mat, e
from numpy.linalg import *
from vec_hsqc import pred_vec
import os

curdir = os.path.dirname( os.path.abspath( __file__ ) )


X = np.loadtxt( os.path.join( curdir, 'pred_eg_01_X' ) )
y = np.loadtxt( os.path.join( curdir, 'pred_eg_01_Y') )
legmat = np.loadtxt( os.path.join( curdir, 'pred_eg_01_legmat' ), dtype = 'str' )
#X = np.loadtxt( 'first500k_X.npy')
#y = np.loadtxt( 'first500k_y.npy')

#X = mat(c_[ X ])
#y = c_[ y ]

X = mat(c_[ X[:500000, :] ])
y = c_[ y[:500000] ]
legmat = legmat[:500000, :]

np.savetxt( os.path.join( curdir, 'first500k_X.npy' ), X )
np.savetxt( os.path.join( curdir, 'first500k_y.npy' ), y )
np.savetxt( os.path.join( curdir, 'first500k_legmat.npy' ), legmat, fmt = "%s" )

#X = np.loadtxt( 'first500k_X.npy' )
#y = np.loadtxt( 'first500k_y.npy' )
#legmat = np.loadtxt( 'first500k_legmat.npy', dtype = 'str' )

print X.shape, y.shape, legmat.shape



#y = np.loadtxt( 'pred_eg_01_Y' )

X = mat(c_[ np.hstack( [np.reshape( np.ones( X.shape[0] ), ( X.shape[0], 1 ) ), X] ) ] )

print X.shape

a = pred_vec.PredLog( X, y )
a.fscale()
a.train_classifier()
a.make_prediction()

np.savetxt( os.path.join( curdir, 'scaled_x_500k' ), a.X )

np.savetxt( os.path.join( curdir, 'first500k_predicted_Y' ), a.pred_Y )
np.savetxt( os.path.join( curdir, 'first500k_prediction' ), a.pred )
