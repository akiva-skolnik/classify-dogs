#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#
# PROGRAMMER: Akiva
# DATE CREATED: 18/10/2023
# REVISED DATE:
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results
#          dictionary (results_dic).
#         This function inputs:
#            -The results dictionary as results_dic within print_results
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main.
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.

def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs=False, print_incorrect_breed=False):
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
            results_stats_dic["n_correct_dogs"] + results_stats_dic["n_correct_notdogs"] != results_stats_dic["n_images"]):
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


