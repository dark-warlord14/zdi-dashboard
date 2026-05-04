# ZDI-10-287: Microsoft SharePoint Server Arbitrary File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-287
- **ZDI-CAN:** ZDI-CAN-706
- **Date:** 2010-12-14
- **CVE:** CVE-2010-3964
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Oleksandr Mirosh
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-287/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Sharepoint Server utilizing Microsoft's Office Document Load Balancer. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Office Document Conversions Launcher service and occurs due to insufficient parameter validation on a particular SOAP request. Sucessful exploitation will allow an attacker to upload and execute an arbitrary file on the target server.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS10-104.mspx

## Disclosure Timeline

- 2010-03-12 - Vulnerability reported to vendor
- 2010-12-14 - Coordinated public release of advisory
