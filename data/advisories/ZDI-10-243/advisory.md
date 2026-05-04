# ZDI-10-243: Novell GroupWise Internet Agent TZNAME Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-243
- **ZDI-CAN:** ZDI-CAN-954
- **Date:** 2010-11-08
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Groupwise
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-243/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell GroupWise. Authentication is not required to exploit this vulnerability. The specific flaw exists within the gwwww1.dll module responsible for parsing VCALENDAR data within e-mail messages. When the code encounters a TZNAME variable it allocates up to 0xFFFF bytes for the variable's value. It then proceeds to copy the value into the fixed-length buffer without checking if it will fit. By specifying a large enough string in the e-mail, an attacker can overflow the buffer and execute arbitrary code under the context of the SYSTEM user.

## Additional Details

Linux - http://download.novell.com/Download?buildid=04oMMaiI9nI~ NetWare/Windows - http://download.novell.com/Download?buildid=aq06Eoy7rf4~ The GroupWise Internet Agent (GWIA) has multiple vulnerabilities in the way that it parses variables within a received VCALENDAR message, which could potentially allow an unauthenticated remote attacker to execute arbitrary code on vulnerable installations of GWIA. Affected versions: GroupWise 8.0x, 8.01x, 8.02. Previous versions of GroupWise are likely also vulnerable but are no longer supported. Customers on earlier versions of GroupWise should, at a minimum, upgrade their GWIAs and associated Domains to version 8.02HP in order to secure their system. These vulnerabilities were discovered and reported by Anonymous working with TippingPoint's Zero Day Initiative ( http://www.zerodayinitiative.com ) ZDI-CAN-954,ZDI-CAN-960, ZDI-CAN-961 Novell bugs 642339, 642345, 642349, CVE numbers pending Related TID: http://www.novell.com/support/search.do?usemicrosite=true&searchString=7007155

## Disclosure Timeline

- 2010-09-24 - Vulnerability reported to vendor
- 2010-11-08 - Coordinated public release of advisory
