# ZDI-25-859: Firebird SQL Database Server XDR Message Parsing NULL Pointer Dereference Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-859
- **ZDI-CAN:** ZDI-CAN-26486
- **Date:** 2025-08-21
- **CVE:** CVE-2025-54989
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Firebird
- **Affected Products:** Firebird SQL
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-859/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Firebird SQL. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing of XDR messages. The issue results from dereferencing a null pointer. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Firebird has issued an update to correct this vulnerability. More details can be found at: https://github.com/FirebirdSQL/firebird/commit/169da595f8693fc1a65a79c741724b1bc8db9f25

## Disclosure Timeline

- 2025-05-02 - Vulnerability reported to vendor
- 2025-08-21 - Coordinated public release of advisory
- 2025-08-21 - Advisory Updated
