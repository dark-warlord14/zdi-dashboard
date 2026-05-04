# ZDI-23-890: (Pwn2Own) Microsoft Windows UMPDDrvEnablePDEV Improper Input Validation Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-890
- **ZDI-CAN:** ZDI-CAN-20722
- **Date:** 2023-06-16
- **CVE:** CVE-2023-29539
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Marcin Wiazowski
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-890/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the UMPDDrvEnablePDEV function. The issue results from the lack of proper validation of user-supplied bitmaps prior to processing them. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-29359

## Disclosure Timeline

- 2023-03-30 - Vulnerability reported to vendor
- 2023-06-16 - Coordinated public release of advisory
