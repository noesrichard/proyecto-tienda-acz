/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package interfaces;

import cliente.Conexion;
import interfaces.InterfaceBrands;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JOptionPane;
import javax.swing.table.DefaultTableModel;

/**
 *
 * @author zapju
 */
public class InterfaceCategories extends javax.swing.JFrame {
	
	Conexion conexion; 
    /**
     * Creates new form Cliente
     */
    public InterfaceCategories() {
        initComponents();
		this.conexion = new Conexion(); 
        try {
            llenarTabla();
        } catch (Exception ex) {
            Logger.getLogger(InterfaceCategories.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    public void llenarTabla() throws Exception {
        //Este metodo carga desde la API la tabla
        //Recive una matriz y lo carga por filas en un ciclo
        DefaultTableModel modelo = (DefaultTableModel) jTabla.getModel();
        String[][] categorias = this.conexion.getCategories();
        for (int i = 0; i < categorias.length; i++) {
            modelo.addRow(categorias[i]);
        }
    }

    public void crearCategoria(String nombre) {
        try {
            // TODO add your handling code here:
            this.conexion.crearCategoria(nombre);
            JOptionPane.showMessageDialog(this, "Se a creado la categoria exitosamente!");
            actualizarTabla();
        } catch (Exception ex) {
            Logger.getLogger(InterfaceCategories.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    public void actualizarTabla() {
        jTabla.repaint();
    }

    public void eliminarCategoria(String id) {
        try {
            this.conexion.eliminarCategoria(id);
            JOptionPane.showMessageDialog(this, "Se elimino la categoria exitosamente!");
            actualizarTabla();
        } catch (Exception ex) {
            Logger.getLogger(InterfaceCategories.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jTxtID = new javax.swing.JTextField();
        jTxtNombre = new javax.swing.JTextField();
        jBtnCrear = new javax.swing.JButton();
        jBtnEliminar = new javax.swing.JButton();
        jBtnActualizar = new javax.swing.JButton();
        jScrollPane1 = new javax.swing.JScrollPane();
        jTabla = new javax.swing.JTable();
        jLabel1 = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();
        jMenuBar2 = new javax.swing.JMenuBar();
        jMnCategorias = new javax.swing.JMenu();
        jMnMarcas = new javax.swing.JMenu();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Categoria");

        jTxtID.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jTxtIDActionPerformed(evt);
            }
        });

        jTxtNombre.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jTxtNombreActionPerformed(evt);
            }
        });

        jBtnCrear.setText("Crear");
        jBtnCrear.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jBtnCrearActionPerformed(evt);
            }
        });

        jBtnEliminar.setText("Eliminar");
        jBtnEliminar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jBtnEliminarActionPerformed(evt);
            }
        });

        jBtnActualizar.setText("Actualizar");

        jTabla.setBorder(javax.swing.BorderFactory.createBevelBorder(javax.swing.border.BevelBorder.RAISED));
        jTabla.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {

            },
            new String [] {
                "ID", "Nombre"
            }
        ) {
            Class[] types = new Class [] {
                java.lang.String.class, java.lang.String.class
            };
            boolean[] canEdit = new boolean [] {
                false, false
            };

            public Class getColumnClass(int columnIndex) {
                return types [columnIndex];
            }

            public boolean isCellEditable(int rowIndex, int columnIndex) {
                return canEdit [columnIndex];
            }
        });
        jScrollPane1.setViewportView(jTabla);

        jLabel1.setText("ID");

        jLabel2.setText("Nombre");

        jMnCategorias.setText("Categorias");
        jMenuBar2.add(jMnCategorias);

        jMnMarcas.setText("Marcas");
        jMnMarcas.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jMnMarcasMouseClicked(evt);
            }
        });
        jMnMarcas.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jMnMarcasActionPerformed(evt);
            }
        });
        jMenuBar2.add(jMnMarcas);

        setJMenuBar(jMenuBar2);

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addGap(30, 30, 30)
                .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 290, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 125, Short.MAX_VALUE)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                        .addComponent(jTxtNombre, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 96, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addComponent(jTxtID, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 96, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addComponent(jLabel1)
                    .addComponent(jLabel2))
                .addGap(71, 71, 71)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                    .addComponent(jBtnActualizar, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(jBtnCrear, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(jBtnEliminar, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 89, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(28, 28, 28))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(jBtnCrear)
                .addGap(18, 18, 18)
                .addComponent(jBtnEliminar)
                .addGap(26, 26, 26)
                .addComponent(jBtnActualizar)
                .addGap(238, 238, 238))
            .addGroup(layout.createSequentialGroup()
                .addGap(31, 31, 31)
                .addComponent(jLabel1)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 319, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(jTxtID, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(18, 18, 18)
                        .addComponent(jLabel2)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(jTxtNombre, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addContainerGap(18, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void jTxtNombreActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jTxtNombreActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_jTxtNombreActionPerformed

    private void jTxtIDActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jTxtIDActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_jTxtIDActionPerformed

    private void jBtnCrearActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jBtnCrearActionPerformed
        crearCategoria(jTxtNombre.getText());
    }//GEN-LAST:event_jBtnCrearActionPerformed

    private void jBtnEliminarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jBtnEliminarActionPerformed
        // TODO add your handling code here:
        eliminarCategoria(jTxtID.getText());
    }//GEN-LAST:event_jBtnEliminarActionPerformed

    private void jMnMarcasActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jMnMarcasActionPerformed
        // TODO add your handling code here:

    }//GEN-LAST:event_jMnMarcasActionPerformed

    private void jMnMarcasMouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_jMnMarcasMouseClicked
        // TODO add your handling code here:
        InterfaceBrands fram2 = new InterfaceBrands();
        fram2.setVisible(true);
        this.setVisible(false);
    }//GEN-LAST:event_jMnMarcasMouseClicked

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(InterfaceCategories.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(InterfaceCategories.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(InterfaceCategories.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(InterfaceCategories.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new InterfaceCategories().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton jBtnActualizar;
    private javax.swing.JButton jBtnCrear;
    private javax.swing.JButton jBtnEliminar;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JMenuBar jMenuBar2;
    private javax.swing.JMenu jMnCategorias;
    private javax.swing.JMenu jMnMarcas;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JTable jTabla;
    private javax.swing.JTextField jTxtID;
    private javax.swing.JTextField jTxtNombre;
    // End of variables declaration//GEN-END:variables
}
