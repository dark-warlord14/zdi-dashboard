# ZDI-22-708: Oracle MySQL Cluster Data Node Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-708
- **ZDI-CAN:** ZDI-CAN-16408
- **Date:** 2022-04-28
- **CVE:** CVE-2022-21489
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** MySQL Cluster
- **Credit:** lc
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-708/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Oracle MySQL Cluster. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of Data Node jobs. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a buffer. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2022.html

## Disclosure Timeline

- 2022-03-02 - Vulnerability reported to vendor
- 2022-04-28 - Coordinated public release of advisory
