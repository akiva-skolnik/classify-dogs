def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs: bool = False, print_incorrect_breed: bool = False):
    """
    Prints summary results on the classification and then prints incorrectly
    classified dogs and incorrectly classified dog breeds if user indicates
    they want those printouts (use non-default values)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and
                            0 = pet Image 'is-NOT-a' dog.
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image
                            'as-a' dog and 0 = Classifier classifies image
                            'as-NOT-a' dog.
      results_stats_dic - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value
      model - Indicates which CNN model architecture will be used by the
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and
                             False doesn't print anything(default) (bool)
      print_incorrect_breed - True prints incorrectly classified dog breeds and
                              False doesn't print anything(default) (bool)
    Returns:
           None - simply printing results.
    """
    LABEL = 0
    CLASSIFIER_LABEL = 1
    IS_MATCH = 2
    IS_DOG = 3
    IS_CLASSIFIER_DOG = 4

    print()
    print("Model used: {}".format(model))

    if print_incorrect_dogs and (
            results_stats_dic["n_correct_dogs"] + results_stats_dic["n_correct_notdogs"] != results_stats_dic[
        "n_images"]):
        print()
        print("Incorrectly classified dogs:")
        for value in results_dic.values():
            if value[IS_DOG] != value[IS_CLASSIFIER_DOG]:
                print("Pet image label: {} | Classifier label: {}".format(value[LABEL], value[CLASSIFIER_LABEL]))

    if print_incorrect_breed and results_stats_dic["n_correct_dogs"] != results_stats_dic["n_correct_breed"]:
        print()
        print("Incorrectly classified breeds:")
        for value in results_dic.values():
            if value[IS_DOG] and value[IS_CLASSIFIER_DOG] and not value[IS_MATCH]:
                print("Pet image label: {} | Classifier label: {}".format(value[LABEL], value[CLASSIFIER_LABEL]))

    print()
    print("Number of images: {}".format(results_stats_dic["n_images"]))
    print("Number of dog images: {}".format(results_stats_dic["n_dogs_img"]))
    print("Number of not-dog images: {}".format(results_stats_dic["n_notdogs_img"]))
    print("Percentage of correct matches: {}".format(results_stats_dic["pct_match"]))
    print("Percentage of correctly classified dogs: {}".format(results_stats_dic["pct_correct_dogs"]))
    print("Percentage of correctly classified dog breeds: {}".format(results_stats_dic["pct_correct_breed"]))
    print("Percentage of correctly classified not-dogs: {}".format(results_stats_dic["pct_correct_notdogs"]))
