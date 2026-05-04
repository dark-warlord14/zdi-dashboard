# ZDI-23-348: Bentley View SKP File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-348
- **ZDI-CAN:** ZDI-CAN-19084
- **Date:** 2023-03-31
- **CVE:** CVE-2022-43653
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Bentley
- **Affected Products:** View
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-348/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Bentley View. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SKP files. Crafted data in an SKP file can trigger a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in Bentley View version 17.2

## Disclosure Timeline

- 2022-10-06 - Vulnerability reported to vendor
- 2023-03-31 - Coordinated public release of advisory
