# ZDI-22-051: Microsoft Windows DirectComposition Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-051
- **ZDI-CAN:** ZDI-CAN-15188
- **Date:** 2022-01-13
- **CVE:** CVE-2022-21876
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** namnp
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-051/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within DirectComposition. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-21876

## Disclosure Timeline

- 2021-09-22 - Vulnerability reported to vendor
- 2022-01-13 - Coordinated public release of advisory
