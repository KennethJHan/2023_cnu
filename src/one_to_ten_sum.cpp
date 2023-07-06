#include <iostream>

int make_sum(int num)
{
    int result = 0;
    for (int i = 1; i < num + 1; i++)
    {
        result += i;
    }
    return result;
}

int main()
{
    int result = make_sum(10);
    std::cout << result << std::endl; // 55
    return 0;
}
