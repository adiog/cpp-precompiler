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
