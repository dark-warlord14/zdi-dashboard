# ZDI-23-1164: 7-Zip SquashFS File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1164
- **ZDI-CAN:** ZDI-CAN-18589
- **Date:** 2023-08-23
- **CVE:** CVE-2023-40481
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** 7-Zip
- **Affected Products:** 7-Zip
- **Credit:** goodbyeselene
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1164/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of 7-Zip. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SQFS files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

7-Zip has issued an update to correct this vulnerability. More details can be found at: https://sourceforge.net/p/sevenzip/discussion/45797/thread/713c8a8269/

## Disclosure Timeline

- 2022-11-21 - Vulnerability reported to vendor
- 2023-08-23 - Coordinated public release of advisory
