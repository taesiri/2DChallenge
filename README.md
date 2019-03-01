# 2D Pattern Matching

Create a program that stores a set of 2D patterns, which can be matched against a 2D matrix of variable size. A match is found only if the input matrix contains exactly one pattern where both values and positions are equal. The program should take an input matrix as predicate and return the name of first matched pattern. [Full problem statement](https://gist.github.com/pomle/10d7d54fb00d50fe4a329e9a2bd49c90).

## About the Problem

When I first saw this problem, I thought it is asking for a general 2D pattern matching with `'.'` char as a wildcard that can match anything. As I was familiar with Signal Processing, I knew that performing a ``Cross Correlation`` with the pattern as ``Mask`` on the input matrix followed by a linear scan to find special values in the output will instantly solve the problem. The only preprocessing that this algorithm need is to swap each character in the matrix with a numerical value corresponding to that character (One simply can use a Hash function). From the performance point of view, both ``Convolution`` and ``Cross Correlation`` operators might seem bad, but these operators are very well known and almost all implementations of these functions, utilize the ``SIMD`` capabilities of the processor; thus they are very efficient.

After carefully reviewing the problem and test cases, I concluded that the question is asking for a much simpler version of 2D pattern matching. I assumed that the output of the algorithm should be nothing when the input matrix contains extra characters, even one single one.

## My Approach

I decided to use my numpy magical skill to solve this problem. First I eliminate all the empty rows and columns and then I try to match the remaining entities in the matrix with each pattern.

```python
# Step 1
matrix = matrix[~np.all(matrix=='.', axis=1)] # Removing empty rows
matrix = matrix[:, ~np.all(matrix=='.', axis=0)] # Removing empty columns
```

```python
#Step 2
sliceM = sliceM.reshape(-1)
pattern = pattern.reshape(-1)
return all([x==y for x, y in zip(sliceM, pattern)])
```

Since the problem description doesn't talk about the number of patterns, size of them and the maximum size of the input matrix, it is hard to optimize this code.

## Running

The ``run.py`` is the starting point of this program. Just run ``python run.py`` and navigate your browser to ``http://localhost:10100/``.

## Pattern Matching

For performing pattern matching, you should send a ``POST`` request with appropriate ``JSON`` file as input to ``localhost:10100/simple`` endpoint. See below for input format.

## Input format

This program expects a ``JSON`` object as input. This object contains one key, ``data`` which stores a list of list, containing all elements in the input Matrix row by row. See the following for sample input.

```javascript
{ "data" :
    [[".", ".", "."],
    [".", ".", "."],
    [".", ".", "."]]
}
```