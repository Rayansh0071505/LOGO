# LOGO

In this project we try to put logo in our webcam screen

<h3>  Here is the work-flow
Setup the webcam process flow

Before entering the main loop, do all the preprocessing

<li> Read the logo

<li>Resize it

<li>Gray scale it

<li>Get a mask (In the mask  we are setting up threshold which we range it from 1 to 255)

<li>In the main loop, set a region of interest (roi) of the size of the logo

<li>Use the mask to "mask out" the pixels.

<li>Add the logo in roi 
