# ZDI-21-1366: Trend Micro Worry-Free Business Security Unnecessary Privileges Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1366
- **ZDI-CAN:** ZDI-CAN-14221
- **Date:** 2021-11-30
- **CVE:** CVE-2021-44021
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Worry-Free Business Security
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1366/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Worry-Free Business Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Security Server. The issue results from allowing an untrusted process to impersonate the client of a pipe. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000289230

## Disclosure Timeline

- 2021-06-25 - Vulnerability reported to vendor
- 2021-11-30 - Coordinated public release of advisory
