#!/usr/bin/env python
# -*- coding: utf-8 -*-
##
## Author: Adriano Monteiro Marques <adriano@umitproject.org>
## Author: Diogo Pinheiro <diogormpinheiro@gmail.com>
##
## Copyright (C) 2011 S2S Network Consultoria e Tecnologia da Informacao LTDA
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU Affero General Public License as
## published by the Free Software Foundation, either version 3 of the
## License, or (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Affero General Public License for more details.
##
## You should have received a copy of the GNU Affero General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.
##

from django.utils import simplejson
from google.appengine.api import channel
import logging

     
class NotificationInterface:

    def eventReceived(self, event):
        return NotImplemented


class NotificationSystem:

    subscribers = []

    def registerSubscriber(subscriber):
        if isinstance(subscriber, NotificationInterface):
            NotificationSystem.subscribers.append(subscriber)
        else:
            raise TypeError, 'subscriber doesnt implement notification interface'

    def publishEvent(event):
        logging.info(NotificationSystem.subscribers)
        try:
            for subscriber in NotificationSystem.subscribers:
                subscriber.eventReceived(event)
        except Exception,ex:
            logging.error(ex)

    registerSubscriber = staticmethod(registerSubscriber)
    publishEvent = staticmethod(publishEvent)


class RealtimeBox(NotificationInterface):

    def eventReceived(self, event):
        logging.info("event received on realtimebox")
        try:
            message = simplejson.dumps(event.getDict())
            channel.send_message('realtimebox', message)
        except Exception,ex:
            logging.error(ex)


class RealtimeMap(NotificationInterface):

    def eventReceived(self, event):
        logging.info("event received on realtimemap")
        try:
            message = simplejson.dumps(event.getDict())
            channel.send_message('map', message)
        except Exception,ex:
            logging.error(ex)


realtimeBox = RealtimeBox()
realtimeMap = RealtimeMap()
NotificationSystem.registerSubscriber(realtimeBox)
NotificationSystem.registerSubscriber(realtimeMap)