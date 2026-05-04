# ZDI-22-1410: Microsoft Windows DosDevices Activation Context Cache Poisoning Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1410
- **ZDI-CAN:** ZDI-CAN-17847
- **Date:** 2022-10-14
- **CVE:** CVE-2022-37987
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Simon Zuckerbraun - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1410/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the CSRSS.exe process. By performing a DOS device redirection, an attacker can alter a path used for searching for dependencies. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-37987

## Disclosure Timeline

- 2022-07-11 - Vulnerability reported to vendor
- 2022-10-14 - Coordinated public release of advisory
- 2023-01-17 - Advisory Updated
