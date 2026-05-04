# ZDI-24-1373: IrfanView SID File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1373
- **ZDI-CAN:** ZDI-CAN-23280
- **Date:** 2024-10-11
- **CVE:** CVE-2024-9260
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** IrfanView
- **Affected Products:** IrfanView
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1373/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of IrfanView. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SID files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in test version: http://www.irfanview.info/test/iview64_test.zip

## Disclosure Timeline

- 2024-02-13 - Vulnerability reported to vendor
- 2024-10-11 - Coordinated public release of advisory
- 2024-10-11 - Advisory Updated
