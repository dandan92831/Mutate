# Mutate

### Task
Use srcML (https://www.srcml.org/) and any XML manipulation library (e.g., XOM: http://www.xom.nu) to write a program transformation tool that inserts a random binary operator replacement operation (e.g., replaces > with ==).

### Data
The original java code file is in "mutated/java1/src/initial/Sample.java"
The mutated java code file is in "mutated/java1/src/after_mutating/Sample.java"

### The flow
Firstly, Randomly replace binary operators in the original file with other operators. This includes the conversion to XML.
```
Run mutated/python1/mutated.py
```
Then we can perform unit tests on the original file and the mutated file to verify the validity of the mutation.
```
Run mutated/java1/src/initial/TestSuite
Run mutated/java1/src/after_mutating/TestSuite
```
