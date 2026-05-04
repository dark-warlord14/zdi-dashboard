# ZDI-22-497: Microsoft Windows CLFS Integer Overflow Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-497
- **ZDI-CAN:** ZDI-CAN-15986
- **Date:** 2022-03-09
- **CVE:** CVE-2022-23281
- **CVSS:** 4.2
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:L/I:N/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-497/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the CLFS.SYS driver. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before reading from memory. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-23281

## Disclosure Timeline

- 2021-12-15 - Vulnerability reported to vendor
- 2022-03-09 - Coordinated public release of advisory
