import java.util.*;

interface Transaction {
    void deposit(double amount);
    void withdraw(double amount);
}

abstract class Account implements Transaction {
    private String accountholder;
    private int accountnumber;
    protected double balance;

    public Account(String name, int accno, double balance) {
        this.accountholder = name;
        this.accountnumber = accno;
        this.balance = balance;
    }

    public String getAccountholder() {
        return accountholder;
    }

    public int getAccountnumber() {
        return accountnumber;
    }

    public void display() {
        System.out.println("Name: " + accountholder);
        System.out.println("Account Number: " + accountnumber);
        System.out.println("Balance: " + balance);
    }

    abstract void accountType();
}

// Savings Account
class SavingsAccount extends Account {

    public SavingsAccount(String name, int accno, double balance) {
        super(name, accno, balance);
    }

    void accountType() {
        System.out.println("Savings Account");
    }

    public void deposit(double amount) {
        balance += amount;
        System.out.println("Deposited: " + amount);
    }

    public void withdraw(double amount) {
        if (amount <= balance) {
            balance -= amount;
            System.out.println("Withdrawn: " + amount);
        } else {
            System.out.println("Insufficient Balance");
        }
    }
}

// Current Account
class CurrentAccount extends Account {

    public CurrentAccount(String name, int accno, double balance) {
        super(name, accno, balance);
    }

    void accountType() {
        System.out.println("Current Account");
    }

    public void deposit(double amount) {
        balance += amount;
        System.out.println("Deposited: " + amount);
    }

    public void withdraw(double amount) {
        if (amount <= balance + 5000) { // overdraft limit
            balance -= amount;
            System.out.println("Withdrawn: " + amount);
        } else {
            System.out.println("Overdraft limit exceeded");
        }
    }
}

// Main Class
public class Bank {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the name: ");
        String name = sc.nextLine();

        System.out.print("Enter the account number: ");
        int accno = sc.nextInt();

        System.out.print("Enter the balance: ");
        double balance = sc.nextDouble();

        System.out.println("1. Savings Account\n2. Current Account");
        int choice = sc.nextInt();

        Account acc;

        if (choice == 1) {
            acc = new SavingsAccount(name, accno, balance);
        } else {
            acc = new CurrentAccount(name, accno, balance);
        }

        int option;

        do {
            System.out.println("\n1. Deposit 2. Withdraw 3. Display 4. Exit");
            option = sc.nextInt();

            switch (option) {
                case 1:
                    System.out.print("Enter amount: ");
                    acc.deposit(sc.nextDouble());
                    break;

                case 2:
                    System.out.print("Enter amount: ");
                    acc.withdraw(sc.nextDouble());
                    break;

                case 3:
                    acc.accountType();
                    acc.display();
                    break;

                case 4:
                    System.out.println("Thank You!");
                    break;

                default:
                    System.out.println("Invalid choice");
            }

        } while (option != 4);

        sc.close();
    }
}
