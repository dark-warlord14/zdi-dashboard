# ZDI-21-477: Foxit Studio Photo JPM File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-477
- **ZDI-CAN:** ZDI-CAN-12377
- **Date:** 2021-04-26
- **CVE:** CVE-2021-31434
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** Studio Photo
- **Credit:** Wenguang Jiao
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-477/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foxit Studio Photo. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of JPM files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.html

## Disclosure Timeline

- 2020-12-02 - Vulnerability reported to vendor
- 2021-04-26 - Coordinated public release of advisory
