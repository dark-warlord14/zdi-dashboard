# ZDI-21-1468: Bentley View J2K File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1468
- **ZDI-CAN:** ZDI-CAN-14832
- **Date:** 2021-12-08
- **CVE:** CVE-2021-34879
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Bentley
- **Affected Products:** View
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1468/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Bentley View. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of J2K files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Bentley has issued an update to correct this vulnerability. More details can be found at: https://www.bentley.com/en/common-vulnerability-exposure/BE-2021-0006

## Disclosure Timeline

- 2021-08-11 - Vulnerability reported to vendor
- 2021-12-08 - Coordinated public release of advisory
