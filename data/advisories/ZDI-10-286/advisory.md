# ZDI-10-286: Microsoft Exchange 2007 Infinite Loop Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-286
- **ZDI-CAN:** ZDI-CAN-598
- **Date:** 2010-12-14
- **CVE:** CVE-2010-3937
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:L/Au:S/C:N/I:N/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Exchange
- **Credit:** Oleksandr Mirosh
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-286/
## Vulnerability Details

This vulnerability allows attackers to deny services on vulnerable installations of Microsoft Exchange Server 2007. Authentication is required to exploit this vulnerability. The specific flaw exists within store.exe during the handling of a particular MAPI call. The service will enter a loop whose termination is controlled by an attacker. If the attacker specifies an invalid value, the loop will never terminate causing the service to stop responding to requests. This results in a denial of service against the target server.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS10-106.mspx

## Disclosure Timeline

- 2009-10-27 - Vulnerability reported to vendor
- 2010-12-14 - Coordinated public release of advisory
