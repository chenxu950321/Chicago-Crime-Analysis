package pre_process;

import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import scala.Tuple2;

public class wordCount {
    public enum Type {
        ward, location, block, district, month, day, community, hour, monthday
    }
    public void count (String input, String pType, Type type, String output) {
        // ID:0; case:1; data:2; block:3; pType:5; desc:6; location:7; district:11; ward:12; community:13

        switch (type) {
            case block: // not, remove first
                block_count(input, pType, output);
                break;
            case location: // single
            case district: // single
            case ward: // single
            case community: // single
                single_count(input, pType, type, output);
                break;
            case month: // not
            case day: // not
            case hour: 
            case monthday: 
                time_count(input,pType,type,output);
                break;
        }

    }
    public void single_count(String input, String pType, Type type, String output) {
        // ID:0; case:1; data:2; block:3; pType:5; desc:6; location:7; district:11; ward:12; community:13
        int num = 0;
        switch (type) {
            case location: // single
                num = 7;
                break;
            case district: // single
                num = 11;
                break;
            case ward: // single
                num = 12;
                break;
            case community: // single
                num = 13;
                break;
        }

        JavaSparkContext sc = new JavaSparkContext(new SparkConf());
        JavaRDD<String> in = sc.textFile(input);
        String header = in.first();
        JavaRDD<String> in1 = in.filter(s -> s != header);
        //word count

        int finalNum = num;
        JavaPairRDD<String, Integer> pair = null; 
        // if (pType != "0")
            pair = in1
                    .map(s -> s.split(","))
                    .mapToPair(s -> new Tuple2<>(s[5], s[finalNum]))
                    .filter(s -> s._1.equals(pType))
                    .mapToPair(s -> new Tuple2<>(s._2, 1))
                    .reduceByKey((x, y) -> x+y);  // x 1st element, y 2nd element
        // else 
        //     pair = in1
        //             .map(s -> s.split(","))
        //             .mapToPair(s -> new Tuple2<>(s[5], s[finalNum]))
        //             // .filter(s -> s._1.equals(pType))
        //             .mapToPair(s -> new Tuple2<>(s._2, 1))
        //             .reduceByKey((x, y) -> x+y);  // x 1st element, y 2nd element
        JavaRDD<String> ave = pair
                .map(data -> data._1 + " " + data._2)
                .coalesce(1);

        ave.saveAsTextFile(output);

        //stop sc
        sc.stop();
        sc.close();
    }

    public void block_count(String input, String pType, String output) {
        // ID:0; case:1; data:2; block:3; pType:5; desc:6; location:7; district:11; ward:12; community:13
        // 042XX W IOWA ST
        int num = 3;
        JavaSparkContext sc = new JavaSparkContext(new SparkConf());
        JavaRDD<String> in = sc.textFile(input);
        String header = in.first();
        JavaRDD<String> in1 = in.filter(s -> s != header);
        JavaPairRDD<String, Integer> pair = null; 
        //word count
        // if (pType != "0")
        pair = in1
                .map(s -> s.split(","))
                .mapToPair(s -> new Tuple2<>(s[5], s[num]))
                .filter(s -> s._2.length()>12)
                .mapValues(s -> s.substring(8))
                .filter(s -> s._1.equals(pType))
                .mapToPair(s -> new Tuple2<>(s._2, 1))
                .reduceByKey((x, y) -> x+y);  // x
        // else 
        //     pair = in1
        //             .map(s -> s.split(","))
        //             .mapToPair(s -> new Tuple2<>(s[5], s[num]))
        //             .filter(s -> s._2.length()>12)
        //             .mapValues(s -> s.substring(8))
        //             // .filter(s -> s._1.equals(pType))
        //             .mapToPair(s -> new Tuple2<>(s._2, 1))
        //             .reduceByKey((x, y) -> x+y);  // x

        JavaRDD<String> ave = pair 
                .map(data -> data._1 + " " + data._2)
                .coalesce(1);

        ave.saveAsTextFile(output);

        //stop sc
        sc.stop();
        sc.close();
    }
    public void time_count(String input, String pType, Type type, String output) {
        // ID:0; case:1; data:2; block:3; pType:5; desc:6; location:7; district:11; ward:12; community:13

        // 11/02/2019 11:59:00 PM
        int l1 = "11/02/2019 11:07:32 PM".length(); 
        int l2 = "11".length(); 
        int l3 = "11/02".length(); 
        int i = 0, j = 0, l = 0;
        int m = 20, n = 22; 

        switch (type) {
            case hour: 
                l = l1; 
                i = 11; 
                j = 13;
                break; 
            case month:
                l = l2; 
                i = 0; 
                j = 2;
                break;
            case day:
                l = l3; 
                i = 3;
                j = 5;
                break;
            case monthday: 
                l = l3; 
                i = 0; 
                j = 5;
                break; 
        }

        int num = 2;
        JavaSparkContext sc = new JavaSparkContext(new SparkConf());
        JavaRDD<String> in = sc.textFile(input);
        String header = in.first();
        JavaRDD<String> in1 = in.filter(s -> s != header);
        //word count
        int finalL = l; 
        int finalI = i;
        int finalJ = j;
        JavaPairRDD<String, Integer> pair = null; 
        if (l == l1)
            pair = in1
                    .map(s -> s.split(","))
                    .mapToPair(s -> new Tuple2<>(s[5], s[num]))
                    .filter(s -> s._2().length() >= finalL)
                    .mapValues(s -> s.substring(finalI, finalJ) + s.substring(m, n))
                    .filter(s -> s._1.equals(pType))
                    .mapToPair(s -> new Tuple2<>(s._2, 1))
                    .reduceByKey((x, y) -> x+y);  // x
        else 
        //     if (pType != "0")
            pair = in1
                    .map(s -> s.split(","))
                    .mapToPair(s -> new Tuple2<>(s[5], s[num]))
                    .filter(s -> s._2().length() >= finalL)
                    .mapValues(s -> s.substring(finalI, finalJ))
                    .filter(s -> s._1.equals(pType))
                    .mapToPair(s -> new Tuple2<>(s._2, 1))
                    .reduceByKey((x, y) -> x+y);  // x
        //     else 
        //         pair = in1
        //                 .map(s -> s.split(","))
        //                 .mapToPair(s -> new Tuple2<>(s[5], s[num]))
        //                 .filter(s -> s._2().length() >= finalL)
        //                 .mapValues(s -> s.substring(finalI, finalJ))
        //                 // .filter(s -> s._1.equals(pType))
        //                 .mapToPair(s -> new Tuple2<>(s._2, 1))
        //                 .reduceByKey((x, y) -> x+y);  // x
        // }


        JavaRDD<String> ave = pair
                .map(data -> data._1 + " " + data._2)
                .coalesce(1);

        ave.saveAsTextFile(output);
        // ave.collect(); 

        //stop sc
        sc.stop();
        sc.close();
    }

}
