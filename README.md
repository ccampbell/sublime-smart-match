# Sublime Text 2 Smart Match

Sublime Text 2 by default does not allow you to close parenthesis that are directly preceding other parenthesis.  This is the same behavior with brackets and square brackets.

Sometimes this is the desired behavior but let's say you have something like this: ``function1(foo)``.

If you go to wrap it in another function ``function2(function1(foo)`` then insert the cursor after foo but before the ending parenthesis to close the parenthesis it will not let you even though it should be allowed.

This package makes it smarter so it detects matching parenthesis to see if the insertion is allowed.

For more information about the issue see the ticket I created at:  
http://www.sublimetext.com/forum/viewtopic.php?f=3&t=5708

## Installation

This has been submitted to Sublime Package Control.  Until it is added you can use package control ``cmd+shift+p``.  Choose the option ``Package Control: Add Repository`` and type in ``https://github.com/ccampbell/sublime-smart-match``.

After that you can select ``Package Control: Install Package`` and choose ``sublime-smart-match``.

Another option is running the following command (this is the os x version):

```
cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
git clone git@github.com:ccampbell/sublime-smart-match.git SmartMatch
```