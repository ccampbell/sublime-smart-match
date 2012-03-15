# Sublime Text 2 Smart Match

Sublime Text 2 by default does not allow you to close parenthesis that are directly preceding other parenthesis.  This is the same behavior with brackets and square brackets.

Sometimes this is the desired behavior but let's say you have something like this: ``function1(foo)``.

If you go to wrap it in another function ``function2(function1(foo)`` then insert the cursor after foo to close the parenthesis it will not let you even though that parenthesis should be allowed.

This package makes it smarter so it detects matching parenthesis to see if the insertion is allowed.

For more information about the issue see the ticket I created at:  
http://www.sublimetext.com/forum/viewtopic.php?f=3&t=5708