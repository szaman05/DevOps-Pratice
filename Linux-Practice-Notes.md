# Linux Important Commands Practice Notes:

## 5/28/2022:

### \# cut commad:

<img src="../images/Linux-Practice-Notes/media/image1.png"
style="width:6.5in;height:3.47917in" />

### \# grep command:

Problem 1 : Write a command to count the number of code lines in a shell
script:

Solution: grep -Ev '^#\|^$' mdConvert.sh \| wc -l

<img src="../images/Linux-Practice-Notes/media/image2.png"
style="width:6.04167in;height:3.51042in" />

# 5/30/2022:

#### \# sed command:

Q: Replace a variable name globally inside a shell script.

A:

-   Change and Display output to screen: sed 's/docxName/docuName/g'
    mdConvert.sh

-   Change and Insert into the file: sed -i 's/docxName/docuName/g'
    mdConvert.sh

-   Change 1<sup>st</sup> occurrence of every line only: sed
    's/docxName/docuName/1'
    mdConvert.sh<img src="../images/Linux-Practice-Notes/media/image3.png"
    style="width:6.5in;height:3.20486in" />

Q: show a script from line 12 to 18 only.

A:

-   sed -n 12,18p mdConvert.sh

<img src="../images/Linux-Practice-Notes/media/image4.png"
style="width:5.71875in;height:1.44792in" />

Q: show a script discard/hide line 12 to 18.

A:

-   sed 12,18d mdConvert.sh
    <img src="../images/Linux-Practice-Notes/media/image5.png"
    style="width:6.5in;height:5.08194in" />
