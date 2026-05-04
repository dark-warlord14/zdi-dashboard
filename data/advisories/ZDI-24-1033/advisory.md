# ZDI-24-1033: NI FlexLogger Redis Server Incorrect Permission Assignment Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1033
- **ZDI-CAN:** ZDI-CAN-23183
- **Date:** 2024-07-30
- **CVE:** CVE-2024-6122
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** NI
- **Affected Products:** FlexLogger
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1033/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of NI FlexLogger. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the configuration of Redis. The issue results from the incorrect assignment of permissions to access Redis credentials. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

NI has issued an update to correct this vulnerability. More details can be found at: https://www.ni.com/en/support/security/available-critical-and-security-updates-for-ni-software/incorrect-default-directory-permissions-for-ni-systemlink-redis-service.html

## Disclosure Timeline

- 2024-01-23 - Vulnerability reported to vendor
- 2024-07-30 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
