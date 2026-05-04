# ZDI-16-435: Apple OS X WindowServer Heap-Buffer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-435
- **ZDI-CAN:** ZDI-CAN-3769
- **Date:** 2016-07-20
- **CVE:** CVE-2016-4640
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** 93d508e936401e2b20d18c822504839b
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-435/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within CoreGraphics. By interacting with _XRegisterCursorWithData, an attacker can cause a heap buffer overflow. An attacker could leverage this vulnerability to execute arbitrary code under the context of the WindowServer.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT206903

## Disclosure Timeline

- 2016-05-20 - Vulnerability reported to vendor
- 2016-07-20 - Coordinated public release of advisory
