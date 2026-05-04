# ZDI-22-623: Siemens Simcenter Femap NEU File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-623
- **ZDI-CAN:** ZDI-CAN-15592
- **Date:** 2022-04-28
- **CVE:** CVE-2022-28663
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** Simcenter Femap
- **Credit:** xina1i
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-623/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens Simcenter Femap. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of NEU files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Siemens has issued an update to correct this vulnerability. More details can be found at: https://cert-portal.siemens.com/productcert/pdf/ssa-998762.pdf

## Disclosure Timeline

- 2021-12-15 - Vulnerability reported to vendor
- 2022-04-28 - Coordinated public release of advisory
