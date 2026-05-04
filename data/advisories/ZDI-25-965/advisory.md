# ZDI-25-965: DataChain data_storage Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-965
- **ZDI-CAN:** ZDI-CAN-27165
- **Date:** 2025-10-27
- **CVE:** CVE-2025-61677
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** DataChain
- **Affected Products:** DataChain
- **Credit:** Peter Girnus (@gothburz) of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-965/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of DataChain. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the data_storage module. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

DataChain has issued an update to correct this vulnerability. More details can be found at: https://github.com/iterative/datachain/security/advisories/GHSA-6px8-mr29-cj4r

## Disclosure Timeline

- 2025-05-21 - Vulnerability reported to vendor
- 2025-10-27 - Coordinated public release of advisory
- 2025-10-27 - Advisory Updated
