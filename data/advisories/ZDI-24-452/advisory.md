# ZDI-24-452: Microsoft Windows cldflt Type Confusion Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-452
- **ZDI-CAN:** ZDI-CAN-22417
- **Date:** 2024-05-14
- **CVE:** CVE-2024-30034
- **CVSS:** 8.4
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Wei Lei and Sergey Kornienko (@b1thvn_) of PixiePoint Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-452/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Cloud Files Mini Filter Driver, cldflt.sys. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to disclose information in the context of the kernel.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-30034

## Disclosure Timeline

- 2024-01-23 - Vulnerability reported to vendor
- 2024-05-14 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
