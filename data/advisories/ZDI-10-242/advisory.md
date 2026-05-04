# ZDI-10-242: Novell Groupwise Internet Agent IMAP LIST Command Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-242
- **ZDI-CAN:** ZDI-CAN-846
- **Date:** 2010-11-08
- **CVE:** N/A
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Groupwise
- **Credit:** Francis Provencher for Protek Researchh Lab's
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-242/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell Groupwise Internet Agent. Authentication is not required to exploit this vulnerability. The flaw exists within the IMAP server component which listens by default on TCP port 143. When handling an IMAP LIST command with a large parameter the process attempts to free the same memory twice. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the IMAP server.

## Additional Details

Linux - http://download.novell.com/Download?buildid=04oMMaiI9nI~ NetWare/Windows - http://download.novell.com/Download?buildid=aq06Eoy7rf4~ Description: The GroupWise Internet Agent has a vulnerability in its IMAP component that could potentially allow an unauthenticated remote attacker to execute arbitrary code on vulnerable installations of GWIA where IMAP services are enabled. Affected versions: GroupWise 8.0x, 8.01x, 8.02. Previous versions of GroupWise are likely also vulnerable but are no longer supported. Customers on earlier versions of GroupWise should, at a minimum, upgrade their GWIAs and associated Domains to version 8.02HP in order to secure their system. This vulnerability was discovered and reported by Francis Provencher working with TippingPoint's Zero Day Initiative ( http://www.zerodayinitiative.com ) ZDI-CAN-846 Novell bug 647519, CVE number pending Related TID: http://www.novell.com/support/search.do?usemicrosite=true&searchString=7007151

## Disclosure Timeline

- 2010-07-20 - Vulnerability reported to vendor
- 2010-11-08 - Coordinated public release of advisory
