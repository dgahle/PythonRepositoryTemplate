# Python Repository Template

TODO: Give a short introduction of your project. Let this section explain the objectives or the motivation behind this project. 

Step:
1. Set up the repo/project
2. Develop!

__Requesting changes:__ Raise an issue on the GitHub repository page and describes the error or the desired functionality, 
ideally with test data that can be used to make tutorials and unit tests.

## Getting Started
TODO: Guide users through getting your code up and running on their own system. In this section you can talk about:
1.	Installation process
2.	Software dependencies
3.	Latest releases
4.	API references

## Build and Test
TODO: Describe and show how to build your code and run the tests. 

## Python Environment

Python 3.8 is used here so there is forward compatibility up to Python 3.12

## How to Contribute

The following steps describe how to add new functionality to the repo:
1. Raise an issue in this report that describes the functionality you want to add, 
2. branch from `dev` with the name convention `feature\<descriptive-branch-name>`
3. Add code to `feature\<descriptive-branch-name>`
4. Create a (draft) pull request with `dev` as the target (link the PR is the corresponding issue)

In the review the scripts will be reviewed against the coding standards below, passing unit tests that verify the 
functionality, and updated documentation and tutorials. 
Assistance can be provided if you are unfamiliar with implementing some of these standards. 

### Coding Standards

As the code should be easy if not trivial for others to reuse blind there are a series of standards that example 
scripts need to meet:
- Descriptive programming style - As in variable, function, and class names should describe what they are/do.
- Type hinting - All declared variables should have the types declared alongside it.
- Well commented - The example should be understandable from the comments with only brief references to the code.
- Doc string - Comment blocks at the beginning of functions and class methods that describes what the function/method 
does and lists the inputs, outputs, and exceptions that could be raised. This is important for the documentation of the 
repository.
- An example of using the function - This will be used for automated testing to ensure functionality is maintained with
changes in the repo and to write the tutorial in the document.

### Testing

Unit tests should be written to verify that the examples meet their objectives.  
GitHub Actions are used to automate the running of the unit tests as a condition for merging into the main and dev 
branch.