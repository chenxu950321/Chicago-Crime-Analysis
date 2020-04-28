package pre_process;
import pre_process.wordCount.*;

public class execute {
    public static void main(String args[]) {
        /*
        * 0: input
        * 1: primary ptype
        * 2: output ward 
        * 3: output block
        * 4: output district
        * 5: output time month
        * 6: output time day
        * 7: output location
        * 8: output community
        * */
        // ward, location, block, district, month, day, community
        String input = args[0], output = args[1]; 
        wordCount w = new wordCount(); 
        String[] ps = {"NARCOTICS", "THEFT"}; 
        // ward
        // w.count(input, pType, Type.ward, output+"/ward");
        // w.count(input, pType, Type.block, output+"/block");
        // w.count(input, pType, Type.district, output+"/district");
        // w.count(input, pType, Type.location, output+"/location");
        // w.count(input, pType, Type.community, output+"/community");
        for (String p: ps) {
            // w.count(input, p, Type.block, output+"/block/"+p);
            // w.count(input, p, Type.month, output+"/month/"+p);
            // w.count(input, p, Type.day, output+"/day/"+p); 
            w.count(input, p, Type.hour, output+"/hour1/"+p); 
            // w.count(input, pType, Type.monthday, output+"/monthday"+pType); 
        }

    }
}
