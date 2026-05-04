# ZDI-24-213: NI FlexLogger userservices Missing Authorization Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-213
- **ZDI-CAN:** ZDI-CAN-21773
- **Date:** 2024-02-28
- **CVE:** CVE-2024-1155
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NI
- **Affected Products:** FlexLogger
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-213/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of NI FlexLogger. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the userservices executable. The issue results from the lack of authorization prior to allowing access to functionality. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

NI has issued an update to correct this vulnerability. More details can be found at: https://www.ni.com/en/support/security/available-critical-and-security-updates-for-ni-software/incorrect-permissions-for-shared-systemlink-elixir-based-service.html

## Disclosure Timeline

- 2023-11-28 - Vulnerability reported to vendor
- 2024-02-28 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
