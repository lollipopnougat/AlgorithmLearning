import java.util.ArrayList;
import java.util.Scanner;

public class Program {
    public static void main(String[] args) {

        CalculatorDecimal ca = new CalculatorDecimal();
        Scanner sc = new Scanner(System.in);
        System.out.println("命令行简单计算器 V1.0");
        while (true)
        {
            System.out.print(">>");
            String input = sc.nextLine();
            try
            {
                ca.SetNew(input);
                System.out.println(ca.GetDoubleResult());
            }
            catch (Exception er)
            {
                System.out.println("错误!" + er.getMessage());
            }
        }
    }
}
