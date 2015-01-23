package com.hcsinergia.service;

import java.util.List;

import com.hcsinergia.model.User;

public interface UserService {
	
	void insert (User user);
	
	User find(Integer idUser);
	
	List<User> findAll();

	User updateUser(User user);
	
}
