# ZDI-18-429: Microsoft Edge XML File Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-429
- **ZDI-CAN:** ZDI-CAN-5626
- **Date:** 2018-05-14
- **CVE:** CVE-2018-8112
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** Danny__Wei of Tencent's Xuanwu Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-429/
## Vulnerability Details

This vulnerability allows local attackers to escape the sandbox on vulnerable installations of Microsoft Edge. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists due to the fact that various operations can be triggered from within the Microsoft Edge sandbox. Considered individually, these operations do not pose a risk. However, they can be used in combination to produce an unsafe result. An attacker can leverage this in conjunction with other vulnerabilities to execute code under the context of the current user at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8112

## Disclosure Timeline

- 2018-01-30 - Vulnerability reported to vendor
- 2018-05-14 - Coordinated public release of advisory
- 2018-05-14 - Advisory Updated
