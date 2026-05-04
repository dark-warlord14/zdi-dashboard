# ZDI-13-094: Oracle WebCenter Content CheckOutAndOpen.dll ActiveX coao/openWebdav Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-094
- **ZDI-CAN:** ZDI-CAN-1689
- **Date:** 2013-05-29
- **CVE:** CVE-2013-1559
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** WebCenter Content
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-094/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle WebCenter Content. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the CheckOutAndOpen.dll ActiveX control's coao and openWebdav methods. By specifying a carefully constructed path an attacker can force the contents of the file to be passed to ShellExecuteExW. An attacker can leverage this vulnerability to execute code under the context of the current user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpuapr2013-1899555.html

## Disclosure Timeline

- 2013-01-07 - Vulnerability reported to vendor
- 2013-05-29 - Coordinated public release of advisory
