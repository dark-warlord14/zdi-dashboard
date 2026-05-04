# ZDI-21-889: MySQL InnoDB Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-889
- **ZDI-CAN:** ZDI-CAN-13551
- **Date:** 2021-07-22
- **CVE:** CVE-2021-2429
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** MySQL
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-889/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of MySQL. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of InnoDB commands. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujul2021.html

## Disclosure Timeline

- 2021-04-28 - Vulnerability reported to vendor
- 2021-07-22 - Coordinated public release of advisory
- 2021-08-23 - Advisory Updated
