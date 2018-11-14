def process_file(file_name):
    """
    Given a file name, returns a list of lists [name, gender, births]
    HINT: https://stackoverflow.com/a/35340988/941742

    :param file_name: a string
    :return: a list of lists, [[name1, gender1, births1], [name2, gender2, births2]...]

    Example:
    process_file('yob1880.txt')
        will return
    [["Mary","F",7065], ["Anna","F",2604],...]

    """

    # Did not use csv because I thought that counted as a third party library
    source_data = open(file_name, 'r',encoding='utf8')
    line_list = source_data.readlines()
    formatted_list = [[line.split(',')[0], line.split(',')[1], int(line.strip('\n').split(',')[2])] for line in line_list]
    source_data.close()
    return formatted_list

def total_births(year):
    """

    :param year: an integer, between 1880 and 2010
    :return: an integer, the total births of all the babies in that year
    """

    file_name = 'babynames/yob' + str(year) + '.txt'
    return sum([entry[2] for entry in process_file(file_name)])

def proportion(name, gender, year):
    """

    :param name: a string, first name
    :param gender: a string, "F" or "M"
    :param year: an integer, between 1880 and 2010
    :return: a floating number, the proportion of babies with the given name to total births in given year
    """
    
    file_name = 'babynames/yob' + str(year) + '.txt'
    year_data = process_file(file_name)
    individual_births = [data[2] for data in year_data if data[0] == name and data[1] == gender][0]
    return individual_births / total_births(1940)

    # delete this line and replace with your code here


def highest_year(name, gender):
    """

    :param name: a string
    :param gender: a string, "F" or "M"
    :return: an integer, the year when the given name has the highest proportion over the years (among all the proportions of the same name in different years)
    """
    year_proportions = {year:proportion(name,gender,year) for year in range(1880,2011)}
    return max(year_proportions, key=year_proportions.get)
    

def main():
    print(highest_year('Aaron','M'))

if __name__ == '__main__':
    main()
