# pyquiz
Hone your Python skills

This quiz set is based on a quiz set from a Ruby SaaS course in the university of Berkley.

### Instructions

1. Clone this repo
2. Make a new branch to answer the quizes
3. Start to code
4. When your in the green and proud of your code push it.
5. Refactor whenever you want and update your branch.
6. After answering see how others did it.

#### Invoke
To test a specific quiz use this shortcut `invoke test --quiz=THEQUIZNUMBER`.
Even shorter `inv test -q THEQUIZNUMBER`.
You can run `inv` to run all.

#### General Objective
Learn new skills in python and the art of refactoring.
By doing these quizes you should learn to work in a more pythonic way.
Answer the questions, then refactor what you did to be more pythonic.
Because refactoring is important here, when refactoring you shouldn't feel obligated 
to `git commit -a --amend`.
Just commit and see where your code starts and how it transforms.

#### Goals By Quiz

##### Quiz 1
The first quiz should let you see different ways of manipulating strings.
Strings can be iterated, sliced, manipulated with regex, and has it's own helpful slew of methods.
To get the most out of this quiz use a python console (ipython suggested) to  try all forms of manipulating strings.

##### Quiz 2
The point of this quiz is learn to reduce if statements.
The soltion can be reduced to one `if else` statement per our two functions.
* Know a python idiom is to ask forgiveness not permission.

##### Quiz 3
Play with Collections/ Iterables.

Lists, strings, dictionaries, comprehension, generators python is strong at iterating
through data.
Useful mentions:
    ''.join
    __builtin__ => Python builtin functions like filter, reduce, sorted, set, plus more
    comprehension => there is comprehension for lists, dicts, generators, and more

##### Quiz 4
Starts you off using classes, inheritance, and properties.

##### Quiz 5
This quiz explores decorators and metaprogramming.

##### Quiz 6
This quiz should be solved in a single iteration.
You will use method chaining, caching, lazy iteration (genarators), higher order
functions, and how to create a DSL.
