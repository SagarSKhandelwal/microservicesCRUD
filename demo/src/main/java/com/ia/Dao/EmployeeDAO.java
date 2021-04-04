package com.ia.Dao;

import java.util.ArrayList;

import com.ia.model.Employee;

public interface EmployeeDAO {

	//Insert employee data
	public boolean insertEmployeeData(Employee  employee);
	
	//Retrive employee list
	public ArrayList<Employee> getEmployeeData();
	
	
}
