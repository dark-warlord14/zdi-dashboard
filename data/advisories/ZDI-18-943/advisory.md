# ZDI-18-943: Microsoft Windows Font Subsetting Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-943
- **ZDI-CAN:** ZDI-CAN-6181
- **Date:** 2018-08-14
- **CVE:** CVE-2018-8344
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Pengsu Cheng of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-943/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the FontSub.dll module. Crafted data in a font file can trigger an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8344

## Disclosure Timeline

- 2018-05-08 - Vulnerability reported to vendor
- 2018-08-14 - Coordinated public release of advisory
- 2018-08-14 - Advisory Updated
