package com.hcsinergia.service;

import java.util.List;

import com.hcsinergia.model.User;

public interface UserService {
	
	void insert (User user);
	
	List<User> findAll();

	User updateUser(User user);

	User find(User user);
	
}
