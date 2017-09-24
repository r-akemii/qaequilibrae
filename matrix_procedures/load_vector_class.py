"""
 -----------------------------------------------------------------------------------------------------------
 Package:    AequilibraE

 Name:       Loads vectors from file/layer
 Purpose:    Implements vector loading

 Original Author:  Pedro Camargo (c@margo.co)
 Contributors:
 Last edited by: Pedro Camargo

 Website:    www.AequilibraE.com
 Repository:  https://github.com/AequilibraE/AequilibraE

 Created:    2016-08-15
 Updated:    30/09/2016
 Copyright:   (c) AequilibraE authors
 Licence:     See LICENSE.TXT
 -----------------------------------------------------------------------------------------------------------
 """

from qgis.core import *
from PyQt4.QtCore import *
import numpy as np
from ..common_tools.worker_thread import WorkerThread
import struct
from aequilibrae.matrix import AequilibraEData

class LoadVector(WorkerThread):
    def __init__(self, parentThread, layer, index_field, fields):
        WorkerThread.__init__(self, parentThread)
        self.layer = layer
        self.index_field = index_field
        self.fields = fields
        self.error = None
        self.python_version = (8 * struct.calcsize("P"))

    def doWork(self):
        # idx = self.idx
        # feat_count = self.layer.featureCount()
        # self.emit(SIGNAL("ProgressMaxValue( PyQt_PyObject )"), (feat_count))
        #
        # idx1 = idx[0]
        # idx2 = idx[1]
        # # We read all the vectors and put in a list of lists
        # vector = []
        # P = 0
        # for feat in self.layer.getFeatures():
        #     P += 1
        #     a = feat.attributes()[idx1]
        #     b = feat.attributes()[idx2]
        #     vector.append([a, b])
        #     if P % 100 == 0:
        #         self.emit(SIGNAL("ProgressValue( PyQt_PyObject )"), (int(P)))
        #
        # vector = np.array(vector)  # transform the list of lists in NumPy array
        #
        # # bincount has odd behavior on 32 vs 64, so we need to control for that
        # if self.python_version == 32:
        #     zones = np.bincount(vector[:,0].astype(np.int32))
        # else:
        #     zones = np.bincount(vector[:, 0].astype(np.int64))
        #
        # if np.max(zones)  > 1:
        #     self.error = 'Zone field is not unique'
        # else:
        #     zones = np.max(vector[:, 0]) + 1
        #     vec = np.zeros(zones)
        #     vec[vector[:, 0].astype(int)] = vector[:, 1]
        #
        #     self.vector = vec
        if self.error is None:
            self.data = AequilibraEData()


        self.emit(SIGNAL("ProgressValue( PyQt_PyObject )"), (int(feat_count)))
        self.emit(SIGNAL("finished_threaded_procedure( PyQt_PyObject )"), 'Vector loaded')