# Colour-Replacement-In-An-Image
A Python script that uses OpenCV to replace an area(s) of one colour with another colour.

This program demonstrates the use of OpenCV functionality to replace regions of one colour  
 in an image with another colour.  In this case, areas of white are replaced by green.       
 To run this program, OpenCV 3.4 must be installed on your computer.                         
                                                                                             
 Colour replacement is achieved by adding two images of the same size together.              
 In a digital image when a colour in one image is added to a corresponding area of black in  
 another image it is unchanged because black has a value of zero.                             
 So in the original image, areas of white have to be identified and then changed to black in 
 order to be replaced by green. This is a 6 step process.  After each step the resulting     
 image is displayed to illustrate the image processing that has taken place.                                                                         
                                                                                             
 Set the constant IMAGE_FILE_PATH to the file path & name of an image containing an area(s)  
 of white.                                                                                   
                                                                                             
 First the original image is displayed.  Press any key to advance to the next stage of image 
 processing.                                                                                 
                                                                                             
 The program will then create a mask displaying the identified regions of white against a    
 black background.   Areas of white correspond to those areas in the original image that     
 will be converted to green.                                                                 
                                                                                             
 The cursor can now be used as an eraser to remove areas of the mask that should not be      
 converted to green.                                                                         
 To do this press the left mouse key and move the cursor over the mask.                      
 Areas of white under the cursor will be replaced by black and the corresponding areas of    
 the original image will not now be converted to green.                                      
 Release the left mouse key to stop erasing.  Pressing the 'r' key will reset the            
 mask to it's original state.                                                                
  
 Press the 'q' key when you are happy that the mask represents the area of the image you      
 wish to change to green.                                                                         
                                                                                             
 Press any key to advance through the remaining stages of image processing.  
                                                                                             
 To close the program, close the 6 windows displaying the images by pressing the 'q' key.
 Then press any key to close the console.   
