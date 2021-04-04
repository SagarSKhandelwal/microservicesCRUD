package com.ia.controller;

import java.util.ArrayList;

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import com.ia.Dao.EmployeeDAO;
import com.ia.model.Employee;

@Controller
public class HomeController {
 
	@Autowired
	EmployeeDAO  employeeDAO;
	
	
	@RequestMapping(value="/")
	public String home(Model model,HttpSession session) {
		
		
		return "index";
	}
	
	@RequestMapping(value="/empInsert" , method = RequestMethod.POST )
	@ResponseBody public ArrayList<Employee> empInsert(Employee employee) {
		
		employeeDAO.insertEmployeeData(employee);
		
		return null;
		
	}	
		
	
	 
	
	@RequestMapping(value="/demo/{demoId}/{demoName}" , method = {RequestMethod.POST , RequestMethod.GET})
	@ResponseBody public ArrayList<Employee> demodetails(@PathVariable ("demoId") int testID,@PathVariable("demoName") String demoName ) {
		
		
		/*Employee employee = new Employee();
		employee.setEmpId(1);
		employee.setEmpName("Ankit");
		employee.setPosition("IT");
		employee.setSalary(4000d);*/
		
		//employeeDAO.insertEmployeeData(employee);
		
		 
		
		System.out.println(testID +"-----------"+demoName);
		
		return employeeDAO.getEmployeeData();
	}
	  
	  
}
