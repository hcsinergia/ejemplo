package com.hcsinergia.service.impl;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.hcsinergia.dao.Dao;
import com.hcsinergia.model.User;
import com.hcsinergia.service.UserService;

@Service
public class UserServiceImpl implements UserService{

	@Autowired
	private Dao<User> dao;
	
	@Override
	@Transactional
	public void insert(User user) {
		dao.insert(user);		
	}

	@Transactional
	@Override
	public User find(Integer idUser) {
		return dao.findById(User.class, idUser);
	}
	
	@Transactional
	@Override
	public List<User> findAll() {
		return dao.find();
	}
	
	@Transactional
	@Override
	public User updateUser(User user){
		return dao.update(user);
	}

}
