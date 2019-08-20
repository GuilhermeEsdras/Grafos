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

    @Override
    public String toString() {
        return "Grafo {" + "\n" +
                "N (Vértices) = " + this.getN() + ",\n" +
                "A (Arestas) = " + this.getA() + "\n" +
                "}";
    }
}
