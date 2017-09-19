#include <iostream>

int coroutine(int factor) {
    for(int i = 0; i < 7; i++) {
        co_yield i*factor;
    }
    while(true) {
       co_yield 7*factor;
    }
}

int main()
{
    int index = 0;
    for(auto x : generator(coroutine, 2)) {
        std::cout << x << std::endl;
        if (index++ == 42) {
            break;
        }
    }
    return 0;
}
