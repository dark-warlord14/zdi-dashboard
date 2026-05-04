# ZDI-24-076: Trend Micro Deep Security Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-076
- **ZDI-CAN:** ZDI-CAN-21780
- **Date:** 2024-01-19
- **CVE:** CVE-2023-52338
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Deep Security
- **Credit:** NT AUTHORITY\ANONYMOUS LOGON
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-076/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Deep Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Trend Micro Anti-Malware Solution Platform. By creating a symbolic link, an attacker can abuse the service to delete a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000296337

## Disclosure Timeline

- 2023-09-07 - Vulnerability reported to vendor
- 2024-01-19 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
