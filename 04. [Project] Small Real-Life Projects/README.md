# 04. [Project] Small Real-Life Projects

- [04. [Project] Small Real-Life Projects](#04-project-small-real-life-projects)
  - [Bookshelf](#bookshelf)
    - [Problem](#problem)
    - [Solution](#solution)
  - [Phone Book](#phone-book)
    - [Problem](#problem-1)
    - [Solution](#solution-1)
  - [Date and Time](#date-and-time)
    - [Problem](#problem-2)
    - [Solution](#solution-2)
  - [Web Address](#web-address)
    - [Problem](#problem-3)
    - [Solution](#solution-3)
  - [Stocks](#stocks)
    - [Problem](#problem-4)
    - [Solution](#solution-4)

## Bookshelf

### Problem

The file contains 30 books and each line in the file contains the name of the author, the book title and the publishing year separated by a semicolon.

```
Terry-Thomas;Filling the Gap;1959
Harpo Marx;Harpo Speaks;1961
Charlie Chaplin;My Autobiography;1964
Moe Howard;Moe Howard and the Three Stooges, AKA I Came, I Stooged, I Conquered (released posthumously);1974
Sid Caesar;Where Have I Been?;1982
...
```

Solve the exercises below:

1. Match All The Authors Whose Book Titles are Shorter Than 25 Characters
2. Match All The Authors who Published Their Books Starting with Year 2000

### Solution

```python
import re

# read file content to string
file = open(r"bookshelf.txt")
string = file.read()

# 01. Match All The Authors Whose Book Titles are Shorter Than 25 Characters
result = re.findall(r".+?;(.{1,25});.+?", string)

# 02. Match All The Authors who Published Their Books Starting with Year 2000
result = re.findall(r"(.+?);.+?;20[0-9][0-9]", string)
```

<br/>
<div align="right">
  <b><a href="#04-project-small-real-life-projects">[ ↥ Back To Top ]</a></b>
</div>
<br/>

## Phone Book

### Problem

The file contains a list of 50 first and last names along with their phone numbers. Each entry is on separate line and each line starts with the first and the last name of the person followed by a tab character then a space and then the phone number itself.

```
Zion Martinez	(631) 472-4834
Moriah Velez	(201) 684-8134
Jenna Peterson	(355) 554-9561
Ayaan Novak	(812) 883-7304
Elena Sosa	(504) 478-1208
...
```

Solve the exercises below:

1. Get the Last Name and Phone Number of All the People Having an Area Code Ends with 0.
2. Get the Area Code of Each Phone Number that Ends with 7.

### Solution

```python
import re

# read file content to string
file = open(r"phonebook.txt")
string = file.read()

# 01. Get the Last Name and Phone Number of All the People Having an Area Code Ends with 0
result = re.findall(r".+ (.+)\t\(\d\d0\)\s(.+)", string)

# 02. Get the Area Code of Each Phone Number that Ends with 7.
result = re.findall(r".+\t\((\d{3})\)\s.{7}7", string)
```

<br/>
<div align="right">
  <b><a href="#04-project-small-real-life-projects">[ ↥ Back To Top ]</a></b>
</div>
<br/>

## Date and Time

### Problem

We're going to use the file that contains log messages from a Windows computer.

```
Level Date and Time Source Event ID Task Category
Critical 1/27/2020 8:19:22 AM Microsoft-Windows-Kernel-Power 41 (63) The system has rebooted without cleanly shutting down first. This error could be caused if the system stopped responding, crashed, or lost power unexpectedly.
Critical 1/26/2020 10:09:54 AM Microsoft-Windows-Kernel-Power 41 (63) The system has rebooted without cleanly shutting down first. This error could be caused if the system stopped responding, crashed, or lost power unexpectedly.
Critical 1/25/2020 10:12:58 AM Microsoft-Windows-Kernel-Power 41 (63) The system has rebooted without cleanly shutting down first. This error could be caused if the system stopped responding, crashed, or lost power unexpectedly.
Error 1/25/2020 10:03:44 AM Microsoft-Windows-WER-SystemErrorReporting 1001 None The computer has rebooted from a bugcheck.  The bugcheck was: 0x0000009f (0x0000000000000003, 0xffff810ec8c31060, 0xfffff80716e687b0, 0xffff810ed30e3c20). A dump was saved in: C:\WINDOWS\MEMORY.DMP. Report Id: 7fcfb77c-e4b0-4e3b-b4c7-af9dafdafc7f.
Error 1/25/2020 10:03:29 AM TPM 15 None The device driver for the Trusted Platform Module (TPM) encountered a non-recoverable error in the TPM hardware, which prevents TPM services (such as data encryption) from being used. For further help, please contact the computer manufacturer.
...
```

Solve the exercises below:

- Search All the Log Entries that are Critical and were Generated Between the 11th and 16th Day of the Month of January 2020.

### Solution

```python
import re

# read file content to string
file = open(r"logs.txt")
string = file.read()

# Search All the Log Entries that are Critical and were Generated Between the 11th and 16th Day of the Month of January 2020.
re.findall(r"Critical 1/1[1-6]/2020 .+ [A-Z]{2} (.+?) \d+", string)
```

<br/>
<div align="right">
  <b><a href="#04-project-small-real-life-projects">[ ↥ Back To Top ]</a></b>
</div>
<br/>

## Web Address

### Problem

The file contains information about the most popular websites on the Internet.

```
Site	Domain	Alexa top 50 global sites	SimilarWeb top 50 sites	Type	Principal country/territory
Google	https://google.com	1 (Steady)	1 (Steady)	Internet services and products	United States U.S.
YouTube	https://youtube.com	2 (Steady)	2 (Increase1)	Video sharing	United States U.S.
Tmall	https://tmall.com	3 (Steady)	82 (Steady)	Online shopping	China China
Facebook	https://facebook.com	4 (Increase3)	3 (Decrease1)	Social networking	United States U.S.
Baidu	https://baidu.com	5 (Decrease1)	4 (Increase11)	Internet-related services and products	China China
...
```

Solve the exercises below:

- Match All the URLs that are Associated with Online Shopping Services

### Solution

```python
import re

# read file content to string
file = open(r"web.txt")
string = file.read()

# Match All the URLs that are Associated with Online Shopping Services
result = re.findall(r".+\s+(http.*://.+\.\w{2,})\s.+Online shopping.+", string)
```

<br/>
<div align="right">
  <b><a href="#04-project-small-real-life-projects">[ ↥ Back To Top ]</a></b>
</div>
<br/>

## Stocks

### Problem

The file contains various pieces of informaiton about 30 U.S. stocks such as the company name, the average volume begin traded, the revenue of each company and the P/E ratio.

```
Name	        AverageVolume	Revenue	    P/E Ratio
3M              5.03M	        32.14B	    18.74
Alphabet C	    2.41M	        161.86B	    26.01
Amazon.com	    6.01M	        280.52B	    103.18
Apple	        51.02M	        267.68B	    22.34
Boeing	        23.63M	        84.82B		20.31
...
```

Solve the exercises below:

- Match All the Company Names and Their Revenue, as long as the Revnue is Less Than 50 Billion U.S. dollars.

### Solution

```python
import re

# read file content to string
file = open(r"stocks.txt")
string = file.read()

# Match All the Company Names and Their Revenue, as long as the Revnue is Less Than 50 Billion U.S. dollars.
result = re.findall(r"(.+?)\s+[0-9]+\.[0-9]+M\s+[1-4][0-9]\.[0-9]+B\s+[0-9]+\.[0-9]+", string)
```

<br/>
<div align="right">
  <b><a href="#04-project-small-real-life-projects">[ ↥ Back To Top ]</a></b>
</div>
<br/>