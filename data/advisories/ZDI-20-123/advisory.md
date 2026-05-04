# ZDI-20-123: Microsoft Windows CLFS Driver Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-123
- **ZDI-CAN:** ZDI-CAN-9423
- **Date:** 2020-01-15
- **CVE:** CVE-2020-0615
- **CVSS:** 8.4
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-123/
## Vulnerability Details

This vulnerability allows attackers to disclose sensitive information on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the CLFS driver. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute code in the context of the kernel.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0615

## Disclosure Timeline

- 2019-10-01 - Vulnerability reported to vendor
- 2020-01-15 - Coordinated public release of advisory
