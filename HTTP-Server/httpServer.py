from socket import *
import datetime
import os
import time
import random
import threading
from _thread import *
import shutil  # to implement delete method
import csv  # used in put and post method to insert data
import base64  # used for decoding autherization header in delete method
import sys
import logging
from config import *  # import variables
import signal  # signal to handle Ctrl+C and other SIGNALS
from supplement.breakdown import *  # to breakdown entity
from supplement.last_modified import *  # last_modified for condi get


class http_methods:
    def response_get_head(self, connectionsocket, entity, switcher, query,
                          method, glob):
        serversocket, file_extension, conditional_get, conn, ip, serverport, scode, IDENTITY, client_thread = glob
        isItFile = os.path.isfile(entity)
        isItDir = os.path.isdir(entity)
        show_response = ''
        if isItFile:
            show_response += 'HTTP/1.1 200 OK'
            scode = 200
            if (os.access(entity, os.R_OK)):
                if (os.access(entity, os.W_OK)):
                    pass
                else:
                    glob = status(connectionsocket, 403,
                                  [ip, client_thread, scode])
                    ip, client_thread, scode = glob
            else:
                glob = status(connectionsocket, 403,
                              [ip, client_thread, scode])
                ip, client_thread, scode = glob
            try:
                size = os.path.getsize(entity)
                f = open(entity, "rb")
                data = f.read(size)
            except:
                glob = status(connectionsocket, 500,
                              [ip, client_thread, scode])
                ip, client_thread, scode = glob
        elif isItDir:
            dir_list = os.listdir(entity)
            show_response += 'HTTP/1.1 200 OK'
            scode = 200
            # if it is a directory
            if os.access(entity, os.R_OK):
                if (os.access(entity, os.W_OK)):
                    pass
                else:
                    glob = status(connectionsocket, 403,
                                  [ip, client_thread, scode])
                    ip, client_thread, scode = glob
            else:
                glob = status(connectionsocket, 403,
                              [ip, client_thread, scode])
                ip, client_thread, scode = glob
            for i in dir_list:
                if i.startswith('.'):
                    dir_list.remove(i)
                else:
                    pass
        else:
            entity = entity.rstrip('/')
            isItDir = os.path.isdir(entity)
            isItFile = os.path.isfile(entity)
            if isItDir:
                scode = 200
                show_response += 'HTTP/1.1 200 OK'
                dir_list = os.listdir(entity)
                entity = entity.rstrip('/')
                if (os.access(entity, os.W_OK)):
                    if (os.access(entity, os.R_OK)):
                        pass
                    else:
                        glob = status(connectionsocket, 403,
                                      [ip, client_thread, scode])
                        ip, client_thread, scode = glob
                else:
                    glob = status(connectionsocket, 403,
                                  [ip, client_thread, scode])
                    ip, client_thread, scode = glob
                for i in dir_list:
                    if i.startswith('.'):
                        dir_list.remove(i)
                    else:
                        pass
            elif isItFile:
                show_response += 'HTTP/1.1 200 OK'
                scode = 200
                if (os.access(entity, os.R_OK)):
                    if (os.access(entity, os.W_OK)):
                        pass
                else:
                    glob = status(connectionsocket, 403,
                                  [ip, client_thread, scode])
                    ip, client_thread, scode = glob
                try:
                    size = os.path.getsize(entity)
                    f = open(entity, "rb")
                    data = f.read(size)
                except:
                    # error while accesing the file
                    glob = status(connectionsocket, 500,
                                  [ip, client_thread, scode])
                    ip, client_thread, scode = glob
            else:
                glob = status(connectionsocket, 404,
                              [ip, client_thread, scode])
                ip, client_thread, scode = glob
        show_response += '\r\n' + COOKIE + str(IDENTITY) + MAXAGE
        IDENTITY += random.randint(1, 10)
        for state in switcher:
            if state == 'User-Agent':
                if isItDir:
                    show_response += '\r\nServer: ' + ip
                elif isItFile:
                    l = time.ctime().split(' ')
                    l[0] = l[0] + ','
                    conversation = (' ').join(l)
                    show_response += '\r\nServer: ' + ip
                    conversation = '\r\nDate: ' + conversation
                    show_response += conversation
                    show_response += '\r\n' + last_modified(entity)
                else:
                    pass
            elif state == 'Host':
                pass
            elif state == 'Accept':
                if isItFile:
                    try:
                        file_ext = os.path.splitext(entity)
                        if file_ext[1] in file_extension.keys():
                            conversation = file_extension[file_ext[1]]
                            temp = 0
                        else:
                            conversation = 'text/plain'
                            temp = 1
                        conversation = '\r\nContent-Type: ' + conversation
                        show_response += conversation
                    except:
                        glob = status(connectionsocket, 415,
                                      [ip, client_thread, scode])
                        ip, client_thread, scode = glob
                        # scode = 415
                elif isItDir:
                    conversation = '\r\nContent-Type: text/html'
                    show_response += conversation
                else:
                    pass
            elif state == 'Accept-Language':
                conversation = '\r\nContent-Language: ' + switcher[state]
                show_response += conversation
            elif state == 'Accept-Encoding':
                if isItFile:
                    conversation = '\r\nContent-Length: ' + str(size)
                    show_response += conversation
                else:
                    pass
            elif state == 'Connection':
                if isItFile:
                    conn = True
                    show_response += '\r\nConnection: keep-alive'
                elif isItDir:
                    conn = False
                    show_response += '\r\nConnection: close'
                else:
                    pass
            elif state == 'If-Modified-Since':
                if_modify(switcher[state], entity)
            else:
                continue
        if isItDir and method == 'GET':
            show_response += '\r\n\r\n'
            show_response += '\r\n<!DOCTYPE html>'
            show_response += '\r\n<html>\n<head>'
            show_response += '\r\n<title>Directory listing</title>'
            show_response += '\r\n<meta http-equiv="Content-type" content="text/html;charset=UTF-8" /></head>'
            show_response += '\r\n<body><h1>Directory listing..</h1><ul>'
            for line in dir_list:
                if entity == '/':
                    link = 'http://' + ip + ':' + \
                        str(serverport) + entity + line
                    l = '\r\n<li><a href ="' + link + '">' + line + '</a></li>'
                    show_response += l
                else:
                    link = 'http://' + ip + ':' + \
                        str(serverport) + entity + '/' + line
                    l = '\r\n<li><a href ="' + link + '">' + line + '</a></li>'
                    show_response += l
            show_response += '\r\n</ul></body></html>'
            encoded = show_response.encode()
            connectionsocket.send(encoded)
            connectionsocket.close()
        elif len(query) > 0 and not isItFile and not isItDir:
            show_response = ''
            row = ''
            entity = CSVFILE
            fields = ''
            for d in query:
                fields += d + ','
                for i in query[d]:
                    row += i + ','
            file_exists = os.path.exists(entity)
            if file_exists:
                scode = 200
                show_response += 'HTTP/1.1 200 OK'
                fi = open(entity, "a")
                row = list(row.split(","))
                csvwriter = csv.writer(fi)
                csvwriter.writerow(row)
            else:
                fi = open(entity, "w")
                show_response += 'HTTP/1.1 201 Created'
                scode = 201
                show_response.append('Location: ' + entity)
                csvwriter = csv.writer(fi)
                csvwriter.writerow(fields)
                csvwriter.writerow(row)
            fi.close()
            show_response += '\r\nServer: ' + ip
            show_response += '\r\n' + date()
            f = open(WORKFILE, "rb")
            show_response += '\r\nContent-Language: en-US,en'
            size = os.path.getsize(WORKFILE)
            conversation = '\r\nContent-Length: ' + str(size)
            show_response += '\r\nContent-Type: text/html'
            show_response += conversation
            show_response += '\r\n' + last_modified(entity)
            show_response += '\r\n\r\n'
            encoded = show_response.encode()
            connectionsocket.send(encoded)
            connectionsocket.sendfile(f)
        elif isItFile:
            show_response += '\r\n\r\n'
            if conditional_get == False and method == 'GET':
                encoded = show_response.encode()
                connectionsocket.send(encoded)
                connectionsocket.sendfile(f)
            elif conditional_get == False and method == 'HEAD':
                encoded = show_response.encode()
                connectionsocket.send(encoded)
            elif conditional_get == True and (method == 'GET'
                                              or method == 'HEAD'):
                status_304(connectionsocket, entity, [ip, scode])
        else:
            glob = status(connectionsocket, 400, [ip, client_thread, scode])
            ip, client_thread, scode = glob
        return [
            serversocket, file_extension, conditional_get, conn, ip,
            serverport, scode, IDENTITY
        ]

    def response_post(self, ent_body, connectionsocket, switcher, glob):
        ip, serverport, scode = glob
        show_response = ''
        entity = CSVFILE
        query = parse_qs(ent_body)
        if os.access(entity, os.W_OK):
            pass
        else:
            status(connectionsocket, 403, [ip, client_thread, scode])
        fields = ''
        row = ''
        for d in query:
            fields += d + ', '
            for i in query[d]:
                row += i + ', '
        file_exists = os.path.exists(entity)
        if file_exists:
            fi = open(entity, "a")
            show_response += 'HTTP/1.1 200 OK'
            scode = 200
            csvwriter = csv.writer(fi)
            csvwriter.writerow(row)
        else:
            fi = open(entity, "w")
            show_response += 'HTTP/1.1 201 Created'
            scode = 201
            show_response += '\r\nLocation: ' + entity
            csvwriter = csv.writer(fi)
            csvwriter.writerow(fields)
            csvwriter.writerow(row)
        fi.close()
        show_response += '\r\nServer: ' + ip
        show_response += date()
        f = open(WORKFILE, "rb")
        show_response += '\r\nContent-Language: en-US,en'
        size = os.path.getsize(WORKFILE)
        conversation = 'Content-Length: ' + str(size)
        show_response += '\r\nContent-Type: text/html'
        show_response += '\r\n' + conversation
        show_response += '\r\n' + last_modified(entity)
        show_response += '\r\n\r\n'
        encoded = show_response.encode()
        connectionsocket.send(encoded)
        connectionsocket.sendfile(f)
        return [ip, serverport, scode]

    def response_put(self, connectionsocket, addr, ent_body, filedata, entity,
                     switcher, f_flag, scode, glob):
        ip, client_thread, scode = glob
        try:
            length = int(switcher['Content-Length'])
        except:
            scode = 411
            glob = status(connectionsocket, 411, [ip, client_thread, scode])
            ip, client_thread, scode = glob
        show_response = ''
        try:
            filedata = filedata + ent_body
        except TypeError:
            ent_body = ent_body.encode()
            filedata = filedata + ent_body
        isItFile = os.path.isfile(entity)
        isItDir = os.path.isdir(entity)
        i = len(ent_body)
        size = length - i
        # r = length % SIZE
        # q = int(length // SIZE)
        # isItDir = os.path.isdir(entity)
        # isItFile = os.path.isdir(entity)
        for _ in iter(int, 1):
            if not size > 0:
                break
            ent_body = connectionsocket.recv(SIZE)
            try:
                filedata = filedata + ent_body
            except:
                ent_body = ent_body.encode()
                print("encoding...")
                filedata = filedata + ent_body
            size -= len(ent_body)
        mode_f, r_201, move_p = True, False, False
        limit = len(ROOT)
        l = len(entity)
        if not l < limit:
            if isItFile:
                if os.access(entity, os.W_OK):
                    # no need for read access
                    if os.access(entity, os.R_OK):
                        pass
                    else:
                        pass
                else:
                    glob = status(connectionsocket, 403,
                                  [ip, client_thread, scode])
                    ip, client_thread, scode = glob
                # writing File mode ON
                mode_f = True
                if f_flag == 1:
                    f = open(entity, "wb")
                    f.write(filedata)
                elif f_flag == 0:
                    f = open(entity, "w")
                    f.write(filedata.decode())
                else:
                    f = open(entity, "wb")
                    f.write(filedata)
                f.close()
            elif isItDir:
                move_p = True
                loc = ROOT + '/' + str(addr[1])
                if os.access(entity, os.W_OK):
                    # no need for read access
                    if os.access(entity, os.R_OK):
                        pass
                    else:
                        pass
                else:
                    glob = status(connectionsocket, 403,
                                  [ip, client_thread, scode])
                    ip, client_thread, scode = glob
                try:
                    loc = loc + \
                        file_type[switcher['Content-Type'].split(';')[0]]
                except:
                    glob = status(connectionsocket, 403,
                                  [ip, client_thread, scode])
                    ip, client_thread, scode = glob
                if f_flag == 1:
                    f = open(loc, "wb")
                    f.write(filedata)
                elif f_flag == 0:
                    f = open(loc, "w")
                    f.write(filedata.decode())
                else:
                    f = open(loc, "wb")
                    f.write(filedata)
                f.close()

            else:
                if ROOT in entity:
                    entity = ROOT + '/' + str(addr[1])
                    try:
                        entity = entity + \
                            file_type[switcher['Content-Type'].split(';')[0]]
                    except:
                        # error in header
                        glob = status(connectionsocket, 403,
                                      [ip, client_thread, scode])
                        ip, client_thread, scode = glob
                    if f_flag:
                        f = open(entity, "wb")
                        f.write(filedata)
                    elif f_flag == 0:
                        # open the file in write mode
                        f = open(entity, "w")
                        f.write(filedata.decode())
                    else:
                        # open the file in write binary mode
                        f = open(entity, "wb")
                        f.write(filedata)
                    f.close()
                    r_201 = True
                else:
                    mode_f = False
        else:
            move_p = True
            loc = ROOT + '/' + str(addr[1])
            try:
                loc = loc + file_type[switcher['Content-Type']]
            except:
                glob = status(connectionsocket, 403,
                              [ip, client_thread, scode])
                ip, client_thread, scode = glob
            if f_flag == 0:
                f = open(loc, "w")
            else:
                f = open(loc, "wb")
            f.write(filedata)
            f.close()
        if move_p:
            scode = 301
            show_response += 'HTTP/1.1 301 Moved Permanently'
            show_response += '\r\nLocation: ' + loc
        elif mode_f:
            scode = 204
            show_response += 'HTTP/1.1 204 No Content'
            show_response += '\r\n\Content-Location: ' + entity
        elif r_201:
            scode = 201
            show_response += 'HTTP/1.1 201 Created'
            show_response += '\r\nContent-Location: ' + entity
        elif not mode_f:
            scode = 501
            show_response += 'HTTP/1.1 501 Not Implemented'
        show_response += '\r\nConnection: keep-alive'
        show_response += '\r\n\r\n'
        encoded = show_response.encode()
        connectionsocket.send(encoded)
        connectionsocket.close()
        return None

    def response_delete(self, entity, connectionsocket, ent_body, switcher,
                        glob):
        ip, serverport, scode, client_thread = glob
        isItDir = os.path.isdir(entity)
        isItFile = os.path.isfile(entity)
        # print(f"deleting {entity} ")
        # print(isItFile)
        option_list = entity.split('/')
        show_response = ''
        if 'Authorization' in switcher.keys():
            conversation = switcher['Authorization']
            # print("Auth process started:")
            if conversation:
                conversation = conversation.split(' ')
                conversation = base64.decodebytes(
                    conversation[1].encode()).decode()
                conversation = conversation.split(':')
            else:
                scode = 401
                show_response += 'HTTP/1.1 401 Unauthorized'
                show_response += '\r\nWWW-Authenticate: Basic'
                show_response += '\r\n\r\n'
                encoded = show_response.encode()
                connectionsocket.send(encoded)
                return [ip, serverport, scode]

            if conversation[0] == USERNAME:
                if conversation[1] == PASSWORD:
                    pass
                else:
                    scode = 401
                    show_response += 'HTTP/1.1 401 Unauthorized'
                    show_response += '\r\nWWW-Authenticate: Basic'
                    show_response += '\r\n\r\n'
                    encoded = show_response.encode()
                    connectionsocket.send(encoded)
                    return [ip, serverport, scode]
            else:
                scode = 401
                show_response += 'HTTP/1.1 401 Unauthorized'
                show_response += '\r\nWWW-Authenticate: Basic'
                show_response += '\r\n\r\n'
                encoded = show_response.encode()
                connectionsocket.send(encoded)
                return [ip, serverport, scode]
        else:
            scode = 401
            show_response += 'HTTP/1.1 401 Unauthorized'
            show_response += '\r\nWWW-Authenticate: Basic'
            show_response += '\r\n\r\n'
            encoded = show_response.encode()
            connectionsocket.send(encoded)
            return [ip, serverport, scode]
        if len(ent_body) > 1 or 'delete' in option_list or isItDir:
            scode = 405
            show_response += 'HTTP/1.1 405 Method Not Allowed'
            show_response += '\r\nAllow: GET, HEAD, POST, PUT'
        elif isItFile:
            scode = 200
            show_response += 'HTTP/1.1 200 OK'
            try:
                if (os.access(entity, os.W_OK)):
                    if (os.access(entity, os.R_OK)):
                        pass
                    else:
                        glob = status(connectionsocket, 403,
                                      [ip, client_thread, scode])
                        ip, client_thread, scode = glob
                else:
                    glob = status(connectionsocket, 403,
                                  [ip, client_thread, scode])
                    ip, client_thread, scode = glob
                shutil.move(entity, DELETE)
            except shutil.Error:
                os.remove(entity)
        else:
            scode = 400
            show_response += 'HTTP/1.1 400 Bad Request'
        show_response += '\r\nServer: ' + ip
        show_response += '\r\nConnection: keep-alive'
        show_response += '\r\n' + date()
        show_response += '\r\n\r\n'
        encoded = show_response.encode()
        connectionsocket.send(encoded)
        return [ip, serverport, scode]


m = http_methods()

# function to check if the resource has been modified or not since the date in HTTP request


def if_modify(state, entity):
    global conditional_get, month
    valid = False
    day = state.split(' ')
    if len(day) == 5:
        valid = True
    if valid:
        m = month[day[1]]
        date = int(day[2])
        t = day[3].split(':')
        t[0], t[1], t[2] = int(t[0]), int(t[1]), int(t[2])
        y = int(day[4])
        ti = datetime.datetime(y, m, date, t[0], t[1], t[2])
        hsec = int(time.mktime(ti.timetuple()))
        fsec = int(os.path.getmtime(entity))
        if hsec == fsec:
            conditional_get = True
        elif hsec < fsec:
            conditional_get = False
    return conditional_get


# function to return current date


def date():
    #  Sun, 06 Nov 1994 08:49:37 GMT  ; RFC 822, updated by RFC 1123
    # Sunday, 06-Nov-94 08:49:37 GMT ; RFC 850, obsoleted by RFC 1036
    # Sun Nov  6 08:49:37 1994       ; ANSI C's asctime() format
    now = datetime.datetime.now()
    datenow = now.strftime('%A,%d %B %Y %H:%M:%S ')
    datenow += "GMT"
    conversation = 'Date: ' + datenow
    return conversation


# function to give response if server is busy


def status(connectionsocket, code, glob):
    ip, client_thread, scode = glob
    scode = code
    show_response = ''
    if (code == '505') or (code == 505):
        show_response += 'HTTP/1.1 505 HTTP version not supported'
    elif (code == '415') or (code == 415):
        show_response += 'HTTP/1.1 415 Unsupported Media Type'
    elif (code == '403') or (code == 403):
        show_response += 'HTTP/1.1 403 Forbidden'
    elif (code == '404') or (code == 404):
        show_response += 'HTTP/1.1 404 Not Found'
    elif (code == '414') or (code == 414):
        show_response += 'HTTP/1.1 414 Request-URI Too Long'
    elif (code == '500') or (code == 500):
        show_response += 'HTTP/1.1 500 Internal Server Error'
    elif (code == '503') or (code == 503):
        show_response += 'HTTP/1.1 503 Server Unavailable'
    show_response += '\r\nServer: ' + ip
    show_response += '\r\n' + date()
    show_response += '\r\n\r\n'
    if code == 505:
        show_response += '\r\nSupported Version - HTTP/1.1 \n Rest Unsupported'
    encoded = show_response.encode()
    connectionsocket.send(encoded)
    logging.info('	{}	{}\n'.format(connectionsocket, scode))
    try:
        client_thread.remove(connectionsocket)
        connectionsocket.close()
    except:
        pass
    server([
        serversocket, file_extension, conditional_get, conn, SIZE,
        client_thread, scode, ip, IDENTITY, serverport
    ])
    return [ip, client_thread, scode]


# function for conditional get implementation
def status_304(connectionsocket, entity, glob):
    ip, scode = glob
    scode = 304
    show_response = ''
    show_response += 'HTTP/1.1 304 Not Modified'
    show_response += '\r\n' + date()
    show_response += '\r\n' + last_modified(entity)
    show_response += '\r\nServer: ' + ip
    show_response += '\r\n\r\n'
    encoded = show_response.encode()
    connectionsocket.send(encoded)


# function which operates between response and requests
def bridgeFunction(connectionsocket, addr, start, glob):
    serversocket, file_extension, conditional_get, conn, SIZE, client_thread, scode, ip, IDENTITY, serverport = glob
    conditional_get = False
    urlflag = 0
    f_flag = 0
    filedata = b""
    conn = True
    for _ in iter(int, 1):
        if not conn:
            # print("Connection not established")
            break
        if SIZE > 0:
            pass
        else:
            break
        try:
            message = connectionsocket.recv(SIZE)
        except OSError:
            message = connectionsocket.recv(SIZE)
        try:
            f_flag = 0
            message = message.decode('utf-8')
            req_list = message.split('\r\n\r\n')
            # print(req_list)
        except UnicodeDecodeError:
            f_flag = 1
            # if you're using non UTF-8 chars
            req_list = message.split(b'\r\n\r\n')
            req_list[0] = req_list[0].decode(errors='ignore')
            # print(req_list)
        if len(req_list) == 1:
            status(connectionsocket, 505, [ip, client_thread, scode])
            print("\nBlank line expected at the end\n")
            break
        elif len(req_list) > 1:
            # every line ends with a \r\n so for only headers it'll create ['req', '']
            pass
        else:
            status(connectionsocket, 505, [ip, client_thread, scode])
            print("Error in headers\n")
            break
        try:
            LOG.write(((addr[0]) + '\n' + req_list[0] + '\n\n'))
        except:
            pass
        # show_response = ''
        # header_len = len(header_list)
        ent_body = req_list[1]
        header_list = req_list[0].split('\r\n')
        request_line = header_list[0].split(' ')
        if len(req_list) < 2:
            status(connectionsocket, 505, [ip, client_thread, scode])
        else:
            pass
        entity = request_line[1]
        method = request_line[0]
        if entity == '/':
            entity = os.getcwd()
        elif (entity == favicon) or (entity
                                     == 'favicon') or (entity
                                                       == 'favicon.ico'):
            entity = FAVICON
        entity, query = breakdown(entity)
        if (len(entity) > MAX_URL and urlflag == 0):
            status(connectionsocket, 414, [ip, client_thread, scode])
            connectionsocket.close()
            break
        elif len(entity) <= MAX_URL:
            # print("working Fine")
            urlflag = 1
            pass
        else:
            urlflag = 1
        version = request_line[2]
        try:
            version_num = version.split('/')[1]
            if (version_num == RUNNING_VERSION):
                # print("using HTTP 1.1")
                pass
            elif not (version_num == RUNNING_VERSION):
                status(connectionsocket, 505, [ip, client_thread, scode])
        except IndexError:
            # print("EXPECTED HTTP version number")
            status(connectionsocket, 505, [ip, client_thread, scode])
        request_line = header_list.pop(0)
        switcher = {}
        i = 0
        while i < len(header_list):
            line = header_list[i]
            line_list = line.split(': ')
            switcher[line_list[0]] = line_list[1]
            i += 1
        if (method == 'HEAD') or (method == 'GET'):
            # connectionsocket, entity, switcher, query, method, glob
            glob = m.response_get_head(
                connectionsocket, entity, switcher, query, method, [
                    serversocket, file_extension, conditional_get, conn, ip,
                    serverport, scode, IDENTITY, client_thread
                ])

            serversocket, file_extension, conditional_get, conn, ip, serverport, scode, IDENTITY = glob
        elif method == 'POST':
            glob = m.response_post(ent_body, connectionsocket, switcher,
                                   [ip, serverport, scode])
            ip, serverport, scode = glob
        elif method == 'DELETE':
            glob = m.response_delete(entity, connectionsocket, ent_body,
                                     switcher,
                                     [ip, serverport, scode, client_thread])
            ip, serverport, scode = glob
            conn = False
            connectionsocket.close()
        elif method == 'PUT':
            m.response_put(connectionsocket, addr, ent_body, filedata, entity,
                           switcher, f_flag, scode, [ip, client_thread, scode])
        else:
            method = 'Not Defined'
            break
        # use the logging formatting
        logging.info('	{}	{}	{}	{}	{}\n'.format(addr[0], addr[1], request_line,
                                                entity, scode))
    try:
        connectionsocket.close()
        client_thread.remove(connectionsocket)
    except:
        pass


# function handling multiple requests


def server(glob):
    serversocket, file_extension, conditional_get, conn, SIZE, client_thread, scode, ip, IDENTITY, serverport = glob
    for _ in iter(int, 1):
        # connectionsocket = request, addr = port,ip
        connectionsocket, addr = serversocket.accept()
        start = 0
        client_thread.append(connectionsocket)  # add connections
        if not (len(client_thread) < MAX_REQUEST):
            status(connectionsocket, 503, [ip, client_thread, scode])
            connectionsocket.close()
        else:
            start_new_thread(bridgeFunction, (connectionsocket, addr, start, [
                serversocket, file_extension, conditional_get, conn, SIZE,
                client_thread, scode, ip, IDENTITY, serverport
            ]))
    serversocket.close()


'''
Function to handle the exit ( Ctrl+C and other signals )
'''
sig_rec = False


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    print("q for quit\n r for restart")
    sys.exit(0)


if __name__ == '__main__':
    ip = None  # IP
    conn = True  # to receive requests continuously in client's thread
    scode = 0  # Status code initialization

    IDENTITY = 0  # Cookie ID . This project Increments it by 1
    conditional_get = False  # check : is it conditional get method?
    month = MONTH

    # Dictionary to convert content types into the file extentions eg. text/html to .html
    file_type = FORMAT2
    # Dictionary to convert file extentions into the content types eg. .html to text/html
    file_extension = FORMAT

    client_thread = []  # list to work with the threads

    serversocket = socket(AF_INET, SOCK_STREAM)
    s = socket(AF_INET, SOCK_DGRAM)
    logging.basicConfig(filename=LOG,
                        level=logging.INFO,
                        format='%(asctime)s:%(filename)s:%(message)s')

    # To run it on the localhost if you dont want google DNS
    ip = '127.0.0.1'
    # print(ip)
    try:
        serverport = int(sys.argv[1])
    except:
        print(
            "Port Number missing\n\nTO RUN\nType: python3 httpserver.py port_number"
        )
        sys.exit()
    try:
        serversocket.bind(('', serverport))
    except:
        print('\nTO RUN:python3 httpserver.py port_number')
        sys.exit()
    serversocket.listen(5)
    print('HTTP server running on ip: ' + ip + ' port: ' + str(serverport) +
          '\nGo to this in the browser: (http://' + ip + ':' +
          str(serverport) + '/)')
    server([
        serversocket, file_extension, conditional_get, conn, SIZE,
        client_thread, scode, ip, IDENTITY, serverport
    ])  # IMP calling the main server Function
    sys.exit()
