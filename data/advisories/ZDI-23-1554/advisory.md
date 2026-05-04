# ZDI-23-1554: Microsoft Windows bStretch Improper Input Validation Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1554
- **ZDI-CAN:** ZDI-CAN-21342
- **Date:** 2023-10-11
- **CVE:** CVE-2023-36731
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Marcin Wiazowski
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1554/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the BLTRECORD::bStretch function in the win32kfull driver. The issue results from the lack of proper validation of user-supplied bitmaps prior to processing them. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36731

## Disclosure Timeline

- 2023-07-06 - Vulnerability reported to vendor
- 2023-10-11 - Coordinated public release of advisory
