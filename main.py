# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# p = Person('A', 18)
# print(p.name)
# print(p.age)
# n = input("Qaysi attributga kirishni xohlaysiz: ")
# print(getattr(p, n, "Bunaqasi yo'q"))
# n = input("Qaysi atributni o'zgartirmoqchisiz: ")
# print(getattr(p, n, f"Bunaqa attribut yoq...{p}"))
# if hasattr(p, n):
#     value = input("Buni nimaga o'zgartirmoqchisiz: ")
#     setattr(p, n, value)
#     print(f"Yangi {n}: {getattr(p, n)}")
# else:
#     print("!!")
# print(p.name)
# print(p.age)


# class T:
#     pass


# class A:
#     pass
#
#
# class B(A):
#     pass
#
#
# class C(B, T):
#     pass
#
#
# print(T.__base__)
# print(A.__bases__)
# print(B.__bases__)
# print(C.__bases__)

"""Overloding"""
import asyncio
import operator

# class A:
#     def add(self, *args):
#         return sum(args)
#
#
# a = A()
#
# print(a.add(1, 2, 3, 4))
# print(a.add(1, 2, 3, 4, 5))

"""Overriding"""

# class A:
#     def add(self, B, C):
#         pass
#
#     def add2(self, B, C):
#         pass
#
#
# object = A()
#
# print(object.add())

# async def main():

#     await asyncio.sleep(4)
#     print("Hello World")

#     await asyncio.sleep(2)
#     print("Goodbye World")

# asyncio.run(main())


import asyncio
import operator


class Interpreter:
    def __init__(self):
        self.variables = {}
        self.operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

    async def evaluate(self, expression):
        tokens = expression.split()
        if '=' in tokens:
            return await self.assign_variable(tokens)
        elif tokens[0] == 'print':
            return await self.print_expression(tokens[1:])
        else:
            return await self.evaluate_expression(tokens)

    async def assign_variable(self, tokens):
        var_name = tokens[0]
        value = await self.evaluate_expression(tokens[2:])
        self.variables[var_name] = value
        return f"{var_name} Uchun {value} tayinlandi"

    async def print_expression(self, tokens):
        result = await self.evaluate_expression(tokens)
        return f"Natija: {result}"

    async def evaluate_expression(self, tokens):
        if len(tokens) == 1:
            return self.get_value(tokens[0])

        left = self.get_value(tokens[0])
        operation = self.operations[tokens[1]]
        right = self.get_value(tokens[2])
        return operation(left, right)

    def get_value(self, token):
        try:
            return float(token)
        except ValueError:
            return self.variables.get(token, 0)


class AsyncInterpreter:
    def __init__(self):
        self.interpreter = Interpreter()

    async def run(self):
        while True:
            try:
                expression = await asyncio.get_event_loop().run_in_executor(
                    None, input, "Ifodarni kiritishingz mumkun (chiqish uchun (exit)): "
                )
                if expression.lower() == 'exit':
                    break
                result = await self.interpreter.evaluate(expression)
                print(result)
            except Exception as e:
                print(f"Error: {e}")


async def main():
    interpreter = AsyncInterpreter()
    await interpreter.run()


if __name__ == "__main__":
    asyncio.run(main())
