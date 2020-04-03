# Kinect-Maze
(Deprecated)

**NiTE C has been fully replaced with Openni2, and Openni2 has then been replaced by the Azure Kinect**

New release! Use Openni2 instead of NiTE's C code.
For more documentation, see the project wiki.

## Dependencies
[Libfreenect](https://github.com/OpenKinect/libfreenect),
[OpenNI2](https://github.com/occipital/openni2),
[NiTE2](https://github.com/dpengineering/NiTE2/archive/v1.0.0.tar.gz)

### Installing Dependencies
 `sudo apt install freenect libopenni2-0 libopenni2-dev opencv-python`
 If the NiTE2 folder is not in root, install it from the link above and put it into /kinetic-maze (the home/root folder).


## Todo

Overarching objectives:
Remove need for supervision during use

### Ideas
Instead of a traditional menu, make a semitransparent GUI that overlays on top of the skeleton tracking feed, and when both of the user's hands (or if the user "pushes" on a button) it selects that option?

### GUI/Display
- [ ] Reconsider GUI design
- [ ] Add custom title art/font
- [ ] Make high score button actually display scores, top 10?
- [ ] limit score names to ~10 chars (8?)
- [ ] add a menu selector
- [ ] implement joystick? Or control menu via kinect (since that's possible now)

- [ ] Add line between hands to show what the program is tracking?
- [ ] Make everything more retro looking


- [ ] Write Admin screen functions
- [ ] Make admin and passcode screens have black background


### Functionality
- [ ] Have autosolve kick in after inactivity
- [ ] Reimplement scores and stopwatch
- [ ] Make the logger better
