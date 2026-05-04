# ZDI-26-038: (0Day) Langflow Disk Cache Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-038
- **ZDI-CAN:** ZDI-CAN-27919
- **Date:** 2026-01-09
- **CVE:** CVE-2026-0772
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Langflow
- **Affected Products:** Langflow
- **Credit:** Peter Girnus (@gothburz), Brandon Niemczyk of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-038/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Langflow. Authentication is required to exploit this vulnerability. The specific flaw exists within the disk cache service. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

08/21/25 – ZDI submitted the report to the vendor’s GitHub account 09/15/25 – ZDI asked for updates 09/24/25 – ZDI asked for the fix 12/10/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-08-21 - Vulnerability reported to vendor
- 2026-01-09 - Coordinated public release of advisory
- 2026-01-09 - Advisory Updated
