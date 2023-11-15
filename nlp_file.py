"""
© 2017 Hoàng Lê Hải Thanh (Thanh Hoang Le Hai) aka GhostBB
If there are any problems, contact me at mail@hoanglehaithanh.com or 1413492@hcmut.edu.vn 
This project is under [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0) (Inherit from NLTK)
"""

file_name=["output_a.txt",
           "output_b.txt",
           "output_c.txt",
           "output_d.txt",
           "output_e.txt"]

def write_file(question_number, content):
    with open(file_name[question_number-1], 'w', encoding='utf-8') as file:
        file.write(content)
    