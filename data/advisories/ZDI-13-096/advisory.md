# ZDI-13-096: Novell iPrint Client IPP Response Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-096
- **ZDI-CAN:** ZDI-CAN-1715
- **Date:** 2013-05-29
- **CVE:** CVE-2013-1091
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Novell
- **Affected Products:** iPrint
- **Credit:** nullPtr Crew
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-096/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell iPrint. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of functions that take a URI as a parameter. The issue lies in the failure to validate the size of received data prior to copying it into a fixed size buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/kb/doc.php?id=7012344

## Disclosure Timeline

- 2013-01-07 - Vulnerability reported to vendor
- 2013-05-29 - Coordinated public release of advisory
