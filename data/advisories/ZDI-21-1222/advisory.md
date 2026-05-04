# ZDI-21-1222: Trend Micro Apex One Uncontrolled Search Path Element Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1222
- **ZDI-CAN:** ZDI-CAN-13830
- **Date:** 2021-10-19
- **CVE:** CVE-2021-42102
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Xavier DANEST - Decathlon
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1222/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One Security Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the configuration of OpenSSL. The process loads an OpenSSL configuration file from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000289229

## Disclosure Timeline

- 2021-07-09 - Vulnerability reported to vendor
- 2021-10-19 - Coordinated public release of advisory
