# ZDI-18-1054: Microsoft Windows SMB Client Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1054
- **ZDI-CAN:** ZDI-CAN-6283
- **Date:** 2018-09-14
- **CVE:** CVE-2018-8336
- **CVSS:** 1.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Haikuo Xie of Baidu Security Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1054/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the kernel-mode portion of the Windows SMB client. Crafted data in an SMB reply can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to escalate privilege to the level of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8336

## Disclosure Timeline

- 2018-05-24 - Vulnerability reported to vendor
- 2018-09-14 - Coordinated public release of advisory
- 2018-09-14 - Advisory Updated
