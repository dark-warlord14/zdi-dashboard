# ZDI-11-048: (0Day) IBM Lotus Domino iCalendar Meeting Request Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-048
- **ZDI-CAN:** ZDI-CAN-373
- **Date:** 2011-02-07
- **CVE:** CVE-2011-0915
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Lotus Domino
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-048/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on systems with vulnerable installations of IBM Lotus Domino. Authentication is not required to exploit this vulnerability. The specific flaw exists within the nrouter.exe service while processing a malformed calendar meeting request. The process copies the contents of the name parameter within the Content-Type header into a fixed size stack buffer. By providing enough data this buffer can overflow leading to arbitrary code execution under the context of the SYSTEM user.

## Additional Details

http://www-01.ibm.com/support/docview.wss?uid=swg21461514

## Disclosure Timeline

- 2008-08-26 - Vulnerability reported to vendor
- 2011-02-07 - Coordinated public release of advisory
