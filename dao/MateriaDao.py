# Data access object - DAO
from flask import current_app as app
from conexion.Conexion import Conexion

class MateriaDao:
    
    def getMaterias(self):

        materiaSQL = """
        SELECT id, descripcion
        FROM materias
        """
        #objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
          cur.execute(materiaSQL)
          #trae datos de db
          lista_materias = cur.fetchall()
          #retorno de datos
          lista_ordenada = []
          for item in lista_materias:
              lista_ordenada.append({
                  "id": item[0],
                  "descripcion": item[1]
                })
          return lista_ordenada
        except con.Error as e:
           app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getMateriaById(self, id):

        materiaSQL = """
        SELECT id, descripcion
        FROM materias WHERE id=%s
        """
        #objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
          cur.execute(materiaSQL, (id,))
          #trae datos de db
          materiaEncontrada = cur.fetchone()
          #retorno de datos
          return {
                    "id": materiaEncontrada[0],
                    "descripcion": materiaEncontrada[1]
                }
        except con.Error as e:
             app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarMateria(self, descripcion):
        
        insertMateriaSQL = """
        INSERT INTO materias(descripcion) VALUES(%s)
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        #Ejecucion exitosa
        try:
            cur.execute(insertMateriaSQL, (descripcion,))
            #se confirma la isercion
            con.commit()

            return True

        #si algo falla aqui
        except con.Error as e:
            app.logger.info(e)
            
        #siempre se va a ejecutar
        finally:
            cur.close()
            con.close()

        return False    
          
    def updateMateria(self, id, descripcion):

        updateMateriaSQL = """
        UPDATE materias
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateMateriaSQL, (descripcion, id,))
            # se confirma la insercion
            con.commit()

            return True

        # Si algo fallo entra aqui
        except con.Error as e:
            app.logger.info(e)

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

        return False
    
    def deleteMateria(self, id):

        updateMateriaSQL = """
        DELETE FROM materias
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateMateriaSQL, (id,))
            # se confirma la insercion
            con.commit()

            return True

        # Si algo fallo entra aqui
        except con.Error as e:
            app.logger.info(e)

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

        return False    