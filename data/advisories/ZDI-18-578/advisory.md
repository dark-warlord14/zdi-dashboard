# ZDI-18-578: Microsoft Windows ksecdd IOCTL 0x390400 Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-578
- **ZDI-CAN:** ZDI-CAN-5702
- **Date:** 2018-06-13
- **CVE:** CVE-2018-8207
- **CVSS:** 5.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:N/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Lucas Leong (@wmliang) of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-578/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of ksecdd IOCTL 0x390400, which is implemented in cng.sys. Crafted parameters to this IOCTL can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8207

## Disclosure Timeline

- 2018-02-28 - Vulnerability reported to vendor
- 2018-06-13 - Coordinated public release of advisory
- 2018-06-13 - Advisory Updated
