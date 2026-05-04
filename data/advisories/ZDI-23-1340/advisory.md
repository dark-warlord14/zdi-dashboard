# ZDI-23-1340: Synology RT6600ax SYNO.Core Uncontrolled Resource Consumption Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1340
- **ZDI-CAN:** ZDI-CAN-19742
- **Date:** 2023-09-07
- **CVE:** CVE-2023-41739
- **CVSS:** 5.7
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Synology
- **Affected Products:** RT6600ax
- **Credit:** Discovered by: Claroty Research - Vera Mens, Noam Moshe, Uri Katz, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1340/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to create a denial-of-service condition on affected installations of Synology RT6600ax routers. Authentication is required to exploit this vulnerability. The specific flaw exists within the SYNO.Core file. The issue results from uncontrolled resource consumption. An attacker can leverage this vulnerability to create a denial-of-service condition on the device.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/en-global/security/advisory/Synology_SA_23_10

## Disclosure Timeline

- 2022-12-02 - Vulnerability reported to vendor
- 2023-09-07 - Coordinated public release of advisory
