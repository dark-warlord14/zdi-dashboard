# ZDI-25-847: NVIDIA Isaac-GR00T TorchSerializer Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-847
- **ZDI-CAN:** ZDI-CAN-27210
- **Date:** 2025-08-20
- **CVE:** CVE-2025-23296
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NVIDIA
- **Affected Products:** Isaac-GR00T
- **Credit:** Peter Girnus (@gothburz) of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-847/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of NVIDIA Isaac-GR00T. Authentication is not required to exploit this vulnerability. The specific flaw exists within the TorchSerializer class. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NVIDIA has issued an update to correct this vulnerability. More details can be found at: https://nvidia.custhelp.com/app/answers/detail/a_id/5681

## Disclosure Timeline

- 2025-05-22 - Vulnerability reported to vendor
- 2025-08-20 - Coordinated public release of advisory
- 2025-09-03 - Advisory Updated
