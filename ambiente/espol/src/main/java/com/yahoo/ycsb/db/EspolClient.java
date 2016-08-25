/**
 * Copyright (c) 2012 YCSB contributors. All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you
 * may not use this file except in compliance with the License. You
 * may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
 * implied. See the License for the specific language governing
 * permissions and limitations under the License. See accompanying
 * LICENSE file.
 */

/**
 * Redis client binding for YCSB.
 *
 * All YCSB records are mapped to a Redis *hash field*.  For scanning
 * operations, all keys are saved (by an arbitrary hash) in a sorted set.
 */

package com.yahoo.ycsb.db;

import java.io.*;
import java.net.*;
import java.io.DataInputStream;
import java.util.logging.Level;
import java.util.logging.Logger;

import com.yahoo.ycsb.ByteIterator;
import com.yahoo.ycsb.DB;
import com.yahoo.ycsb.DBException;
import com.yahoo.ycsb.Status;
import com.yahoo.ycsb.StringByteIterator;


import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Properties;
import java.util.Set;
import java.util.Vector;


public class EspolClient extends DB {
  public static final String HOST_PROPERTY = "espol.host";
  public static final String PORT_PROPERTY = "espol.port";
  public DbLayer db;


  public void init() throws DBException {
    Properties props = getProperties();
    int port;

    String portString = props.getProperty(PORT_PROPERTY);
    if (portString != null) {
      port = Integer.parseInt(portString);
    } else {
      port = 12345;
    }
    String host = props.getProperty(HOST_PROPERTY);
   
            //PrintWriter out = new PrintWriter(kkSocket.getOutputStream(), true);
    try{
      Socket csocket = new Socket(host, port);
      DataInputStream entrada = new DataInputStream(csocket.getInputStream());

      byte[] bs = new byte[2];
      entrada.read(bs);
      this.db = new DbLayer(csocket);
    }
    catch(java.io.IOException e)
    {
      System.out.println("Error Conexion");
    }
    
  }

  public void cleanup() throws DBException {
    
  }

  /*
   * Calculate a hash for a key to store it in an index. The actual return value
   * of this function is not interesting -- it primarily needs to be fast and
   * scattered along the whole space of doubles. In a real world scenario one
   * would probably use the ASCII values of the keys.
   */

  // XXX jedis.select(int index) to switch to `table`

  @Override
  public Status read(String table, String key, Set<String> fields,
      HashMap<String, ByteIterator> result) {
    db.read(key);
    return Status.OK;
  }

  @Override
  public Status insert(String table, String key,
      HashMap<String, ByteIterator> values) {
    db.insert(key,values.toString());
    return Status.OK;
  }

  @Override
  public Status delete(String table, String key) {
    return Status.OK;
  }

  @Override
  public Status update(String table, String key,
      HashMap<String, ByteIterator> values) {
    return Status.OK;
  }

  @Override
  public Status scan(String table, String startkey, int recordcount,
      Set<String> fields, Vector<HashMap<String, ByteIterator>> result) {
    return Status.OK;
  }

}

class DbLayer {

    Socket con;

    DbLayer(Socket conn) {
        this.con = conn;
    }

    void read(String key) {
        byte[] buffer;
        String cadena;
        String longitud = getRequesStrLen("get", key, "");
        //System.out.println(longitud);
        DataInputStream entrada;
        DataOutputStream salida;
        try {
            salida = new DataOutputStream(this.con.getOutputStream());
            buffer = new byte[10];
            salida.write(longitud.getBytes());
            salida.flush();
            cadena = "get " + key + " ";
            salida.write(cadena.getBytes());
            salida.flush();
            
            cadena = getResponseServer();
            //System.out.println(cadena);
        } catch (IOException ex) {
            Logger.getLogger(DbLayer.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    void insert(String key, String value) {
        byte[] buffer;
        String cadena;
        String longitud = getRequesStrLen("set", key, value);
        //System.out.println(longitud);
        DataInputStream entrada;
        DataOutputStream salida;
        try {
            salida = new DataOutputStream(this.con.getOutputStream());
            buffer = new byte[10];
            salida.write(longitud.getBytes());
            salida.flush();
            cadena = "set " + key + " " + value;
            salida.write(cadena.getBytes());
            salida.flush();
            entrada = new DataInputStream(this.con.getInputStream());
            entrada.read(buffer);
            cadena = new String(buffer, "UTF-8");
            //System.out.println(cadena);
        } catch (IOException ex) {
            Logger.getLogger(DbLayer.class.getName()).log(Level.SEVERE, null, ex);
        }

    }

    String getRequesStrLen(String instruccion, String key, String value) {
        String longitud = String.valueOf(instruccion.length() + key.length() + value.length() + 2);
        while (longitud.length() < 10) {
            longitud = "0" + longitud;
        }
        return longitud;
    }

    String getResponseServer() {
        byte[] buffer;
        String cadena = "";
        String salida = "";
        String separador = "$operativos$";
        try {
            DataInputStream entrada = new DataInputStream(this.con.getInputStream());
            buffer = new byte[1024];
            entrada.read(buffer);
            cadena = new String(buffer, "UTF-8");
            while (cadena.endsWith(separador)) {
                salida = salida + cadena.substring(0, cadena.length() - separador.length() - 1);
                buffer = new byte[1024];
                entrada.read(buffer);
                cadena = new String(buffer, "UTF-8");
                
            }

        } catch (IOException ex) {
            Logger.getLogger(DbLayer.class.getName()).log(Level.SEVERE, null, ex);
        }

        return salida + cadena;
    }
}
