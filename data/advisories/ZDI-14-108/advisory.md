# ZDI-14-108: Oracle Data Quality DscXB onloadstatechange Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-108
- **ZDI-CAN:** ZDI-CAN-1935
- **Date:** 2014-04-21
- **CVE:** CVE-2014-2417
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Data Quality
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-108/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Data Quality. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the TSS12.DscXB.XB ActiveX control. The issue lies in the ability to dereference arbitrary pointers from JavaScript. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpuapr2014-1972952.html

## Disclosure Timeline

- 2013-07-23 - Vulnerability reported to vendor
- 2014-04-21 - Coordinated public release of advisory
