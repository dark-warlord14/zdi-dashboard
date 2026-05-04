# ZDI-15-133: Adobe Flash Player AVSource Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-133
- **ZDI-CAN:** ZDI-CAN-2680
- **Date:** 2015-04-15
- **CVE:** CVE-2015-0347
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** s3tm3m
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-133/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of AVSource objects. By sending a specially crafted SWF an attacker can force a memory corruption condition. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb15-06.html

## Disclosure Timeline

- 2015-01-27 - Vulnerability reported to vendor
- 2015-04-15 - Coordinated public release of advisory
