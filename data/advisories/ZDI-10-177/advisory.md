# ZDI-10-177: IBM Lotus Domino iCalendar MAILTO Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-177
- **ZDI-CAN:** ZDI-CAN-371
- **Date:** 2010-09-14
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Lotus Domino
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-177/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on systems with vulnerable installations of IBM Lotus Domino. Authentication is not required to exploit this vulnerability. The specific flaw exists within the nrouter.exe service while processing a malformed e-mail. The process copies the contents of the MAILTO header within a calendar request into a fixed size stack buffer. By providing enough data this buffer can overflow leading to arbitrary code execution under the context of the SYSTEM user.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-01.ibm.com/support/docview.wss?rs=475&uid=swg21446515

## Disclosure Timeline

- 2008-08-26 - Vulnerability reported to vendor
- 2010-09-14 - Coordinated public release of advisory
