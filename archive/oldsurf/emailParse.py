from __future__ import print_function
from apiclient import errors

import pickle
import os.path
import email
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64
import mailinglists as ml


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def GetMessage(service, user_id, msg_id):
  """Get a Message with given ID.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: The ID of the Message required.

  Returns:
    A Message.
  """
  try:
    message = service.users().messages().get(userId=user_id, id=msg_id).execute()

    print('Message snippet: %s' % message['snippet'])

    return message
  except:
      pass


def GetMimeMessage(service, user_id, msg_id):
  """Get a Message and use it to create a MIME Message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: The ID of the Message required.

  Returns:
    A MIME Message, consisting of data from Message.
  """
  try:
    message = service.users().messages().get(userId=user_id, id=msg_id,
                                             format='raw').execute()

    print('Message snippet: %s' % message['snippet'])

    msg_str = base64.urlsafe_b64decode(message['raw'].encode('ASCII'))

    mime_msg = email.message_from_string(msg_str)

    return mime_msg
  except:
      pass
      # errors.HttpError, error:
    # print 'An error occurred: %s' % error

def getEmails(user_id="me",maxNum=100):
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


    print(ids)
    print("Getting emails")
    messages = []
    for id in ids:
        print(id)
        # GetMimeMessage(service,'me',id['id'])

        # try:
        #     message = service.users().messages().get(userId=user_id,
        #                                              id=id['id'],
        #                                              format='full').execute()
        #
        #     message = message['payload']['body']['data']
        #     message = base64.urlsafe_b64decode(message.encode('ASCII')).decode(
        #         'UTF-8')
        #     message =
            # message = " ".join(message.split())
            # mime_msg = email.message_from_string(msg_str)
            #
            # print(message)
            #
            # return message
        # except:
        #     print("error")
    return message




def GetMimeMessage(service, user_id, msg_id):
    """Get a Message and use it to create a MIME Message.

    Args:
      service: Authorized Gmail API service instance.
      user_id: User's email address. The special value "me"
      can be used to indicate the authenticated user.
      msg_id: The ID of the Message required.

    Returns:
      A MIME Message, consisting of data from Message.
    """
    try:
        message = service.users().messages().get(userId=user_id,
                                                 id=msg_id, format = 'full').execute()

        message = message['payload']['body']['data']
        message = base64.urlsafe_b64decode(message.encode('ASCII')).decode('UTF-8')
        # message =
        message = " ".join(message.split())
        # mime_msg = email.message_from_string(msg_str)

        # print(message)

        return message
    except:
        print("error")
    # except errors.HttpError, error:
    #   print ('An error occurred: %s' % error)


def ListMessagesMatchingQuery(service, user_id, query=''):
    """List all Messages of the user's mailbox matching the query.

    Args:
      service: Authorized Gmail API service instance.
      user_id: User's email address. The special value "me"
      can be used to indicate the authenticated user.
      query: String used to filter messages returned.
      Eg.- 'from:user@some_domain.com' for Messages from a particular sender.

    Returns:
      List of Messages that match the criteria of the query. Note that the
      returned list contains Message IDs, you must use get with the
      appropriate ID to get the details of a Message.
    """
    try:
        response = service.users().messages().list(userId=user_id,
                                                   q=query).execute()
        messages = []
        if 'messages' in response:
            messages.extend(response['messages'])

        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = service.users().messages().list(userId=user_id, q=query,
                                                       pageToken=page_token).execute()
            messages.extend(response['messages'])

        return messages
    except:
        pass
    # except errors.HttpError, error:
    #     print ('An error occurred: %s' % error)


def ListMessagesWithLabels(service, user_id, label_ids=[]):
    """List all Messages of the user's mailbox with label_ids applied.

    Args:
      service: Authorized Gmail API service instance.
      user_id: User's email address. The special value "me"
      can be used to indicate the authenticated user.
      label_ids: Only return Messages with these labelIds applied.

    Returns:
      List of Messages that have all required Labels applied. Note that the
      returned list contains Message IDs, you must use get with the
      appropriate id to get the details of a Message.
    """
    try:
        response = service.users().messages().list(userId=user_id,
                                                   labelIds=label_ids).execute()
        messages = []
        if 'messages' in response:
            messages.extend(response['messages'])

        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = service.users().messages().list(userId=user_id,
                                                       labelIds=label_ids,
                                                       pageToken=page_token).execute()
            messages.extend(response['messages'])
        return messages
    except:
        pass
    # except errors.HttpError, error:
    #     print 'An error occurred: %s' % error



def main():
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

    print("Getting Email IDs")
    listIDs = ListMessagesWithLabels(service, "cmuhoneypot@gmail.com")
    print("# of emails total: ", len(listIDs))


    print("\nGetting Emails in full")
    oEmailurl = "assets/openedEmail.txt"
    alreadyCheckedMail = ml.imp(oEmailurl)
    print("Already checked " + str(len(alreadyCheckedMail)) + " emails, " + str(len(listIDs)-len(alreadyCheckedMail)) + " left")

    i=0
    with open(oEmailurl,'w') as f:
        emailList = []
        for idDic in listIDs:
            id = idDic['id']
            if id not in alreadyCheckedMail:
                emailList.append(GetMimeMessage(service,user_id = "me", msg_id = id))
                f.write(id + ", ")
                print(i)
                i+=1
        f.close()




    # print("Parsing links from emails and writing to file")
    # linkListURL = "assets/confirmLinks.txt"
    # confirmList = []
    # with open(linkListURL) as f:
    #     for email in emailList:
    #         try:
    #             confirmList.extend([x for x in email.split() if "http" in x])
    #         except:
    #             pass
    #         for linq in confirmList:
    #             f.write(linq + ", ")
    #         confirmList = []
    #     f.close()












def checkAllLinks(url):
    opener = webdriver.Chrome("assets/chromedriver")
    alreadyclickedurl = "assets/clickedConfirms.txt"

    links = ml.imp(url)
    doneLinks = ml.imp(alreadyclickedurl)


    print("We have " + str(len(links) - len(doneLinks)) + " unclicked links to click! Let's get started")
    i=0

    with open(alreadyclickedurl,'a') as f:
        for link in links:
            if link not in doneLinks:
                try:
                    opener.get(link)
                except:
                    pass

                try:
                    opener.find_element_by_xpath("/html/body/form/table/tbody/tr[8]/td[1]/div/input").click()
                except:
                    pass

                f.write(link + ", ")

                print(i)
                i += 1
        f.close()




# 168e03bb57dc89d8
# checkAllLinks("assets/confirmLinks.txt")
main()

# getEmails(maxNum = 100)