# -*- coding: utf-8 -*-
#/usr/bin/python2
'''
By kyubyong park. kbpark.linguist@gmail.com. 
https://www.github.com/kyubyong/tacotron
'''

class Hyperparams:
    '''Hyper parameters'''
    # data
    vctk = 'VCTK-Corpus/txt/*/*.txt'
    web = 'WEB/text.csv'
    max_len = 50 # maximum length of text
    max_duration = 5.0 # maximum duration of a sound file. seconds.
    max_word_vocab_size = 3000
    
    # signal processing
    sr = 22050 # Sampling rate. Paper => 24000
    n_fft = 2048 # fft points (samples)
    frame_shift = 0.0125 # seconds
    frame_length = 0.05 # seconds
    hop_length = int(sr*frame_shift) # samples  This is dependent on the frame_shift.
    win_length = int(sr*frame_length) # samples This is dependent on the frame_length.
    n_mels = 80 # Number of Mel banks to generate
    
    # model
    embed_size = 512 # alias = E
    encoder_num_banks = 16
    decoder_num_banks = 8
    num_highwaynet_blocks = 4
    r = 5 # Reduction factor. Paper => 2, 3, 5
    
    # training scheme
    lr = 0.001 # Paper => Exponential decay
    logdir = "logdir"
    batch_size = 32
    num_epochs = 20 # Paper => 2M global steps!
    loss_type = "l1" # Or you can test "l2"
    
    # etc
    num_gpus = 1 # If you have multiple gpus, adjust this option, and increase the batch size
                 # and run `train_multiple_gpus.py` instead of `train.py`.
    target_zeros_masking = True # If True, we mask zero padding on the target, 
                                 # so exclude them from the loss calculation.     