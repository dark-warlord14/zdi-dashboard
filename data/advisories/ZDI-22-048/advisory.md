# ZDI-22-048: Microsoft Windows Storage Spaces Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-048
- **ZDI-CAN:** ZDI-CAN-14957
- **Date:** 2022-01-13
- **CVE:** CVE-2022-21877
- **CVSS:** 5.6
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Quang Linh of STAR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-048/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the spaceport.sys driver. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated array. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-21877

## Disclosure Timeline

- 2021-10-06 - Vulnerability reported to vendor
- 2022-01-13 - Coordinated public release of advisory
