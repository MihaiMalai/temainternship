import numpy as np
from scipy.io import wavfile
import logging


def measure_wav_db_level(wav_file):
    logging.info(f'Reading {wav_file} wave audio file')
    fs, x = wavfile.read(wav_file)
    log_scale = 20*np.log10(32767)

    # convert data to float64, because it's hard to work on int16
    t = (np.array(x)).astype(np.float64)
    orig_SPL = 20*np.log10(np.sqrt(np.mean(np.absolute(t)**2))) - log_scale
    logging.info(f'Sound level:   {str(orig_SPL)} dFFS')
