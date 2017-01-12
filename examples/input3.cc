#include <iostream>
#include <utility>
std::pair<int, int> corut(int factor) {
    int calls = 1;
    co_yield {calls, 10*factor};
    calls++;
    co_yield {calls, 20*factor};
    calls++;
    co_return {calls, 30*factor};
}

int main()
{
    auto r1 = corut.invoke(2);
    std::cout << r1.first << " " << r1.second << std::endl;
    auto r2 = corut.resume();
    std::cout << r2.first << " " << r2.second << std::endl;
    auto r3 = corut.resume();
    std::cout << r3.first << " " << r3.second << std::endl;
    return 0;
}
