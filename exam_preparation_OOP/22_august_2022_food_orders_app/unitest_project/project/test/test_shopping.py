from project.shopping_cart import ShoppingCart
import unittest


class TestShoppingCart(unittest.TestCase):
    def setUp(self) -> None:
        self.shopping_cart = ShoppingCart("Zara", 1000.0)

    def test_init_constructor(self):
        self.assertEqual(self.shopping_cart.shop_name, "Zara")
        self.assertEqual(self.shopping_cart.budget, 1000.0)
        self.assertEqual(self.shopping_cart.products, {})

    def test_shop_name_raises_exception_when_first_value_is_not_capital(self):
        with self.assertRaises(ValueError) as ex:
            test_shop = ShoppingCart("zara", 1000.0)

        self.assertEqual(str(ex.exception), "Shop must contain only letters and must start with capital letter!")

    def test_shop_name_raises_exception_when_name_does_not_contain_only_letters(self):
        with self.assertRaises(ValueError) as ex:
            test_shop = ShoppingCart("Zara1", 1000.0)

        self.assertEqual(str(ex.exception), "Shop must contain only letters and must start with capital letter!")

    def test_add_to_cart_method_when_product_is_too_expensive(self):
        self.assertEqual(self.shopping_cart.products, {})

        with self.assertRaises(ValueError) as ex:
            self.shopping_cart.add_to_cart("hat", 100.1)

        self.assertEqual(str(ex.exception), f"Product hat cost too much!")

        self.assertEqual(self.shopping_cart.products, {})

    def test_add_to_cart_method_successful(self):
        self.assertEqual(self.shopping_cart.products, {})

        result = self.shopping_cart.add_to_cart("hat", 99)

        self.assertEqual(result, f"hat product was successfully added to the cart!")
        self.assertEqual(self.shopping_cart.products, {"hat": 99})

    def test_remove_from_cart_method_raises_exception_when_removing_items_that_not_in_cart(self):
        self.assertEqual(self.shopping_cart.products, {})

        with self.assertRaises(ValueError) as ex:
            self.shopping_cart.remove_from_cart("hat")

        self.assertEqual(str(ex.exception), "No product with name hat in the cart!")

    def test_remove_from_cart_method_successful(self):
        self.shopping_cart.products = {"hat": 99, "blouse": 98}

        result = self.shopping_cart.remove_from_cart("hat")

        self.assertEqual(result, "Product hat was successfully removed from the cart!")
        self.assertEqual(self.shopping_cart.products, {"blouse": 98})


    def test_add_method(self):
        shop_1 = ShoppingCart("Bershka", 1000)
        shop_1.products = {"hat": 50}

        shop_2 = ShoppingCart("Stradivarius", 1500)
        shop_2.products = {"jeans": 70}

        new_shop = shop_1 + shop_2

        self.assertEqual(new_shop.shop_name, "BershkaStradivarius")
        self.assertEqual(new_shop.budget, 2500.0)
        self.assertEqual(new_shop.products, {"hat": 50, "jeans": 70})

    def test_buy_products_raises_exception(self):
        self.shopping_cart.budget = 50
        self.shopping_cart.products = {"hat": 30, "blouse": 70}

        with self.assertRaises(ValueError) as ex:
            self.shopping_cart.buy_products()

        self.assertEqual(str(ex.exception),f"Not enough money to buy the products! Over budget with 50.00lv!")

    def test_buy_product_method_successful(self):
        self.shopping_cart.products = {"hat": 30, "blouse": 70}

        result = self.shopping_cart.buy_products()

        self.assertEqual(result, f'Products were successfully bought! Total cost: 100.00lv.')



if __name__ == "__main__":
    unittest.main()