# ZDI-24-811: Hewlett Packard Enterprise OneView clusterService Authentication Bypass Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-811
- **ZDI-CAN:** ZDI-CAN-22455
- **Date:** 2024-06-18
- **CVE:** CVE-2023-50275
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** OneView
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-811/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Hewlett Packard Enterprise OneView. Authentication is not required to exploit this vulnerability. The specific flaw exists within the clusterService. The issue results from the lack of proper validation of the attacker's IP address, which results in exposure of functionality that should be available only on the loopback interface. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbgn04586en_us&docLocale=en_US

## Disclosure Timeline

- 2023-11-28 - Vulnerability reported to vendor
- 2024-06-18 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
