package com.ia.Impl;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import javax.sql.DataSource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.ia.Dao.EmployeeDAO;
import com.ia.model.Employee;
import com.mysql.jdbc.Statement;

@Component("employeeDAO")
public class EmployeeIMPL implements EmployeeDAO {

	@Autowired
	DataSource dataSource; 
	
	Connection con;
	
	
	@Override
	public boolean insertEmployeeData(Employee employee) {
		// TODO Auto-generated method stub
		
		String sql = "insert into employee (name,salary,position) values(?,?,?)";
		
		try (Connection con = (Connection) dataSource.getConnection()){
			PreparedStatement ps = (PreparedStatement) con.prepareStatement(sql,Statement.RETURN_GENERATED_KEYS);
			ps.setString(1, employee.getEmpName());
			ps.setDouble(2, employee.getSalary());
			ps.setString(3, employee.getPosition());
			ps.executeUpdate();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return false;
		}
		
		
		
		return true;
	}

	@Override
	public ArrayList<Employee> getEmployeeData() {
		// TODO Auto-generated method stub
		ArrayList<Employee> arrayList = new ArrayList<>();
		String sql = "select * from employee";
		
		try (Connection con = (Connection) dataSource.getConnection()){
			PreparedStatement ps = (PreparedStatement) con.prepareStatement(sql);
			
			ResultSet rs = ps.executeQuery();
			while (rs.next()) {
				
				Employee employee= new Employee();
				employee.setEmpId(rs.getInt("employee_id"));
				employee.setEmpName(rs.getString("name"));
				employee.setSalary(rs.getDouble("salary"));
				employee.setPosition(rs.getString("position"));
				arrayList.add(employee);
			}
			con.close();
		
		}catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		
		
		return arrayList;
	}

}
