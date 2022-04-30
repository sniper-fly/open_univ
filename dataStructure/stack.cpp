#include <stack>
#include <sstream>
#include <iostream>
#include <string>

int main(int argc, char const* argv[]) {
  std::stack<int> s;
  std::string     raw_formula;

  if (argc == 1) {
    raw_formula = "5 1 2 + 4 * + 3 -";
  } else {
    raw_formula = argv[1];
  }

  // split argv with space
  std::istringstream formula(raw_formula);
  std::string        token;

  while (formula >> token) {
    if (! s.empty()) {
      int top = s.top();
    }
    if (token == "+") {
      int a = s.top();
      s.pop();
      int b = s.top();
      s.pop();
      s.push(a + b);
    } else if (token == "-") {
      int a = s.top();
      s.pop();
      int b = s.top();
      s.pop();
      s.push(b - a);
    } else if (token == "*") {
      int a = s.top();
      s.pop();
      int b = s.top();
      s.pop();
      s.push(a * b);
    } else if (token == "/") {
      int a = s.top();
      s.pop();
      int b = s.top();
      s.pop();
      s.push(b / a);
    } else {
      try {
        s.push(std::stoi(token));
      } catch (std::exception& e) {
        std::cerr << "invalid operand" << std::endl;
        exit(1);
      }
    }
  }
  std::cout << s.top() << std::endl;
}
