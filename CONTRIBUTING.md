Contributing a new script:

1. Write a manim script and test it with the manim command line utility. You can install it from pypi (`pip install manimlib`) and create a video with it (`manim myfile.py MyScene`). Make sure the output video looks correct.
2. Make sure it fullfills the following criteria:
   * Easy to Read
   * Minimal Example
   * Not already in the library
3. Choose a folder where you think the script fits in.
e.g. [basics](https://github.com/flipdot/manim-gallery/tree/master/src/examples/01_basics) , or
[animations](https://github.com/flipdot/manim-gallery/tree/master/src/examples/02_animations). If you are creating a new category, make sure to add an empty `__init__.py` file
4. In the folder, click on "Propose new file" and paste your script
5. Click on "Create new pull request"
6. Make sure all tests were passed. As long as the build fails, your pull request won't be accepted

Thank you for contributing!
