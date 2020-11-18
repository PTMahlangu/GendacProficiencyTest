
import requests
import json
from  requests.exceptions import HTTPError

def _url(path):
    return 'http://gendacproficiencytest.azurewebsites.net/api/ProductsAPI' + path


def get_all_products():
    """ This method Get a List of all the products """
    try:
        response = requests.get(_url(''))
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as errh:
        return "An Http Error occurred:" + repr(errh)
    except requests.exceptions.ConnectionError as errc:
        return "An Error Connecting to the API occurred:" + repr(errc)
    except requests.exceptions.Timeout as errt:
        return "A Timeout Error occurred:" + repr(errt)
    except requests.exceptions.RequestException as err:
        return "An Unknown Error occurred" + repr(err)


def retrieve_specific_product(id):
    """ This method Retrieve a specific Product. """
    try:
        response = requests.get(_url('/{}/'.format(id)))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as errh:
        return "An Http Error occurred:" + repr(errh)
    except requests.exceptions.ConnectionError as errc:
        return "An Error Connecting to the API occurred:" + repr(errc)
    except requests.exceptions.Timeout as errt:
        return "A Timeout Error occurred:" + repr(errt)
    except requests.exceptions.RequestException as err:
        return "An Unknown Error occurred" + repr(err)

def delete_product(id):
    """ This method Delete an existing Product """  

    try:
        response = requests.delete(_url('/{:d}/'.format(id)))
        response.raise_for_status()
        return response.status_code
    except requests.exceptions.HTTPError as errh:
        return "An Http Error occurred:" + repr(errh)
    except requests.exceptions.ConnectionError as errc:
        return "An Error Connecting to the API occurred:" + repr(errc)
    except requests.exceptions.Timeout as errt:
        return "A Timeout Error occurred:" + repr(errt)
    except requests.exceptions.RequestException as err:
        return "An Unknown Error occurred" + repr(err)


def add_new_product(name, category,price):
    """ This method Add a new Product. """  

    try:
        response = requests.post(_url(''), json={
        'Name': name,
        'Category': category,
        'Price' :price,
        })
        response.raise_for_status()
        return response.status_code
    except requests.exceptions.HTTPError as errh:
        return "An Http Error occurred:" + repr(errh)
    except requests.exceptions.ConnectionError as errc:
        return "An Error Connecting to the API occurred:" + repr(errc)
    except requests.exceptions.Timeout as errt:
        return "A Timeout Error occurred:" + repr(errt)
    except requests.exceptions.RequestException as err:
        return "An Unknown Error occurred" + repr(err)


def update_product(id, name, category,price):
    """ This method Update an existing Product """ 
    url = _url('/{:d}/'.format(id))
    try:
        response = requests.put(url, json={
        'Name': name,
        'Category':category,
        'Price': price,
        })
        response.raise_for_status()
        return response.status_code
    except requests.exceptions.HTTPError as errh:
        return "An Http Error occurred:" + repr(errh)
    except requests.exceptions.ConnectionError as errc:
        return "An Error Connecting to the API occurred:" + repr(errc)
    except requests.exceptions.Timeout as errt:
        return "A Timeout Error occurred:" + repr(errt)
    except requests.exceptions.RequestException as err:
        return "An Unknown Error occurred" + repr(err)


def get_page(page,pageSize,orderBy,ascending,filter=''):
    """ This method retrieves a paged, ordered and filtered result set of products """ 
    url = "?page={page}&pageSize={pageSize}&orderBy={orderBy}&ascending={ascending}&filter={filter}".format(page=page,pageSize=pageSize,orderBy=orderBy,ascending=ascending,filter=filter)
    url = _url(url)

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as errh:
        return "An Http Error occurred:" + repr(errh)
    except requests.exceptions.ConnectionError as errc:
        return "An Error Connecting to the API occurred:" + repr(errc)
    except requests.exceptions.Timeout as errt:
        return "A Timeout Error occurred:" + repr(errt)
    except requests.exceptions.RequestException as err:
        return "An Unknown Error occurred" + repr(err)


        


if __name__ == '__main__':

    print(""" Reply with a number to perform a query:
    1. Get all products.
    2. Retrieve a specific product with an Id.
    3. Delete a specific product with an Id.
    4. Update a product with an Id.
    5. Add a product.
    6. Get pages.
     """)
    query = int(input('Perform a query (i.e 3 to delete a product): '))
    while query !=7:
        if query ==7:
            break
        elif query == 1:
            rep = get_all_products()
            print()
            for items in range(len(rep.json())):
                print(rep.json()[items])

        elif query == 2:
            id = int(input("Input product id: "))
            print()
            rep = retrieve_specific_product(id)
            print(rep)

        elif query == 3:
            id = int(input("Input product id: "))
            print()
            rep = delete_product(id)
            if rep != 200:
                print(rep)
            else:
                print("Product with id={} succefuly deleted.".format(id))
            

        elif query == 4:
            id = int(input("Input product id: "))
            name = input("Input product name: ")
            category = int(input("Input product category: "))
            price = float(input("Input product price: "))
            print()
            rep = update_product(id,name,category,price)
            if rep !=200:
                print(rep)
            else:
                print("Product was succefuly updated.")

        elif query == 5:
            name = input("Input product name: ")
            category = int(input("Input product category: "))
            price = float(input("Input product price: "))
            print()
            rep = add_new_product(name,category,price)
            if rep !=200:
                print(rep)
            else:
                print("Product was succefuly added.")

        elif query == 6:
            page = int(input("Input page: "))
            pagesize = int(input("Input page size: "))
            orderBy = input("Orderby : ")
            ascending = bool(input("Ascending (true/false): "))
            print()
            rep = get_page(page,pagesize,orderBy,ascending,'')
            print(rep.json())
        query = int(input('\nPerform a query (i.e 3 to delete a product): '))
