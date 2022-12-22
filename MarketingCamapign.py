import pickle   
import os
import pathlib




############################################## Main Program Modules
class Ticket:
    name = ''
    email = ''
    campaignname = ''
    reference = 200000

    def check(self):
        file = pathlib.Path("tickets.data")
        if file.exists():
            infile = open('tickets.data', 'rb')
            ticketdetails = pickle.load(infile)
            for ticket in ticketdetails:
                if ticket.email == self.email and ticket.campaignname == self.campaignname:
                    return True
            infile.close()
            
    def getBookedSeatCount(self):
        file = pathlib.Path("tickets.data")
        counter= 0
        if file.exists():
            infile = open('tickets.data', 'rb')
            ticketdetails = pickle.load(infile)
            for ticket in ticketdetails:
                if ticket.campaignname == self.campaignname:
                    counter = counter + 1
            return int(counter)
        return 0


############################ Create Campaignname Class


class Campaignname:
    campaignnamename = ''
    campaignnamecode = ''
    campaignnameTotalAvaibleSeat = 10

    def createCampaignname(self):
        self.campaignnamename= input("Enter Campaignname Name: ")
        self.campaignnamecode = input("Enter Campaignname Code: ")
        self.campaignnameTotalAvaibleSeat = input("Enter Campaignname Total Availble Seats: ")
        print("\n\n ------> Campaignname Created!")


def createCampaignname():
    campaignname=Campaignname()
    campaignname.createCampaignname()
    saveCampaignnameDetails()

# Save Campaignname Details to File

def saveCampaignnameDetails(campaignname):
    file = pathlib.Path("marketingcampaigns.data")
    if file.exists():
        infile = open('marketingcampaigns.data', 'rb')
        oldlist = pickle.load(infile)
        oldlist.append(campaignname)
        infile.close()
        os.remove('marketingcampaigns.data')
    else:
        oldlist = [campaignname]
    outfile = open('tempmarketingcampaigns.data', 'wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('tempmarketingcampaigns.data', 'marketingcampaigns.data')

# Display All Campaignname Details

def getMarketingcampaignsDetails():
    file = pathlib.Path("marketingcampaigns.data")
    if file.exists ():
        infile = open('marketingcampaigns.data','rb')
        campaignnamedetails = pickle.load(infile)
        print("---------------CAMPAIGNNAME DETAILS---------------------")
        print("E-Name    E-Code    E-Total-Seats")
        for campaignname in campaignnamedetails :
            print(campaignname.campaignnamename,"\t", campaignname.campaignnamecode, "\t",campaignname.campaignnameTotalAvaibleSeat)
        infile.close()
        print("--------------------------------------------------")
        input('Press Enter To Main Menu')
    else :
        print("NO MARKETINGCAMPAIGNS RECORDS FOUND")

# Create Campaignname Module

def createCampaignname():
    campaignname = Campaignname()
    campaignname.createCampaignname()
    saveCampaignnameDetails(campaignname)
    
# Display Reports About Marketingcampaigns

def getMarketingcampaignsSummary():
    filetickets = pathlib.Path("tickets.data")
    if filetickets.exists():
        infiletickets = open('tickets.data', 'rb')
        ticketdetails = pickle.load(infiletickets)


    fileMarketingcampaigns = pathlib.Path("marketingcampaigns.data")
    if fileMarketingcampaigns.exists ():
        infileMarketingcampaigns = open('marketingcampaigns.data','rb')
        campaignnamedetails = pickle.load(infileMarketingcampaigns)


        print("---------------REPORTS---------------------")
        for campaignname in campaignnamedetails :
            print("\n\nCampaignname Name : " + campaignname.campaignnamename + " | Total Seats : " + campaignname.campaignnameTotalAvaibleSeat + " \n")
            for ticket in ticketdetails:
                if campaignname.campaignnamecode == ticket.campaignname:
                    print(ticket.reference, "\t", ticket.name, "\t", ticket.email)

        infileMarketingcampaigns.close()
        infiletickets.close()

        print("--------------------------------------------------")
        input('Press Enter To Main Menu')
    else :
        print("NO MARKETINGCAMPAIGNS RECORDS FOUND")


###################################################### Start Program
ch=''
num=0
while ch != 8:
    print("\t\t\t\t-----------------------")
    print("\t\t\t\tCAMPAIGNNAME MANAGEMENT SYSTEM")
    print("\t\t\t\t-----------------------")
    print("\tMAIN MENU")
    print("\t1. CREATE MARKETINGCAMPAIGNS")
    print("\t2. VIEW MARKETINGCAMPAIGNS")
    print("\t3. SHOW SUMMARY")
    print("\tSelect Your Option (1-3) ")
    ch = input()

   
    if ch == '1':
        createCampaignname()
    elif ch == '2':
        getMarketingcampaignsDetails()
    elif ch == '3':
        getMarketingcampaignsSummary()
