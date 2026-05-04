# ZDI-14-429: (0Day) Agilent Technologies 2100 Expert CSDispatcher.exe Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-429
- **ZDI-CAN:** ZDI-CAN-2279
- **Date:** 2015-10-05
- **CVE:** CVE-2014-5145
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Agilent Technologies
- **Affected Products:** 2100 Expert
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-429/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Agilent Technologies 2100 Expert. Authentication is not required to exploit this vulnerability. The specific flaw exists within the CSDispatcher.exe process, which listens on port 3434. By sending a crafted packet to this port, an attacker is able to control a dereferenced pointer, and execute arbitrary code in the SYSTEM context.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 08/01/2014 - ZDI disclosed to vendor 08/12/2014 - Vendor indicated 3rd party company involvement and asked for additional assistance on repro steps and feedback on fixing 02/27/2015 - ZDI dropped 0-day on a different case for this vendor and shortly after senior persons from the vendor's development indicated further willingness to work with ZDI 03/24/2015 - Vendor indicated they are working on the issue and mustering resources 03/26/2015 - ZDI inquired how close they may be to resolution and for any ETA 03/31/2015 - The vendor indicated the case was escalated internally 07/07/2015 - ZDI again requested any update 07/10/2015 - The vendor indicated they had gone through a restructuring 07/23/2015 - The vendor requested a call with ZDI 09/21/2015 - The ZDI call with the vendor occurred and the vendor indicated a favorable update was immediately forthcoming 09/28/2015 - A second ZDI call with the vendor occurred in which the vendor indicated they finally have a fix, but cannot release until Nov 09/28/2015 - ZDI indicated final intent to 0-day -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting. These features are available in the native Windows Firewall, as described in http://technet.microsoft.com/en-us/library/cc725770%28WS.10%29.aspx and numerous other Microsoft Knowledge Base articles.

## Disclosure Timeline

- 2014-08-01 - Vulnerability reported to vendor
- 2015-10-05 - Coordinated public release of advisory
