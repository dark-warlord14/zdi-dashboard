# ZDI-21-880: MySQL memcached Plugin Integer Underflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-880
- **ZDI-CAN:** ZDI-CAN-13265
- **Date:** 2021-07-22
- **CVE:** CVE-2021-2389
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** MySQL
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-880/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of MySQL. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of Append and Prepend commands in the memcached plugin. The issue results from the lack of proper validation of user-supplied data, which can result in an integer underflow before writing to memory. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujul2021.html

## Disclosure Timeline

- 2021-03-10 - Vulnerability reported to vendor
- 2021-07-22 - Coordinated public release of advisory
