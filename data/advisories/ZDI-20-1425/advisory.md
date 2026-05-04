# ZDI-20-1425: Microsoft Excel XLS File Parsing Integer Signedness Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1425
- **ZDI-CAN:** ZDI-CAN-11752
- **Date:** 2020-12-11
- **CVE:** CVE-2020-17128
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Excel
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1425/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of XLS files. Crafted data in an XLS file can trigger a dereference of a user-supplied value as a pointer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-17128

## Disclosure Timeline

- 2020-09-25 - Vulnerability reported to vendor
- 2020-12-11 - Coordinated public release of advisory
