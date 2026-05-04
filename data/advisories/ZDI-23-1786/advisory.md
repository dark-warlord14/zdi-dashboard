# ZDI-23-1786: Microsoft Word SKP File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1786
- **ZDI-CAN:** ZDI-CAN-18056
- **Date:** 2023-12-14
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Word
- **Credit:** khangkito - Tran Van Khang (VinCSS)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1786/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Word. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SKP files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://insider.microsoft365.com/en-us/blog/add-sketchup-files-to-office-creations

## Disclosure Timeline

- 2022-08-25 - Vulnerability reported to vendor
- 2023-12-14 - Coordinated public release of advisory
