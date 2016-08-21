package ClienteJava;

import java.io.IOException;
import Cliente;


//Clase principal que hará uso del cliente
public class ClienteEspolKeyValueStore
{
    public static void main(String[] args) throws IOException
    {  
        Cliente cli = new Cliente(); //Se crea el cliente
        
        System.out.println("Iniciando cliente\n");
        cli.startClient(); //Se inicia el cliente
    }
}