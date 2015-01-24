package com.hcsinergia.controllers;

import java.util.List;

import javax.annotation.PostConstruct;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;

import com.hcsinergia.model.User;
import com.hcsinergia.service.UserService;



@Controller
public class UserController {
	
	//private int id;
	private String name;
	private String surname;
	
	@Autowired
	private UserService userService;
	
	private User user;	
	private User userSelected;
	private User updateUser;
	private User limpiar;
	


	private List<User> users;
	
	@PostConstruct
	public void init(){
		this.user = new User();		
		this.userSelected = new User();
						
	}
	
	public void createUser() {
		userService.insert(user);
		this.user = new User();
	}
	
	public void findUser() {
		User user = new User();
		user.setId(1);
		user = userService.find(user);
	}
	
	public void findAll() {
		users = userService.findAll();
	}
	
	public void updateUser(){
		 userService.updateUser(userSelected);
		 //limpiar();		 
	}
	
	public void limpiar(){
		//user.setId(0);
		user.setName("");
		user.setSurname("");
	}
	

	public User getUser() {
		return user;
	}

	public void setUser(User user) {
		this.user = user;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getSurname() {
		return surname;
	}

	public void setSurname(String surname) {
		this.surname = surname;
	}
	
	public User getUserSelected() {
		return userSelected;
	}

	public void setUserSelected(User userSelected) {
		this.userSelected = userSelected;
	}

	public List<User> getUsers() {
		return users;
	}

	public void setUsers(List<User> users) {
		this.users = users;
	}

	public User getUpdateUser() {
		return updateUser;
	}

	public void setUpdateUser(User updateUser) {
		this.updateUser = updateUser;
	}

	public User getLimpiar() {
		return limpiar;
	}

	public void setLimpiar(User limpiar) {
		this.limpiar = limpiar;
	}

//	public int getId() {
//		return id;
//	}
//
//	public void setId(int id) {
//		this.id = id;
//	}
	
	
	
}
