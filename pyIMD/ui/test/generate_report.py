import matplotlib.pyplot as plt
import math
from pathlib import Path
import pandas as pd
from scipy.misc import imread
import numpy as np
import os
from pyIMD.plotting.figures import create_montage_array

image_file_path = 'C:\\Users\\localadmin\\ownCloud\\Projects\\Collaborations\\David_Gotthold\\optical yeast data to analyze\\20180628\\ImageCrop'
data_path = "C:\\Users\\localadmin\\ownCloud\\SoftwareDev\\Python\\pyIMD\\pyIMD\\tests\\testData\\20180628\\CalculatedCellMass"
figure_rows = 5
rows_to_plot = 300

# image_file_path = 'C:\\Users\\localadmin\\ownCloud\\Projects\\Collaborations\\David_Gotthold\\optical yeast data to analyze\\20180711\\ImageCrop'
# data_path = "C:\\Users\\localadmin\\ownCloud\\Projects\\Collaborations\\David_Gotthold\\Yeast data to analyze\\PLL\\20180711\\CalculatedCellMass"
# figure_rows = 2
# rows_to_plot = -1

# Create list of all image files
files = []
for file in os.listdir(image_file_path):
    if file.endswith(".tif"):
        files.append(os.path.join(image_file_path, file))
# Read images to image stack
image_array = []
for iFile in files:
    a = imread(iFile, flatten=1)
    image_array.append(a)
image_stack = np.array(image_array)


def get_montage_array_size(size, image_row_count, frame_count, image_col_count):

    if len(size) == 0 or np.isnan(size).all():
        col = math.sqrt(image_row_count * frame_count / image_col_count)

        col = math.ceil(col)
        row = math.ceil(frame_count / col)
        montage_size = [row, col]

    elif any(np.isnan(size)):
        montage_size = size
        nan_idx = np.isnan(size)
        montage_size[nan_idx] = np.ceil(frame_count / size[~nan_idx])

    elif size[0] * size[1] < frame_count:
        return

    else:
        montage_size = size

    return montage_size


def create_montage_array(image_row_count, image_col_count, frame_count, img_array, montage_size):
    montage_size = list(np.int_(montage_size))
    montage_row_count = montage_size[0]
    montage_col_count = montage_size[1]

    montage_image_size = [montage_row_count * image_row_count, montage_col_count * image_col_count]

    montage_image_size = list(np.int_(montage_image_size))
    montage = np.zeros(montage_image_size)

    rows = list(range(0, image_row_count))
    cols = list(range(0, image_col_count))
    i_frame = 0

    for i in range(0, montage_row_count):
        for j in range(0, montage_col_count):
            if i_frame < frame_count:
                r = list(np.asarray(rows) + i * image_row_count)
                c = list(np.asarray(cols) + j * image_col_count)
                montage[np.ix_(r, c)] = img_array[i_frame, :, :]

            else:
                montage = montage
            i_frame = i_frame + 1

    return montage


intended_size = np.array([figure_rows, np.nan])
image_row_count = np.shape(image_stack)[1]
image_col_count = np.shape(image_stack)[2]
frame_count = np.shape(image_stack)[0]
montage_size = get_montage_array_size(intended_size, image_row_count, frame_count, image_col_count)

montage = create_montage_array(image_row_count, image_col_count, frame_count, image_stack, montage_size)



# Plot data
p = Path(data_path)
dd = pd.read_csv(data_path, sep='\t')
plt.suptitle('Experiment ID: %s' % (p.parts[-1-1]), size=16)
plt.subplot(211)
plt.plot(dd.iloc[0:rows_to_plot, 0]*60, dd.iloc[0:rows_to_plot, 1], 'ko', alpha=0.4)
dd['Mean mass [ng]'] = dd['Mass [ng]'].rolling(window=5).mean()
plt.plot(dd.iloc[0:rows_to_plot, 0]*60, dd.iloc[0:rows_to_plot, 2], 'r-')
plt.xlabel('Time [min]')
plt.ylabel('Mass [ng]')
plt.arrow(0,0,0,0.11, -0.2, fc="k", ec="k", head_width=2, head_length=0.04)
plt.arrow(80,0,0,0.11, -0.2, fc="k", ec="k", head_width=2, head_length=0.04)
plt.legend(['Measured data', 'Rolling mean', 'Bud event'])
plt.subplot(212)
plt.imshow(montage, cmap='gray', vmin=0, vmax=150)
ticks_x = np.arange(0, montage.shape[1], step=image_col_count/2)

x_names = []
x_ticks = []
for i in range(1, ticks_x.shape[0], 2):
    x_names.append(i)
    x_ticks.append(ticks_x[i])
x_names = np.array(x_names)
x_ticks = np.array(x_ticks)

x_tick_names = np.arange(1, x_names.shape[0]+1)
plt.xticks(x_ticks, x_tick_names)
ticks_y = np.arange(0, montage.shape[0], step=image_row_count/2)
y_names = []
print(montage_size)
print(montage.shape)
print(frame_count)
for i in range(1, 125, int(montage_size[1])):
    y_names.append(i)

y_ticks = []
for i in range(1, ticks_y.shape[0], 2):
    y_ticks.append(ticks_y[i])

y_names = np.array(y_names)
y_ticks = np.array(y_ticks)
y_tick_names = np.arange(y_names.shape[0])

plt.yticks(y_ticks, y_names)
plt.xlabel('Frame number')
plt.ylabel('Frame number')
# plt.axis('off')
plt.show()
# plt.savefig(str(Path(p.parent, 'ResultFigure.pdf')), dpi=300)




