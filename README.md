# SUMMARY
Was bored and wanted to see if I could remeber how to do this
by hand. It's a basic Huffman coding algorithm that can be used
for compression and it encodes characters into bits. The more frequently
the character in the alphabet is used in the string the smaller the
number of bits needed to represent it. Huffman algorithm ensures that
you always have a unique encoding and that it is almost as close to entropy as possible while still maintaining unique decodability. Not always the fastest and best option for text compression though.

## HOW THE ALGO WORKS

You start with each unique character and either its percentage of occuring in the string or its frequency in the string. You then take the two most uncommon characters in the alphabet and essentially merge them together along with their probabilities/frequencies. So if you have the char 'a' and 'b' that are the two most uncommon characters in the alphabet and they each have a .05 probability of occuring then you "merge" them together and now "ab" is treated as a singular entity and when encoded these characters will differ by a single bit. Essentially meaning one is on the left side of the tree representing a 0 and the other on the right representing a 1. We then continue merging until their are only 2 of these either characters in the alphabet or merged characters left. We then work our way down the tree. Since We are not doing this by hand the easiest way to do this computationally is to use recursion where each Node holds a left and right child representing those two branches and we decompose all the merges working our way down so at the bottom of the tree will be our least common characters. The reason we group them together and can't just do the obvious of building a regular tree is this problem of unique decodability. If we have a string aab and we want to encode that as a series of bits we have to ensure that when we decode from bits we get the same result so we must ensure that we get the same number of characters as well as the same characters. For example if we had a string "aacb" and a was encoded as 0 and c was encoded as 00 and b 1 we couldn't have that because our encoding would be 00001 which could be decoded as aaaab or ccb etc..

![image](https://github.com/phagmaier/huffmancode/assets/97493681/564a916f-5f54-421e-ab6c-9536c3e4109c)
