#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    File name: __init__.py
    Author: Luis Roberto Pereira de Paula
    Date created: 2015-11-20
    Date last modified: 2015-11-20
"""

import requests
from requests.exceptions import HTTPError
from parser import SimprocHtmlParser
from settings import SIMPROC_URL, HTTP_CONNECTION_TIMEOUT


def process_details(process_number):
    """
    Gets the details of a Simproc process.

    :param process_number: the Simproc process number
    :return: a dictionary with details of the process
    """

    payload = {
        'numSimproc': process_number,
        'numEtiqueta': '',
        'Button_1': 'PESQUISAR'
    }

    try:
        r = requests.post(SIMPROC_URL, data=payload, timeout=HTTP_CONNECTION_TIMEOUT)

        if r.status_code == 200:
            data = r.text
            response = SimprocHtmlParser(data).parse()
            response['process_number'] = process_number
            return response
        else:
            raise HTTPError('The request returned the following status code: %s' % r.status_code)
    except Exception as e:
        return {
            'process_number': process_number,
            'has_errors': True,
            'error_message': str(e)
        }


if __name__ == '__main__':
    import sys

    try:
        process_number = sys.argv[1]
        print(process_details(process_number))
    except:
        print('Usage: $ python %s <process_number>' % sys.argv[0])
