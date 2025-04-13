import pytest
from shapes import Rectangle


class TestRectangle1:
    rect = Rectangle(8, 2)

    def test_initialization(self):
        assert self.rect.get_length() == 8
        assert self.rect.get_width() == 2
        assert self.rect.number_of_sides() == 4

    def test_set_width_n_length(self):
        self.rect.set_length(16)
        self.rect.set_width(4)

        assert self.rect.get_length() == 16
        assert self.rect.get_width() == 4

    def test_get_length_n_width(self):
        assert self.rect.get_length() == 16 # because rect is a class attribute
        assert self.rect.get_width() == 4


class TestRectangle2:

    # such that i dont pass the fixture to every test function
    # the fixture can be accessed via self as an instance attribute
    @pytest.fixture(autouse=True) 
    def set_up_rect(self):
        self.rect = Rectangle(8, 2)

    def test_initialization(self):
        assert self.rect.get_length() == 8
        assert self.rect.get_width() == 2
        assert self.rect.number_of_sides() == 4

    def test_set_width_n_length(self):
        self.rect.set_length(16)
        self.rect.set_width(4)

        assert self.rect.get_length() == 16
        assert self.rect.get_width() == 4

    def test_get_length_n_width(self):
        assert self.rect.get_length() == 8  # because rect is a instance attribute
        assert self.rect.get_width() == 2


class TestRectangle22:

    # such that i dont pass the fixture to every test function
    # the fixture can be accessed via self as an instance attribute
    @pytest.fixture(scope="class", autouse=True)
    def set_up_rect(self, request):
        request.cls.rect = Rectangle(8, 2)

    def test_initialization(self):
        assert self.rect.get_length() == 8
        assert self.rect.get_width() == 2
        assert self.rect.number_of_sides() == 4

    def test_set_width_n_length(self):
        self.rect.set_length(16)
        self.rect.set_width(4)

        assert self.rect.get_length() == 16
        assert self.rect.get_width() == 4

    def test_get_length_n_width(self):
        assert self.rect.get_length() == 16  # because rect is a class attribute
        assert self.rect.get_width() == 4


class TestRectangle3:

    # cant access the fixture via self, i have to pass to the test functions that need it
    @pytest.fixture
    def rect(self):
        return Rectangle(8, 2)

    def test_initialization(self, rect):
        assert rect.get_length() == 8
        assert rect.get_width() == 2
        assert rect.number_of_sides() == 4

    def test_set_width_n_length(self, rect):
        rect.set_length(16)
        rect.set_width(4)

        assert rect.get_length() == 16
        assert rect.get_width() == 4

    def test_get_length_n_width(self, rect):
        assert rect.get_length() == 8
        assert rect.get_width() == 2


class TestRectangle33:

    # cant access the fixture via self, i have to pass to the test functions that need it
    @pytest.fixture(scope="class")
    def rect(self):
        return Rectangle(8, 2)

    def test_initialization(self, rect):
        assert rect.get_length() == 8
        assert rect.get_width() == 2
        assert rect.number_of_sides() == 4

    def test_set_width_n_length(self, rect):
        rect.set_length(16)
        rect.set_width(4)

        assert rect.get_length() == 16
        assert rect.get_width() == 4

    def test_get_length_n_width(self, rect):
        assert rect.get_length() == 16 # because the scope of the fixture has been set to `class`
        assert rect.get_width() == 4


class TestRectangle4:

    def test_initializing_with_equal_sides(self):
        with pytest.raises(ValueError) as exec_info:
            rect = Rectangle(8, 8)

        assert str(exec_info.value) == "Rectangle cannot have length equal to width"
