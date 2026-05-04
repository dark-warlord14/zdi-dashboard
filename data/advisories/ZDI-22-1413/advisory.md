# ZDI-22-1413: Microsoft Windows CSRSS Activation Context Cache Poisoning Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1413
- **ZDI-CAN:** ZDI-CAN-18149
- **Date:** 2022-10-14
- **CVE:** CVE-2022-37989
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Simon Zuckerbraun - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1413/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the CSRSS.exe process. By sending a crafted message to CSRSS, an attacker can cause an arbitrary DLL to be loaded. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-37989

## Disclosure Timeline

- 2022-07-28 - Vulnerability reported to vendor
- 2022-10-14 - Coordinated public release of advisory
- 2023-01-17 - Advisory Updated
