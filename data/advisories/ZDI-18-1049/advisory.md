# ZDI-18-1049: Microsoft Windows Excel Database Driver FORMULA Record Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1049
- **ZDI-CAN:** ZDI-CAN-6255
- **Date:** 2018-09-14
- **CVE:** CVE-2018-8392
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Pengsu Cheng of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1049/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the msexcl40.dll Excel database driver module, which ships with Microsoft Windows. A crafted FORMULA record in an Excel database file can trigger an integer overflow before writing to memory. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8392

## Disclosure Timeline

- 2018-06-05 - Vulnerability reported to vendor
- 2018-09-14 - Coordinated public release of advisory
- 2018-09-14 - Advisory Updated
