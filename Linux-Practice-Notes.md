# Linux Important Commands Practice Notes:

## 5/28/2022:

**<u>\# cut commad:</u>**

<img src="./images/Linux-Practice-Notes/media/image1.png"
style="width:6.5in;height:3.47917in" />

\# grep command:

Problem: Write a command to count the number of code lines in a shell
script:

Solution: grep -Ev '^#\|^$' mdConvert.sh \| wc -l
