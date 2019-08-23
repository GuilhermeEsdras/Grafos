import java.lang.reflect.Array;
import java.util.*;

class VerticeInvalidoException extends Exception {
    public VerticeInvalidoException(String msg) {
        super(msg);
    }
}

class ArestaInvalidaException extends Exception {
    public ArestaInvalidaException(String msg) {
        super(msg);
    }
}

public class Grafo {

    private int qtdMaxSeparador = 1;
    private char separadorDeAresta = '-';

    private ArrayList<Character> N = new ArrayList<Character>();
    private HashMap<String, String> A = new HashMap<String, String>();

    public Grafo(ArrayList<Character> listaDeVertices, HashMap<String, String> dicionarioDeArestas)
            throws VerticeInvalidoException, ArestaInvalidaException {

        setN(listaDeVertices);
        setA(dicionarioDeArestas);

    }

    public ArrayList<Character> getN() {
        return N;
    }

    private void setN(ArrayList<Character> n) throws VerticeInvalidoException {

        for ( Character v : n ) {
            if ( !(this.verticeValido(v)) ) {
                throw new VerticeInvalidoException("O vértice " + v + " é inválido!");
            }
        }

        this.N = n;
    }

    public Map<String, String> getA() {
        return this.A;
    }

    private void setA(HashMap<String, String> a) throws ArestaInvalidaException {

        for ( Map.Entry<String, String> aresta : a.entrySet() ) {
            if ( !(this.arestaValida(aresta.getValue())) ) {
                throw new ArestaInvalidaException("A aresta " + aresta.getValue() + " é inválida!");
            }
        }

        this.A = a;
    }

    public Boolean arestaValida(String aresta) {

        int qtdSeparador = aresta.length() - aresta.replace("-", "").length();
        if (qtdSeparador != this.qtdMaxSeparador)
            return false;

        int iSeparador = aresta.indexOf(this.separadorDeAresta);
        if ( (iSeparador == 0) || (aresta.lastIndexOf(this.separadorDeAresta) == (aresta.length() - 1)) )
            return false;

        if ( !(this.existeVertice(aresta.charAt(0))) || !(this.existeVertice(aresta.charAt(2))) )
            return false;

        return true;
    }

    public Boolean verticeValido(Character vertice) {
        return ( !(vertice.toString().isEmpty()) && !(vertice.equals(this.separadorDeAresta)) );
    }
    
    public Boolean existeVertice(Character vertice) {
        return ( (this.verticeValido(vertice)) && (this.getN().contains(vertice)) );
    }

    public Boolean existeAresta(String aresta) {

        boolean existe = false;

        if (this.arestaValida(aresta)) {
            for (Map.Entry<String, String> k : this.getA().entrySet()) {
                if (aresta.equals(k.getKey())) {
                    existe = true;
                    break;
                }
            }
        }

        return existe;
    }

    public void adicionaVertice(Character v) throws VerticeInvalidoException {

        if ( (this.verticeValido(v)) && !(this.existeVertice(v)) ) {
            this.N.add(v);
        } else {
            throw new VerticeInvalidoException("O vértice " + v + " é inválido!");
        }

    }

    public void adicionaAresta(String nome, String a) throws ArestaInvalidaException {

        if (this.arestaValida(a)) {
            this.A.put(nome, a);
        } else {
            throw new ArestaInvalidaException("A aresta " + this.A.get(nome) + " é inválida");
        }
    }

    //--//

    /**
     * Minhas soluções dos exercícios e questões dos Roteiros
     *
     * @autor       Guilherme Esdras
     * @curso       Engenharia de Computação - IFPB
     * @período     3º - 2019.2
     * @disciplina  Teoria dos Grafos
     * @professor   Henrique Cunha
     *
     */

    /*  - Roteiro 1, Ínicio -
        (Copyright © Guilherme Esdras 2019.2)  */

    public ArrayList<String> verticesNaoAdjacentes() {

        ArrayList<String> listaDeNaoAdjacentes = new ArrayList<>();

        for (Character v1 : this.getN()) {
            for (Character v2 : this.getN()) {
                String arestaIndo = String.format("%c%c%c", v1, this.separadorDeAresta, v2);
                String arestaVindo = String.format("%c%c%c", v2, this.separadorDeAresta, v1);
                if ( !(this.getA().containsValue(arestaIndo)) && !(this.getA().containsValue(arestaVindo)) ) {
                    listaDeNaoAdjacentes.add(arestaIndo);
                }
            }
        }

        return listaDeNaoAdjacentes;
    }

    public Boolean haLaco() {

        for (String vertice : this.getA().values()) {
            if (vertice.charAt(0) == vertice.charAt(2)) {
                return true;
            }
        }

        return false;
    }

    public Boolean haParalelas() {

        ArrayList<String> arestasIndoVerificadas = new ArrayList<>();
        ArrayList<String> arestasVindoVerificadas = new ArrayList<>();

        for (String aresta : this.getA().values()) {

            String arestaIndo = String.format("%c%c%c", aresta.charAt(0), this.separadorDeAresta, aresta.charAt(2));
            String arestaVindo = String.format("%c%c%c", aresta.charAt(2), this.separadorDeAresta, aresta.charAt(0));

            if ( (arestasIndoVerificadas.contains(arestaIndo)) && (arestasVindoVerificadas.contains(arestaVindo)) ) {
                return true;
            } else {
                arestasIndoVerificadas.add(arestaIndo);
                arestasVindoVerificadas.add(arestaVindo);
            }
        }

        return false;
    }

    public int grau(Character v) {

        Collection<String> listaDeArestas = this.getA().values();

        int grau = 0;

        for (String vertice : listaDeArestas) {
            if ( (vertice.charAt(0) == v) || (vertice.charAt(2) == v) ) {
                grau++;
            }
        }

        return grau;
    }

    public ArrayList<String> arestasSobreVertice(Character vertice) {

        ArrayList<String> listaDeArestas = new ArrayList<>();

        for (Map.Entry<String, String> aresta : this.getA().entrySet()) {
            if ( (aresta.getValue().charAt(0) == vertice) ||
                    (aresta.getValue().charAt(2) == vertice) ) {
                listaDeArestas.add(aresta.getKey());
            }
        }

        return listaDeArestas;
    }

    public Boolean ehCompleto() {

        int n = this.N.size();
        if (n == 1) return true;

        int maxDeArestas = (n * (n-1)) / 2;

        ArrayList<String> arestasVerificadas = new ArrayList<>();

        for (String vertice : this.getA().values()) {
            String verticeContrario = String.format("%c%c%c", vertice.charAt(2), this.separadorDeAresta, vertice.charAt(0));
            if ( (arestasVerificadas.contains(vertice)) || (arestasVerificadas.contains(verticeContrario)) ) {
                return false;
            } else {
                arestasVerificadas.add(vertice);
            }
        }

        return (arestasVerificadas.size() == maxDeArestas) || (arestasVerificadas.size() == 2);
    }

    /*  - Roteiro 1, Fim -
        (Copyright © Guilherme Esdras 2019.2)  */

    //--//

    /*  - Roteiro 2, Ínicio -
        (Copyright © Guilherme Esdras 2019.2)  */

    private List<String> DFSAuxiliar(Collection<Map.Entry<String, String>> grafo, Character vertice,
                                          List<String> verificados) {
        for (Map.Entry<String, String> g : grafo) {

            if (g.getValue().charAt(0) == vertice) {

                String vertice1 = Character.toString(g.getValue().charAt(0));
                String vertice2 = Character.toString(g.getValue().charAt(2));

                if ( !(verificados.contains(vertice1)) ) {
                    verificados.add(vertice1);
                }

                if ( !(verificados.contains(vertice2)) ) {
                    verificados.add(g.getKey());
                    verificados.add(vertice2);
                    DFSAuxiliar(grafo, g.getValue().charAt(2), verificados);
                }
            }

            else if (g.getValue().charAt(2) == vertice) {

                String vertice1 = Character.toString(g.getValue().charAt(0));
                String vertice2 = Character.toString(g.getValue().charAt(2));

                if ( !(verificados.contains(vertice2)) ) {
                    verificados.add(vertice2);
                }

                if ( !(verificados.contains(vertice1)) ) {
                    verificados.add(g.getKey());
                    verificados.add(vertice1);
                    DFSAuxiliar(grafo, g.getValue().charAt(0), verificados);
                }
            }
        }

        return verificados;
    }

    public List<String> DFS(Character verticeRaiz) {
        Set<Map.Entry<String, String>> grafo = this.getA().entrySet();
        return DFSAuxiliar(grafo, verticeRaiz, Collections.emptyList());
    }

    /*  - Roteiro 2, Fim -
            (Copyright © Guilherme Esdras 2019.2)  */


    @Override
    public String toString() {
        return "N (Vértices) = " + this.getN() + ",\n" +
                "A (Arestas) = " + this.getA();
    }
}
