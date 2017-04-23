#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy.orm import sessionmaker

import orm_multi_fk

Session_class = sessionmaker(bind=orm_multi_fk.engine)
Session = Session_class()  # 生成session实例

# # 添加
# addr1 = orm_multi_fk.Address(street='33-34 72nd St', city='Brooklyn',
#                              state='NewYork')
# addr2 = orm_multi_fk.Address(street='Jackson Heights', city='Queens',
#                              state='NewYork')
# addr3 = orm_multi_fk.Address(street='New York 11372', city='Staten Island',
#                              state='NewYork')
# Session.add_all([addr1, addr2, addr3])
#
# c1 = orm_multi_fk.Customer(name='Jack', billing_address=addr1,
#                            shipping_address=addr2)
# c2 = orm_multi_fk.Customer(name='Lucy', billing_address=addr3,
#                            shipping_address=addr3)
# Session.add_all([c1, c2])

# 查询
obj = Session.query(orm_multi_fk.Customer).filter(
    orm_multi_fk.Customer.name == 'Jack').first()
print(obj.name)
print(obj.billing_address)
print(obj.shipping_address)

Session.commit()
