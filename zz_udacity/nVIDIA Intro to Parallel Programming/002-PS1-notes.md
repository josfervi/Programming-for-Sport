#CUDA Pixels#

represented as a unsigned char 4 struct

struct uchar4{
    //red
    unsigned char x;
    // green
    unsigned char y;
    // blue
    unsigned char z;
    // alpha - transperancy
    unsigned char w;
}

#RGB to GreyScale#

##option 1##
- take their average (I = intensity)
- I = (R + G + B)/3

##option 2##
- take into account the human visual system
(we are sensitive to green the most, red second, and blue third)
- I = .299f * R + .587 * G + .114f * B

//Notice the trailing f's on the numbers which indicate that they are 
//single precision floating point constants and not double precision
//constants.