import numpy as np
import scipy.sparse
import json
import os
import glob
import pretty_midi
import joblib
import sys

def msd_id_to_dirs(msd_id):
    """Given an MSD ID, generate the path prefix.E.g. TRABCD12345678 -> A/B/C/TRABCD12345678"""
    return os.path.join(msd_id[2], msd_id[3], msd_id[4], msd_id)

def rank(array):
    temp = array.argsort()
    ranks = np.empty(len(array), int)
    ranks[temp] = np.arange(len(array))
    return ranks

def get_top(a,N):
    return np.argsort(a)[::-1][-N:]

def csc_to_array(csc):
    return scipy.sparse.csc_matrix((csc['data'], csc['indices'], csc['indptr']), shape= csc['shape']).toarray()
def reshape_to_bar(flat_array):
    return flat_array.reshape(-1,96,128)


def id2file(msd_id):
    midi_file = glob.glob(os.path.join('/home/richardyang/NAS/salu133445/midinet/lmd_parsed/lmd_matched/' + msd_id_to_dirs(msd_id), '*.mid'))
    return midi_file[0]


with open('/home/richardyang/NAS/RichardYang/Dataset/Lakh_MIDI_Dataset/subset_id/rock/rock_id') as data_file:    
    s_id = json.load(data_file)

c_key_id = []
#test = []


def filter_C(idx, msd_id):
    sys.stdout.write("\r%d " %( idx+1))
    sys.stdout.flush()
    try:
        pm =  pretty_midi.PrettyMIDI(id2file(msd_id))
    #print 'key_numbers',[k.key_number for k in pm.key_signature_changes]
        if [k.key_number for k in pm.key_signature_changes] == [0]:
        #print 'C'
            return [msd_id]
            #c_key_id.extend([msd_id])
            
    except Exception as e:
        pass

c_key_id = joblib.Parallel(n_jobs=40)(joblib.delayed(filter_C)(idx, msd_id)for idx, msd_id in enumerate(s_id))
c_key_id = [x for x in c_key_id if x is not None]
'''for idx, msd_id in enumerate(s_id[:200]):
    try:
        pm =  pretty_midi.PrettyMIDI(id2file(msd_id))
    #print 'key_numbers',[k.key_number for k in pm.key_signature_changes]
        if [k.key_number for k in pm.key_signature_changes] == [0]:
        #print 'C'
            
            test.extend([msd_id])
            
    except Exception as e:
        pass
    #print msd_id_to_dirs(msd_id)
    sys.stdout.write("\r%d / %d" %( idx+1, len(s_id)))
    sys.stdout.flush()
'''
    
    



with open('rock_C_id', 'wb') as outfile:
    json.dump(c_key_id, outfile)


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          