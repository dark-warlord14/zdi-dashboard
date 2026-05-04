# ZDI-23-1499: Cacti link Local File Inclusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1499
- **ZDI-CAN:** ZDI-CAN-21001
- **Date:** 2023-10-04
- **CVE:** CVE-2023-39365
- **CVSS:** 6.6
- **CVSS Vector:** AV:N/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cacti
- **Affected Products:** Cacti
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1499/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Cacti. Authentication is required to exploit this vulnerability. The specific flaw exists within the link endpoint. The issue results from the lack of proper validation of data retrieved from the database prior to passing it to a PHP include function. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the service account.

## Additional Details

Cacti has issued an update to correct this vulnerability. More details can be found at: https://github.com/cacti/cacti/security/advisories/GHSA-v5w7-hww7-2f22

## Disclosure Timeline

- 2023-05-03 - Vulnerability reported to vendor
- 2023-10-04 - Coordinated public release of advisory
