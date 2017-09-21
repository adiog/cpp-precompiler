#include <iostream>

int fibonacci(int f0=1, int f1=1) {
    while(true) {
       co_yield f0;
       f0 += f1;
       std::swap(f0, f1);
    }
}

int main()
{
    int index = 0;
    for(auto fib : generator(fibonacci)) {
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
