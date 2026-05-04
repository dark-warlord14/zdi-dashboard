# ZDI-24-456: NI FlexLogger FLXPROJ File Parsing Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-456
- **ZDI-CAN:** ZDI-CAN-21906
- **Date:** 2024-05-15
- **CVE:** CVE-2024-4044
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** NI
- **Affected Products:** FlexLogger
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-456/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of NI FlexLogger. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of FLXPROJ files. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

NI has issued an update to correct this vulnerability. More details can be found at: https://ni.com/r/CVE-2024-4044

## Disclosure Timeline

- 2023-11-28 - Vulnerability reported to vendor
- 2024-05-15 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
