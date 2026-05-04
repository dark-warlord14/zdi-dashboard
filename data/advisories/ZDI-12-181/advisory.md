# ZDI-12-181: Novell iPrint nipplib.dll client-file-name Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-181
- **ZDI-CAN:** ZDI-CAN-1466
- **Date:** 2012-08-29
- **CVE:** CVE-2011-4186
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** iPrint
- **Credit:** Ivan Rodriguez Almuina
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-181/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell iPrint Client. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the nipplib component which is used by both the ActiveX and Netscape compatible browser plugins as well as the Microsoft Windows spooler service. When handling certain requests the client-file-name parameter is improperly copied to a local stack buffer. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/kb/doc.php?id=7008708

## Disclosure Timeline

- 2011-12-22 - Vulnerability reported to vendor
- 2012-08-29 - Coordinated public release of advisory
