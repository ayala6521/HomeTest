def check_frequency(dict_of_frequency, pairs):
    final_frequency_lst = []  # the final list of names and frequency
    for item in pairs:
        current_pair_A = item[0]  # the first nickname in the pair
        current_pair_B = item[1]  # the second nickname in the pair

        # calc the frequency of each nickname in the pair
        frequency_of_A = 0
        frequency_of_B = 0
        if current_pair_A in dict_of_frequency.keys():  # if frequency exist for the first nickname
            frequency_of_A = dict_of_frequency[current_pair_A]
        if current_pair_B in dict_of_frequency.keys():  # if frequency exist for the first nickname
            frequency_of_B = dict_of_frequency[current_pair_B]

        # if the final list is empty
        if len(final_frequency_lst) == 0:
            temp_lst = [[current_pair_A, current_pair_B], frequency_of_A + frequency_of_B]
            final_frequency_lst.append(temp_lst)

        # if the final list is not empty we have to check inside the final list
        else:
            is_added = False
            for name_frequency in final_frequency_lst:  # scan the existing list

                # if the first nickname is in the final list and not next to the second
                if current_pair_A in name_frequency[0] and current_pair_B not in name_frequency[0]:

                    # remove the first nickname from the final list and add it again with the second nickname
                    final_frequency_lst.remove(name_frequency)
                    name_frequency[0].append(current_pair_B)
                    name_frequency[1] += frequency_of_B

                    # before we add it again, check if the second nickname is not exist in another place
                    for another_name_frequency in final_frequency_lst:
                        if name_frequency != another_name_frequency:
                            # if the second nickname is exist, combine them
                            if current_pair_B in another_name_frequency[0]:
                                final_frequency_lst.remove(another_name_frequency)
                                name_frequency[0] = list(set(name_frequency[0] + another_name_frequency[0]))
                                name_frequency[1] = name_frequency[1] + another_name_frequency[1] - frequency_of_B

                    # save the changes
                    final_frequency_lst.append(name_frequency)
                    is_added = True
                    break

                # if the second nickname is in the final list and not next to the first
                if current_pair_B in name_frequency[0] and current_pair_A not in name_frequency[0]:

                    # remove the second nickname from the final list and add it again with the first nickname
                    final_frequency_lst.remove(name_frequency)
                    name_frequency[0].append(current_pair_A)
                    name_frequency[1] += frequency_of_A

                    # before we add it again, check if the first nickname is not exist in another place
                    for another_name_frequency in final_frequency_lst:
                        if name_frequency != another_name_frequency:
                            # if the first nickname is exist, combine them
                            if current_pair_A in another_name_frequency[0]:
                                final_frequency_lst.remove(another_name_frequency)
                                name_frequency[0] = list(set(name_frequency[0] + another_name_frequency[0]))
                                name_frequency[1] = name_frequency[1] + another_name_frequency[1] - frequency_of_A

                    # save the changes
                    final_frequency_lst.append(name_frequency)
                    is_added = True
                    break
            # if the pair is not exist at all in the final list, add it as a new pair
            if not is_added:
                temp_lst = [[current_pair_A, current_pair_B], frequency_of_A + frequency_of_B]
                final_frequency_lst.append(temp_lst)  # save the changes

    return final_frequency_lst


# Names that do not have different writing options
def unique_names(dict_of_frequency, duplicates_final_frequency):
    unique_names_list = []
    for name in duplicates_final_frequency:
        for nickname in name[0]:
            unique_names_list.append(nickname)

    for key in dict_of_frequency:
        if key not in unique_names_list:
            duplicates_final_frequency.append([[key], dict_of_frequency[key]])

    return duplicates_final_frequency


def main():
    # read the nicknames pairs from pairs.txt file
    pairs = []
    try:
        with open("pairs.txt", 'r') as file:
            for line in file.readlines():
                current_pair = line.split(",")
                current_pair[1] = current_pair[1].replace("\n", '')
                pairs += [(current_pair[0], current_pair[1])]
    except Exception:
        print("Something went wrong")
        return

    # read the frequency from frequency.txt file
    dict_of_frequency = {}
    try:
        with open("frequency.txt", 'r') as file:
            for line in file.readlines():
                current_name = line.split(":")
                current_name[1] = int(current_name[1].replace("\n", ''))
                dict_of_frequency[current_name[0]] = current_name[1]
    except Exception:
        print("Something went wrong")
        return

    # save the final frequency in final_frequency.txt file
    try:
        with open("final_frequency.txt", 'w') as file:
            duplicates_final_frequency = check_frequency(dict_of_frequency, pairs)
            final_frequency = unique_names(dict_of_frequency, duplicates_final_frequency)
            for name_frequency in final_frequency:
                file.write(','.join(name_frequency[0]) + ":" + str(name_frequency[1]) + "\n")
    except Exception:
        print("Something went wrong")
        return


if __name__ == "__main__":
    # Call the main handler function
    main()
