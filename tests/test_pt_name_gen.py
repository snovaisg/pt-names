def test_import():
    from pt_names.gender_classifier import GenderClassifier
    return

def test_classify_gender():
    from pt_names.gender_classifier import GenderClassifier

    clf = GenderClassifier()
    
    assert clf("Victor") == "M"
    assert clf("Simao") == "M"
    assert clf("Joana sá costa") == "F", f"expected F, got {clf('Joana sá costa')}"
    assert clf("mariana da silva basto") == "F", f"expected F, got {clf('mariana da silva basto')}"
    return