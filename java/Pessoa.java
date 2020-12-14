public class Pessoa {
    private int idade;
    private String nome;

    public Pessoa(String nome, int idade){
        this.nome = nome;
        this.idade = idade;
    }

    public int getidade() {
        return idade;
    }

    public String getnome() {
        return nome;
    }

    public void setnome(String nome) {
        this.nome = nome;
    }

    public void setidade(int idade) {
        this.idade = idade;
    }

    public static void main(String[] args) {
        Pessoa bruno = new Pessoa("Bruno", 19);
        System.out.println(bruno.nome);
    }


}