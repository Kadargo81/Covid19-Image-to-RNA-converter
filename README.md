# Covid19-Image-to-RNA-converter
This is a little program to turn an RGB image representing Covid-19 RNA into a text file containing the original RNA strand.

I made this program after seing the original image [here](https://www.reddit.com/r/dataisbeautiful/comments/mg1cxr/oc_entire_genome_of_covid_virus_sarscov2/):
I wondered if I could reverse engineer the image into the original RNA string as challenge to myself.

This program has many flaws some I am probably not aware of yet, some of the ones I am aware of are:

* This is a static program with hardcoded input and hardcoded variables.
* The image is 519px by 519px but appears to only contain 173px worth of data, because of this...
* The program loops 6x for every pixel in the image 3x across and 3x down.
* The colors of the pixels had to be "found" by me first and then hardcoded, I am sure there is a more elegant solution but I don't know what that is.
* I am aware that the string concatenation method I used can be slow but the program completes in an instant and it was the simplest method I know of.
