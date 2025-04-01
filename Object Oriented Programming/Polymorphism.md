## Introduction

Polymorphism is one of the four fundamental principles of Object-Oriented Programming (OOP). It allows objects of different classes to be treated as objects of a common base class. The main advantage of polymorphism is that it enables code reusability and flexibility in program design.

Polymorphism in C++ can be classified into:

- **Compile-time (Static) Polymorphism**
- **Run-time (Dynamic) Polymorphism**

---

## 1. Compile-time (Static) Polymorphism

Compile-time polymorphism is achieved using **function overloading** and **operator overloading**. It is resolved during compilation.

### Function Overloading

Function overloading allows multiple functions with the same name but different parameters.

#### Example:

```cpp
#include <iostream>
using namespace std;

class Math {
public:
    int add(int a, int b) {
        return a + b;
    }
    
    double add(double a, double b) {
        return a + b;
    }
};

int main() {
    Math obj;
    cout << obj.add(5, 10) << endl;       // Calls int version
    cout << obj.add(3.5, 2.5) << endl;   // Calls double version
    return 0;
}
```

### Operator Overloading

C++ allows operators to be overloaded to work with user-defined data types.

#### Example:

```cpp
class Complex {
public:
    int real, imag;
    Complex(int r, int i) : real(r), imag(i) {}
    
    Complex operator+(const Complex& obj) {
        return Complex(real + obj.real, imag + obj.imag);
    }
};

int main() {
    Complex c1(2, 3), c2(4, 5);
    Complex c3 = c1 + c2;
    cout << "Result: " << c3.real << "+" << c3.imag << "i" << endl;
    return 0;
}
```

---

## 2. Run-time (Dynamic) Polymorphism

Run-time polymorphism is achieved using **function overriding** and **virtual functions**. It is resolved at runtime.

### Function Overriding

A derived class provides a specific implementation of a function that is already defined in its base class.

#### Example:

```cpp
class Parent {
public:
    virtual void show() {
        cout << "Parent class" << endl;
    }
};

class Child : public Parent {
public:
    void show() override {
        cout << "Child class" << endl;
    }
};

int main() {
    Parent* obj;
    Child c;
    obj = &c;
    obj->show();  // Calls Child class method (dynamic binding)
    return 0;
}
```

### Virtual Functions

A virtual function ensures that the function call is dynamically bound.

#### Example:

```cpp
class Base {
public:
    virtual void display() {
        cout << "Base class display" << endl;
    }
};

class Derived : public Base {
public:
    void display() override {
        cout << "Derived class display" << endl;
    }
};

int main() {
    Base* bptr;
    Derived d;
    bptr = &d;
    bptr->display();  // Calls Derived class method
    return 0;
}
```

---

## Key Differences Between Static and Dynamic Polymorphism

|Feature|Static Polymorphism|Dynamic Polymorphism|
|---|---|---|
|Binding|Compile-time|Run-time|
|Achieved By|Function Overloading, Operator Overloading|Function Overriding, Virtual Functions|
|Performance|Faster|Slightly slower due to vtable lookup|
|Flexibility|Less flexible|More flexible|

---

## Advantages of Polymorphism

- **Increases Code Reusability**
- **Enhances Readability and Maintainability**
- **Supports Scalability and Extensibility**
- **Facilitates Object-Oriented Design Principles**

---

## Conclusion

Polymorphism is an essential OOP concept that enables flexibility and scalability in programming. Understanding function overloading, operator overloading, function overriding, and virtual functions is crucial for writing efficient and maintainable C++ programs.