import pytest

from catinabox import cattery


@pytest.fixture(params=[cattery.Cattery])
def c(request):
    return request.param()


###########################################################################
# add_cats
###########################################################################

def test__add_cats__succeeds(c):
    c = cattery.Cattery()
    c.add_cats(["Fluffy", "Snookums"])
    assert c.cats == ["Fluffy", "Snookums"]
    assert c.num_cats == 2


###########################################################################
# remove_cat
###########################################################################

def test__remove_cat__succeeds(c):
    c = cattery.Cattery()
    c.add_cats(["Fluffy", "Junior"])
    c.remove_cat("Fluffy")
    assert c.cats == ["Junior"]
    assert c.num_cats == 1


def test__remove_cat__no_cats__fails(c):
    c = cattery.Cattery()
    with pytest.raises(cattery.CatNotFound):
        c.remove_cat("Fluffles")


def test__remove_cat__cat_not_in_cattery__fails(c):
    c = cattery.Cattery()
    c.add_cats(["Fluffy"])
    with pytest.raises(cattery.CatNotFound):
        c.remove_cat("Snookums")
