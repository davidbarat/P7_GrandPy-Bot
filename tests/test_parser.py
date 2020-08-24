from stop_words import stops


def test_delete_stopwords():
    test_search_post = "Je cherche, l'adresse d'Openclassroom"
    # a revoir ponctuation, virgule etc...
    expected_list = ['cherche,', "d'Openclassroom"]
    list_search_post = test_search_post.split(" ")
    clean_search_post = [word for word in list_search_post if word.lower() not in stops]
    print(clean_search_post)
    assert clean_search_post == expected_list