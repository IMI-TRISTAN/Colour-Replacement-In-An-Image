import cv2
import numpy as np
import os.path

###################################################################################################
### This program demonstrates the use of OpenCV functionality to replace regions of one colour  ###
### in an image with another colour.  In this case, areas of white are replaced by green.       ###
### To run this program, OpenCV 3.4 must be installed on your computer.                         ###
###                                                                                             ###
### Colour replacement is achieved by adding two images of the same size together.              ###
### In a digital image when a colour in one image is added to a corresponding area of black in  ###
### another image it is unchanged because black has a value of zero.                            ### 
### So in the original image, areas of white have to be identified and then changed to black in ###
### order to be replaced by green. This is a 6 step process.  After each step the resulting     ###
### image is displayed to illustrate the image processing that has taken place.                 ###                                                        ###
###                                                                                             ###
### Set the constant IMAGE_FILE_PATH to the file path & name of an image containing an area(s)  ###
### of white.                                                                                   ###
###                                                                                             ###
### First the original image is displayed.  Press any key to advance to the next stage of image ###
### processing.                                                                                 ###
###                                                                                             ###
### The program will then create a mask displaying the identified regions of white against a    ###
### black background.   Areas of white correspond to those areas in the original image that     ###
### will be converted to green.                                                                 ###
###                                                                                             ###
### The cursor can now be used as an eraser to remove areas of the mask that should not be      ###
### converted to green.                                                                         ###
### To do this press the left mouse key and move the cursor over the mask.                      ###
### Areas of white under the cursor will be replaced by black and the corresponding areas of    ###
### the original image will not now be converted to green.                                      ###
### Release the left mouse key to stop erasing.  Pressing the 'r' key will reset the            ###
### mask to it's original state.                                                                ###
###                                                                                             ###
### Press the 'q' key when you are happy that the mask represents the area of the image you     ###
### wish to change to green.                                                                    ###
###                                                                                             ###
### Press any key to advance through the remaining stages of image processing.                  ###
###                                                                                             ###                                                                                            ###
### To close the program, close the 6 windows displaying the images by pressing the 'q' key.    ###
### Then press any key to close the console.                                                    ###             
###################################################################################################   
"""Replaces areas of white in an image with green."""

#######################################################################
### Window display function                                         ###
#######################################################################
def display_window(window_name, origin_x, origin_y, width, height, window_title, image):
    """Displays an image called image in a window called window_name with the title
        window_title. It's bottom left-hand corner is at (origin_x, origin_y). """
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.moveWindow(window_name, origin_x, origin_y)
    cv2.resizeWindow(window_name, width, height)
    cv2.setWindowTitle(window_name, window_title)
    cv2.imshow(window_name, image)

#######################################################################
### Mouse callback function - executed when there is a mouse event. ###
#######################################################################
def eraser(event,x,y,flags,param):
    """Allows the cursor to be used as an eraser to remove areas of the mask."""
    global erase, image_name

    ERASER_COLOUR = (0,0,0)  #Black
    CIRCLE_RADIUS = 35 #pixels

    if event == cv2.EVENT_LBUTTONDOWN:
        # left mouse button pressed, start erasing the image
        # at position x,y (current cursor position) when the mouse is moved. 
        erase = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if erase == True:
            # If the left mouse button has been pressed,
            # indicated by the boolean erase being True
            # and the mouse is moving 
            # draw a filled black (BRG(0,0,0)) circle
            # of radius 35 pixels at position x, y. 
            cv2.circle(image_name, (x,y), CIRCLE_RADIUS, ERASER_COLOUR, cv2.FILLED)

    elif event == cv2.EVENT_LBUTTONUP:
        # stop erasing
        erase = False

# Initialise the global variable that determines if the area of the mask 
# under the moving cursor should be erased or not. 
erase = False

#######################################################################
###     Start of Python Script                                      ###
#######################################################################       
try:
        IMAGE_FILE_PATH= 'ManWithWhiteFerret.jpg'
        # First check the image exists at the given location
        if os.path.isfile(IMAGE_FILE_PATH):
            # STEP 1 - Load the image as a colour image into the variable original_image 
            original_image = cv2.imread(IMAGE_FILE_PATH, cv2.IMREAD_COLOR)
            
            # Display the original image
            display_window('original', 0, 0, 450, 600, 'Original Image', original_image)
            cv2.waitKey(0) #Halt execution of the script until any key is pressed 


            # STEP 2 - Create the mask and display it in a while loop so the user can modify it.
            # First convert the original image from the BGR colourspace 
            # to the Hue, Saturation, Value (HSV) colourspace.  
            # HSV better models how humans see colour.  It takes into to account light intensity. 
            # H – Hue ( Dominant Wavelength - colour ).
            # S – Saturation ( Purity / shades of the color ).
            # V – Value ( Light intensity ).
            original_image_hsv = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
            
            # define range of white color in HSV.  The array values [H, S, V] may need to 
            # be adjusted for your image. Data type, np.uint8, is integers in range 0-255
            lower_white = np.array([0,0,100], dtype=np.uint8) 
            upper_white = np.array([30,70,255], dtype=np.uint8)
            
            # Create the mask. White areas map to areas of white
            # in the original image that have HSV values in the range  
            # lower_white to upper_white 
            mask = cv2.inRange(original_image_hsv, lower_white, upper_white)
            
            # Display the mask 
            display_window('mask', 450, 0, 450, 600, 'Mask - Modify it if necessary.', mask)
            
            # Set the global variable, image_name, used by the function called eraser
            image_name=mask
            
            # Make a copy of the original mask in case the user wishes
            # to undo any changes they make to the mask
            original_mask = mask.copy()
            
            #Bind the mouse callback function to the window called mask.  
            #Each time a mouse event is fired, function eraser is called  
            cv2.setMouseCallback('mask', eraser)
            
            #keep looping until the 'q' key is pressed
            while True:
                cv2.imshow('mask',mask)
                key = cv2.waitKey(1) & 0xFF

                # if the 'r' key is pressed, 'undo changes'
                # by displaying the original mask again
                if key == ord('r'):
                    mask = original_mask.copy()
                    image_name=mask  #Put the original mask back into the image_name variable
 
	            # if the 'q' key is pressed, break from the loop
                elif key == ord('q'):
                    break


            # STEP 3 - Invert the mask by changing white areas to black and black areas to white
            # The bitwise_not function, inverts every bit of an array by changing 0's (black)
            # to 1's (white) and 1's to 0's
            mask_inverse = cv2.bitwise_not(mask)
            
            #Display the inverse of the mask
            display_window('mask_inverse', 450, 0, 450, 600, 'Inverse of the mask', mask_inverse)
            cv2.waitKey(0)  #Halt execution of the script until any key is pressed 

            # STEP 4 - Use the inverse mask to change white to black in the original image.
            # cv2.bitwise_and calculates the per-element bit-wise conjunction of two arrays
            # Where a white pixel overlays a black pixel the result is a black pixel 
            # because a logical True (white=1) AND False (black=0) = False (black=0)
            # Same agrument applies to a white pixel and a pixel of any colour.
            # And White + White = White  (True AND True = True)
            original_image_white2black = cv2.bitwise_and(original_image, original_image, mask= mask_inverse)
            
            #Display the resulting image
            display_window('original_image_white2black', 900, 0, 450, 600, \
                'Original image - With the inverse mask added.', original_image_white2black)
            cv2.waitKey(0) #Halt execution of the script until any key is pressed 
             

            # STEP 5 - Create a green rectangle with the same size as the image in IMAGE_FILE_PATH
            # The mask will then be used to mask areas of green when the rest of the rectangle is set to black. 
            
            #Get the dimensions of the original image
            width, height = original_image.shape[:2]
            
            #Initialise an RGB-image that is just black, which is the same size as the original image.
            green_rectangle = np.zeros((width,height,3), np.uint8)
            
            #Change black pixels to green
            green_rectangle[:,:] = (0,255,0) # (B, G, R)
            
            # Convert the green rectangle to black except for the area corresponding to the mask
            green_rectangle_masked = cv2.bitwise_and(green_rectangle, green_rectangle, mask = mask)
            
            #Display the resulting image
            display_window('green_rectangle_masked', 450, 0, 450, 600, \
                'green rectangle - with mask', green_rectangle_masked)
            cv2.waitKey(0) #Halt execution of the script until any key is pressed 
        
            # STEP 6 - Perform the colour replacement by adding the original image with white
            # changed to black to the masked green rectangle (unmasked areas changed to black).  
            # Note black + anycolor = anycolor because the value of black is 0 in openCV.
            result = cv2.add(original_image_white2black, green_rectangle_masked)
           
           # Display the image with white replaced by green
            display_window('result', 450, 0, 450, 600, 'Original image after colour replacement', result)
            cv2.waitKey(0) #Halt execution of the script until any key is pressed 
            cv2.destroyAllWindows()  
        else:
            raise IOError("Image file not found.")
except Exception as e:
    print(str(e))  
