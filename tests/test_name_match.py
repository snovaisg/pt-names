def test_import():
    from pt_names.pt_name_gen import Person
    from pt_names.pt_name_gen import read_names_from_csv
    from pt_names.pt_name_gen import generate_name
    return

def test_generate_name():
    from pt_names.pt_name_gen import generate_name
    from pt_names.pt_name_gen import Person
    import random
    # set random seed
    random.seed(0)
    # generate a name

    person = generate_name()

    assert isinstance(person, Person)
    return
    


from pt_names.gender_classifier import GenderClassifier