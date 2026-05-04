# ZDI-23-1112: Microsoft Windows Error Reporting Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1112
- **ZDI-CAN:** ZDI-CAN-21597
- **Date:** 2023-08-15
- **CVE:** CVE-2023-35359
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Le Qi Chen
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1112/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. Furthermore, exploitation is possible only in limited circumstances. The specific flaw exists within the processing of unhandled exceptions. By redirecting a DOS device, an attacker can abuse a high-privileged service to launch an arbitrary executable. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of a high-privileged service account.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-35359

## Disclosure Timeline

- 2023-08-03 - Vulnerability reported to vendor
- 2023-08-15 - Coordinated public release of advisory
