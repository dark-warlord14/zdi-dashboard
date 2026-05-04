# ZDI-11-049: (0Day) IBM Lotus Domino SMTP Multiple Filename Arguments Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-049
- **ZDI-CAN:** ZDI-CAN-375
- **Date:** 2011-02-07
- **CVE:** CVE-2011-0916
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Lotus Domino
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-049/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on systems with vulnerable installations of IBM Lotus Domino. Authentication is not required to exploit this vulnerability. The specific flaw exists within the SMTP service while processing a malformed e-mail. The process continually appends each argument within a filename parameter into a buffer in memory. By providing enough data this buffer can overflow leading to arbitrary code execution under the context of the SYSTEM user.

## Additional Details

http://www-01.ibm.com/support/docview.wss?uid=swg21461514

## Disclosure Timeline

- 2008-08-26 - Vulnerability reported to vendor
- 2011-02-07 - Coordinated public release of advisory
