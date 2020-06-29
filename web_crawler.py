from bs4 import BeautifulSoup
import os.path


def element_absolute_path_output(files, original_element):
    print('File:  Path to the element')
    print('----------------------------')
    for file in files:
        print(file, end=':  ')
        for tag in sample_file_parser(file, original_element):
            print(tag.name, end=' < ')
            for parent in tag.parents:
                if parent is None:
                    print(parent, end=' < ')
                else:
                    print(parent.name, end=' < ')
            print('directory')
            print('----------------------------')


def origin_file_parser(file='pages/sample-0-origin.html', element_id='make-everything-ok-button'):
    if os.path.isfile(file):
        with open(file, 'r') as f:
            contents = f.read()
            xml_soup = BeautifulSoup(contents, 'xml')
            element = xml_soup.find('a', id=element_id)
            return element
    else:
        print("Error: File does not appear to exist.")
        return 0


def sample_file_parser(file, original):
    if os.path.isfile(file):
        with open(file, 'r') as f:
            contents = f.read()
            xml_soup = BeautifulSoup(contents, 'xml')
            a_tags = [el for el in xml_soup.find_all('a')]
            tags = []  # I use list, because there may be two or more elements on the page which we need
            for a_tag in a_tags:
                if a_tag.attrs.keys() == original.attrs.keys() and \
                        (a_tag['class'] == original['class'] or a_tag['title'] == original['title']):
                    tags.append(a_tag)
            return tags
    else:
        print("Error: File does not appear to exist.")
        return 0


# origin_file_path = input('Enter path to the sample file ')
# other_sample_file_path = input('Enter path to the sample file ')
# origin_element_id = input('Enter origin element id ')

other_samples_file_paths = ['pages/sample-1-evil-gemini.html', 'pages/sample-2-container-and-clone.html',
                            'pages/sample-3-the-escape.html', 'pages/sample-4-the-mash.html']

original_button = origin_file_parser()
del original_button.attrs['id']
element_absolute_path_output(other_samples_file_paths, original_button)

