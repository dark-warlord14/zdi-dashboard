# ZDI-24-572: Trend Micro Apex One Security Agent Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-572
- **ZDI-CAN:** ZDI-CAN-22693
- **Date:** 2024-06-06
- **CVE:** CVE-2024-36305
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** NT AUTHORITY\ANONYMOUS LOGON
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-572/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One Security Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Apex One NT RealTime Scan service. By creating a junction, an attacker can abuse the service to create arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/dcx/s/solution/000298063?language=en_US

## Disclosure Timeline

- 2024-01-03 - Vulnerability reported to vendor
- 2024-06-06 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
