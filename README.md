# nth_fibonacci
A python program that returns the nth number in a fibonacci sequence

*Note: It is recommended to use pyhton3.*

## How to run the program:
1.  In terminal or command prompt navigate to the directory where the python is located using the 'cd <dir-name>' command(s)
2.  run the program by typing:
    ```
    python3 fibonacci.py
    ```
    Note: If you use any different alias for python3, you can use that as well. 
    I have an alias 'py' for 'pyhton3' so for me the following works as well:
    ```
    py fibonacci.py
    ```
3.  Enter one number, large or small and press Enter. 
    Then for windows Press Control-Z or for Mac/Linux press Control-d and enter.
    Then you should see the result printed in a new line.
  
## Algorithm of the program:
The time complexity is O(n)
The space complexity is O(1)
  
Here the program uses a loop instead of recursion calls to the method itself, this way it saves storing recursion call values in the class stack. It doesn't need any data structures to store the values as it simply uses a previous and current variable and iteratively calculated the fibonacci sequence nth value and stores it there, saving on space complexity. 
  
Another possible solution is to use memiozation and store each fibonacci value in a hash table, but that would require storage om the memory and thus increase the space complexity to O(n), which I'm trying to avoid. 

## License
[MIT](https://choosealicense.com/licenses/mit/)
