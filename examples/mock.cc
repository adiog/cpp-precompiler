#include <iostream>

int yield_square(int x) {
    co_yield x*x;
}

int return_square(int x) {
    co_return x*x;
}

int main()
{
    for(int x : {1,2,3}) {
        std::cout << yield_square(x) << std::endl;
    }
    for(int x : {1,2,3}) {
        std::cout << return_square(x) << std::endl;
    }
    return 0;
}
