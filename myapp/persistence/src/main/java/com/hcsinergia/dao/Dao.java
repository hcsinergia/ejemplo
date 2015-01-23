package com.hcsinergia.dao;

import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.persistence.Query;
import javax.persistence.criteria.CriteriaBuilder;
import javax.persistence.criteria.CriteriaQuery;
import javax.persistence.criteria.Root;

import org.hibernate.usertype.UserCollectionType;
import org.springframework.jdbc.object.StoredProcedure;
import org.springframework.stereotype.Repository;

import com.hcsinergia.model.User;

@Repository
public class Dao<T> {
	
	
	@PersistenceContext
    private EntityManager entityManager;
	
	public void insert(T entity) {
		entityManager.persist(entity);
		
	}
	
	@SuppressWarnings("unchecked")
	public List<T> find() {
		Query query = entityManager.createQuery("select u from USER u");
		//Query query = entityManager.createNativeQuery("{call SelectAllUser}");
		
		//List<UserCollectionType> result = query.getResultList();
		//StoredProcedure query = createStoredProcedureQuery("{call SelectAllUser}");
		
		//return (List<T>) query.getResultList();
		
		return query.getResultList();
	}
	
	
	
	public List<T> findAll(Class<T> clazz, Integer idStart, Integer idEnd) {
		CriteriaBuilder cb = entityManager.getCriteriaBuilder();
		CriteriaQuery<T> criteriaQuery = cb.createQuery(clazz);
		Root<T> t = criteriaQuery.from(clazz);
		criteriaQuery.select(t);
		return entityManager.createQuery(criteriaQuery).getResultList();
	}
	
	public T findById(Class<T> clazz, Integer idUser) {
		return entityManager.find(clazz, idUser);
	}
	
	/**
	 * Resibe un objeto T, actualiza en db y lo devuelve actualizado
	 * 
	 * @param entity
	 * @return
	 */
	public T update(T entity) {
		return entityManager.merge(entity);	
	}

}
