def make_division_by(n):
    """This closure returns a function that returns the division
       of an x number by n 
    """
    # You have to code here!
    def division_number(x):
        assert type(x) == int,'Solo Puedes enviar numeros'
        assert n > 0, 'El divisor no puede ser 0'
        return x/n
    return division_number


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))  # The expected output is 6

    division_by_5 = make_division_by(5)
    print(division_by_5(100))  # The expected output is 20

    division_by_18 = make_division_by(18)
    print(division_by_18(54))  # The expected output is 3


if __name__ == '__main__':
    import unittest

    class ClosureSuite(unittest.TestCase):
        def test_closure_make_division_by(self):
            self.num_division = {
                40: [120,3],
                15: [45,3],
                35: [525,15]
            }

            def test_division_number_closures(self):
                for key,value in self.num_division.items():
                    division_by_number = make_division_by(value[1])
                    self.assertEqual(key,division_by_number(value[0]))
            
            def tearDown(self):
                    del(self.num_division)

    #unittest.main()
    run()
