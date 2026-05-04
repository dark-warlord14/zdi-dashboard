# ZDI-14-130: (Pwn2Own) Adobe Flash Display Object Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-130
- **ZDI-CAN:** ZDI-CAN-2235
- **Date:** 2014-05-19
- **CVE:** CVE-2014-0510
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** Zeguang Zhao of Team509 and Liang Chen of KeenTeam
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-130/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of display objects. The issue lies in modifying an object's parent within a callback. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://helpx.adobe.com/security/products/flash-player/apsb14-14.html

## Disclosure Timeline

- 2014-03-13 - Vulnerability reported to vendor
- 2014-05-19 - Coordinated public release of advisory
