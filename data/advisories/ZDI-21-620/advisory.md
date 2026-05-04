# ZDI-21-620: OpenText Brava! Desktop dwg2dl Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-620
- **ZDI-CAN:** ZDI-CAN-12654
- **Date:** 2021-06-02
- **CVE:** CVE-2021-31480
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** OpenText
- **Affected Products:** Brava! Desktop
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-620/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of OpenText Brava! Desktop. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DXF files. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in version 16.6.4.114

## Disclosure Timeline

- 2021-02-08 - Vulnerability reported to vendor
- 2021-06-02 - Coordinated public release of advisory
- 2021-06-11 - Advisory Updated
