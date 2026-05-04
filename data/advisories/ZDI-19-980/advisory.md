# ZDI-19-980: Microsoft Windows Kernel Type 1 Font Processing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-980
- **ZDI-CAN:** ZDI-CAN-9265
- **Date:** 2019-11-13
- **CVE:** CVE-2019-1412
- **CVSS:** 8.4
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Hossein Lotfi of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-980/
## Vulnerability Details

This vulnerability allows attackers to disclose sensitive information on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of Type 1 fonts in the Windows kernel. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute code in the context of the kernel.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1412

## Disclosure Timeline

- 2019-08-08 - Vulnerability reported to vendor
- 2019-11-13 - Coordinated public release of advisory
