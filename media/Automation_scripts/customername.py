class CustomerNameMapping:
    def __init__(self):
        self.mapping = {
        'Achilles Information Limited'          : ( 'c_Achilles Information Limited','Colt Technology Services, Achilles Managed Hosting'),
        'Allen and Overy Sherman'               : ( 'Allen & Overy LLP','Allen and Overy, LLP','Allen & Overy, LLP','Colt Technology Services, Allen and Overy Managed Hosting'),
        'Apergy USA Inc'                        : ('APERGY USA, INC.','APERGY USA, INC.'),
        'Asda Stores Ltd'                       : ('c_Asda Stores Ltd','Colt Technology Services, ASDA Managed Hosting'),
        'Bank of America'                       : ('Bank Of America','Bank Of America'),
        'CenturyLink Communications, LLC'       : ('CenturyLink Communications, LLC','CenturyLink Communications, LLC'),
        'CenturyLink Data Services'             : ('CenturyLink Data Services','CenturyLink Data Services'),
        'Chick-fil-A, Inc.'                     : ('Chick-fil-A, Inc.','Chick-fil-A, Inc.'),
        'Colt Technology Services'              : ('Colt Technology Services','Colt Technology Services Co., Ltd'),
        'Convertium Pte Ltd'                    : ('CONVERTIUM PTE LTD','CONVERTIUM PTE LTD'),
        'County of Monterey'                    : ('Monterey, County of','Monterey, County of'),
        'EasyJet Airline Co. Ltd.'              : ('EasyJet Airline Co. Ltd.','EasyJet Airline Co. Ltd.'),
        'Edward Don & Company'                  : ('Edward Don & Company','Edward Don & Company'),
        'Euroclear UK & International Limited'  : ('c_EUROCLEAR UK & INTERNATIONAL LIMITED','Colt Technology Services, Euroclear Managed Hosting','EUROCLEAR UK & INTERNATIONAL LIMITED'),
        'GW&K Investment Management, LLC'       : ('GW&K Investment Management, LLC','GW&K Investment Management, LLC'),
        'Howard Associates, LLC'                : ('Howard Associates, LLC','Howard Associates, LLC'),
        'Howard Midstream Energy Partners, LLC' : ('Howard Midstream Energy Partners, LLC','Howard Midstream Energy Partners, LLC'),
        'Ipsos America Inc'                     : ('Ipsos America Inc','Ipsos America Inc'),
        'Kronos Incorporated'                   : ('Kronos Incorporated','c_Kronos Incorporated'),
        'Lloyds Bank PLC'                       : ('Lloyds Bank PLC','Colt Technology Services, Lloyds Bank Managed Hosting'),
        'Neenah, Inc.'                          : ('NEENAH, INC.','NEENAH, INC.'),
        'Refinitiv Limited'                     : ('c_Refinitiv Limited','Refinitiv Limited'),
        'Reuters.com'                           : ('Reuters.com','c_Reuters Limited'),
        'Ryan, LLC'                             : ('Ryan, LLC','Ryan, LLC'),
        'SAP-HEC Partnership-Infra'             : ('SAP-HEC Partnership-Infra','SAP-HEC Partnership-Infra'),
        'Savvis'                                : ('Savvis','c_Savvis','Savvis UK Ltd','Savvis Internal - GHIE'),
        'Subito GSD'                            : ('Subito GSD','Subito GSD'),
        'ST Logistics Pte. Ltd.'                : ('ST LOGISTICS PTE. LTD.','ST LOGISTICS PTE. LTD.'),
        'The Common Fund'                       : ('The Common Fund for Nonprofit Organizations','The Common Fund for Nonprofit Organizations'),
        'Third Federal'                         : ('Third Federal Savings and Loan Association of Cleveland','Third Federal Savings and Loan Association of Cleveland'),
        'Wall Street Systems'                   : ('Wall Street Systems - ION','Wall Street Systems - ION'),
        'YMCA'                                  : ('YMCA (SCCI)','YMCA of Singapore')
    }

    def get_customer_name(self, company_name):
        for new_name, old_names in self.mapping.items():
            if company_name in old_names:
                return new_name
        return company_name  # Return original name if no mapping exists
    
    def get_all_mapped_names(self):
        all_names = self.mapping
        return all_names