# ZDI-23-346: Bentley View SKP File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-346
- **ZDI-CAN:** ZDI-CAN-18960
- **Date:** 2023-03-31
- **CVE:** CVE-2022-43651
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Bentley
- **Affected Products:** View
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-346/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Bentley View. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SKP files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in Bentley View version 17.2

## Disclosure Timeline

- 2022-09-28 - Vulnerability reported to vendor
- 2023-03-31 - Coordinated public release of advisory
