# Imports
import skimage as ski
import matplotlib.pyplot as plt
from IPython.display import clear_output
from time import time
import contextlib

# Timer
@contextlib.contextmanager
def timer(msg):
    tic = time()
    yield
    print(msg + ": %.2f s" % (time() - tic))
    
# Useful functions
def show_image(im, title='',show_colorbar=False,vmin=None,vmax=None,figsize=None):
    if figsize!=None:
        fig, ax = plt.subplots(1,1,figsize=figsize)
    if im.ndim == 2:
        plt.imshow(im, cmap=plt.cm.gray,vmin=vmin, vmax=vmax)
#         plt.imshow(im, cmap=plt.cm.gray)#,vmin=vmin, vmax=vmax)
    else:
        plt.imshow(im)
    clear_output(wait = True)
    
    plt.axis('off')
    plt.title(title)
    if show_colorbar:
        plt.colorbar()
        
    return plt.gcf(), plt.gca()

def show_multi_image(im_title, row_col = None, show_colorbar=False, vmin=None, vmax=None, figsize=None, tight_layout=False):
    unzipped_list = list(zip(*im_title))
    im_list = unzipped_list[0]
    if len(unzipped_list)==1:
        title_list = [''] * len(im_list)
    elif len(unzipped_list)==2:
        title_list = unzipped_list[1]
    else:
        raise ValueError("im_title must be a list or tuple containing either only images or (image,title) tuples (or list)")
            
    

    if row_col == None:
        fig, ax = plt.subplots(1,len(im_list),figsize=figsize,tight_layout=tight_layout)
    else:
        fig, ax = plt.subplots(row_col[0],row_col[1],figsize=figsize,tight_layout=tight_layout)
    ax = ax.flatten()
    if title_list == None:
        title_list = [''] * len(im_list)

    for i in range(len(im_list)):
        plt.sca(ax[i])
        show_image(im_list[i],title_list[i])
        
    for i in range(len(im_list),len(ax)):
        plt.sca(ax[i])
        plt.axis('off')
        
    return fig, ax