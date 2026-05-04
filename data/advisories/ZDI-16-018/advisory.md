# ZDI-16-018: Microsoft Internet Explorer NewMessage Protected Mode Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-018
- **ZDI-CAN:** ZDI-CAN-3330
- **Date:** 2016-01-12
- **CVE:** CVE-2016-0020
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Ashutosh Mehra (https://twitter.com/ashutoshmehra)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-018/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the IShdocvwBroker::NewMessage API. Calling this API causes the broker process to load a DLL from a potentially unsafe location. An attacker can leverage this vulnerability to execute code under the context of the user at medium integrity.

## Disclosure Timeline

- 2015-10-08 - Vulnerability reported to vendor
- 2016-01-12 - Coordinated public release of advisory
