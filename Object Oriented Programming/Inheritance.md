## Introduction

Inheritance is one of the core principles of Object-Oriented Programming (OOP) that allows one class to acquire the properties and behavior of another class. It promotes code reusability, modularity, and hierarchy in program design.

## Why Use Inheritance?

- **Code Reusability:** Avoids redundant code by reusing existing functionalities.
- **Modularity:** Enhances maintainability and scalability.
- **Extensibility:** Allows easy modification and extension of functionalities.
- **Hierarchy Representation:** Models real-world relationships.

## Types of Inheritance in C++

C++ supports different types of inheritance:

### 1. **Single Inheritance**

A derived class inherits from a single base class.

#### Example:

```cpp
#include <iostream>
using namespace std;

class Parent {
public:
    void display() {
        cout << "This is the Parent class" << endl;
    }
};

class Child : public Parent {
};

int main() {
    Child obj;
    obj.display(); // Inherits method from Parent
    return 0;
}
```

### 2. **Multiple Inheritance**

A derived class inherits from more than one base class.

#### Example:

```cpp
class A {
public:
    void showA() {
        cout << "Class A" << endl;
    }
};

class B {
public:
    void showB() {
        cout << "Class B" << endl;
    }
};

class C : public A, public B {
};

int main() {
    C obj;
    obj.showA();
    obj.showB();
    return 0;
}
```

### 3. **Multilevel Inheritance**

A derived class inherits from another derived class.

#### Example:

```cpp
class Grandparent {
public:
    void showGrandparent() {
        cout << "Grandparent class" << endl;
    }
};

class Parent : public Grandparent {
public:
    void showParent() {
        cout << "Parent class" << endl;
    }
};

class Child : public Parent {
public:
    void showChild() {
        cout << "Child class" << endl;
    }
};

int main() {
    Child obj;
    obj.showGrandparent();
    obj.showParent();
    obj.showChild();
    return 0;
}
```

### 4. **Hierarchical Inheritance**

Multiple derived classes inherit from a single base class.

#### Example:

```cpp
class Parent {
public:
    void show() {
        cout << "Parent class" << endl;
    }
};

class Child1 : public Parent {
};

class Child2 : public Parent {
};

int main() {
    Child1 obj1;
    Child2 obj2;
    obj1.show();
    obj2.show();
    return 0;
}
```

### 5. **Hybrid (Virtual) Inheritance**

A combination of two or more types of inheritance. Often resolved using **virtual inheritance** to avoid duplication issues.

#### Example:

```cpp
class A {
public:
    void showA() {
        cout << "Class A" << endl;
    }
};

class B : virtual public A {
};

class C : virtual public A {
};

class D : public B, public C {
};

int main() {
    D obj;
    obj.showA(); // Avoids duplication using virtual inheritance
    return 0;
}
```

## Access Specifiers in Inheritance

The access level of inherited members depends on the mode of inheritance:

|Base Class Member|`public` Inheritance|`protected` Inheritance|`private` Inheritance|
|---|---|---|---|
|`public`|Public|Protected|Private|
|`protected`|Protected|Protected|Private|
|`private`|Not Inherited|Not Inherited|Not Inherited|

## Real-World Example

A `Vehicle` class can be inherited by `Car` and `Bike` classes to reuse common attributes like speed and fuel capacity.

```cpp
class Vehicle {
protected:
    int speed;
public:
    void setSpeed(int s) {
        speed = s;
    }
    void showSpeed() {
        cout << "Speed: " << speed << " km/h" << endl;
    }
};

class Car : public Vehicle {
};

class Bike : public Vehicle {
};

int main() {
    Car myCar;
    myCar.setSpeed(120);
    myCar.showSpeed();
    return 0;
}
```

## Conclusion

Inheritance is a powerful OOP concept that promotes code reuse, reduces redundancy, and models real-world relationships efficiently. Understanding different types of inheritance and access control ensures better program design and maintainability.