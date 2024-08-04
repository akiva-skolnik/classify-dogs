from time import time

from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from classify_images import classify_images
# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
# Imports print functions that check the lab
from print_functions_for_lab_checks import *
from print_results import print_results


def main():
    start_time = time()

    # This function retrieves 3 Command Line Arugments from user as input from
    # the user running the program from a terminal window. This function returns
    # the collection of these command line arguments from the function call as
    # the variable in_arg
    in_arg = get_input_args()

    # Function that checks command line arguments using in_arg
    check_command_line_arguments(in_arg)

    # This function creates the results dictionary that contains the results,
    # this dictionary is returned from the function call as the variable results
    results = get_pet_labels(in_arg.dir)

    # Function that checks Pet Images in the results Dictionary using results
    check_creating_pet_image_labels(results)

    # Creates Classifier Labels with classifier function, Compares Labels,
    # and adds these results to the results dictionary - results
    classify_images(in_arg.dir, results, in_arg.arch)

    # Function that checks Results Dictionary using results
    check_classifying_images(results)

    # Adjusts the results dictionary to determine if classifier correctly
    # classified images as 'a dog' or 'not a dog'. This demonstrates if
    # model can correctly classify dog images as dogs (regardless of breed)
    adjust_results4_isadog(results, in_arg.dogfile)

    # Function that checks Results Dictionary for is-a-dog adjustment using results
    check_classifying_labels_as_dogs(results)

    # This function creates the results statistics dictionary that contains a
    # summary of the results statistics (this includes counts & percentages). This
    # dictionary is returned from the function call as the variable results_stats
    # Calculates results of run and puts statistics in the Results Statistics
    # Dictionary - called results_stats
    results_stats = calculates_results_stats(results)

    # Function that checks Results Statistics Dictionary using results_stats
    check_calculating_results(results, results_stats)

    # Prints summary results, incorrect classifications of dogs (if requested)
    # and incorrectly classified breeds (if requested)
    print_results(results, results_stats, in_arg.arch, True, True)

    end_time = time()

    tot_time = end_time - start_time  # Calculate difference between end time and start time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time / 3600))) + ":" + str(int((tot_time % 3600) / 60)) + ":"
          + str(int((tot_time % 3600) % 60)))


# Call to main function to run the program
if __name__ == "__main__":
    main()
