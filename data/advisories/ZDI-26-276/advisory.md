# ZDI-26-276: Microsoft Windows Secure Kernel Double Free Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-276
- **ZDI-CAN:** ZDI-CAN-28189
- **Date:** 2026-04-15
- **CVE:** CVE-2026-26179
- **CVSS:** 7.5
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** fastfail
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-276/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Windows Secure Kernel. The issue results from the lack of validating the existence of an object prior to performing further free operations on the object. An attacker can potentially leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the VTL1 Secure Kernel.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-26179

## Disclosure Timeline

- 2025-12-09 - Vulnerability reported to vendor
- 2026-04-15 - Coordinated public release of advisory
- 2026-04-15 - Advisory Updated
