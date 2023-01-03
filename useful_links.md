*Remember: to view .md in VS code, use the shortcut: Command+Shift+V*

[Understanding XPATH in Selenium]( 
https://www.browserstack.com/guide/xpath-in-selenium#:~:text=Using%20Text-,What%20is%20XPath%20in%20Selenium%3F,both%20HTML%20and%20XML%20documents.)

**Summary**

```
How many types of xpath are there?
    - Two types of xpath
-> What are the two types?
    - Absolute and Relative xpath
    #1- Absolute xpath:
        - starts with / 
        - Starts from the very beginning of the html page, 
        and goes down to desired web element 1 by 1.
        - it is NOT dependable at all. 
        - easly brakes if there is any minimal changes 
        in the structure of the HTML page.
    #2- Relative xpath:
        - starts with //
        - // means you can start from anywhere in the HTML code
        - it will jump to the first matching value and return it 
        - There are MANY different options to use relative xpath
        Commmon xpaths:
            #1- //tagName[@attribute='value']
            #2- //*[@attribute='value'] --> * means look for all web elements
            #3- //tagName[.='text'] --> returns the web element with given text.
    -> instead of giving tag name if you pass * it return all the web elements 
    that contain given attribute and value regardless of the tag name.
```
