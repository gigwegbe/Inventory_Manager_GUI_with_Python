from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5 import QtWidgets 
from PyQt5.QtCore import * 
from PyQt5 import QtCore 
from PyQt5.QtWidgets import QMainWindow 
from PyQt5.QtWidgets import QApplication 


import sys 
from os import path
from PyQt5.uic import loadUiType 

FORM_CLASS, _ = loadUiType(path.join(path.dirname('__file__'), "main.ui"))

import sqlite3 

class Main(QMainWindow, FORM_CLASS): 
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Buttons()
        self.NAVIGATE()
    
    
    def Handel_Buttons(self):
        self.refresh_btn.clicked.connect(self.GET_DATA)
        self.search_btn.clicked.connect(self.SEARCH)
        self.check_btn.clicked.connect(self.LEVEL)
        self.update_btn.clicked.connect(self.UPDATE)
        self.delete_btn.clicked.connect(self.DELETE)
        self.add_btn.clicked.connect(self.ADD)
    

    def GET_DATA(self): 
        db = sqlite3.connect("final_parts_table.db")
        cursor = db.cursor()

        command = ''' SELECT * from data '''
        result = cursor.execute(command)
        self.table.setRowCount(0) 

        for row_number, row_data in enumerate(result): 
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data): 
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        
        cursor2 = db.cursor()
        cursor3 = db.cursor()

        parts_nbr = ''' SELECT COUNT (DISTINCT PartName) from data '''
        ref_nbr = ''' SELECT COUNT (DISTINCT Reference) from data '''

        result_ref_nbr = cursor2.execute(ref_nbr)
        result_part_nbr = cursor3.execute(parts_nbr)

        self.lbl_ref_nbr.setText(str(result_ref_nbr.fetchone()[0]))
        self.lbl_parts_nbr.setText(str(result_part_nbr.fetchone()[0]))

        cursor4 = db.cursor()
        cursor5 = db.cursor()

        min_hole = ''' SELECT MIN(NumberOfHoles), Reference from data'''
        max_hole = ''' SELECT MAX(NumberOfHoles), Reference from data'''

        result_min_hole = cursor4.execute(min_hole)
        result_max_hole = cursor5.execute(max_hole)

        r1 = result_min_hole.fetchone()
        r2 = result_max_hole.fetchone()
    
        self.lbl_min_holes.setText(str(r1[0]))
        self.lbl_max_holes.setText(str(r2[0]))

        self.lbl_min_holes_2.setText(str(r1[1]))
        self.lbl_max_holes_2.setText(str(r2[1]))


    def SEARCH(self): 
        db = sqlite3.connect("final_parts_table.db")
        cursor = db.cursor()

        nbr = int(self.count_filter_txt.text())
        command = ''' SELECT * from data WHERE count <= ?'''
        result = cursor.execute(command,[nbr])
        self.table.setRowCount(0) 

        for row_number, row_data in enumerate(result): 
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data): 
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    

    def LEVEL(self): 
        db = sqlite3.connect("final_parts_table.db")
        cursor = db.cursor()

        command = ''' SELECT Reference, PartName, Count from data order by Count asc LIMIT 3'''
        result = cursor.execute(command)
        self.table2.setRowCount(0) 

        for row_number, row_data in enumerate(result): 
            self.table2.insertRow(row_number)
            for column_number, data in enumerate(row_data): 
                self.table2.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    
    def NAVIGATE(self): 
        db = sqlite3.connect("final_parts_table.db")
        cursor = db.cursor()

        command = ''' SELECT * from data'''
        result = cursor.execute(command)
        val = result.fetchone()

        self.id.setText(str(val[0]))
        self.reference.setText(str(val[1]))
        self.part_name.setText(str(val[2]))
        self.min_area.setText(str(val[3]))
        self.max_area.setText(str(val[4]))
        self.number_of_holes.setText(str(val[5]))
        self.min_diameter.setText(str(val[6]))
        self.max_diameter.setText(str(val[7]))
        self.count.setValue(val[8])
    
    def UPDATE(self): 
        db = sqlite3.connect("final_parts_table.db")
        cursor = db.cursor()

        id_ = int(self.id.text())
        reference_ = self.reference.text()
        part_name_ = self.part_name.text()
        min_area_ = self.min_area.text()
        max_area_ = self.max_area.text()
        number_of_holes_ = self.number_of_holes.text()
        min_diameter_ = self.min_diameter.text()
        max_diameter_ = self.max_diameter.text()
        count_ = str(self.count.value())

        row = (reference_,part_name_,min_area_,max_area_,number_of_holes_,min_diameter_,max_diameter_,count_)
        command = ''' UPDATE data SET Reference=?,PartName=?,MinArea=?,MaxArea=?,NumberOfHoles=?,MinDiameter=?,MaxDiameter=?,Count=?'''
        cursor.execute(command,row)
        db.commit()


    def DELETE(self): 
        db = sqlite3.connect("final_parts_table.db")
        cursor = db.cursor()
        d = self.id.text()

        command = ''' DELETE FROM data WHERE ID=? '''
        cursor.execute(command,d)
        db.commit()


    def ADD(self): 
        db = sqlite3.connect("final_parts_table.db")
        cursor = db.cursor()

        reference_ = self.reference.text()
        part_name_ = self.part_name.text()
        min_area_ = self.min_area.text()
        max_area_ = self.max_area.text()
        number_of_holes_ = self.number_of_holes.text()
        min_diameter_ = self.min_diameter.text()
        max_diameter_ = self.max_diameter.text()
        count_ = str(self.count.value())

        row = (reference_,part_name_,min_area_,max_area_,number_of_holes_,min_diameter_,max_diameter_,count_)
        command = ''' INSERT INTO data(Reference,PartName,MinArea,MaxArea,NumberOfHoles,MinDiameter,MaxDiameter,Count) VALUES (?,?,?,?,?,?,?,?)'''
        cursor.execute(command,row)
        db.commit()




    



def main(): 
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__=='__main__': 
    main()