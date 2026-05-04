# ZDI-21-1444: OpenText Brava! Desktop DWG File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1444
- **ZDI-CAN:** ZDI-CAN-14979
- **Date:** 2021-12-03
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** OpenText
- **Affected Products:** Brava! Desktop
- **Credit:** rac
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1444/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of OpenText Brava! Desktop. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DWG files. Crafted data in a DWG file can trigger a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in version 16.6.5.

## Disclosure Timeline

- 2021-09-10 - Vulnerability reported to vendor
- 2021-12-03 - Coordinated public release of advisory
