import cv2 as cv
import os
import numpy as np
from skimage import color

if not os.path.exists('./GrayImages'):
    os.makedirs('./GrayImages')

if not os.path.exists('./DiscImages'):
    os.makedirs('./DiscImages')

if not os.path.exists('./BlackWhite'):
    os.makedirs('./BlackWhite')

if not os.path.exists('./ChangedHSL'):
    os.makedirs('./ChangedHSL')

if not os.path.exists('./CloseColors'):
    os.makedirs('./CloseColors')


def GrayConverter(img):
    img = img/255
    gray_img = 0.299 * img[:, :, 0] + 0.587 * img[:, :, 1] + 0.114 * img[:, :, 2]
    return gray_img


def find_close_colors(pixel, threshold, img):
    # Convert pixel from RGB to Lab color space
    pixel_lab = color.rgb2lab(pixel)
    height, width, channels = img.shape

    for y in range(height):
        for x in range(width):
            lab_color = color.rgb2lab(img[y, x])
            diff = color.deltaE_ciede2000(pixel_lab, lab_color)

            if diff <= threshold:
                img[y, x] = (0, 255, 0)

    return img

# reading images
daylightBright = cv.imread('./Images/IMG_3581.jpg')
daylightDim = cv.imread('./Images/IMG_3585.jpg')
fluoBright = cv.imread('./Images/IMG_3586.jpg')
fluoDim = cv.imread('./Images/IMG_3590.jpg')

# converting to grayscale
dayBright_togray = GrayConverter(daylightBright)
dayDim_togray = GrayConverter(daylightDim)
fluoBright_togray = GrayConverter(fluoBright)
fluoDim_togray = GrayConverter(fluoDim)

# saving grayscale images
cv.imwrite('./GrayImages/DayBright_gray.jpg', dayBright_togray * 255)
cv.imwrite('./GrayImages/DayDim_gray.jpg', dayDim_togray * 255)
cv.imwrite('./GrayImages/FluoBright_gray.jpg', fluoBright_togray * 255)
cv.imwrite('./GrayImages/FluoDim_gray.jpg', fluoDim_togray * 255)

# discretizing grayscale images and saving
dayBright_disc = (dayBright_togray*255//128)*128
dayDim_disc = (dayDim_togray*255//64)*64
fluoBright_disc = (fluoBright_togray*255//128)*128
fluoDim_disc = (fluoDim_togray*255//64)*64

cv.imwrite('./DiscImages/DayBright_disc.jpg', dayBright_disc)
cv.imwrite('./DiscImages/DayDim_disc.jpg', dayDim_disc)
cv.imwrite('./DiscImages/FluoBright_disc.jpg', fluoBright_disc)
cv.imwrite('./DiscImages/FluoDim_disc.jpg', fluoDim_disc)

# creating black-white images and saving
thr_value = 128  # threshold value

dayBright_BW = np.where(np.array(dayBright_togray*255) >= thr_value, 255, 0)
dayBright_BW = cv.convertScaleAbs(dayBright_BW)

dayDim_BW = np.where(np.array(dayDim_togray*255) >= thr_value/1.3, 255, 0)
dayDim_BW = cv.convertScaleAbs(dayDim_BW)

fluoBright_BW = np.where(np.array(fluoBright_togray*255) >= thr_value, 255, 0)
fluoBright_BW = cv.convertScaleAbs(fluoBright_BW)

fluoDim_BW = np.where(np.array(fluoDim_togray*255) >= thr_value/2, 255, 0)
fluoDim_BW = cv.convertScaleAbs(fluoDim_BW)

cv.imwrite('./BlackWhite/DayBright_BW.jpg', dayBright_BW)
cv.imwrite('./BlackWhite/DayDim_BW.jpg', dayDim_BW)
cv.imwrite('./BlackWhite/FluoBright_BW.jpg', fluoBright_BW)
cv.imwrite('./BlackWhite/FluoDim_BW.jpg', fluoDim_BW)

# changing hue, saturation and brightness
dayBright_HLS = cv.cvtColor(daylightBright, cv.COLOR_BGR2HLS)
dayBright_HLS[:, :, 0] += 100
dayBright_HLS[:, :, 1] += 30
dayBright_HLS[:, :, 2] += 30
dayBright_HLS = cv.cvtColor(dayBright_HLS, cv.COLOR_HLS2BGR)

dayDim_HLS = cv.cvtColor(daylightDim, cv.COLOR_BGR2HLS)
dayDim_HLS[:, :, 0] += 100
dayDim_HLS[:, :, 1] += 30
dayDim_HLS[:, :, 2] += 30
dayDim_HLS = cv.cvtColor(dayDim_HLS, cv.COLOR_HLS2BGR)

fluoBright_HLS = cv.cvtColor(fluoBright, cv.COLOR_BGR2HLS)
fluoBright_HLS[:, :, 0] += 100
fluoBright_HLS[:, :, 1] += 30
fluoBright_HLS[:, :, 2] += 30
fluoBright_HLS = cv.cvtColor(fluoBright_HLS, cv.COLOR_HLS2BGR)

fluoDim_HLS = cv.cvtColor(fluoDim, cv.COLOR_BGR2HLS)
fluoDim_HLS[:, :, 0] += 100
fluoDim_HLS[:, :, 1] += 30
fluoDim_HLS[:, :, 2] += 30
fluoDim_HLS = cv.cvtColor(fluoDim_HLS, cv.COLOR_HLS2BGR)

cv.imwrite('./ChangedHSL/DayBright_HSL.jpg', dayBright_HLS)
cv.imwrite('./ChangedHSL/DayDim_HSL.jpg', dayDim_HLS)
cv.imwrite('./ChangedHSL/FluoBright_HSL.jpg', fluoBright_HLS)
cv.imwrite('./ChangedHSL/FluoDim_HSL.jpg', fluoDim_HLS)

# finding close colors
newSize = [400, 400]  # example pixel in RGB format
threshold = 10  # example threshold value

print('Finding close colors on object and background for each of the images...')

daylightBrightRS = cv.resize(daylightBright, newSize) #resized image
dayBrightCloseObj = find_close_colors(daylightBrightRS[300, 200], threshold, daylightBrightRS)
cv.imwrite('./CloseColors/DayBright_CloseObj.jpg', dayBrightCloseObj)
daylightBrightRS = cv.resize(daylightBright, newSize) #resized image
dayBrightCloseBack = find_close_colors(daylightBrightRS[100, 100], threshold, daylightBrightRS)
cv.imwrite('./CloseColors/DayBright_CloseBack.jpg', dayBrightCloseBack)

print('Finished for DayLight Bright image')

daylightDimRS = cv.resize(daylightDim, newSize) #resized image
dayDimCloseObj = find_close_colors(daylightDimRS[300, 200], threshold, daylightDimRS)
cv.imwrite('./CloseColors/DayDim_CloseObj.jpg', dayDimCloseObj)
daylightDimRS = cv.resize(daylightDim, newSize) #resized image
dayDimCloseBack = find_close_colors(daylightDimRS[100, 100], threshold, daylightDimRS)
cv.imwrite('./CloseColors/DayDim_CloseBack.jpg', dayDimCloseBack)

print('Finished for Daylight Dim image')

FluoBrightRS = cv.resize(fluoBright, newSize) #resized image
fluoBrightCloseObj = find_close_colors(FluoBrightRS[300, 200], threshold, FluoBrightRS)
cv.imwrite('./CloseColors/FluoBright_CloseObj.jpg', fluoBrightCloseObj)
FluoBrightRS = cv.resize(fluoBright, newSize) #resized image
fluoBrightCloseBack = find_close_colors(FluoBrightRS[100, 100], threshold, FluoBrightRS)
cv.imwrite('./CloseColors/FluoBright_CloseBack.jpg', fluoBrightCloseBack)

print('Finished for Fluorescent Bright image')

FluoDimRS = cv.resize(fluoDim, newSize) #resized image
fluoDimCloseObj = find_close_colors(FluoDimRS[300, 200], threshold, FluoDimRS)
cv.imwrite('./CloseColors/FluoDim_CloseObj.jpg', fluoDimCloseObj)
FluoDimRS = cv.resize(fluoDim, newSize) #resized image
fluoDimCloseBack = find_close_colors(FluoDimRS[100, 100], threshold, FluoDimRS)
cv.imwrite('./CloseColors/FluoDim_CloseBack.jpg', fluoDimCloseBack)

print('Finished for Fluorescent Dim image')

print('All Processes finished successfully and the results are saved!')
# cv.imshow('Close colors on Back', dayDimCloseBack)
# cv.waitKey(0)



