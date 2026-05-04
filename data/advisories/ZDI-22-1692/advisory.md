# ZDI-22-1692: Microsoft Windows GreDrawStream Use-After-Free Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1692
- **ZDI-CAN:** ZDI-CAN-18562
- **Date:** 2022-12-28
- **CVE:** CVE-2022-44671
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Marcin Wiazowski
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1692/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the GreDrawStream function. Crafted data passed to this function can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-44671

## Disclosure Timeline

- 2022-09-08 - Vulnerability reported to vendor
- 2022-12-28 - Coordinated public release of advisory
