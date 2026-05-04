# ZDI-23-1027: Triangle MicroWorks SCADA Data Gateway Directory Traversal Arbitrary File Creation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1027
- **ZDI-CAN:** ZDI-CAN-20531
- **Date:** 2023-08-04
- **CVE:** CVE-2023-39459
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Triangle MicroWorks
- **Affected Products:** SCADA Data Gateway
- **Credit:** Li Jiantao, Ngo Wei Lin, Pan Zhenpeng of STAR Labs SG Pte. Ltd.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1027/
## Vulnerability Details

This vulnerability allows remote attackers to create arbitrary files on affected installations of Triangle MicroWorks SCADA Data Gateway. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of workspace files. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to create files in the context of Administrator.

## Additional Details

Triangle MicroWorks has issued an update to correct this vulnerability. More details can be found at: https://www.trianglemicroworks.com/products/scada-data-gateway/what's-new

## Disclosure Timeline

- 2023-05-03 - Vulnerability reported to vendor
- 2023-08-04 - Coordinated public release of advisory
