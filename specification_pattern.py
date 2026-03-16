#!/usr/bin/env python3
"""Specification pattern — composable boolean predicates."""
class Spec:
    def is_satisfied(self,item):raise NotImplementedError
    def __and__(self,other):return AndSpec(self,other)
    def __or__(self,other):return OrSpec(self,other)
    def __invert__(self):return NotSpec(self)
class AndSpec(Spec):
    def __init__(self,a,b):self.a=a;self.b=b
    def is_satisfied(self,item):return self.a.is_satisfied(item) and self.b.is_satisfied(item)
class OrSpec(Spec):
    def __init__(self,a,b):self.a=a;self.b=b
    def is_satisfied(self,item):return self.a.is_satisfied(item) or self.b.is_satisfied(item)
class NotSpec(Spec):
    def __init__(self,s):self.s=s
    def is_satisfied(self,item):return not self.s.is_satisfied(item)
class MinAge(Spec):
    def __init__(self,age):self.age=age
    def is_satisfied(self,item):return item.get("age",0)>=self.age
class HasRole(Spec):
    def __init__(self,role):self.role=role
    def is_satisfied(self,item):return self.role in item.get("roles",[])
def main():
    spec=MinAge(18) & HasRole("admin")
    users=[{"name":"Alice","age":25,"roles":["admin"]},{"name":"Bob","age":16,"roles":["admin"]},{"name":"Carol","age":30,"roles":["user"]}]
    for u in users: print(f"{u['name']}: {spec.is_satisfied(u)}")
if __name__=="__main__":main()
