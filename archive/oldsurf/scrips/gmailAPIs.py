from __future__ import print_function


import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64






def getEmails(user_id="cmuhoneypot@gmail.com"):
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    print("Getting email IDs")
    label_ids = []
    try:
        response = service.users().messages().list(userId=user_id,
                                                   labelIds=label_ids).execute()
        ids = []
        if 'messages' in response:
            ids.extend(response['messages'])

        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = service.users().messages().list(userId=user_id,
                                                       labelIds=label_ids,
                                                       pageToken=page_token).execute()
            ids.extend(response['messages'])
    except:
        print("error getting IDs")

    {'partId': '', 'mimeType': 'multipart/alternative', 'filename': '',
     'headers': [{'name': 'Delivered-To', 'value': 'cmuhoneypot@gmail.com'},
                 {'name': 'Received',
                  'value': 'by 2002:a25:19c5:0:0:0:0:0 with SMTP id 188csp2267010ybz;        Mon, 18 Feb 2019 05:36:30 -0800 (PST)'},
                 {'name': 'X-Received',
                  'value': 'by 2002:a7b:c5d2:: with SMTP id n18mr16799036wmk.30.1550496990621;        Mon, 18 Feb 2019 05:36:30 -0800 (PST)'},
                 {'name': 'ARC-Seal',
                  'value': 'i=1; a=rsa-sha256; t=1550496990; cv=none;        d=google.com; s=arc-20160816;        b=FTlrA/7LR7oSaAmvrooYwWOtbS7U56RE1enYtvIs6UsVMU8I3Fs48uiTiQsIsMq9yX         PCWFik3pvU8WU+uEci8W+rIJFUltXvmOLHkrS5PPTvhAj2V/x8BTeuOJIV2KXk31IBCi         ix+rzE7lMcanWQ6fJrOm94D+S17GOJZa96Qq2LT6vLn3avcQqN18iSHhlS5dWixg8XtN         cGIgO4sRJSlAeDgxsw7fO77WKDCSOmfkR2juXq52ZY3AUlfkTXGRbj16hZSnMexD3+M9         IbUZQh4iIoORwWa5afxa1b5M8ahy/f7nj8hZWNQiAmpfCZ7KCPl1MNejXmamw8OBV60x         nMvA=='},
                 {'name': 'ARC-Message-Signature',
                  'value': 'i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;        h=to:subject:message-id:date:from:mime-version:dkim-signature;        bh=08p5mviqP/jNokkAA7sbPP8EULpYe067DJevzDzv+hM=;        b=0kSQ2/bE86KOI0IFROfueShcLfLWXsV2AN/Y0nKcp6B8IlZ1oodrJ/CmSGUcIRBq/z         3khNmXY45P8p2UCOWJxPxepUcn3LV9PlM9usRcFsIIC1PmUpgJ9NsvPUeC2LrunM/yTn         vsEpliMHu/UzaO6m3XyQrjMJ0+ZMFDCwzw2yNAnvw3+YYaicFhYsR6ZEhNbxUlTvQhm4         P2oM8b3s8ph5GPgR3jKR5Y59n7WY1Q3IeU2fwsMxYA9/hsveLKn+EFNv8NzEPWklh/IC         YSe3OsX90NmN8/3QGPbPeuZjYELDfHMBSxifEIsxevuxLQdlJTvceLmZUMH+AngKc0jw         Rptw=='},
                 {'name': 'ARC-Authentication-Results',
                  'value': 'i=1; mx.google.com;       dkim=pass header.i=@andrew-cmu-edu.20150623.gappssmtp.com header.s=20150623 header.b=CFiMn72y;       spf=pass (google.com: domain of akong@andrew.cmu.edu designates 209.85.220.41 as permitted sender) smtp.mailfrom=akong@andrew.cmu.edu;       dmarc=pass (p=NONE sp=NONE dis=NONE) header.from=andrew.cmu.edu'},
                 {'name': 'Return-Path', 'value': '<akong@andrew.cmu.edu>'},
                 {'name': 'Received',
                  'value': 'from mail-sor-f41.google.com (mail-sor-f41.google.com. [209.85.220.41])        by mx.google.com with SMTPS id o67sor2827977wma.24.2019.02.18.05.36.30        for <cmuhoneypot@gmail.com>        (Google Transport Security);        Mon, 18 Feb 2019 05:36:30 -0800 (PST)'},
                 {'name': 'Received-SPF',
                  'value': 'pass (google.com: domain of akong@andrew.cmu.edu designates 209.85.220.41 as permitted sender) client-ip=209.85.220.41;'},
                 {'name': 'Authentication-Results',
                  'value': 'mx.google.com;       dkim=pass header.i=@andrew-cmu-edu.20150623.gappssmtp.com header.s=20150623 header.b=CFiMn72y;       spf=pass (google.com: domain of akong@andrew.cmu.edu designates 209.85.220.41 as permitted sender) smtp.mailfrom=akong@andrew.cmu.edu;       dmarc=pass (p=NONE sp=NONE dis=NONE) header.from=andrew.cmu.edu'},
                 {'name': 'DKIM-Signature',
                  'value': 'v=1; a=rsa-sha256; c=relaxed/relaxed;        d=andrew-cmu-edu.20150623.gappssmtp.com; s=20150623;        h=mime-version:from:date:message-id:subject:to;        bh=08p5mviqP/jNokkAA7sbPP8EULpYe067DJevzDzv+hM=;        b=CFiMn72y4Gtqn1apRgQHchMvBLui5p1DcVH6Wj1/aynwRX8TxJta9RmTuF1s8otbYj         5MfY/tfOxo/L+0eYFcEMuBDzxjilDVpVF7GakMkwNcflCI5TLPpSPVeH8CL/w1JXdw/n         sg4lHre5WzuEAz2hucIsq6+qO1PodIX11r/LPFcUbbbiRsIoE84IiVSmwlehxD81eGF5         M/iGy7khl+4x0ZgRJ7XIAc322zt0Po/yoWhE7M/QXMry4n2xJmAH92iX7Zeue+EXQ65J         mwG4r9Xs30I+9z8OrTPek9evhRp+rcbyFMd5CCUkqRqC76wRM82z90GtHt2+AhD9+cJP         hCew=='},
                 {'name': 'X-Google-DKIM-Signature',
                  'value': 'v=1; a=rsa-sha256; c=relaxed/relaxed;        d=1e100.net; s=20161025;        h=x-gm-message-state:mime-version:from:date:message-id:subject:to;        bh=08p5mviqP/jNokkAA7sbPP8EULpYe067DJevzDzv+hM=;        b=Ym2qJB9AW6tJEzqshJKkejkRBQPG420C1DQ4KfzwHAuFsZoIoR8FQqj0gBlhE6lwnE         bL111g/45LBs2utbiTKXOwQM9tLiPow27ZSBWyd8qDlwejaYaMjnmaHhfrPHwKWuyaS0         V1T9PbDQ/EIevZpDevw7QmxM7oreCvNTwiQ5Hwak2QNYc/oXDVn+4E6bUrnIcknoAxnx         xTyF203hHx4DHnyrjpKajf7+2tTEmauy51OAQLT5lyKvq8mE+vSvTMhPbi34CDTtZ7vr         knXA+RkbO+GweKAqVlWonUDizLoydHGIM5udq6o2P1D6yuHjqVCi3p2RkvXOdsHIf057         K8Ug=='},
                 {'name': 'X-Gm-Message-State',
                  'value': 'AHQUAuaBI1QIpzo1/eiW59O35LDp78uFz5PBYBBpMgr/A951gWH0u07U y43Z9vK4xfPqcpzmwPj6K5SOzuIFWzKKhkIujovyX7foB8A='},
                 {'name': 'X-Google-Smtp-Source',
                  'value': 'AHgI3IY1Jd9TpkYH1WchkSoQeRnLKO8Sv8v7O18mWW91v94QvoWBmWt2ahvTcR9LKuno4eI2AhBfhXGnEGj/5MPPn8Q='},
                 {'name': 'X-Received',
                  'value': 'by 2002:a1c:9810:: with SMTP id a16mr15896390wme.37.1550496989947; Mon, 18 Feb 2019 05:36:29 -0800 (PST)'},
                 {'name': 'MIME-Version', 'value': '1.0'},
                 {'name': 'From', 'value': 'Andy Kong <akong@andrew.cmu.edu>'},
                 {'name': 'Date', 'value': 'Mon, 18 Feb 2019 08:36:18 -0500'},
                 {'name': 'Message-ID',
                  'value': '<CAA7LO2wq+hOFd5m7MFmtswajxYevfcUpAANA7jGDWBi1djs-ug@mail.gmail.com>'},
                 {'name': 'Subject', 'value': 'Hey'},
                 {'name': 'To', 'value': 'cmuhoneypot@gmail.com'},
                 {'name': 'Content-Type',
                  'value': 'multipart/alternative; boundary="0000000000004fc83b05822b36f9"'}],
     'body': {'size': 0}, 'parts': [
        {'partId': '0', 'mimeType': 'text/plain', 'filename': '', 'headers': [
            {'name': 'Content-Type', 'value': 'text/plain; charset="UTF-8"'}],
         'body': {'size': 18, 'data': 'UGxlYXNlIHJlYWQgdGhpcw0K'}},
        {'partId': '1', 'mimeType': 'text/html', 'filename': '', 'headers': [
            {'name': 'Content-Type', 'value': 'text/html; charset="UTF-8"'}],
         'body': {'size': 39,
                  'data': 'PGRpdiBkaXI9Imx0ciI-UGxlYXNlIHJlYWQgdGhpczwvZGl2Pg0K'}}]}

    print("Getting emails")
    print(ids)
    messages = []
    for id in ids:
        try:
            message = service.users().messages().get(userId=user_id,id=id['id'],format="full").execute()
    #
            message = message['payload']['parts']
            message = message[0]['body']['data']


            message = base64.urlsafe_b64decode(message.encode('ASCII')).decode('UTF-8')
            message = " ".join(message.split())

            print(message)
            messages.append(message)

        # mime_msg = email.message_from_string(msg_str)

        # print(message)

        # messages.extend(message)
        except:
            print("error")
    return messages


getEmails()