# ZDI-21-1377: Avira Free Antivirus Unnecessary Privileges Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1377
- **ZDI-CAN:** ZDI-CAN-14119
- **Date:** 2021-12-03
- **CVE:** N/A
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Avira
- **Affected Products:** Free Antivirus
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1377/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Avira Free Antivirus. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the endpoint client. The issue results from allowing an untrusted process to impersonate the client of a pipe. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed in version 15.0.2108.2113

## Disclosure Timeline

- 2021-07-19 - Vulnerability reported to vendor
- 2021-12-03 - Coordinated public release of advisory
