package com.hcsinergia.service.impl;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.hcsinergia.dao.UserDao;
import com.hcsinergia.model.User;
import com.hcsinergia.service.UserService;

@Service
public class UserServiceImpl implements UserService{

	@Autowired
	private UserDao dao;
	
	@Override
	public void insert(User user) {
		dao.insert(user);		
	}

	@Override
	public User find(User user) {
		return dao.findById(user);
	}
	
	@Override
	public List<User> findAll() {
		return dao.find();
	}
	
	@Override
	public User updateUser(User user){
		return dao.update(user);
	}

}
