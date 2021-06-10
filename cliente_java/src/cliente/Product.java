/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package cliente;

import java.io.Serializable;

/**
 *
 * @author carri
 */
public class Product {
    private int id_pro, id_cat_pro, id_bra_pro;
    private String nam_pro, des_pro;
    double pri_pro; 

    public int getId_pro() {
        return id_pro;
    }

    public void setId_pro(int id_pro) {
        this.id_pro = id_pro;
    }

    public int getId_cat_pro() {
        return id_cat_pro;
    }

    public void setId_cat_pro(int id_cat_pro) {
        this.id_cat_pro = id_cat_pro;
    }

    public int getId_bra_pro() {
        return id_bra_pro;
    }

    public void setId_bra_pro(int id_bra_pro) {
        this.id_bra_pro = id_bra_pro;
    }

    public String getNam_pro() {
        return nam_pro;
    }

    public void setNam_pro(String nam_pro) {
        this.nam_pro = nam_pro;
    }

    public String getDes_pro() {
        return des_pro;
    }

    public void setDes_pro(String des_pro) {
        this.des_pro = des_pro;
    }

    public double getPri_pro() {
        return pri_pro;
    }

    public void setPri_pro(double pri_pro) {
        this.pri_pro = pri_pro;
    }

}
