# PDF reordering script

This script can be helpful for re-arranging a pdf file which may have pages out of order.

## About the script ReArrange.py**

* It takes path of the file as an Input.
* Then it takes current page which is in the wrong order and the right page no. it should be on.
* Seperate values by a comma ',' and line by line.
  * Example:-  
  
	`1,2`  
	`3,1`  
	`2,3`
     	
      *here the 1st page in the pdf should be on the 2nd page instead and so on.*

* The script parses and sorts the input values by the function input_and_parse(n) 
which takes no. of pages in pdf file as input.
* Then using the re_arrange() function we can get the desired file after rearranging.

## Setup instructions

- We use **pdfrw** library for this script. 
	- To install this library, type `pip install pdfrw` in your terminal.

- To run the script `python3 pdf_reorder_.py` and then enter the required information.

- After running the script it will create a modified file in the same folder as that of the original pdf file.


## Output:
 
A short demo of how the script works

Here We have a pdf file wrong.pdf which has pages in wrong order.

![Image 1](https://i.postimg.cc/zB7VCcMt/1.png)

We can see in the below two images that in the PDF file contents of page 5 are on page 1.
Similar error exists throughout the pdf file

![Image 2](https://i.postimg.cc/T1H1SWTn/2.png)

After entering the required input like the path of the file and the current page which is in the wrong order and the right page no. it should be on seperated by commas ','.
The script runs and a modified file is created.

![Image 3](https://i.postimg.cc/BbvtMCfq/3.png)

We can see the contents of the directory and the modified file will be present there.

![Image 4](https://i.postimg.cc/8ky7sxLs/4.png)

Voila! the pages are in the right order now.

![Image 5](https://i.postimg.cc/zXVVhpk7/5.png)

![image 6](https://i.postimg.cc/VLp5WMG8/6.png)

## Author:

[Mohta Rahul Suresh](https://github.com/Rahul555-droid/)

### Note:

I have also added wrong.pdf file for testing purposes in this directory.
