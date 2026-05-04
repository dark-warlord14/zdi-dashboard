# ZDI-22-112: Oracle MySQL Cluster Data Node Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-112
- **ZDI-CAN:** ZDI-CAN-14503
- **Date:** 2022-01-21
- **CVE:** CVE-2022-21327
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** MySQL Cluster
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-112/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Oracle MySQL Cluster. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of Data Node jobs. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujan2022.html

## Disclosure Timeline

- 2021-07-23 - Vulnerability reported to vendor
- 2022-01-21 - Coordinated public release of advisory
