# ZDI-15-369: (Pwn2Own) Adobe Reader opendoc Broker Message Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-369
- **ZDI-CAN:** ZDI-CAN-2822
- **Date:** 2015-07-29
- **CVE:** CVE-2015-5109
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** Nicolas Joly
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-369/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within processing of the opendoc message. A specially crafted opendoc message can cause an integer wrap of a size value passed to a malloc call, which is followed by a strncpy call. An attacker can leverage this vulnerability to execute code at medium integrity.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/reader/apsb15-15.html

## Disclosure Timeline

- 2015-03-18 - Vulnerability reported to vendor
- 2015-07-29 - Coordinated public release of advisory
