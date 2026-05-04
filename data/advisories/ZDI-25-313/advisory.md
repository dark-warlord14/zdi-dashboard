# ZDI-25-313: Hewlett Packard Enterprise StoreOnce VSA determineInclusionAndExtract Server-Side Request Forgery Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-313
- **ZDI-CAN:** ZDI-CAN-24982
- **Date:** 2025-06-02
- **CVE:** CVE-2025-37090
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** StoreOnce VSA
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-313/
## Vulnerability Details

This vulnerability allows remote attackers to initiate arbitrary server-side requests on affected installations of Hewlett Packard Enterprise StoreOnce VSA. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the determineInclusionAndExtract method. The issue results from the lack of proper validation of a URI prior to accessing resources. An attacker can leverage this vulnerability to disclose information in the context of the service account.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbst04847en_us&docLocale=en_US

## Disclosure Timeline

- 2024-10-31 - Vulnerability reported to vendor
- 2025-06-02 - Coordinated public release of advisory
- 2025-06-02 - Advisory Updated
