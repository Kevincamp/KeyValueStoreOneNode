package ClienteJava;

import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class Conexion
{
    private final int PUERTO = 12345; //Puerto para la conexión
    private final String HOST = "Mac-mini.local"; //Host para la conexión
    protected Socket cs; //Socket del cliente
    protected DataOutputStream salidaServidor, salidaCliente; //Flujo de datos de salida
    
    public Conexion(String host,String puerto) throws IOException //Constructor
    {
        cs = new Socket(HOST, PUERTO); //Socket para el cliente en localhost en puerto 12345
    }
}