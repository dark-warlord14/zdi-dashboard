# ZDI-23-132: Open Design Alliance (ODA) Drawing SDK DGN File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-132
- **ZDI-CAN:** ZDI-CAN-19152
- **Date:** 2023-02-09
- **CVE:** CVE-2021-32944
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Open Design Alliance (ODA)
- **Affected Products:** Drawing SDK
- **Credit:** Mat Powell & Jimmy Calderon (@vectors2final) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-132/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Open Design Alliance (ODA) Drawing SDK. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DGN files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://www.opendesign.com/security-advisories

## Disclosure Timeline

- 2022-10-18 - Vulnerability reported to vendor
- 2023-02-09 - Coordinated public release of advisory
