# ZDI-20-1367: Microsoft Excel XLS File Parsing Double Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1367
- **ZDI-CAN:** ZDI-CAN-11518
- **Date:** 2020-11-11
- **CVE:** CVE-2020-17019
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Excel
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1367/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of XLS files. The issue results from the lack of validating the existence of an object prior to performing further free operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2020-17019

## Disclosure Timeline

- 2020-08-05 - Vulnerability reported to vendor
- 2020-11-11 - Coordinated public release of advisory
