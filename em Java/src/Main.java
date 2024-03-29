import java.util.*;

public class Main {
    public static void main(String[] args) throws VerticeInvalidoException, ArestaInvalidaException {

        ArrayList<Character> vertices = new ArrayList<>();
        vertices.add('J');
        vertices.add('C');
        vertices.add('E');
        vertices.add('P');
        vertices.add('M');
        vertices.add('T');
        vertices.add('Z');

        HashMap<String, String> arestas = new HashMap<String, String>() {{
            // Forma de inicializar e já adicionar elementos em um map
            put("a1", "J-C");
            put("a2", "C-E");
            put("a3", "C-E");
            put("a4", "C-P");
            put("a5", "C-P");
        }};

        // Forma clássica de adicionar elementos posteriormente em um map
        arestas.put("a6", "C-M");
        arestas.put("a7", "C-T");
        arestas.put("a8", "M-T");
        arestas.put("a9", "T-Z");

        Grafo paraiba = new Grafo(vertices, arestas);

        System.out.println(paraiba);
        System.out.println(paraiba.verticesNaoAdjacentes());
        System.out.println(paraiba.haLaco());
        System.out.println(paraiba.haParalelas());
        System.out.println(paraiba.grau('J'));
        System.out.println(paraiba.grau('C'));
        System.out.println(paraiba.arestasSobreVertice('P'));
        System.out.println(paraiba.ehCompleto());
//        System.out.println(paraiba.DFS('J'));
    }
}