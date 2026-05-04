# ZDI-14-132: (Pwn2Own) Adobe Reader Sandbox Bypass Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-132
- **ZDI-CAN:** ZDI-CAN-2211
- **Date:** 2014-05-19
- **CVE:** CVE-2014-0512
- **CVSS:** 4.6
- **CVSS Vector:** AV:L/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** VUPEN
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-132/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of file writes. The issue lies in the failure to properly validate user-supplied paths. An attacker can leverage this to execute code outside the context of the sandbox.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://helpx.adobe.com/security/products/reader/apsb14-15.html

## Disclosure Timeline

- 2014-03-13 - Vulnerability reported to vendor
- 2014-05-19 - Coordinated public release of advisory
