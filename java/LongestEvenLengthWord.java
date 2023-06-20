public class LongestEvenLengthWord {

    public static void main(String[] args) {
        System.out.println(Longest_Even_Length_Word( "This is a testing string"));
        System.out.println(Longest_Even_Length_Word( "The tallest mountian is Mount Everest in Nepal"));
    }

    public static String Longest_Even_Length_Word(String sentence){

        String [] subStrings = sentence.split(" ");
        String maxSubtring = null;
        int maxLength = -1;

        for (int i = 0; i < subStrings.length; i++){
            if (subStrings[i].length() > maxLength && subStrings[i].length() % 2 == 0){
                maxLength = subStrings[i].length();
                maxSubtring = subStrings[i];
            }
        }
        if (maxLength > -1) {
            return maxSubtring;
        } else {
            return "00";
        }
    }
}