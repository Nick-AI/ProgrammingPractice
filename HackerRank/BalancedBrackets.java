import java.util.*;

public class BalancedBrackets {

    public static void main(String[] args){
        List<Character> close = Arrays.asList(')', '}', ']');
        Scanner s = new Scanner(System.in);
        int reps = s.nextInt();
        s.nextLine();

        for(int i =0; i < reps; i++){
            Stack<Character> bal = new Stack<>();
            char[] bracks = s.nextLine().toCharArray();
            for(char item : bracks){
                if(bal.empty() || close.contains(bal.peek()))
                    bal.push(item);
                else {
                    if(bal.peek() == '(' && item == ')')
                        bal.pop();
                    else if(bal.peek() == '{' && item == '}')
                        bal.pop();
                    else if(bal.peek() == '[' && item == ']')
                        bal.pop();
                    else
                        bal.push(item);
                }
            }
            if(bal.empty())
                System.out.println("YES");
            else
                System.out.println("NO");
        }
    }
}
