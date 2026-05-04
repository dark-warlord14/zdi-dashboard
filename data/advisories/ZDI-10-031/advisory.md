# ZDI-10-031: Apple Webkit Blink Event Dangling Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-031
- **ZDI-CAN:** ZDI-CAN-596
- **Date:** 2010-03-16
- **CVE:** CVE-2010-0050
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** wushi&Z of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-031/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable software utilizing Apple's WebKit library. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists due to a failure to unregister a callback pointer during the destruction of a particular type of element when embedded inside a 'blink' container. The application dereferences the original resource which can can be leveraged by an attacker to execute arbitrary code under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4070

## Disclosure Timeline

- 2009-10-27 - Vulnerability reported to vendor
- 2010-03-16 - Coordinated public release of advisory
