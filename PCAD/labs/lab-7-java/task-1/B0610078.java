// SALOHIDDIN USMONALIYEV
// B0610078 
// LAB 7

// TASK 1
// A school library wants to know how much of each book a student has read.
// Write your first Java class with fields, a constructor, this and toString(). Put the class
// Book and the class Main (with the main method) in one file Main.java.

// class Book {
//     String title;
//     int pages;
//     int pagesRead;

//     Book(String title, int pages) {
//         this.title = title;
//         this.pages = pages;
//         pagesRead = 0;
//     }

//     void read(int count) {
//         this.pagesRead += count;
//     }
//     @Override
//     public String toString() {
//         return title + ": " + pagesRead + "/" + pages + " pages";
//     }
// }
// public class Main {
//     public static void main(String[] args) {
//         Book firstbook = new Book("Java Basics", 200);
//         Book secondbook = new Book("Algorithms", 350);

//         firstbook.read(30);
//         firstbook.read(20);
//         secondbook.read(100);
//         System.out.println(firstbook);
//         System.out.println(secondbook);

//     }
// }



// TASK 2
// A company has employees. Every employee has a name and a salary and can
// print information about himself, but managers and developers have extra data. Use
// inheritance, so you do not repeat the same code.

// class Employee {
//     String name;
//     double salary;

//     Employee(String name, double salary) {
//         this.name = name;
//         this.salary = salary;
//     }
//     void info() {
//         System.out.println(name + " earns " + salary);
//     }
// }

// class Manager extends Employee {
//     double bonus;

//     Manager(String name, double salary, double bonus) {
//         super(name, salary);
//         this.bonus = bonus;
//     }

//     @Override 
//     void info() {
//         super.info();
//         System.out.println("Bonus: " + bonus);
//     }
// }

// class Developer extends Employee {
//     String language;
//     Developer(String name, double salary, String language) {
//         super(name, salary);
//         this.language = language;
//     }
//     @Override
//     void info() {
//         System.out.println(name + " writes " + language + " and earns " + salary);
//     }
// }
// public class Main {
//     public static void main(String[] args) {
//         Employee[] employees = {
//             new Employee("Ali", 800),
//             new Manager("Vali", 1500, 300),
//             new Developer("Dilnoza", 1200, "Java")
//         };
//         for (Employee e : employees) {
//             e.info();
//         }
//     }
// }



//TASK 3
// The university club wants a small Java program that asks a new member a few
// questions and prints a student card. You will use the Java types, the Scanner class
// and System.out.println().

// import java.util.Scanner;
// public class Card {
//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);
//         System.out.print("Enter your name: ");
//         String name = scanner.nextLine();
//         System.out.print("Enter your city: ");
//         String city = scanner.nextLine();
//         System.out.print("Enter your age: ");
//         int age = scanner.nextInt();
//         System.out.print("Enter your gpa: ");
//         double gpa = scanner.nextDouble();

//         int birthyear = 2026 - age;

//         System.out.println("---Student Card---");
//         System.out.println(name + " lives in "+ city);
//         System.out.println("Age: " + age);
//         System.out.println("GPA: " + gpa);
//         System.out.println("Year of birth: " + birthyear);
//         System.out.println("In 5 years " + name + " will be " + (age + 5));

//     }
// }


// TASK 4
// An online shop accepts different kinds of payment. Every payment must
// calculate its fee, but each kind calculates it in its own way. Use an abstract class and
// an interface.

// abstract class Payment {
//     String name;
//     Payment(String name) {
//         this.name = name;
//     }
//     abstract double fee(double amount);

//     void pay(double amount) {
//         double total = amount + fee(amount);
//         System.out.println(name + ": " + total);
//     }


// }


// interface Discountable {
//     double discount(double amount);
    
// }

// class CardPayment extends Payment implements Discountable {
//     CardPayment() {
//         super("Card");
//     }
//     @Override
//     double fee(double amount) {
//         return amount * 0.02;
    
//     }

//     @Override
//     public double discount(double amount) {
//         return amount * 0.05;
//     }
// }
// class CashPayment extends Payment {
//     CashPayment() {
//         super("Cash");
//     }

//     @Override
//     double fee(double amount) {
//         return 0;
//     }
// }

// public class Main {
//     public static void main(String[] args) {
//         Payment[] payments = {
//             new CardPayment(),
//             new CashPayment()
//         };

//         for (Payment payment : payments) {
//             payment.pay(1000);
//         }
//         CardPayment card = new CardPayment();
//         System.out.println("Discount: " + card.discount(1000));
//     }
// }



// TASK 5
// A smart home has different devices. Some devices can be switched on and
// off, some can also be charged. Use interfaces: one class can implement several
// interfaces


interface Switchable {
    void turnOn();
    void turnOff();
}
interface Chargeable {
    void charge(int percent);
}


class Lamp implements Switchable {
    @Override
    public void turnOn() {
        System.out.println("Lamp is on");
    }

    @Override
    public void turnOff() {
        System.out.println("Lamp is off");
    }
}




class Phone implements Switchable, Chargeable {
    int battery = 20;
    @Override
    public void turnOn() {
        System.out.println("Phone is on, battery: " + battery + "%");
    }
    @Override
    public void turnOff() {
        System.out.println("Phone is off");
    }
    @Override
    public void charge(int percent) {
        battery += percent;
    }
}

public class Main {
    public static void main(String[] args) {
        Switchable[] devices = {
            new Lamp(),
            new Phone()
        };
        for (Switchable device : devices) {
            device.turnOn();
        }
        Phone phone = new Phone();
        phone.charge(50);
        phone.turnOn();
        phone.turnOff();
    }
}