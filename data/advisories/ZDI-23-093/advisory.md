# ZDI-23-093: Cacti poll_for_data Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-093
- **ZDI-CAN:** ZDI-CAN-19046
- **Date:** 2023-01-31
- **CVE:** CVE-2022-46169
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cacti
- **Affected Products:** Cacti
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-093/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Cacti. Authentication is not required to exploit this vulnerability. The specific flaw exists within the poll_for_data function. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Cacti has issued an update to correct this vulnerability. More details can be found at: https://github.com/Cacti/cacti/security/advisories/GHSA-6p93-p743-35gf

## Disclosure Timeline

- 2022-11-25 - Vulnerability reported to vendor
- 2023-01-31 - Coordinated public release of advisory
- 2023-01-31 - Advisory Updated
