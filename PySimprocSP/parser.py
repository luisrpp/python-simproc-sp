# -*- coding: utf-8 -*-
"""
    File name: parser.py
    Author: Luis Roberto Pereira de Paula
    Date created: 2015-11-20
    Date last modified: 2015-11-20
"""

from bs4 import BeautifulSoup
import re


class SimprocHtmlParser(object):
    """
    This class parses the content of the Simproc process details page,
    from the following URL: http://www3.prodam.sp.gov.br/simproc/navega.asp

    To be able to parse the content, this class expects to receive the HTML
    response from the web-page in string format.
    """

    def __init__(self, data):
        """
        :param data: HTML response from the Simproc process details page, as string.
        """

        self.__soup = BeautifulSoup(data, "html.parser")
        self.__response = {'missing_fields': list()}

    def __has_errors(self):
        error_message = self.__soup.find('font', attrs={'color': 'Red'})

        if error_message:
            self.__response['has_errors'] = True
            self.__response['error_message'] = error_message.text.strip().replace(':', '')
        else:
            self.__response['has_errors'] = False

        return self.__response['has_errors']

    def __find_process_number(self):
        try:
            process_number = self.__soup.find(text='Processo:').findNext('td').text.strip()
            if process_number:
                self.__response['process_number'] = process_number
            else:
                raise ValueError('process_number is empty')
        except:
            self.__response['missing_fields'].append('process_number')

    def __find_unit(self):
        try:
            unit = self.__soup.find(text='Unidade:').findNext('td').text.strip()
            if unit:
                self.__response['unit'] = unit
            else:
                raise ValueError('unit is empty')
        except:
            self.__response['missing_fields'].append('unit')

    def __find_complete_unit(self):
        try:
            complete_unit = self.__soup.find(text='Unidade:').parent.findNext('tr').text.strip()
            if complete_unit:
                self.__response['complete_unit'] = complete_unit
            else:
                raise ValueError('complete_unit is empty')
        except:
            self.__response['missing_fields'].append('complete_unit')

    def __find_since(self):
        try:
            since = self.__soup.find(text='Desde:').findNext('td').text[3:].strip()
            if since:
                self.__response['since'] = since
            else:
                raise ValueError('since is empty')
        except:
            self.__response['missing_fields'].append('since')

    def __find_status_date(self):
        try:
            status_date = self.__soup.find(text='Situação:').findNext('td').text.strip()
            if status_date:
                self.__response['status_date'] = status_date
            else:
                raise ValueError('status_date is empty')
        except:
            self.__response['missing_fields'].append('status_date')

    def __find_status(self):
        try:
            status = self.__soup.find(text='Situação:').findNext('td').findNext('td').text.strip()
            if status:
                self.__response['status'] = status
            else:
                raise ValueError('status is empty')
        except:
            self.__response['missing_fields'].append('status')

    def __find_subject(self):
        try:
            subject = self.__soup.find(text='Assunto:').findNext('td').contents[0].text.strip()
            if subject:
                self.__response['subject'] = subject
            else:
                raise ValueError('subject is empty')
        except:
            self.__response['missing_fields'].append('subject')

    def __find_reason(self):
        try:
            reason = self.__soup.find(text='Assunto:').findNext('tr').findNext('tr').text.strip()
            if reason:
                self.__response['reason'] = reason
            else:
                raise ValueError('reason is empty')
        except:
            self.__response['missing_fields'].append('reason')

    def __find_interested(self):
        try:
            interested = self.__soup.find(text='Interessado:').findNext('td').text.strip()
            if interested:
                self.__response['interested'] = interested
            else:
                raise ValueError('interested is empty')
        except:
            self.__response['missing_fields'].append('interested')

    def __find_requested_subjects(self):
        try:
            requested_subjects = self.__soup.find(text=re.compile('ASSUNTOS SOLICITADOS')).findNext('td').findNext(
                'td').findNext('td').text.strip()
            if requested_subjects:
                self.__response['requested_subjects'] = requested_subjects
            else:
                raise ValueError('requested_subjects is empty')
        except:
            self.__response['missing_fields'].append('requested_subjects')

    def __find_request_status(self):
        try:
            request_status = self.__soup.find(text=re.compile('ASSUNTOS SOLICITADOS')).findNext('td').findNext(
                'td').findNext('td').findNext('td').findNext('td').text.strip()
            if request_status:
                self.__response['request_status'] = request_status
            else:
                raise ValueError('request_status is empty')
        except:
            self.__response['missing_fields'].append('request_status')

    def parse(self):
        """
        Parses the content of the Simproc process details page.

        :return: a dictionary with extracted fields.
        """

        if not self.__has_errors():
            self.__find_process_number()
            self.__find_unit()
            self.__find_complete_unit()
            self.__find_since()
            self.__find_status_date()
            self.__find_status()
            self.__find_subject()
            self.__find_reason()
            self.__find_interested()
            self.__find_requested_subjects()
            self.__find_request_status()

        return self.__response
