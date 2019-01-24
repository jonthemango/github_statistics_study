# GitHub Statistics Study
An Software Engineering Statistics Study using the GitHub API.

## Abstract
Our team conducted a statistical survey on the language type preferences of large software projects using a proprietary algorithm that queries the GitHub API. We found that 56% of large software projects prefer explicitly typed languages over implicitly typed languages.


#### Authors and Affiliations
[Jon Mongeau](https://github.com/jonthemango)

[Kerry Gougeon](https://github.com/Kerry-G)

[Isaac Doré](https://github.com/Swess)

[Concordia University](https://www.concordia.ca/)

## Getting Started
Begin by installing the latest version of [Python 3](https://www.python.org/downloads/). 
Clone the repo to the folder where you would like to run it.
Run the command `python main.py`

## Purpose of Study
Our goal is to determine whether large software projects prefer to use statically typed programming languages (like C, C++, Java) or dynamically typed languages (like JavaScript, Python, PHP). It is often said that as software systems increase in _size_ that static type checking becomes a useful feature for eliminating entire classes of bugs, specifically compile-time type errors.

Our interest is to test whether this feature of statically typed languages makes it a more common choice for large software projects.

## Hypothesis
We hypothesize that more than 50% of open source **large software projects** use statically type programming languages as opposed to dynamically typed languages.

## Definitions
#### Determining whether project is large
We consider a large software project to have over 1,000,000 bytes and over 10 contributors. The size of a project refers to these metrics.

#### Determining whether statically typed or dynamically typed
We will assemble a hash-table which maps the most common languages to either 'explicit' or 'implicit'. The list should be comprehensive and can be found in the file `language-types.json`. Research into every language has been conducted to assert that data is correct. Language names were taken from `linguist` provided by Github.

## Statistical Population
Our statistical population is the large open source software engineering projects found on Github.

## Sample Size
```N = 50``` 

## How Data Sampling is conducted
Data is sampled using the public [GitHub API](https://developer.github.com/v3/). 
1. The script queries a **random** project and determines the size of the project. Verify the project id in not already in the sample data set (to preserve independence) 
2. If the project meets the size criteria of a large software project they our added to our sample data set.
3. Continue until N projects are inserted into the sample data set.
4. For each project in the sample data set check its most prominent language.
5. Take that language and check whether statically typed or dynamically typed.
6. Insert the project information into its corresponding data set.
7. The script calculates the sample mean, sample median, sample variance and sample standard deviation.

## Analysis
Our findings found that 28 of the 50 projects that were inspected were using explicitly typed languages.
For more information about the math that we used to determine this please refer to https://drive.google.com/file/d/1lbfze5P0Y2RtJqXF_VUFQSkdVS3xtguR/view?usp=sharing



