# ZDI-24-903: IrfanView WSQ File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-903
- **ZDI-CAN:** ZDI-CAN-24192
- **Date:** 2024-07-18
- **CVE:** CVE-2024-6811
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** IrfanView
- **Affected Products:** IrfanView
- **Credit:** hoon of 78researchlab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-903/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of IrfanView. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of WSQ files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in WSQ plugin (64 bit) https://www.irfanview.com/plugins.htm

## Disclosure Timeline

- 2024-06-21 - Vulnerability reported to vendor
- 2024-07-18 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
