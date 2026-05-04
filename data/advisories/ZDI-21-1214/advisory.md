# ZDI-21-1214: Trend Micro Apex One Unnecessary Privileges Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1214
- **ZDI-CAN:** ZDI-CAN-13936
- **Date:** 2021-10-19
- **CVE:** CVE-2021-42107
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1214/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Security Agent. The issue results from allowing an untrusted process to impersonate the client of a pipe. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000289229

## Disclosure Timeline

- 2021-05-27 - Vulnerability reported to vendor
- 2021-10-19 - Coordinated public release of advisory
