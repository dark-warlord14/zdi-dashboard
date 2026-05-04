# ZDI-18-570: Adobe Flash Microphone Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-570
- **ZDI-CAN:** ZDI-CAN-6131
- **Date:** 2018-06-07
- **CVE:** CVE-2018-4945
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** willJ of Tencent PC Manager
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-570/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Microphone objects. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb18-19.html

## Disclosure Timeline

- 2018-04-25 - Vulnerability reported to vendor
- 2018-06-07 - Coordinated public release of advisory
- 2018-06-07 - Advisory Updated
