import java.io.*;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.HashSet;

public class Main {

    public static void main(String[] args) throws IOException {
        HashSet<String> wordSet = new HashSet<>();

        String fileDir = args[0];
        String[] fileList = new File(fileDir).list();
        Path filePath;
        BufferedWriter writer = new BufferedWriter(new FileWriter(
                Paths.get(fileDir, "extracted.txt").toString()));
        BufferedReader br;
        String line;

        br = new BufferedReader(new FileReader("words.txt"));
        while((line = br.readLine()) != null){
            wordSet.add(line);
        }
        br.close();
        for (String fileName :
                fileList) {
            if(fileName.equals("extracted"))
                continue;
            System.out.println("cleaning and extracting file " + fileName);
            filePath = Paths.get(fileDir, fileName);
            br = new BufferedReader(new FileReader(filePath.toString()));
            StringBuilder sb = new StringBuilder(filePath.toString());

            /**
             * extract need fields, like description, shape, duration
             */
            while((line = br.readLine()) != null){
                if(line.length() == 0 || (line.length() == 1 && line.charAt(0) == ' '))
                    continue;
                line = line.toLowerCase();
                String[] words = line.split(" |/|,|\\.");
                String lastWord = null;
                for (String word :
                        words) {
//                    System.out.println(word + "---------------------");
                    // duration
                    if(word.equals("seconds") || word.equals("secs")
                            || word.equals("mins") || word.equals("minutes")
                            || word.equals("hours") || word.equals("days")){
                        writer.write("duration" + "\t");
                        writer.write(lastWord + " " + word + "\n");
                    }
                    // shape
                    if(word.equals("orb")  || word.equals("flare")
                            || word.equals("egg")|| word.equals("light")
                            || word.equals("delta") || word.equals("teardrop")
                            || word.equals("hexagon") || word.equals("formation")
                            || word.equals("dome") || word.equals("changing")
                            || word.equals("cone") || word.equals("triangle")
                            || word.equals("unknown") || word.equals("sphere")
                            || word.equals("cigar") || word.equals("fireball")
                            || word.equals("oval") || word.equals("cross")
                            || word.equals("disk") || word.equals("diamond")
                            || word.equals("crescent") || word.equals("round")
                            || word.equals("light") || word.equals("pyramid")
                            || word.equals("rectangle") || word.equals("cylinder")
                            || word.equals("chevron") || word.equals("circle")
                            || word.equals("changed") || word.equals("flash")){
                        writer.write("shape" + "\t");
                        writer.write(word + "\n");
                    }
                    // description
                    if(word.equals("description")){
                        writer.write("description" + "\t");
                        Boolean brk = false;
                        for (int i = 0; i < 7; i++) {
                            if(brk)
                                break;
                            line = br.readLine().toLowerCase();
                            String[] splitted = line.split(" |/|,|\\.");
                            for (String str : splitted) {
                                if(str.equals("C") || str.equals("exact")
                                        || str.equals("position") || str.equals("observer")){
                                    brk = true;
                                    break;
                                }
//                                if(str.equals("number") || str.equals("objects")
//                                        || str.equals("aim") || str.equals("brightness")
//                                        || str.equals("colour") || str.equals("shape")){
//                                    break;
//                                }
                                if(wordSet.contains(str)){
                                    // write
                                    if(str.length() > 1)
                                        writer.write(str + " ");
                                }
                            }
                        }
                        writer.write("\n");
                    }
                    lastWord = word;
                }
            }
            br.close();
        }
        writer.close();

        br = new BufferedReader(new FileReader(Paths.get(fileDir, "extracted.txt").toString()));
        System.out.println(args[1]);
        writer = new BufferedWriter(new FileWriter(args[1], true));
        Boolean des = false, dur = false;

        while((line = br.readLine()) != null){
            String[] words = line.split("\t");
            // description
            if(words[0].equals("description")){
                writer.write("\n");
                for (int i = 0; i < 3; i++) {
                    writer.write("\t");
                }
                if(words.length > 1)
                    writer.write(words[1] + "\t");
                else
                    writer.write("\t");
                des = true;
            }
            // duration
            if(words[0].equals("duration")){
                if(des){
                    writer.write("\t");
                }else{
                    writer.write("\n");
                    for (int i = 0; i < 5; i++) {
                        writer.write("\t");
                    }
                }
                writer.write(words[1] + "\t");
                dur = true;
            }
            // latitude, location, longitude
            if(dur){
                writer.write("51.509865" + "\t");
                writer.write("UK" + "\t");
                writer.write("-0.118092" + "\t");
            }else if(des){
                for (int i = 0; i < 2; i++) {
                    writer.write("\t");
                }
                writer.write("51.509865" + "\t");
                writer.write("UK" + "\t");
                writer.write("-0.118092" + "\t");
            }
            // shape
            if(words[0].equals("shape")){
                if((!des) && (!dur)){
                    writer.write("\n");
                    for (int i = 0; i < 6; i++) {
                        writer.write("\t");
                    }
                    writer.write("51.509865" + "\t");
                    writer.write("UK" + "\t");
                    writer.write("-0.118092" + "\t");
//                    for (int i = 0; i < 4; i++) {
//                        writer.write("\t");
//                    }
                }
                for (int i = 0; i < 4; i++) {
                    writer.write("\t");
                }
//                else if(dur){
//                    for (int i = 0; i < 4; i++) {
//                        writer.write("\t");
//                    }
//                }else{
//                    for (int i = 0; i < 6; i++) {
//                        writer.write("\t");
//                    }
//                }
                writer.write(words[1] + "\t");
            }
            des = false;
            dur = false;
        }
        br.close();
        writer.close();
    }
}
