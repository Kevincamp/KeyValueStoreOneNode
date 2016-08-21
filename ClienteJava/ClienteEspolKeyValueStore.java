import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class ClienteEspolKeyValueStore
{
    class Conexion
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

	class Cliente extends Conexion
	{
	    public Cliente() {} //Se usa el constructor para cliente de Conexion

	    public void startClient() { //Metodo para iniciar el cliente
	        try
	        {
	            //Flujo de datos hacia el servidor
	            salidaServidor = new DataOutputStream(cs.getOutputStream());
	            //Se enviarán dos mensajes
	            for (int i = 0; i < 2; i++)
	            {
	                //Se escribe en el servidor usando su flujo de datos
	                salidaServidor.writeUTF("Este es el mensaje número " + (i+1) + "\n");                
	            }
	            cs.close();//Fin de la conexión
	        }
	        catch (Exception e)
	        {
	            System.out.println(e.getMessage());
	        }	
	    }
	}

	public static void main(String[] args) throws IOException
    {  
        Cliente cli = new Cliente(); //Se crea el cliente
        
        System.out.println("Iniciando cliente\n");
        cli.startClient(); //Se inicia el cliente
    }
}