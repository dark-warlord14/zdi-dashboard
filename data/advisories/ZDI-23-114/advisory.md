# ZDI-23-114: VMware vRealize Log Insight addClusterCACertificate Deserialization of Untrusted Data Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-114
- **ZDI-CAN:** ZDI-CAN-17963
- **Date:** 2023-02-09
- **CVE:** CVE-2022-31710
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** VMware
- **Affected Products:** vRealize
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-114/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of VMware vRealize Log Insight. Authentication is not required to exploit this vulnerability. The specific flaw exists within the addClusterCACertificate function. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2023-0001.html

## Disclosure Timeline

- 2022-08-31 - Vulnerability reported to vendor
- 2023-02-09 - Coordinated public release of advisory
