# ZDI-24-177: Siemens Simcenter Femap MODEL File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-177
- **ZDI-CAN:** ZDI-CAN-21712
- **Date:** 2024-02-15
- **CVE:** CVE-2024-24921
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** Simcenter Femap
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-177/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens Simcenter Femap. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of MODEL files within the CatiaV4_2022_2 executable. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Siemens has issued an update to correct this vulnerability. More details can be found at: https://cert-portal.siemens.com/productcert/html/ssa-000072.html

## Disclosure Timeline

- 2023-09-13 - Vulnerability reported to vendor
- 2024-02-15 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
