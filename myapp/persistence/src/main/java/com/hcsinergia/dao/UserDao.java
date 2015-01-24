package com.hcsinergia.dao;

import java.util.List;

import com.hcsinergia.model.User;

public interface UserDao {

	public void insert(User user);

	public List<User> find();

	public User findById(User user);

	public User update(User user);

}
