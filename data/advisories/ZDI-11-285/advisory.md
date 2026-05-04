# ZDI-11-285: Novell Groupwise iCal COMMENT, RRULE, TZNAME Remote Code Execution Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-11-285
- **ZDI-CAN:** ZDI-CAN-1187
- **Date:** 2011-10-13
- **CVE:** CVE-2010-4325
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Groupwise
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-285/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell GroupWise. Authentication is not required to exploit this vulnerability. Multiple flaws exist within the gwwww1.dll module responsible for parsing VCALENDAR data within e-mail messages. When encountering a RRULE, COMMENT, or TZNAME parameter a static sized memory buffer is allocated. Insufficient checks are performed to ensure the size of the parameter's value can be contained in this buffer. An attacker can overflow the buffer and execute arbitrary code under the context of the SYSTEM user.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/search.do?usemicrosite=true&searchString=7009212

## Disclosure Timeline

- 2011-04-01 - Vulnerability reported to vendor
- 2011-10-13 - Coordinated public release of advisory
