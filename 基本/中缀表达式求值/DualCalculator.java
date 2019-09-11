import java.math.BigDecimal;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class DualCalculator {
    private String orExpression;
    private String pattern = "^(\\d+\\.?\\d*)([+|-|*|/])(\\d+\\.?\\d*)$";
    private Pattern regexp = Pattern.compile(pattern);
    private BigDecimal firstNum;
    private BigDecimal secondNum;
    private BigDecimal Result;
    private char op;

    public DualCalculator(String oe) {
        orExpression = oe;
    }

    public double getResult() throws Exception {
        Matcher match = regexp.matcher(orExpression);
        if (!match.find()) throw new Exception("语法错误");
        else {
            firstNum = new BigDecimal(match.group(1));
            secondNum = new BigDecimal(match.group(3));
            op = match.group(2).charAt(0);
        }

        switch (op) {
            case '+':
                Result = firstNum.add(secondNum);
                break;
            case '-':
                Result = firstNum.subtract(secondNum);
                break;
            case '*':
                Result = firstNum.multiply(secondNum);
                break;
            case '/':
                Result = firstNum.divide(secondNum);
                break;
            default:
                throw new Exception("非法符号");
        }
        return Result.doubleValue();
    }
}
