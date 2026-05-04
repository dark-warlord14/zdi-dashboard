# ZDI-22-109: Oracle MySQL Cluster Data Node Improper Validation of Array Index Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-109
- **ZDI-CAN:** ZDI-CAN-14500
- **Date:** 2022-01-21
- **CVE:** CVE-2022-21324
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:L
- **Affected Vendors:** Oracle
- **Affected Products:** MySQL Cluster
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-109/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Oracle MySQL Cluster. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of Data Node jobs. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an array. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the service account.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujan2022.html

## Disclosure Timeline

- 2021-07-23 - Vulnerability reported to vendor
- 2022-01-21 - Coordinated public release of advisory
