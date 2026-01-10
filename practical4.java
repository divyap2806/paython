import java.util.Scanner;

public class practical4 {

public static void main(String[] args) {

Scanner sc = new Scanner(System.in);

double weight;
System.out.println("Enter the weight in pounds: ");
weight = sc.nextDouble();

double height;
System.out.println("Enter the height in inches: ");
height = sc.nextDouble();
 
double wkg = 0.45359237* weight;
System.out.println("weight in kilogaram is :  " +wkg);

double hinch = 0.0254*height;
double hm = wkg*(hinch);
System.out.println("height in meter is : " +hm);

double BMI = ((wkg/ hm)*hm );
System.out.println("BMI : " +BMI);


}
}