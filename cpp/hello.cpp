#include <iostream>
#include <unordered_map>

using namespace std;

int main()
{
    unordered_map<string, string> m;
    m["hello"] = "hey. cout is goofy";
    cout << m["hello"] << endl;
    return 0;
}
