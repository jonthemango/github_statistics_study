# GitHub Statistics Study
An Software Engineering Statistics Study using the GitHub API.

#### Authors
Jon Mongeau
Kerry Gougeon
Isaac Doré 

## Getting Started
Begin by installing the latest version of [Python 3](https://www.python.org/downloads/). 
Clone the repo to the folder where you would like to run it.
Run the command `python main.py`

## Purpose of Study
Our goal is to determine whether large software projects prefer to use statically typed programming languages (like C, C++, Java) or dynamically typed languages (like JavaScript, Python, PHP). It is often said that as software systems increase in _size_ that static type checking becomes a useful feature for eliminating entire classes of bugs, specifically compile-time type errors.

Our interest is to test whether this feature of statically typed languages makes it a more common choice for large software projects. 

## Hypothesis
We hypothosize that more than 50% of open source **large software projects** use statically type programming languages as opposed to dynamically typed languages.

## Definitions
#### Determining whether project is large
We consider a large software project to have over X number of bytes and over Y contributors. The **size** of a project refers to these metrics.

#### Determining whether statically typed or dynamically typed
We will assemble a hash-table which maps the most common languages to either 'static' or 'dynamic'. If a project's top language is not included in our hash-table, the script will ask the user to input the type of the language. The list should be comprehensive and can be found in the file language-types.json. Research into every language has been conducted to assert data is correct.

## Statistical Population
Our statiscical population is large open source software engineering projects.

## Sample Size
```N = 200``` 

## How Data Sampling is conducted
Data is sampled using the public [GitHub API](https://developer.github.com/v4/). 
1. The script queries a **random** project and determines the size of the project. Verify the project id in not already in the sample data set (to preserve independance) 
2. If the project meets the size criteria of a large software project they our added to our sample data set.
3. Continue until N projects are inserted into the sample data set.
4. For each project in the sample data set check its most prominent language.
5. Take that language and check whether statically typed or dynamically typed.
6. Insert the project information into its coresponding data set.
7. The script calculates the sample mean, sample median, sample variance and sample standard deviation.

## Analysis
Our findings found that...

## Final Comments 
- Did your method of sampling result in a random sample? 
- If your sample was not a random sample what sorts of measures could you take if you were to
do this project again, to get a random sample?
- Is your hypothesis true or not? Based on the experiment, would it be appropriate to write a
revised hypothesis (“about 15% of cars in Hampstead go through yellow lights.”) 
- Comment on whether you think your results can be extrapolated to draw more general
conclusions, perhaps on wider populations. State your opinion and then back it up with well
thought out reasons. 


