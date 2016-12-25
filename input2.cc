#include <iostream>

int corut(int factor) {
    int calls = 1;
    co_yield calls+10*factor;
    calls++;
    co_yield calls+20*factor;
    calls++;
    co_return calls+30*factor;
}

int corut2(int factor) {
    int calls = 1;
    co_yield calls+100*factor;
    calls++;
    co_yield calls+200*factor;
    calls++;
    co_return calls+300*factor;
}

int main()
{
    std::cout << corut.start(2) << std::endl;
    std::cout << corut2.start(2) << std::endl;
    std::cout << corut.resume() << std::endl;
    std::cout << corut2.resume() << std::endl;
    std::cout << corut.resume() << std::endl;
    std::cout << corut2.resume() << std::endl;
    return 0;
}
