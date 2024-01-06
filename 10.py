import java.util.Scanner;

public class InequalityProof {

    public static void main(String[] args) {
    while (true) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the value for x: ");
        int x = scanner.nextInt();

        System.out.print("Enter the value for y: ");
        int y = scanner.nextInt();

        int expression1 = Math.abs(x) + Math.abs(y);
        int expression2 = Math.abs(x + y);

        System.out.println("|x| + |y| = |" + x + "| + |" + y + "|");
        System.out.println("          = " + Math.abs(x) + " + " + Math.abs(y));
        System.out.println("The value of |x| + |y| is: " + expression1 + "\n\n");

        System.out.println("|x + y| = |" + x + " + " + y + "|");
        System.out.println("        = |" + (x + y) + "|");
        System.out.println("The value of |x + y| is: " + expression2 + "\n\n");

        if (expression1 > expression2) {
            System.out.println(expression1+ " > " + expression2);
       }
       else if (expression1 == expression2) {
            System.out.println(expression1 + " = " + expression2);

       }
       System.out.println("As |x| + |y| ≥ |x + y|");
}
    }
}
