## Introduction

C++ is an Object-Oriented Programming (OOP) language that revolves around the concept of **classes and objects**. A **class** is a blueprint for creating objects, while an **object** is an instance of a class. This allows for better organization, reusability, and encapsulation of data.

---

## 1. Defining a Class in C++

A class is defined using the `class` keyword, followed by the class name and a pair of curly braces `{}` containing its members (variables and methods).

### Example:

```cpp
#include <iostream>
using namespace std;

class Car {
public:
    string brand;
    int year;
    void display() {
        cout << "Brand: " << brand << ", Year: " << year << endl;
    }
};

int main() {
    Car myCar; // Creating an object
    myCar.brand = "Tesla";
    myCar.year = 2023;
    myCar.display();
    return 0;
}
```

---

## 2. Access Specifiers

C++ provides three access specifiers to control access to class members:

- **`private`**: Accessible only within the same class.
- **`protected`**: Accessible within the same class and derived classes.
- **`public`**: Accessible from anywhere.

### Example:

```cpp
class Example {
private:
    int privateVar;

protected:
    int protectedVar;

public:
    int publicVar;
};
```

---

## 3. Creating Objects in C++

An **object** is an instance of a class, which allows access to class members based on access specifiers.

### Example:

```cpp
class Student {
public:
    string name;
    int age;
};

int main() {
    Student student1;
    student1.name = "Alice";
    student1.age = 20;
    cout << "Student Name: " << student1.name << ", Age: " << student1.age << endl;
    return 0;
}
```

---

## 4. Constructors and Destructors

### **Constructors**

A constructor is a special method that gets called automatically when an object is created.

#### Example:

```cpp
class Person {
public:
    string name;
    Person(string n) { // Constructor
        name = n;
    }
    void show() {
        cout << "Name: " << name << endl;
    }
};

int main() {
    Person p1("John");
    p1.show();
    return 0;
}
```

### **Destructors**

A destructor is used to clean up resources and is called automatically when an object goes out of scope.

#### Example:

```cpp
class Sample {
public:
    ~Sample() {
        cout << "Destructor called" << endl;
    }
};

int main() {
    Sample obj;
    return 0;
}
```

---

## 5. Member Functions and Objects

Member functions can be defined inside or outside the class.

### **Inside Class Definition:**

```cpp
class Example {
public:
    void show() {
        cout << "Hello from Example class!" << endl;
    }
};
```

### **Outside Class Definition:**

```cpp
class Example {
public:
    void show();
};

void Example::show() {
    cout << "Hello from Example class!" << endl;
}
```

---

## 6. `this` Pointer

The `this` pointer is an implicit pointer available in all non-static member functions of a class.

#### Example:

```cpp
class Example {
public:
    int x;
    void setX(int x) {
        this->x = x;
    }
};
```

---

## 7. Static Members

### **Static Variables**

Static members belong to the class rather than individual objects.

#### Example:

```cpp
class Counter {
public:
    static int count;
    Counter() {
        count++;
    }
};
int Counter::count = 0;
```

### **Static Functions**

Static functions can access only static members.

```cpp
class Demo {
public:
    static void show() {
        cout << "Static function called" << endl;
    }
};
```

---

## Conclusion

C++ classes and objects are the foundation of OOP, enabling modularity, reusability, and data encapsulation. Mastering these concepts is essential for writing scalable and maintainable C++ programs.