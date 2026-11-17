// B0610078
// SALOHIDDIN USMONALIYEV
// Lab 8

// TASK 1
// A teacher keeps the marks of a group in an array. Write Java methods that
// calculate the average mark, the best mark and the number of students who passed.

// class Main {
//     static double average(int[] a) {
//         int sum = 0;
//         for (int mark : a) {
//             sum += mark;
//         }
//         return (double) sum / a.length;
//     }

//     static int max(int[] a) {
//         int best = a[0];
//         for (int i = 1; i < a.length; i++) {
//             if (a[i] > best) {
//                 best = a[i];
//             }
//         }
//         return best;
//     }


//     static int countPassed(int[] a, int limit) {
//         int count = 0;
//         for (int mark : a) {
//             if (mark >= limit) {
//                 count++;
//             }
//         }
//         return count;
//     }
//     public static void main(String[] args) {
//         int[] marks = {70, 45, 88, 92, 60, 38};

//         System.out.println("Average: " + average(marks));
//         System.out.println("Best: " + max(marks));
//         System.out.println("Passed: " + countPassed(marks, 50));
//     }
// }




// Task 2
// A museum sells tickets by age. A visitor can type a wrong value, so the
//program must check the input.

// import java.util.Scanner;

// public class Ticket {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         int age = -1;
//         while (age <0 || age > 120) {
//             System.out.print("Enter your age: ");
//             if (!sc.hasNextInt()) {
//                 System.out.println("That is not a number.");
//                 sc.next();
//             } else {
//                 age = sc.nextInt();
//                 if (age < 0 || age > 120) {
//                     System.out.println("Age must be from 0 to 120.");

//                 }
//             }
//         }
//         int price = 0;
//         if (age < 7) {
//             price = 0;
//         }
//         else if (age < 18) {
//             price = 5;
//         } else if (age < 60) {
//             price = 10;
//         } else {
//             price = 6;
//         }
//         System.out.println("Ticket price: " + price);
//         sc.close();
//     }
// }



// Task 3
// A group of students must be stored as objects. Write the class Student and
// work with an array of its objects

// class Student {
//     String name;
//     double gpa;


//     Student(String name, double gpa) {
//         this.name = name;
//         this.gpa = gpa;
//     }
//     boolean isExcellent() {
//         return gpa >= 3.5;
//     }

//     @Override

//     public String toString() {
//         return name + " (" + gpa + ")";
//     }
// }

// public class Main {

//     public static void main(String[] args) {
//         Student[] group = {
//             new Student("Aziz", 3.2),
//             new Student("Madina", 3.8),
//             new Student("Bobur", 2.9),
//             new Student("Zilola", 3.6)
//         };
        
//         Student best = null;
//         double sum = 0;
//         for (Student s : group) {
//             System.out.print(s);

//             if (s.isExcellent()) {
//                 System.out.print("- excellent");
//             }
//             System.out.println();
            
//             sum += s.gpa;

//             if (best == null || best.gpa<s.gpa) {
//                 best = s;
//             }
            
//         }
//         System.out.println("Average GPA: " + sum/group.length);
//         System.out.println("Best student: "+best);

//     }
// }



// Task 4
// Different animals make different sounds, but all animals have a name. Use
// inheritance and method overriding.


class Animal {
    String name;
    Animal(String name) {
        this.name = name;
    }
    void sound() {
        System.out.println(name + " makes a sound");
    }
}



class Dog extends Animal {
    Dog(String name) {
        super(name);
    }


    @Override
    void sound() {
        System.out.println(name + " says Woof");
    }
    void fetch() {
        System.out.println(name + " brings the ball");
    }
}


class Cat extends Animal {
    Cat(String name) {
        super(name);
    }

    @Override
    void sound() {
        System.out.println(name + " says Meow");
    }
}


public class Main {
    public static void main(String[] args) {
        Animal[] pets = {
            new Animal("Creature"),
            new Dog("Rex"),
            new Cat("Tom")
        };

        for (Animal pet : pets) {
            pet.sound();
        }

        Dog d = new Dog("Buddy");
        d.fetch();
    }
}
