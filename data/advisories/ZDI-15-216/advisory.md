# ZDI-15-216: (Pwn2Own) Adobe Flash Player BrokerCreateFile Broker Method Path Traversal Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-216
- **ZDI-CAN:** ZDI-CAN-2820
- **Date:** 2015-05-12
- **CVE:** CVE-2015-3085
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** Nicolas Joly
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-216/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the BrokerCreateFile method. An attacker can force BrokerCreateFile to traverse the path of the output file, allowing the file to be written anywhere on disk. An attacker can leverage this vulnerability to execute code at medium integrity.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/reader/apsb15-10.html

## Disclosure Timeline

- 2015-03-18 - Vulnerability reported to vendor
- 2015-05-12 - Coordinated public release of advisory
