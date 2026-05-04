# ZDI-17-170: Microsoft Windows JavaScript Proxy Setter Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-170
- **ZDI-CAN:** ZDI-CAN-4271
- **Date:** 2017-03-21
- **CVE:** CVE-2017-0094
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** bee13oy of CloverSec Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-170/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of script that sets a property on a JavaScript object that is intercepted by a Proxy object. By performing actions in JavaScript an attacker can trigger a type confusion condition. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Disclosure Timeline

- 2016-12-01 - Vulnerability reported to vendor
- 2017-03-21 - Coordinated public release of advisory
