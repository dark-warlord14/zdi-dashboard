# ZDI-10-237: Novell GroupWise Internet Agent Content-Type Multiple Value Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-237
- **ZDI-CAN:** ZDI-CAN-951
- **Date:** 2010-11-08
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Groupwise
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-237/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell GroupWise. Authentication is not required to exploit this vulnerability. The specific flaw exists within the gwia.exe module responsible for parsing e-mail messages received by the server. When the code encounters a Content-Type header it proceeds to parse out the entities within its contents, separated by a semicolon. The process does not properly check the size of these values before copying them individually to a fixed-length stack buffer. This can be abused by an attacker to overflow the buffer and subsequently execute arbitrary code under the context of the SYSTEM user.

## Additional Details

Linux - http://download.novell.com/Download?buildid=04oMMaiI9nI~ NetWare/Windows - http://download.novell.com/Download?buildid=aq06Eoy7rf4~ The GroupWise Internet Agent (GWIA) has a vulnerability in the way that it parses multiple values within the "Content-Type" header of a received message, which could potentially allow an unauthenticated remote attacker to execute arbitrary code on vulnerable installations of GWIA. Affected versions: GroupWise 8.0x, 8.01x, 8.02. Previous versions of GroupWise are likely also vulnerable but are no longer supported. Customers on earlier versions of GroupWise should, at a minimum, upgrade their GWIAs and associated Domains to version 8.02HP in order to secure their system. This vulnerability was discovered and reported by Anonymous working with TippingPoint's Zero Day Initiative ( http://www.zerodayinitiative.com ) ZDI-CAN-951 Novell bug 642336, CVE number pending Related TID: http://www.novell.com/support/search.do?usemicrosite=true&searchString=7007152

## Disclosure Timeline

- 2010-09-24 - Vulnerability reported to vendor
- 2010-11-08 - Coordinated public release of advisory
