What The Fun
============
This is repository is an extremely naive aproach to learn and understand concept of coroutines.

So what you have done here?
===========================
I have simply picked up the CPP14.g4 grammar that ships with antlr4, and I have tried to modified it to handle basic coroutine definition based on presence of co\_yield statement (btw. why do they need special co\_return keyword?). Based on that I modify the input source code, so definition of coroutine is translated to an object with corresponding methods. I did not figure out how to easily handle the context, so I decided to pick an easy way and run a new thread. The current coroutine template is not perfect, it is not thread-safe, but it demonstrates how the following code can be easily interpreted and executed:
```
#include <iostream>

int coroutine(int factor) {
    int calls = 1;
    co_yield calls+10*factor;
    calls++;
    co_yield calls+20*factor;
    calls++;
    co_return calls+30*factor;
}


int main()
{
    std::cout << coroutine.invoke(2) << std::endl;
    std::cout << coroutine.resume() << std::endl;
    std::cout << coroutine.resume() << std::endl;
    return 0;
}
```

UPDATE
------
Some experiments with generator wrapper have been made. E.g. examples/fib_generator.cc:
```
#include <iostream>

int fibonacci(int f0, int f1) {
    while(true) {
       co_yield f0;
       f0 += f1;
       std::swap(f0, f1);
    }
}

int main()
{
    int index = 0;
    for(auto fib : generator(fibonacci, 1, 1)) {
        std::cout << fib;
        if (index++ == 10) {
            break;
        } else {
            std::cout << ", ";
        }
    }
    std::cout << std::endl;
    return 0;
}
```
The output is as expected:
```
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
```
