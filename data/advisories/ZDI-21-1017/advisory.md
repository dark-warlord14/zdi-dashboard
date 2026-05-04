# ZDI-21-1017: Microsoft Windows Canonical Display Driver DrvStrokeAndFillPath NULL Pointer Dereference Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1017
- **ZDI-CAN:** ZDI-CAN-13202
- **Date:** 2021-08-26
- **CVE:** CVE-2021-34516
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Marcin Wiazowski
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1017/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the cdd.dll driver. The issue results from dereferencing a NULL pointer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34516

## Disclosure Timeline

- 2021-05-13 - Vulnerability reported to vendor
- 2021-08-26 - Coordinated public release of advisory
