# ZDI-20-453: Fuji Electric V-Server Lite VPR File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-453
- **ZDI-CAN:** ZDI-CAN-10138
- **Date:** 2020-04-09
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fuji Electric
- **Affected Products:** V-Server Lite
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-453/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fuji Electric V-Server Lite. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of VPR files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in V-Server 4.0.7.0 and Lite V4.0.9.0.

## Disclosure Timeline

- 2020-02-28 - Vulnerability reported to vendor
- 2020-04-09 - Coordinated public release of advisory
