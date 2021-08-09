# collatz
Visualising the Collatz conjecture with Python

## Inspiration

This Veritasium video: https://www.youtube.com/watch?v=094y1Z2wpJg

## Live demo

Check out the [live demo here](https://htmlpreview.github.io/?https://raw.githubusercontent.com/patrickbrett/collatz/main/output.html)!

## What is this?

This program visualises the the following algorithm, applied to each number from 1 to 100:

1. If the number is even, halve it.
2. If the number is odd, triple it and add one.
3. Repeat until the result is 1.

This has been shown to work for every number up to around 10^20, more than the number of grains of sand on Earth. However, nobody can prove that it works for *all* numbers, and so it remains a conjecture.

The interactive demo shows that every number in the range tested (1 to 100) clearly follows this rule - following the arrows from any point, every number eventually reaches back to 1.

Running this on larger samples (say, up to 5000) and generating full interactive visualisations is possible but quite slow. I've visualised a couple of these below:

## Example visualisations

100 nodes:

![100 Node visualisation](https://raw.githubusercontent.com/patrickbrett/collatz/main/100_nodes.png)

5000 nodes:

![5000 Node visualisation](https://raw.githubusercontent.com/patrickbrett/collatz/main/5000_nodes.png)

## How to use

Clone and run `python src/collatz.py` to generate the output yourself to `output.html`. The depth can be customised by changing the `COLLATZ_DEPTH` constant at the top of the `collatz.py` file.

Note that you will need to run `pip install -r requirements.txt` first in order to load the relevant dependencies.

The default depth is 100, meaning numbers up to 100 will be visualised as a graph.

The largest chain found and its full path will also be output when the program is run.
