# AU-CSC208-HW3
Assignment 3
# Make a Screensaver 
- Translate a list of program requirements to object methods
- Show that you can design methods that produce the desired object behavior
- Demonstrate that you understand how multiple objects are created from classes
- Write classes that implements the required methods you have designed
- Gain some familiarity with PyGame
- Evaluate your program to fix errors

Long gone are the days of screen burn-in, but screensavers are still a fun way to learn the various features of graphical systems like pygame. 

What screensavers are currently built in to your system? They might give you some inspiration. On a Mac, most seem to be about photo manipulation. The current Windows 10 are more like what you would have seen in the '80s and '90s. 

What can you build? Just about anything, as long as it meets the requirements below. Particles to look like dust or fireworks? Cool. Trippy graphics? Cool. Recreating starry night with the buildings? Serene. Recreating flying toasters, but with rice cookers? Neat. Maze Maker and Solver? Cool, but probably hard. Bouncing lines with lots of color and sound? Awesome. One caveat: you cannot build a screensaver of one or more objects (image, graphic, or text) bouncing around the screen (we've done that). If something more complex is bouncing around, bouncing is still okay, but there should be other kinds of movement present.

- NOT OK: [After Dark Bouncing Ball](https://youtu.be/ANnYbX54oU4?t=168)
- OK: [Bouncing Lines with Trails](https://www.youtube.com/watch?v=9uJhdAybFgw)

Unlike the previous assignment(s), you will not be writing to pass any tests. Frankly, they're very difficult to devise for GUIs, especially for something more open-ended like this. If you meet the file requirements and functionality requirements outlined in this document, you will get full credit. 


### File Requirements
1. **screensaver folder** All your source code should go in the top-level folder. No need to create a `src` folder as there are other folders for other types of content. There is no `test` folder this time.
2. **assets folder(s)** If you are using images, you will need a folder for `images`. You will definitely be using sounds, so you will need a folder for `sounds`. These have been created for you with the example image/sounds that we've been using in class. Feel free to use these to get started, but they cannot be in your final product. 
3. **Launch.py** You must create one python file that is used to run your Screensaver. No matter how the rest of your code is organized, if we run this file, your screensaver should open and begin displaying...whatever it is you decided to create. It **must** be called `Launch.py`. A file with this name has been provided. It includes the most basic pygame template with all listed steps.
4. One or more classes you have made to hold the data and control the behavior for something you are drawing to the screen. If you are drawing more than one kind of thing, you might find it easier to create multiple classes. This class is only required to have 3-4 methods:
   - `__init__()`: initializes all necessary object variables and loads any needed assets. will likely need the surface you are drawing to and the dimensions of the screen
   - `update()`: updates the position of the visible object when called
   - `handle()`: **optional** if your class can handle events, it should also have a handle method. If it doesn't handle events, this won't be necessary.
   - `draw()`: creates a visible representation of the object onto the screen through primitive shapes or images
5. **Design Folder** What is this thing supposed to do? In a design folder, provide a Markdown text file (.md) called `plan.md` that, in your own words, describes what you were planning. You can create this file in PyCharm and write everything in your IDE. If you want to include screenshots of a screensaver you were trying to imitate, or a sketch of your designs, this would also be helpful (just make sure to add the screenshots to the repo to make them accessible to us). You might have bitten off more than you could chew, and while you might meet the requirements for the assignment, the screensaver may not do what you planned. So let us know what you were shooting for. 


### Functional Requirements
1. Multiple objects must be animated and/or moving across the screen at a time. The definition of object is pretty loose here, so it might be a single image, a collection of lines, a pixel, some text, or a mix of images and graphic primitives.
2. There must be sound, either individual effects or music. See the example file - ball_with_sound.py to understand how to load sound and play sound in your pygame program. 
3. The screensaver should terminate if the user uses the 'Esc' or the escape button on the keyboard. The user should be able to exit with the window exit button as well.    
4. There should be one or more visible buttons that the user can click to change some visual or auditory aspect of the screensaver. 

### Inspiration (and warnings)
There are many screensavers out there. While looking, you might find some sites that offer to let you download new screensavers for your system. In general, you're probably not going to want to do that. Many of these sites are a bit sketchy, and the opportunity for getting malware onto your system is not worth the risk. 

Instead, scope around video streaming sites for examples:
1. The incredibly popular [After Dark 2.0 collection](https://www.youtube.com/watch?v=ANnYbX54oU4)
2. The longer video of the _deluxe_ edition showing [all screensavers](https://www.youtube.com/watch?v=we8JQe6ugrs) that could be obtained in the package

Feel free to provide links to any screensavers that you're following in your design folder. 

There are many royalty-free image and sound sites out there. Many require a login. Others, like [Pixabay](https://pixabay.com/), mix free content with links to sponsored content in the hopes you will spend some money while digging around in the free stuff. Feel free to use sounds and images from sites like this, but cite where you get them from (just provide a link in a comment in your launch file).

A `Particle` class is provided for you to use if you like. You can build from it and remix it. It can be used for falling objects, explosions, rain, etc. You still need to create your own class, even if you use the one I provided, even if you substantially modify it. Your class cannot be a copy of the Particle class, either.

**A tip**: many of the screensavers in the videos above, online, and on your system may draw on top of [whatever was on screen at the time](https://youtu.be/ANnYbX54oU4?t=182) rather than inside a window. It's a [very cool](https://youtu.be/ANnYbX54oU4?t=215) effect, but to accomplish this is a bit tricky for where you are at with programming. Instead of trying to get the actual current on screen contents of the desktop or other applications, just take a screenshot in your system, save it in your `images` directory, and draw it below all your other objects. It will look similar to what you want to do and is much easier to implement.   

