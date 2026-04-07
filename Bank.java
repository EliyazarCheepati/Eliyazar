import java.util.*;

interface Transaction{
    double deposit(double amount);
    double withdraw(double amount);
}

abstract class Account implements Transaction{
    private String Accountholder;
    private int accountnumber;
    protected double balance;

    public Account(String name,int accno,double balance)
    {
        this.Accountholder=name;
        this.accountnumber=accno;
        this.balance=balance;
    }

    public String getAccountholder()
    {
        return Accountholder;
    }

    public int getaccountnumber()
    {
        return accountnumber;
    }

    public void display()
    {
        System.out.println("name : "+Accountholder);
        System.out.println("accountnumber: "+accountnumber);
        System.out.println("balance: "+balance);
    }

    abstract void accounttype();
}

class SavingsAccounts extends Account{

    public SavingsAcoount(String name,int accno,double balance){
    super(name,accno,balance);
    }
     public void accountype()
     {
        System.out.println("savings account");
     }

     public void deposit(double amount)
     {
        balance+=amount;
        System.out.println("deposited: "+amount);
     }
     public void withdraw(double amount)
     {
        if(amount<=balance)
        {
            balance-=amount;
            System.out.println("withdraw: "+amount);
        }
        else{
            System.out.println("insufficient balance");
        }
     }

}

class currentAccount extends Account{

    public currentAccount(String name,int accno,double balance)
    {
        super(name,accno,balance);
    }
    public void accountype()
    {
        System.out.println("current account");
    }

    public void deposit(double amount)
    {
        balance+=amount;
        System.out.println("deposited: "+amount);
    }

    public void withdraw(double amount)
    {
        if(amount<=balance+5000)
        {
            balance-=amount;
            System.out.println("withdraw: "+amount);
        }
        else{
            System.out.println("overdraft limit exceeded");
        }
    }
}

public class Bank{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);

        System.out.print("enter the name: ");
        String name=sc.nextLine();

        System.out.print("enter the account number: ");
        int accno=sc.nextInt();

        System.out.print("enter the balance: ");
        double balance=sc.nextDouble();

        System.out.print("1.savings account\n2.current account");
        int choice=sc.nextInt();

        Account acc;
        if(choice==1)
        {
            acc=new SavingsAccount(name, accno, balance);
        }
        else{
            acc=new currentAccount(name, accno, balance);
        }
        int option;

        do {
            System.out.println("\n1.Deposit 2.Withdraw 3.Display 4.Exit");
            option = sc.nextInt();

            switch (option) {
                case 1:
                    System.out.println("Enter amount:");
                    acc.deposit(sc.nextDouble());
                    break;

                case 2:
                    System.out.println("Enter amount:");
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

    }
}



