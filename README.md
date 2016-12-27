What The Fun
============
This is repository is an extremely naive aproach to learn and understand concept of coroutines.

Read the open-std n4628.pdf? Besides it is not even there.. who cares..
================================================================
Yeah.. Somehow, I care and I am just curious how it will look like. And true, I have seen the proposal.. And I got the idea of resumable functions, but I have not the slightest idea, what is going on with types.

The types?
==========
Yes, the types. I do not want to see Microsoft messing with types. I simply do not get why the concept of coroutine may be mixed with a function. Why the first paragraph of the proposal has to deal with the main function, while having the concept of coroutine has nothing to do with regular function at all.

Tell me more?
=============
As far as I understand I want a coroutine definition to be translated to an object of a class that has two simple methods invoke(Args &&args...) and resume(). Similary as I look at lambdas - unnamed class with operator()(Args &&args...).

Yes. Of course, did not MS do something like that?
==================================================
It is hard to say. Maybe, but I have not understood their goal yet. As I see now, they have totally polluted the grammar (mixing function and coroutines), they forcing some assumptions on special member functions and so on. I truly want to see a simple object with boosted compilation support for some kind of context handling, proper multithreaded design - then I will be able to write, without any help, an obvious templated generator class wrapper that uses invoke() and resume(), for implementing begin(), end(), next(). I do not see yet why they consider blocking and non-blocking coroutines differently.

What?
=====
Ok, maybe not exactly coroutines itself, but at least there are two separate wrappers generator and async\_generator - I do not see now why I should be writing two different blocks of code, while I simply want to use a regular generator. And yes I can write an additional wrapper, but so far I do not see a point in treating a blocking and non-blocking call differently. Where does it help?

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
    std::cout << coroutine.start(2) << std::endl;
    std::cout << coroutine.resume() << std::endl;
    std::cout << coroutine.resume() << std::endl;
    return 0;
}
```

Hmm.. Sounds interesting.. What can I do to try it?
===================================================
In general, it should work out of the box. Use python3 with virtualenv and antlr4-python3-runtime installed. Also I assume that you have already been using clang-format. There is no need to remind of it, right? I also did not figure out how to handle the preprocessor directives, so anything complex will definitely not work, but some basic stuff can be tested. To run the basic samples, use compiler wrapper:
```
$ ./gcc-wrap.sh -std=c++14 -lpthread input.cc -o coroutine
```

Ok, but what about co\_await?
=============================
I am glad you ask - I have not done anything with it yet. My aproach may be too greedy. I will work on that. If you want give me some hints I will be more than happy to hearing from you how to proceed with the matter.

