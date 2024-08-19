# Pagination

This project focused on implementing pagination techniques for REST APIs.I worked on both simple pagination and pagination with hypermedia metadata, ensuring that my solutions are robust and deletion-resilient.

# Learning Objectives

By the end of this project, I was able to:

  - Paginate a dataset using basic page and page_size parameters.

  - Implement pagination with hypermedia metadata to provide navigational information in responses.

  - Ensure pagination is deletion-resilient, meaning it can handle changes to the dataset without breaking.

# Tasks 📃.

# 0. Simple helper function

  - <u>[0-simple_helper_function.py]()</u>: Python function named index_range that takes two integer arguments page and page_size.

# 1. Simple pagination

  - <u>[1-simple_pagination.py]()</u>: Python file that copy index_range from the previous task.

#  2. Hypermedia pagination

  - <u>[2-hypermedia_pagination.py]()</u>: Implement a get_hyper method that takes the same arguments (and defaults) as get_page.

# 3. Deletion-resilient hypermedia pagination

  - <u>[3-hypermedia_del_pagination.py]()</u>: Implement a get_hyper_index method with two integer arguments: index with a None default value and page_size with default value of 10.
